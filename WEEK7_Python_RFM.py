#1. SUPABASE ÜHENDAMINE JA SALES TABELI TOOMINE
import os
import pandas as pd
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

# Loeme kõik read partiidena
all_rows = []
batch_size = 1000
start = 0

while True:
    response = (
        supabase.table("sales")
        .select("*")
        .range(start, start + batch_size - 1)
        .execute()
    )

    rows = response.data

    # Kui rohkem ridu pole, lõpetame
    if not rows:
        break

    all_rows.extend(rows)

    print(f"Laetud {len(all_rows)} rida...")

    # Kui saime vähem kui batch_size ridu, olime viimases blokis
    if len(rows) < batch_size:
        break

    start += batch_size

# DataFrame
df_sales = pd.DataFrame(all_rows)

print("\nValmis!")
print("Sales tabeli suurus:", df_sales.shape)

# Näita esimesed read
print(df_sales.head())

#2. CUSTOMERS TABELI TOOMINE
import pandas as pd

all_customers = []
batch_size = 1000
start = 0

while True:
    response = (
        supabase.table("customers")
        .select("*")
        .range(start, start + batch_size - 1)
        .execute()
    )

    rows = response.data

    if not rows:
        break

    all_customers.extend(rows)

    if len(rows) < batch_size:
        break

    start += batch_size

df_customers = pd.DataFrame(all_customers)

print("Customers tabeli suurus:", df_customers.shape)
display(df_customers.head())

#3. KAHE TABELI ÜHENDAMINE
df = pd.merge(df_sales, df_customers, on='customer_id', how='left')

#4. PUHASTAMINE
import pandas as pd

# ==========================================
# SAMM 1: Algse seisuga tutvumine
# ==========================================
print("--- PUHASTAMISE ALGUS ---")
algne_shape = df.shape
print(f"Esialgne andmestiku suurus (shape): {algne_shape}")


# ==========================================
# SAMM 2: Duplikaatide eemaldamine
# ==========================================
duplikaatide_arv = df.duplicated().sum()
print(f"Leitud duplikaatide arv: {duplikaatide_arv}")

# Eemaldame duplikaadid
df = df.drop_duplicates()


# ==========================================
# SAMM 3: NULL väärtuste kontroll ja eemaldamine
# ==========================================
print("\nNULL väärtuste arv veergude kaupa enne puhastamist:")
print(df.isnull().sum())

# Eemaldame read, kus kriitilised veerud on tühjad (NULL)
kriitilised_veerud = ['customer_id', 'sale_date', 'total_price']
df = df.dropna(subset=kriitilised_veerud)


# ==========================================
# SAMM 4: Kuupäevade parsimine (tüübi muutmine)
# ==========================================
# Muudame 'sale_date' veeru stringist ametlikuks datetime tüübiks
df['sale_date'] = pd.to_datetime(df['sale_date'])


# ==========================================
# SAMM 5: Outlier'ite (vigaste väärtuste) eemaldamine
# ==========================================
# Loeme kokku, mitu tehingut on negatiivse või null-hinnaga
vigased_hinnad = (df['total_price'] <= 0).sum()
print(f"\nLeitud vigaseid (negatiivseid või 0) hindu: {vigased_hinnad}")

# Jätame alles ainult tehingud, mille hind on suurem kui 0
df = df[df['total_price'] > 0]


# ==========================================
# SAMM 6: PUHASTUSRAPORT
# ==========================================
print("\n" + "="*40)
print("             PUHASTUSRAPORT")
print("="*40)
print(f"Algne andmete suurus:       {algne_shape}")
print(f"Lõplik andmete suurus:      {df.shape}")
print(f"Eemaldatud duplikaate:      {duplikaatide_arv}")
print(f"Unikaalsete klientide arv:   {df['customer_id'].nunique()}")

# Kuna parsisime kuupäevad sammus 4, saame siin küsida kuupäevade vahemikku
algus_kuupaev = df['sale_date'].min()
lopp_kuupaev = df['sale_date'].max()
print(f"Andmete ajaline vahemik:    {algus_kuupaev.strftime('%Y-%m-%d')} kuni {lopp_kuupaev.strftime('%Y-%m-%d')}")

