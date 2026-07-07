
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

[**Järgmine Week 2**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/e67be1a27a3ace40b1993edcfe5ce0030d7311cf/2%20SQL%20Data%20Cleaning.md)
