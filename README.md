# DACA Portfoolio
 
**Programm:** Data Analyst Career Accelerator (DACA)
**Osaleja:** [Tekla Relika Ani]
**Algus:** [27.04.2026]

## Kokkuvõte
10 nädalat tagasi alustasin SQL-i õppimisega. Täna ehitan automatiseeritud andmeanalüüsi lahendusi, mis ühendavad SQL-i, Pythoni ja Power BI ning aitavad ettevõttel teha kiiremaid ja paremaid äriotsuseid. Tänu varasemale kogemusele kaubanduses ei analüüsi ma ainult andmeid – ma otsin võimalusi, kuidas nende põhjal äritulemusi parandada.

Selles portfoolios näitan, kuidas:
- puhastasin ja ühendasin üle 10 000 müügitehingu SQL-i ja Pythoni abil;
- analüüsisin klientide, toodete, müügi ja turunduse andmeid;
- koostasin interaktiivseid Power BI dashboarde juhtidele;
- ehitasin automatiseeritud Pythoni andmepipeline'i, mis uuendab KPI-d ja visualiseeringud automaatselt Supabase'i andmete põhjal;
- koostasin RFM kliendisegmendid ning pakkusin andmetel põhinevaid ärisoovitusi.

# UrbanStyle projekt nädalate kaupa
| |
|---| 
| [**WEEK 0 Onboarding**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/5e4603fedd2c270bdb9c5514b663618e5319ad76/Onboarding.md) | 
| [**WEEK 1 SQL Basics**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/2688e5b521cb176f0afbf1fa3683e22b0acdb58a/SQL%20Basics.md) | 
| [**WEEK 2 SQL Data Cleaning**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/aafaea18590e92ec95334792e5a437e546bfb261/2%20SQL%20Data%20Cleaning.md) | 
| WEEK 3 | 
| [**WEEK 4 SQL Aggregation**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/7b0380a5c2450343626a4ae1955b176d2acfed6b/SQL%20Aggregation.md) | 
| WEEK 5 | 
| WEEK 6 | 
| WEEK 7 | 
| [**WEEK 8 Python APIs & Automation**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/f85716dde9191dacb7159a812fc6c2f003364344/8%20Python%20APIs%20%26%20Automation.md) |

#### Meeskonnatöö: [**Sales Analytics Team**](https://github.com/kaarusdoris-a11y/Sales-Analytics)




- Andmete pu
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
Kasutasin AI-d erinevate JOIN-tüüpide kirjutamiseks, mõistmiseks ja päringute kontrollimiseks. Võrdlesin LEFT JOIN ja INNER JOIN tulemusi ning kontrollisin järeldused SQL päringute väljundite põhjal.

#### Peamised õppetunnid
- Vale JOIN-i tüübi valimine võib muuta analüüsi tulemusi oluliselt.
- Mitme tabeli ühendamine võimaldab leida äriliselt väärtuslikke seoseid, mida ühest tabelist ei näe.
- Inventuuri analüüsimisel tuleb alati võrrelda laoseisu tegeliku müügiga.