print("\nKriitiliste veergude andmetüübid edasiseks RFM analüüsiks:")
print(df[['customer_id', 'sale_date', 'total_price']].dtypes)
print("="*40)

#5. RFM ANALÜÜS
import pandas as pd
import numpy as np

print("--- RFM ANALÜÜSI ALGUS ---")

# ==========================================
# SAMM 1: Viitekuupäeva määramine
# ==========================================
# Kuna andmestik on minevikust, kasutame analüüsiks fikseeritud "tänast" kuupäeva
today = pd.to_datetime('2025-02-28')


# ==========================================
# SAMM 2, 3 ja 4: R, F, M väärtuste arvutamine
# ==========================================
# Grupeerime andmed kliendi ID järgi ja teeme vajalikud arvutused korraga
rfm = df.groupby('customer_id').agg({
    # Recency jaoks leiame viimase ostu kuupäeva
    'sale_date': lambda x: (today - x.max()).days,
    # Frequency jaoks loeme kokku tehingute arvu (eeldusel, et veerg 'sale_id' on olemas)
    'sale_id': 'count',
    # Monetary jaoks liidame kokku kõik ostud summaliselt
    'total_price': 'sum'
})

# Nimetame veerud ümber, et kood oleks loetav
rfm.columns = ['Recency', 'Frequency', 'Monetary']


# ==========================================
# SAMM 5: Skooride määramine (1-5) kvintiilide alusel
# ==========================================
# NB! Recency puhul: mida VÄHEM päevi tagasi klient ostis (madal väärtus), seda PAREM klient (skoor 5).
# Seetõttu on labels=[5, 4, 3, 2, 1] ehk tagurpidi.
rfm['R_score'] = pd.qcut(rfm['Recency'], q=5, labels=[5, 4, 3, 2, 1])

# Frequency ja Monetary puhul: mida suurem number, seda parem skoor (1 kuni 5).
# Kasutame duplicates='drop', juhuks kui paljudel klientidel on sama ostude arv (nt ainult 1 ost).
rfm['F_score'] = pd.qcut(rfm['Frequency'].rank(method='first'), q=5, labels=[1, 2, 3, 4, 5])
rfm['M_score'] = pd.qcut(rfm['Monetary'], q=5, labels=[1, 2, 3, 4, 5])


# ==========================================
# SAMM 6: RFM koondskoor ja segmenteerimine
# ==========================================
# Muudame skoorid täisarvudeks, et saaksime need kokku liita
rfm['R_score'] = rfm['R_score'].astype(int)
rfm['F_score'] = rfm['F_score'].astype(int)
rfm['M_score'] = rfm['M_score'].astype(int)

# Arvutame summaarse skoori (vahemik 3 kuni 15)
rfm['RFM_Score'] = rfm['R_score'] + rfm['F_score'] + rfm['M_score']

# Funktsioon segmentide määramiseks summaarse skoori põhjal
def mairatle_segment(score):
    if 13 <= score <= 15:
        return 'VIP Champions'
    elif 10 <= score <= 12:
        return 'Loyal'
    elif 7 <= score <= 9:
        return 'Potential'
    elif 4 <= score <= 6:
        return 'At Risk'
    elif score == 3:
        return 'Lost'
    else:
        return 'Määramata'

# Rakendame funktsiooni igale kliendile
rfm['Segment'] = rfm['RFM_Score'].apply(mairatle_segment)


# ==========================================
# VÄLJUND: Segmentide kokkuvõttetabel
# ==========================================
print("\n" + "="*50)
# Loeme kokku kliendid igas segmendis
segment_counts = rfm['Segment'].value_counts()
# Arvutame protsentuaalse osakaalu
segment_percentages = rfm['Segment'].value_counts(normalize=True) * 100

# Paneme tulemused ühte ilusasse tabelisse kokku
kokkuvote = pd.DataFrame({
    'Klientide arv': segment_counts,
    'Osakaal (%)': segment_percentages.round(2)
})

print("             RFM SEGMENTIDE KOKKUVÕTE")
print("="*50)
print(kokkuvote)
print("="*50)

# Kuvame ka esimesed 5 strida uuest RFM tabelist, et näha kliendipõhiseid skoore
print("\nEelvaade kliendipõhistest RFM skooridest:")
rfm.head()

