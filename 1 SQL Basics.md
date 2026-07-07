
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
Ettevõte sai teada, et kliendiandmetes esineb puuduvaid ja duplikaatseid e-posti aadresse, mis võib mõjutada turunduskampaaniate täpsust ning kliendisuhtlust. Enne analüüside ja kampaaniate tegemist tuleks andmed puhastada ning kasutada ühtset andmesisestuse standardit.

#### AI kasutamine
Kasutasin AI-d SQL päringute koostamise ja kontrollimise toetamiseks. Kontrollisin kõik tulemused iseseisvalt, võrreldes päringute väljundeid Supabase'i andmebaasis.

#### Peamised õppetunnid
Andmete sisestamisel on oluline kasutada ühtset vormingut. Näiteks käsitleb SQL vaikimisi väärtusi "Tallinn" ja "tallinn" erinevate kirjetena, mis võib moonutada analüüsi tulemusi. Samuti õppisin kasutama COUNT() ja DISTINCT funktsioone andmete kvaliteedi hindamiseks.

#### Failid
- [**WEEK1_sales_customers_exploration.sql**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/2edd6e719d1a7c614f263c25ea5599272f845597/WEEK1_sales_customers_exploration.sql)-- minu SQL päringud
- [**WEEK1_results_screenshots**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/e54de9f223daea5405f11b48740e84738bea25ff/WEEK1_results_screenshots.pdf) -- päringute tulemused
- [**Meeskonna Data Landscape slaid**](https://github.com/kaarusdoris-a11y/Sales-Analytics/blob/2c2bdfb12560f9cf51af47be433ac27316988370/Data_Landscape_Week1.pdf)

[**Week 0**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/0%20Onboarding.md)    [**Week 1**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/1%20SQL%20Basics.md)    [**Week 2**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/2%20SQL%20Data%20Cleaning.md)    [**Week 3**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/3%20SQL%20JOINs.md)    [**Week 4**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/4%20SQL%20Aggregation.md)    [**Week 5**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/5%20Power%20BI.md)    [**Week 6**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/6%20Power%20BI%20Data%20Storytelling%20Dashboard.md)    [**Week 7**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/7%20Python%20RFM%20anal%C3%BC%C3%BCs.md)    [**Week 8**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/8%20Python%20APIs%20%26%20Automation.md)
