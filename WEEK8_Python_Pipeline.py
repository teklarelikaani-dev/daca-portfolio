#1. Data Fetcher (Andmete pärimine) 

import os
import pandas as pd
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()


supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)


def fetch_all(table_name):
    """
    Toob kõik read etteantud tabelist.
    """
    data = []
    page_size = 1000
    page = 0

    while True:
        response = (
            supabase
            .table(table_name)
            .select("*")
            .range(page * page_size, (page + 1) * page_size - 1)
            .execute()
        )

        rows = response.data

        if not rows:
            break

        data.extend(rows)

        if len(rows) < page_size:
            break

        page += 1

    return pd.DataFrame(data)


def fetch_sales(start_date, end_date):
    """
    Toob kõik müügiandmed etteantud kuupäevavahemikus.
    """
    try:
        data = []
        page_size = 1000
        page = 0

        while True:
            response = (
                supabase
                .table("sales")
                .select("*")
                .gte("sale_date", start_date)
                .lte("sale_date", end_date)
                .range(page * page_size, (page + 1) * page_size - 1)
                .execute()
            )

            rows = response.data

            if not rows:
                break

            data.extend(rows)

            if len(rows) < page_size:
                break

            page += 1

        return pd.DataFrame(data)

    except Exception as e:
        print(f"Viga müügiandmete pärimisel: {e}")
        return pd.DataFrame()


def fetch_customers():
    """
    Toob kõik kliendid.
    """
    try:
        return fetch_all("customers")

    except Exception as e:
        print(f"Viga klientide pärimisel: {e}")
        return pd.DataFrame()


def fetch_products():
    """
    Toob kõik tooted.
    """
    try:
        return fetch_all("products")

    except Exception as e:
        print(f"Viga toodete pärimisel: {e}")
        return pd.DataFrame()


if __name__ == "__main__":

    sales = fetch_sales("2023-01-01", "2026-12-31")
    customers = fetch_customers()
    products = fetch_products()

    print(f"Sales: {len(sales)} rida")
    print(sales.head())

    print(f"\nCustomers: {len(customers)} rida")
    print(customers.head())

#2. Data Transform (Andmete töötlemine ja koondnäitajad)

import pandas as pd


def clean_data(df):
    """
    Eemaldab duplikaadid, täidab puuduvad väärtused ja
    teisendab kuupäeva datetime formaati.
    """

    df = df.copy()

    # Eemalda duplikaadid
    df = df.drop_duplicates()

    # Täida puuduvad väärtused
    df = df.fillna(0)

    # Kui on olemas sale_date veerg, teisenda datetime'iks
    if "sale_date" in df.columns:
        df["sale_date"] = pd.to_datetime(df["sale_date"])

    return df


def calculate_weekly_aggregates(df):
    """
    Arvutab nädalased koondnäitajad.
    """

    df = clean_data(df)

    weekly = (
        df.resample("W", on="sale_date")
        .agg(
            revenue=("total_price", "sum"),
            orders=("total_price", "count"),
            average_order=("total_price", "mean"),
        )
        .reset_index()
    )

    return weekly


def calculate_kpis(df):
    """
    Tagastab põhilised KPI-d.
    """

    df = clean_data(df)

    kpis = {
        "total_revenue": df["total_price"].sum(),
        "unique_customers": df["customer_id"].nunique(),
        "avg_order_value": df["total_price"].mean(),
    }

    return kpis


def merge_datasets(df_sales, df_customers):
    """
    Liidab müügi- ja kliendiandmed customer_id järgi.
    """

    merged = pd.merge(
        df_sales,
        df_customers,
        on="customer_id",
        how="left",
    )

    return merged

# Näidisandmed
df_sales = pd.DataFrame({
    "customer_id": [1, 2, 1],
    "total_price": [100, 200, 150],
    "sale_date": ["2024-01-01", "2024-01-03", "2024-01-08"]
})

df_customers = pd.DataFrame({
    "customer_id": [1, 2],
    "name": ["Mari", "Jüri"]
})

