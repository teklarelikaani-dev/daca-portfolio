# DACA Portfoolio
 
**Programm:** Data Analyst Career Accelerator (DACA)
**Osaleja:** [Tekla Relika Ani]
**Algus:** [27.04.2026]

## Kokkuvõte :
#### Meeskonnatöö: [**Sales Analytics Team**](https://github.com/kaarusdoris-a11y/Sales-Analytics)

# UrbanStyle projekt nädalate kaupa

## Week 0 – Onboarding: Töökeskkonna seadistamine

Seadistasin andmeanalüütiku tööks vajalikud tööriistad ning lõin keskkonna, kus saan hallata andmeid, kirjutada SQL päringuid, visualiseerida tulemusi ja versioonihaldust kasutada.

#### Seadistatud tööriistad
- Git & GitHub – versioonihaldus ja projektide haldamine
- Supabase – PostgreSQL andmebaas
- VS Code – arenduskeskkond
- Python – andmeanalüüs ja automatiseerimine
- Power BI – andmete visualiseerimine
- NotebookLM – õppematerjalide organiseerimine ja kokkuvõtete tegemine

#### Mida õppisin
- Mõistsin, kuidas erinevad tööriistad moodustavad ühe andmeanalüüsi töövoo.
- Õppisin kasutama GitHubi projektide versioonihalduseks ja muudatuste jälgimiseks.
- Sain ühenduse Power BI ja Supabase'i vahel, et kasutada andmebaasi andmeid visualiseerimiseks.
- Seadistasin Pythoni keskkonna tulevaste andmeanalüüsi projektide jaoks.
- Õppisin, kui oluline on hästi organiseeritud töökeskkond efektiivseks analüüsiks.

#### AI kasutamine
Kasutasin ChatGPT-d ja NotebookLM-i seadistusjuhendite mõistmiseks ning võimalike vigade lahendamiseks. Kontrollisin, et kõik tööriistad töötasid omavahel korrektselt (GitHub, Supabase, Power BI ja Python).

#### Miks see on oluline?
Korralikult seadistatud töökeskkond võimaldab alustada analüüsi ilma tehniliste takistusteta ning tagab, et projektid on versioonihallatud, reprodutseeritavad ja hõlpsasti jagatavad meeskonnaga.

## Week 1 – SQL Basics: UrbanStyle andmete uurimine

Tutvusin UrbanStyle'i kliendiandmetega ning õppisin kasutama SQL päringuid andmete filtreerimiseks, otsimiseks ja kvaliteedi hindamiseks.

#### Kasutatud SQL teemad
- Andmete lugemine (SELECT, FROM, AS, LIMIT, WHERE, BETWEEN, IN, LIKE, AND, OR) 
- Duplikaatide tuvastamine (COUNT, DISTINCT)

### Meeskonnatöö - Roll: Kliendiandmete uurija ( Customer Data Explorer )

Analüüsisin customers tabelit, et hinnata kliendiandmete kvaliteeti ning koostada ülevaade andmestikust.

#### Peamised tulemused
- Kokku 3150 klienti
- 380 kliendil puudus e-posti aadress
- Perekonnanimi puudus 0 kliendil
- 3150 e-posti aadressist oli 2640 unikaalsed, mis viitab duplikaatidele
- Kliendid olid registreeritud ajavahemikul 2.01.2020 – 27.02.2025
- Kliendid pärinesid 12 Eesti linnast (Tallinn, Tartu, Narva, Pärnu, Rakvere, Viljandi, Võru, Valga, Paide, Jõhvi, Kuressaare ja Haapsalu)

#### Äriline järeldus

Leidsin, et kliendiandmetes esineb puuduvaid ja duplikaatseid e-posti aadresse, mis võib mõjutada turunduskampaaniate täpsust ning kliendisuhtlust. Enne analüüside ja kampaaniate tegemist tuleks andmed puhastada ning kasutada ühtset andmesisestuse standardit.

#### AI kasutamine

Kasutasin ChatGPT-d SQL päringute koostamise ja kontrollimise toetamiseks. Kontrollisin kõik tulemused iseseisvalt, võrreldes päringute väljundeid Supabase'i andmebaasis.

#### Peamised õppetunnid

Andmete sisestamisel on oluline kasutada ühtset vormingut. Näiteks käsitleb SQL vaikimisi väärtusi "Tallinn" ja "tallinn" erinevate kirjetena, mis võib moonutada analüüsi tulemusi. Samuti õppisin kasutama COUNT() ja DISTINCT funktsioone andmete kvaliteedi hindamiseks.