#### Failid
- [**WEEK3_products_sales_join.sql**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/020fb87252c7cbd9920928c8f88ff327e4ba59be/WEEK3_products_sales_join.sql)-- minu SQL päringud
- [**WEEK3_results_screenshots**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/17bd10dcc18b9e46c73661a79642394f755d0a06/WEEK3_results_screenshots.pdf) -- päringute tulemused
- [**Meeskonna Data Landscape slaid**](https://github.com/kaarusdoris-a11y/Sales-Analytics/blob/1ef0426c6e6526395a2ac73ad5b3dcb5185736b4/Data_Landscape_Week3.pdf)

## Week 4 – SQL Aggregation
 Probleem: CEO vajab juhatuse koosolekuks koondnumbreid. Iga domeen (müük, kliendid, inventuur, turundus) peab andma oma koondandmed. Seekord ei piisa lihtsast SELECT-ist — vaja on GROUP BY, HAVING ja CTE-dega ehitatud ärianalüüse.

#### Kasutatud SQL teemad
- GROUP BY
- HAVING
- Agregaatfunktsioonid (COUNT, SUM, AVG)
- CTE (Common Table Expression)

### Meeskonnatöö - Roll: Turunduskanalite ROI (Marketing Campaign Effectiveness)
Analüüsisin tabelite sales, customers ja weblogs andmeid, et hinnata, millised kanalid toovad kõige rohkem kliente, käivet ja suurima keskmise tellimusväärtuse.

#### Peamised tulemused
- Suurim keskmine ostukorv: Instagram Ads – 354 €
- Kõige efektiivsem turunduskanal: Google Organic – 26%
- Madalaima efektiivsusega kanal: TikTok – 4%
- Tugevaimad müügikuud: juuli ja detsember
- Suurim müügikasv: november → detsember (+60%)
- Suurim müügilangus: detsember → jaanuar (−44%)

#### Äriline järeldus
Ettevõte sai teada, et Google Organic oli kõige efektiivsem turunduskanal, mis viitab sellele, et orgaaniline nähtavus toob ettevõttele kvaliteetseid kliente väiksema turunduskuluga. Samas Instagram Ads tõi suurima keskmise tellimusväärtusega ostud. TikToki tulemused olid märgatavalt nõrgemad, mistõttu tasuks selle kanali investeeringud üle vaadata või kampaaniaid optimeerida.

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
 - [**WEEK5_PowerBI_results_screenshot**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/3ed08c10fc92f80542a8f1d50410aeaa5dbff7b4/WEEK5_Visual_Design_PowerBI.png)

## Week 6 – Power BI Data Storytelling
Analüüsisin UrbanStyle'i Tallinna kaupluse müügitulemusi SQL päringute abil ning koostasin Power BI-s interaktiivse dashboardi, mis aitab juhtkonnal hinnata kaupluse tulemuslikkust aastatel 2023–2024.

#### Kasutatud tehnoloogiad
- SQL (PostgreSQL / Supabase)
- Power BI
  
### Meeskonnatöö - Roll: Tallinna kaupluse analüüs (Tallinn Store Analyst)
Koostasin SQL-päringud Tallinna kaupluse andmete analüüsimiseks ning visualiseerisin tulemused Power BI dashboardil.

#### Peamised tulemused
- Tallinna kaupluse kogukäive oli 1,02 miljonit eurot, mis moodustas 38% ettevõtte kogumüügist.
- Aastal 2024 taastus müük kiiresti pärast jaanuarikuu langust ning lõppes rekordilise käibega.
- Keskmine ostukorvi väärtus oli 287 €.
- Alla 25-aastased kliendid moodustasid ainult 9% klientidest.
- 43% klientidest ei kuulunud lojaalsusprogrammi.

#### Äriline järeldus
Tallinna kauplus on ettevõtte üks olulisemaid müügikanaleid ning selle tulemused näitavad tugevat taastumist 2024. aastal. Samas viitab noorte klientide väike osakaal sellele, et ettevõte ei jõua piisavalt hästi noorema sihtrühmani. Samuti näitab lojaalsusprogrammi madal kasutus, et olemasolevate klientide pikaajalist hoidmist saab parandada.

#### Soovitused
- Korrata turunduskampaaniaid, mis aitasid pärast jaanuarikuu müügilangust kiire taastumise saavutada.
- Suunata rohkem turundustegevusi alla 25-aastaste klientide kaasamiseks, näiteks sotsiaalmeedia kampaaniate kaudu.
- Arendada lojaalsusprogrammi ja motiveerida rohkem kliente sellega liituma.

#### Peamised õppetunnid
- Hästi kujundatud dashboard räägib loo ka ilma pika selgituseta.
- Vähem visualiseeringuid annab sageli selgema ülevaate kui suur hulk erinevaid graafikuid.
- Data storytelling aitab muuta andmed juhtidele kiiresti arusaadavaks ning toetab otsuste tegemist.

#### Miks ma selle dashboardi nii kujundasin?
Dashboard kujundati põhimõttel "Overview first, details on demand". Ülemises reas kuvatakse kolm peamist KPI-d, keskel müügitrendid ja kliendisegmendid ning alumises reas konkreetsed ärilised soovitused. Selline ülesehitus võimaldab juhil mõne minutiga saada ülevaate Tallinna kaupluse tulemustest ja peamistest tegevussuundadest.

Dashboard sisaldab 
- 3 KPI-d (müügikäive, tellimuste arv, keskmine ostukorv)
- 4 visualiseeringut (müügitrend kuude lõikes, TOP 5 müüdud toodet, klientide vanusegrupid, lojaalsustasemete jaotus)
- Aastafilter (2023 / 2024) interaktiivseks võrdluseks.
  
#### Failid
- [**WEEK6_PowerBI_Dashboard_screenshot**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/ee10ae2dd4d017e1d69a9071c2780f67bdd3c988/WEEK6_Visual_Design_PowerBI.png)



  

## Kontakt 
    teklarelikaani@gmail.com



