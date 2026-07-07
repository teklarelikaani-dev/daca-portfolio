## Week 2 – SQL Data Cleaning: UrbanStyle tooteandmete puhastamine
Probleem: Ettevõtte andmed on kaoses ja vajavad puhastamist enne analüüsi

#### Kasutatud SQL teemad
- Duplikaatide tuvastamine ja sorteerimine (GROUP BY, HAVING, ROW_NUMBER)
- NULL väärtusted
- Andmetüüpide kontroll

### Meeskonnatöö - Roll: Tooteandmete puhastaja (Product Data Cleaner)
Analüüsisin products tabelit, puhastasin UrbanStyle'i tooteandmeid, et parandada andmete kvaliteeti enne müügi- ja laoseisu analüüsi. Keskendusin duplikaatide, NULL-väärtuste ja võimalike formaadivigade leidmisele.

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

[**Week 0**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/0%20Onboarding.md)    [**Week 1**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/1%20SQL%20Basics.md)    [**Week 2**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/2%20SQL%20Data%20Cleaning.md)    [**Week 3**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/3%20SQL%20JOINs.md)    [**Week 4**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/4%20SQL%20Aggregation.md)    [**Week 5**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/5%20Power%20BI.md)    [**Week 6**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/6%20Power%20BI%20Data%20Storytelling%20Dashboard.md)    [**Week 7**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/7%20Python%20RFM%20anal%C3%BC%C3%BCs.md)    [**Week 8**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/8%20Python%20APIs%20%26%20Automation.md)
