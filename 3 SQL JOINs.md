## Week 3 – SQL JOINs
Probleem: Ettevõttel puudub info milliseid tooted pole kunagi müüdud ja millised on kõige populaarsemad.

#### Kasutatud SQL teemad
- LEFT JOIN
- INNER JOIN
- JOIN mitme tabeli vahel
- Agregaatfunktsioonid
- GROUP BY

### Meeskonnatöö - Roll: Toodete ja inventuuri analüüs (Products + Inventory Analyst)
Kasutasin JOIN päringuid, et ühendada müügi-, toote- ja laoseisu andmed ning analüüsida müümata tooteid, populaarsemaid kategooriaid ja inventuuri efektiivsust.

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

[**Week 0**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/0%20Onboarding.md)    [**Week 1**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/1%20SQL%20Basics.md)    [**Week 2**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/2%20SQL%20Data%20Cleaning.md)    [**Week 3**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/3%20SQL%20JOINs.md)    [**Week 4**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/4%20SQL%20Aggregation.md)    [**Week 5**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/5%20Power%20BI.md)    [**Week 6**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/6%20Power%20BI%20Data%20Storytelling%20Dashboard.md)    [**Week 7**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/7%20Python%20RFM%20anal%C3%BC%C3%BCs.md)    [**Week 8**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/8%20Python%20APIs%20%26%20Automation.md)