# Puhastatud andmed
cleaned = clean_data(df_sales)
print("Puhastatud andmed:")
print(cleaned)

# Nädalased koondandmed
weekly = calculate_weekly_aggregates(df_sales)
print("\nNädalased koondandmed:")
print(weekly)

# KPI-d
kpis = calculate_kpis(df_sales)
print("\nKPI-d:")
print(kpis)

# Liidetud andmed
merged = merge_datasets(df_sales, df_customers)
print("\nLiidetud andmed:")
print(merged)
    print(f"\nProducts: {len(products)} rida")

#3. Visualize (KPI ja nädala graafikud)

import os
from datetime import datetime

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def create_weekly_chart(df_weekly):
    """
    Loob nädalase tulu joondiagrammi.
    """

    fig = px.line(
        df_weekly,
        x="sale_date",
        y="revenue",
        title="Nädalane tulu",
        markers=True
    )

    fig.update_layout(
        xaxis_title="Nädal",
        yaxis_title="Tulu (€)"
    )

    return fig


def create_kpi_summary(kpis):
    """
    Loob KPI tabeli.
    """

    fig = go.Figure(
        data=[
            go.Table(
                header=dict(
                    values=["KPI", "Väärtus"]
                ),
                cells=dict(
                    values=[
                        list(kpis.keys()),
                        list(kpis.values())
                    ]
                )
            )
        ]
    )

    fig.update_layout(title="Peamised KPI-d")

    return fig


def export_results(df, weekly_fig, kpi_fig, output_dir="output"):
    """
    Salvestab CSV ja HTML failid.
    """

    os.makedirs(output_dir, exist_ok=True)

    date_str = datetime.now().strftime("%Y%m%d")

    # CSV
    df.to_csv(
        os.path.join(output_dir, f"weekly_data_{date_str}.csv"),
        index=False
    )

    # HTML diagrammid
    weekly_fig.write_html(
        os.path.join(output_dir, f"weekly_chart_{date_str}.html")
    )

    kpi_fig.write_html(
        os.path.join(output_dir, f"kpi_summary_{date_str}.html")
    )

    print("Failid edukalt salvestatud!")

#4. Pipeline

import logging
import time

from data_fetcher import fetch_sales, fetch_customers
from transform import (
    clean_data,
    calculate_weekly_aggregates,
    calculate_kpis,
    merge_datasets,
)
from visualize_export import (
    create_weekly_chart,
    create_kpi_summary,
    export_results,
)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def run_pipeline():
    try:
        logging.info("Pipeline started")

        # 1. Andmete pärimine
        logging.info("Fetching data...")
        sales = fetch_sales("2020-01-01", "2026-12-31")
        customers = fetch_customers()
        logging.info("Data fetched")

        # 2. Andmete puhastamine
        logging.info("Cleaning data...")
        sales_clean = clean_data(sales)
        logging.info("Cleaning complete")

        # 3. Koondandmed
        logging.info("Calculating weekly aggregates...")
        weekly = calculate_weekly_aggregates(sales_clean)

        logging.info("Calculating KPIs...")
        kpis = calculate_kpis(sales_clean)

        logging.info("Merging datasets...")
        merged = merge_datasets(sales_clean, customers)

        # 4. Graafikud
        logging.info("Creating charts...")
        weekly_chart = create_weekly_chart(weekly)
        kpi_chart = create_kpi_summary(kpis)

        # 5. Eksport
        logging.info("Exporting results...")
        export_results(
            weekly,
            weekly_chart,
            kpi_chart,
            output_dir="output"
        )

        logging.info(f"Rows processed: {len(merged)}")
        logging.info("Pipeline finished successfully.")

        print("\nPipeline completed successfully!")

    except Exception as e:
        logging.error(f"Pipeline failed: {e}")
        print(f"\nPipeline failed: {e}")


if __name__ == "__main__":

    start_time = time.time()

    run_pipeline()

    elapsed = time.time() - start_time

    logging.info(f"Execution time: {elapsed:.2f} seconds")
    print(f"Execution time: {elapsed:.2f} seconds")


    print(products.head())