#6. JOONISTE LOOMINE
import plotly.express as px
import pandas as pd

print("--- VISUALISEERIMINE JA RAPORTEERIMINE (KNAFLIK STYLE) ---")

# Globaalsed stiilimuutujad puhta ilme saavutamiseks
GRAY_LIGHT = '#E5E5E5'
GRAY_DARK = '#555555'
COLOR_FOCUS = '#1F77B4'  # Strateegiline sinine fookuseks
FONT_FAMILY = "Arial, sans-serif"

# Teeme kindlaks, et indeks on veergudeks, et customer_id oleks kättesaadav
rfm_plot = rfm.reset_index()

# ==========================================
# DIAGRAMM 1: Kliendisegmentide jaotus (Horisontaalne)
# ==========================================
df_seg_counts = rfm_plot['Segment'].value_counts().reset_index()
df_seg_counts.columns = ['Segment', 'Klientide arv']
df_seg_counts = df_seg_counts.sort_values(by='Klientide arv', ascending=True)

# Värvime ainult suurima segmendi esiletõstmiseks siniseks, teised halliks
max_seg = df_seg_counts.iloc[-1]['Segment']
colors = [COLOR_FOCUS if seg == max_seg else GRAY_LIGHT for seg in df_seg_counts['Segment']]

fig1 = px.bar(
    df_seg_counts, 
    x='Klientide arv', 
    y='Segment',
    text='Klientide arv',
    orientation='h',
    title='<b>SEGMENTIDE SUURUS:</b> Kus asub meie suurim kliendibaas?'
)

fig1.update_traces(marker_color=colors, textposition='outside', textfont_size=12, cliponaxis=False)
fig1.update_layout(
    plot_bgcolor='white',
    font=dict(family=FONT_FAMILY, color='#333333'),
    title=dict(font=dict(size=16), x=0.0, y=0.95),
    xaxis=dict(showgrid=False, visible=False),
    yaxis=dict(title='', showline=False)
)


# ==========================================
# DIAGRAMM 2: Klientide käitumine (Hajuvusdiagramm / Scatter)
# ==========================================
# Määrame käsitsi 10 mahedat ja professionaalset värvitooni segmentide jaoks
knaflik_palette = ["#F16202", "#75A8EB", "#0EA746", "#A8A099", "#8BF98B"]
                   #98DF8A', '#D62728', '#FF9896', '#9467BD', '#C5B0D5']

fig2 = px.scatter(
    rfm_plot, 
    x='Recency', 
    y='Monetary',
    size='Frequency', 
    color='Segment',
    hover_name='customer_id',
    title='<b>STRATEEGILINE VAADE:</b> Hiljutisus (Recency) vs Kogukulu (Monetary)',
    labels={
        'Recency': 'Päevi viimasest ostust (Vähem on parem)', 
        'Monetary': 'Kogukäive (€)', 
        'Segment': 'Kliendisegment'
    },
    log_y=True,
    color_discrete_sequence=knaflik_palette  # Kasutame enda määratud kindlat paletti
)

fig2.update_layout(
    plot_bgcolor='white',
    font=dict(family=FONT_FAMILY, color='#333333'),
    title=dict(font=dict(size=16), x=0.0),
    xaxis=dict(showgrid=True, gridcolor='#F0F0F0', showline=True, linecolor='#CCCCCC'),
    yaxis=dict(showgrid=True, gridcolor='#F0F0F0', showline=False),
    legend=dict(title='', yanchor="top", y=0.99, xanchor="right", x=0.99)
)


# ==========================================
# DIAGRAMM 3: Top 10 VIP klienti kogukulutuse järgi
# ==========================================
top_vip = rfm_plot[rfm_plot['Segment'] == 'VIP Champions'].nlargest(10, 'Monetary').sort_values(by='Monetary', ascending=True)

fig3 = px.bar(
    top_vip, 
    x='Monetary', 
    y='customer_id',
    text='Monetary',
    orientation='h',
    title='<b>TOP 10 VIP CHAMPIONS:</b> Meie kõige väärtuslikumad kliendid kogukulutuse järgi',
    labels={'customer_id': 'Kliendi ID'}
)