#### Failid
- [**WEEK1_sales_customers_exploration.sql**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/2edd6e719d1a7c614f263c25ea5599272f845597/WEEK1_sales_customers_exploration.sql)-- minu SQL päringud
- [**WEEK1_results_screenshots**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/e54de9f223daea5405f11b48740e84738bea25ff/WEEK1_results_screenshots.pdf) -- päringute tulemused
- [**Meeskonna Data Landscape slaid**](https://github.com/kaarusdoris-a11y/Sales-Analytics/blob/2c2bdfb12560f9cf51af47be433ac27316988370/Data_Landscape_Week1.pdf)


## Week 2: SQL Andmete Puhastamine
- Duplikaatide tuvastamine ja sorteerimine (GROUP BY, HAVING, ROW_NUMBER)
- NULL väärtuste mõistmine
- Andmeformaadid ja tüübikonversioonid
#### Peamised õppetunnid  
- Oluliste muudatuste tegemiseks kasutada esmalt test tabelit
  
### Meeskonnatöö
#### Roll - Tooteandmete puhastaja (Product Data Cleaner)
- Uurisin "Products" tabelit SQL päringutega 
  
#### Failid
- [**week2products_cleaning.sql**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/03b9365e94ef3f6d389b4c86bf2d563ff1ffeae9/week2products_cleaning.sql)-- minu SQL päringud
- [**week2_results_screenshot**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/3455d12b8b52790aade22ea1749a684f4a7f527f/week2_results_screenshot.pdf) -- tulemuste pilt

#### Osalesin meeskonna andmemaastiku koostamisel
- [**Meeskonna Data Landscape slaid**](https://github.com/kaarusdoris-a11y/Sales-Analytics/blob/396ec93e896f27c3a9ce931d103dd75b9b423381/Data_Landscape_Week2.pdf)
 

## Week 3. SQL JOINs
  - Andmete lugemine mitmest tabelist ja tabelite ühendamine (JOIN) 
   #### Peamised õppetunnid
- Vale JOIN-i tüübi valimine muudab päringu tulemust drastiliselt.

### Meeskonnatöö
#### Roll - Tooted + Inventuur (LEFT JOIN)
- Müümata toodete ja inventuuri analüüs. Tabelid: products, sales, inventory

#### Failid
- [**week3products_sales_join.sql**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/19e73b37b04521426db3e83bdc75f2df09914def/week3products_sales_join.sql)-- minu SQL päringud
- [**week3_results_screenshot**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/402820b6edc96dd4ae326df0c8bd3be7b99e7af7/week3_results_screenshot.pdf) -- tulemuste pilt

#### Osalesin meeskonna andmemaastiku koostamisel
- [**Meeskonna Data Landscape slaid**](https://github.com/kaarusdoris-a11y/Sales-Analytics/blob/1ef0426c6e6526395a2ac73ad5b3dcb5185736b4/Data_Landscape_Week3.pdf)


## Week 4. SQL Agregatsioon
  - Andmete grupeerimine (GROUP BY)
  - HAVING ja agregaatfunktsioonid
  - CTE
   #### Peamised õppetunnid
- Kõik SELECT reas olevad veerud, mis ei ole agregaatfunktsiooni sees, peavad olema kirjas GROUP BY listis.

### Meeskonnatöö
#### Roll - Turunduskampaaniate ROI (Marketing Campaign Effectiveness)
- Analüüsisin turunduskanalite efektiivsust. Tabelid: sales, customers, weblogs.

#### Failid
- [**week4marketing_roi.sql**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/ff75632c72a825b148b42bbb473292a0ee6943df/week4marketing_roi.sql)-- minu SQL päringud
- [**week4_results_screenshot**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/ff75632c72a825b148b42bbb473292a0ee6943df/week4_results_screenshot.pdf) -- tulemuste pilt

#### Osalesin meeskonna andmemaastiku koostamisel
- [**Meeskonna Data Landscape slaid**](https://github.com/kaarusdoris-a11y/Sales-Analytics/blob/0be8da608489ced4afa9845a2c4c8299adc69b33/Data_Landscape_Week4.pdf)

## Week 5. Visualization Design
  - Power BI ühendamine Supabase´iga
  - Andmete visualiseerimine Power BI
   #### Peamised õppetunnid
- Õiged andmed loovad korrektsed graafikud.
    
### Meeskonnatöö
#### Roll - Müügikanalite efektiivsus
- Analüüsisin SQL´iga müügikanalite efektiivsust ja klientide kasvu. Visualiseerisin Power BI´ga.
  
 [**week5_results_screenshot**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/b39e3cf42552debe1f4e9f15c927d96a3bb91c2e/Week5_Visual_Design_PowerBI.png)

## Week 6. Visualization Data
  - Andmete visualiseerimine Power BI
  - Data storytelling
   #### Peamised õppetunnid
- Vähem on rohkem.
    
### Meeskonnatöö
#### Roll - Tallinna kaupluse analüüs
- Analüüsisin SQL´iga Tallinna kauplust. Visualiseerisin Power BI´ga.

  [**week6_results_screenshot**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/3292711a9ca78307a276861a4e7596399ac4cc38/Week6_Visual_Design_PowerBI.png)


 
## Oskused
 
- **SQL:** PostgreSQL, Supabase
- **Python:** pandas, plotly (tulemas...)
- **Visualiseerimine:** Power BI / Streamlit (tulemas...)
- **Tööriistad:** Git, GitHub, VS Code
 
## Kontakt 
    teklarelikaani@gmail.com



