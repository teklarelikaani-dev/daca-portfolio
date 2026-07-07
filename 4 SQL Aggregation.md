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

[**Week 0**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/0%20Onboarding.md)    [**Week 1**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/1%20SQL%20Basics.md)    [**Week 2**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/2%20SQL%20Data%20Cleaning.md)    [**Week 3**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/3%20SQL%20JOINs.md)    [**Week 4**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/4%20SQL%20Aggregation.md)    [**Week 5**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/5%20Power%20BI.md)    [**Week 6**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/6%20Power%20BI%20Data%20Storytelling%20Dashboard.md)    [**Week 7**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/7%20Python%20RFM%20anal%C3%BC%C3%BCs.md)    [**Week 8**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/8%20Python%20APIs%20%26%20Automation.md)