fig3.update_traces(
    marker_color=COLOR_FOCUS, 
    texttemplate='%{text}:,.2f} €', 
    textposition='outside',
    cliponaxis=False
)
fig3.update_layout(
    plot_bgcolor='white',
    font=dict(family=FONT_FAMILY, color='#333333'),
    title=dict(font=dict(size=16), x=0.0),
    xaxis=dict(showgrid=False, visible=False),
    yaxis=dict(type='category', title='')
)


# ==========================================
# DIAGRAMM 4: Recency (Värskuse) jaotus (Histogramm)
# ==========================================
fig4 = px.histogram(
    rfm_plot, 
    x='Recency',
    nbins=30,
    title='<b>OSTUAKTIIVSUS:</b> Suur osa klientidest on teinud ostu viimase perioodi jooksul',
    labels={'Recency': 'Päevad viimasest ostust (Recency)', 'count': 'Klientide arv'}
)
fig4.update_traces(marker_color=GRAY_DARK, opacity=0.8, marker_line_color='white', marker_line_width=1)
fig4.update_layout(
    plot_bgcolor='white',
    font=dict(family=FONT_FAMILY, color='#333333'),
    title=dict(font=dict(size=16), x=0.0),
    xaxis=dict(showgrid=False, showline=True, linecolor='#CCCCCC'),
    yaxis=dict(title='Klientide arv', showgrid=True, gridcolor='#F0F0F0')
)


# ==========================================
# DIAGRAMM 5: Ostusageduse (Frequency) jaotus
# ==========================================
fig5 = px.histogram(
    rfm_plot, 
    x='Frequency',
    nbins=20,
    title='<b>OSTUSAGEDUS:</b> Enamik baasist teeb üksikuid oste, fookus on püsiklientidel',
    labels={'Frequency': 'Ostude arv (Frequency)'}
)
fig5.update_traces(marker_color=GRAY_DARK, opacity=0.8, marker_line_color='white', marker_line_width=1)
fig5.update_layout(
    plot_bgcolor='white',
    font=dict(family=FONT_FAMILY, color='#333333'),
    title=dict(font=dict(size=16), x=0.0),
    xaxis=dict(showgrid=False, showline=True, linecolor='#CCCCCC'),
    yaxis=dict(title='Klientide arv', showgrid=True, gridcolor='#F0F0F0')
)


# ==========================================
# DIAGRAMM 6: Segmentide kogupanus käibesse (Monetary panus)
# ==========================================
df_seg_mon = rfm_plot.groupby('Segment')['Monetary'].sum().reset_index().sort_values(by='Monetary', ascending=True)
max_mon_seg = df_seg_mon.iloc[-1]['Segment']
colors_mon = [COLOR_FOCUS if seg == max_mon_seg else GRAY_LIGHT for seg in df_seg_mon['Segment']]

fig6 = px.bar(
    df_seg_mon, 
    x='Monetary', 
    y='Segment',
    text='Monetary',
    orientation='h',
    title='<b>TULUDE JAOTUS:</b> Milline segment toob meile äriliselt suurima tulu?'
)

fig6.update_traces(
    marker_color=colors_mon, 
    texttemplate='%{text}:,.0f} €', 
    textposition='outside',
    cliponaxis=False
)
fig6.update_layout(
    plot_bgcolor='white',
    font=dict(family=FONT_FAMILY, color='#333333'),
    title=dict(font=dict(size=16), x=0.0),
    xaxis=dict(showgrid=False, visible=False),
    yaxis=dict(title='', showline=False)
)

# Kuvame kõik joonised järjest
fig1.show()
fig2.show()
fig3.show()
fig4.show()
fig5.show()
fig6.show()

# ==========================================
# ÄRILINE ARVUTUS RAPORDI JAOKS
# ==========================================
kokku_kaive = rfm['Monetary'].sum()
vip_kaive = rfm[rfm['Segment'] == 'VIP Champions']['Monetary'].sum()
vip_protsent = (vip_kaive / kokku_kaive) * 100
vip_arv = len(rfm[rfm['Segment'] == 'VIP Champions'])
at_risk_arv = len(rfm[rfm['Segment'] == 'At Risk'])

print(f"\n[Süsteemne teade]: Arvutused edukad. VIP käibeosakaal: {vip_protsent:.1f}%")
