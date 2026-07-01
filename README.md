# DACA Portfoolio
 
**Programm:** Data Analyst Career Accelerator (DACA)
**Osaleja:** [Tekla Relika Ani]
**Algus:** [27.04.2026]

## Kokkuvõte : ....
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

### Meeskonnatöö - Roll: Kliendiandmete uurija (Customer Data Explorer)
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
Kasutasin AI-d SQL päringute koostamise ja kontrollimise toetamiseks. Kontrollisin kõik tulemused iseseisvalt, võrreldes päringute väljundeid Supabase'i andmebaasis.

#### Peamised õppetunnid
Andmete sisestamisel on oluline kasutada ühtset vormingut. Näiteks käsitleb SQL vaikimisi väärtusi "Tallinn" ja "tallinn" erinevate kirjetena, mis võib moonutada analüüsi tulemusi. Samuti õppisin kasutama COUNT() ja DISTINCT funktsioone andmete kvaliteedi hindamiseks.

#### Failid
- [**WEEK1_sales_customers_exploration.sql**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/2edd6e719d1a7c614f263c25ea5599272f845597/WEEK1_sales_customers_exploration.sql)-- minu SQL päringud
- [**WEEK1_results_screenshots**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/e54de9f223daea5405f11b48740e84738bea25ff/WEEK1_results_screenshots.pdf) -- päringute tulemused
- [**Meeskonna Data Landscape slaid**](https://github.com/kaarusdoris-a11y/Sales-Analytics/blob/2c2bdfb12560f9cf51af47be433ac27316988370/Data_Landscape_Week1.pdf)

## Week 2 – SQL Data Cleaning: UrbanStyle tooteandmete puhastamine
Puhastasin UrbanStyle'i tooteandmeid, et parandada andmete kvaliteeti enne müügi- ja laoseisu analüüsi. Keskendusin duplikaatide, NULL-väärtuste ja võimalike formaadivigade leidmisele.

#### Kasutatud SQL teemad
- Duplikaatide tuvastamine ja sorteerimine (GROUP BY, HAVING, ROW_NUMBER)
- NULL väärtusted
- Andmetüüpide kontroll

### Meeskonnatöö - Roll: Tooteandmete puhastaja (Product Data Cleaner)
Analüüsisin products tabelit ning koostasin puhastamisraporti koos SQL skriptiga.

#### Peamised tulemused
- Kokku 362 toodet
- 12 duplikaatset tootenime
- 0 NULL väärtust toote nimes
- 0 NULL väärtust kategoorias
- 0 NULL jaehinnas
- 0 NULL omahinnas
- Loogilisi hinnavigu pole
- 5 tootekategooriat

#### Äriline järeldus
Tooteandmete kvaliteet oli üldiselt hea, sest kriitilised väljad ei sisaldanud puuduvaid väärtusi. Suurimaks probleemiks olid 12 duplikaatset tootenime, mis võivad põhjustada ebatäpseid müügi-, lao- ja tooteanalüüse. Enne aruannete koostamist tuleks duplikaadid eemaldada või ühtlustada, et iga toode oleks süsteemis esindatud ainult ühe kirjena.

#### AI kasutamine
Kasutasin AI-d, ROW_NUMBER() ja duplikaatide leidmise SQL-päringute koostamise toetamiseks. Kontrollisin kõik tulemused iseseisvalt Supabase'i andmebaasis ning testisin päringuid enne muudatuste tegemist testkoopial.

#### Peamised õppetunnid
- Enne andmete muutmist tuleb alati töötada testtabeliga.
- ROW_NUMBER() on tõhus viis duplikaatide leidmiseks.
- Andmete puhastamine on usaldusväärsete analüüside eelduseks.
  
#### Failid
- [**WEEK2_products_cleaning.sql**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/d1aef06b2d1dfef876f832e291e42b119a7535fd/WEEK2_products_cleaning.sql)-- minu SQL päringud
- [**WEEK2_results_screenshots**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/8eedc1ef905326930734597ddc56347d11676265/WEEK2_results_screenshots.pdf) -- päringute tulemused
- [**Meeskonna Data Landscape slaid**](https://github.com/kaarusdoris-a11y/Sales-Analytics/blob/396ec93e896f27c3a9ce931d103dd75b9b423381/Data_Landscape_Week2.pdf)
 
## Week 3 – SQL JOINs
Kasutasin JOIN päringuid, et ühendada müügi-, toote- ja laoseisu andmed ning analüüsida müümata tooteid, populaarsemaid kategooriaid ja inventuuri efektiivsust.

#### Kasutatud SQL teemad
- LEFT JOIN
- INNER JOIN
- JOIN mitme tabeli vahel
- Agregaatfunktsioonid
- GROUP BY

### Meeskonnatöö - Roll: Toodete ja inventuuri analüüs (Products + Inventory Analyst)
Analüüsisin tabeleid products, sales ja inventory, et hinnata toodete müüki ning laoseisu.

#### Peamised tulemused
- Leidsin 12 toodet, mida ei olnud kunagi müüdud.
- 231 toodet olid märgistatud staatusega "Telli juurde".
- Jalanõud ja meeste riided moodustasid kokku üle 50% kogu müügist.
- Laoseisu ja müügi võrdlus näitas võimalikku anomaaliat – olemasolevast laovarust piisaks praeguse müügitempo juures ligikaudu 61 aastaks.
  
#### Äriline järeldus
Analüüs viitas sellele, et ettevõtte laoseis võib olla oluliselt suurem kui tegelik nõudlus õigustab. Eriti tasuks üle vaadata müügita tooted ning madalama nõudlusega kategooriad, nagu aksessuaarid ja lasteriided. Samuti tuleks kontrollida laoseisu andmete õigsust, sest väga suur laovaru seob kapitali ja suurendab aegumise ning ladustamise kulusid.

#### Soovitused
- Eemaldada või ümber hinnata tooted, mida ei ole kunagi müüdud.
- Vähendada madala nõudlusega toodete laoseisu.
- Kontrollida inventuuriandmete õigsust ja laoseisu planeerimise loogikat.
- Keskenduda suurema nõudlusega kategooriate (jalanõud ja meeste riided) varude optimeerimisele.

#### AI kasutamine
Kasutasin AI-d erinevate JOIN-tüüpide mõistmiseks ja päringute kontrollimiseks. Võrdlesin LEFT JOIN ja INNER JOIN tulemusi ning kontrollisin järeldused SQL päringute väljundite põhjal.

#### Peamised õppetunnid
- Vale JOIN-i tüübi valimine võib muuta analüüsi tulemusi oluliselt.
- Mitme tabeli ühendamine võimaldab leida äriliselt väärtuslikke seoseid, mida ühest tabelist ei näe.
- Inventuuri analüüsimisel tuleb alati võrrelda laoseisu tegeliku müügiga.

#### Failid
- [**WEEK3_products_sales_join.sql**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/020fb87252c7cbd9920928c8f88ff327e4ba59be/WEEK3_products_sales_join.sql)-- minu SQL päringud
- [**WEEK3_results_screenshots**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/17bd10dcc18b9e46c73661a79642394f755d0a06/WEEK3_results_screenshots.pdf) -- päringute tulemused
- [**Meeskonna Data Landscape slaid**](https://github.com/kaarusdoris-a11y/Sales-Analytics/blob/1ef0426c6e6526395a2ac73ad5b3dcb5185736b4/Data_Landscape_Week3.pdf)

## Week 4 – SQL Aggregation
Analüüsisin UrbanStyle'i turunduskanalite tulemuslikkust, et hinnata, millised kanalid toovad kõige rohkem kliente, käivet ja suurima keskmise tellimusväärtuse.

#### Kasutatud SQL teemad
- GROUP BY
- HAVING
- Agregaatfunktsioonid (COUNT, SUM, AVG)
- CTE (Common Table Expression)

## Meeskonnatöö - Roll: Turunduskanalite ROI (Marketing Campaign Effectiveness)
Analüüsisin tabelite sales, customers ja weblogs andmeid ning koostasin turunduskanalite võrdluse.

#### Peamised tulemused
- Suurim keskmine ostukorv: Instagram Ads – 354 €
- Kõige efektiivsem turunduskanal: Google Organic – 26%
- Madalaima efektiivsusega kanal: TikTok – 4%
- Tugevaimad müügikuud: juuli ja detsember
- Suurim müügikasv: november → detsember (+60%)
- Suurim müügilangus: detsember → jaanuar (−44%)

#### Äriline järeldus
Leidsin, et Google Organic oli kõige efektiivsem turunduskanal, mis viitab sellele, et orgaaniline nähtavus toob ettevõttele kvaliteetseid kliente väiksema turunduskuluga. Samas Instagram Ads tõi suurima keskmise tellimusväärtusega ostud. TikToki tulemused olid märgatavalt nõrgemad, mistõttu tasuks selle kanali investeeringud üle vaadata või kampaaniaid optimeerida.

#### Soovitused
- Suurendada investeeringuid Google Organic kanalisse.
- Jätkata Instagram Ads kampaaniaid suure ostukorvi väärtuse tõttu.
- Analüüsida ja optimeerida TikToki kampaaniaid või hinnata nende tasuvust.
- Parandada turunduskanalite andmete kogumist, et vähendada NULL väärtusi.
- Planeerida suuremad turunduskampaaniad enne juulit ja detsembrit, mil müük on ajalooliselt kõige tugevam.

#### AI kasutamine
Kasutasin AI-d CTE ja agregaatpäringute koostamise toetamiseks ning SQL-päringute optimeerimiseks. Kontrollisin tulemused SQL päringute väljundite ja arvutatud näitajate põhjal.

#### Peamised õppetunnid
- Kõik SELECT lauses olevad veerud, mis ei ole agregaatfunktsiooni sees, peavad olema lisatud GROUP BY lausesse.
- CTE muudab keerukad SQL-päringud loetavamaks ja lihtsamini hallatavaks.
- Agregaatfunktsioonid võimaldavad muuta suure andmemahu selgeteks ärinäitajateks.

#### Failid
- [**WEEK4_marketing_roi.sql**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/7dc13e865f0dc16f6ae9b4967bf71ae2f4763346/WEEK4_marketing_roi.sql)-- minu SQL päringud
- [**WEEK4_results_screenshots**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/9ea37fce605a8b44fd0e9d4689fbcf6bab5b719d/WEEK4_results_screenshots.pdf) -- tulemuste pilt
- [**Meeskonna Data Landscape slaid**](https://github.com/kaarusdoris-a11y/Sales-Analytics/blob/0be8da608489ced4afa9845a2c4c8299adc69b33/Data_Landscape_Week4.pdf)

## Week 5 – Power BI: Müügikanalite efektiivsuse visualiseerimine
Lõin Power BI dashboardi, et visualiseerida müügikanalite tulemuslikkust ja klientide kasvu ajas ning toetada juhtkonna otsuste tegemist.

#### Kasutatud tehnoloogiad
- SQL (PostgreSQL / Supabase)
- Power BI

### Meeskonnatöö - Roll: Müügikanalite analüüs (Marketing Dashboard Analyst)
Koostasin SQL-päringud vajalike andmete leidmiseks ning visualiseerisin tulemused Power BI-s, valmistasin interaktiivse dashboardi.

#### Peamised tulemused
- Avastasin, et suurima käibega kauplused on Tallinna kauplus (1,09M) ja e-pood (1,01M)
- Need kaks kanalit tõid ka kõige rohkem uusi kliente.
- Alates 2022. aastast on uute klientide kasv olnud selges langustrendis.

#### Äriline järeldus
Tallinna kauplus ja e-pood on ettevõtte kõige olulisemad müügikanalid ning nende arendamine võiks olla prioriteet. Samas näitab uute klientide vähenemine pärast 2022. aastat, et ettevõttel võib olla raskusi uute klientide leidmisega. Kui trend jätkub, võib see tulevikus mõjutada müügikasvu.

#### Soovitused
- Analüüsida täpsemalt, mis muutus alates 2022. aastast (turunduseelarve, kampaaniad, konkurents või kliendikäitumine).
- Käivitada uutele klientidele suunatud kampaaniaid ja lojaalsusprogramme.
- Jälgida dashboardi regulaarselt, et märgata muutusi võimalikult varakult.

#### Peamised õppetunnid
- Korrektsed ja puhastatud andmed on usaldusväärsete visualiseeringute aluseks.
- Hästi kujundatud dashboard aitab märgata trende ja toetab kiiremat otsustamist.
- Interaktiivsed filtrid (slicer) muudavad dashboardi kasutajasõbralikumaks ja paindlikumaks.

#### Failid  
 [**WEEK5_PowerBI_results_screenshot**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/3ed08c10fc92f80542a8f1d50410aeaa5dbff7b4/WEEK5_Visual_Design_PowerBI.png)

## Week 6. Visualization Data
  - Andmete visualiseerimine Power BI
  - Data storytelling
   #### Peamised õppetunnid
- Vähem on rohkem.
    
### Meeskonnatöö
#### Roll - Tallinna kaupluse analüüs
- Analüüsisin SQL´iga Tallinna kauplust. Visualiseerisin Power BI´ga.

  [**WEEK6_PowerBI_Dashboard_screenshot**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/ee10ae2dd4d017e1d69a9071c2780f67bdd3c988/WEEK6_Visual_Design_PowerBI.png)


 
## Oskused
 
- **SQL:** PostgreSQL, Supabase
- **Python:** pandas, plotly (tulemas...)
- **Visualiseerimine:** Power BI / Streamlit (tulemas...)
- **Tööriistad:** Git, GitHub, VS Code
 
## Kontakt 
    teklarelikaani@gmail.com



