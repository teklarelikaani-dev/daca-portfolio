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

[**Järgmine Week 3**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/8c2772a12b26c19e8777655dc4a26248acfe5e03/3%20SQL%20JOINs.md)
