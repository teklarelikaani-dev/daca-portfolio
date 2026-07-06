## Week 4 – SQL Aggregation
Analüüsisin UrbanStyle'i turunduskanalite tulemuslikkust, et hinnata, millised kanalid toovad kõige rohkem kliente, käivet ja suurima keskmise tellimusväärtuse.

#### Kasutatud SQL teemad
- GROUP BY
- HAVING
- Agregaatfunktsioonid (COUNT, SUM, AVG)
- CTE (Common Table Expression)

### Meeskonnatöö - Roll: Turunduskanalite ROI (Marketing Campaign Effectiveness)
Analüüsisin tabelite sales, customers ja weblogs andmeid ning koostasin turunduskanalite võrdluse.

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
