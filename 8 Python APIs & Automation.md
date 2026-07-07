## Week 8 – Python APIs & Automation: Automatiseeritud andmepipeline
Probleem: Ettevõttes kulub iga nädal 4 tundi, et lisada uued andmed analüüsiks. Vaja on, et kõik töötaks automaatselt.

#### Kasutatud tehnoloogiad
- Python
- Pandas
- Supabase (PostgreSQL)
- VS Code
  
#### Tööprotsess
Lõin Pythonis automatiseeritud andmepipeline'i, mis laadib UrbanStyle'i andmed Supabase'i andmebaasist, puhastab need, arvutab peamised KPI-d ning koostab automaatselt visualiseeringu müügist nädalate lõikes.
- data_fetcher.py – andmete laadimine Supabase'i andmebaasist.
- transform.py – andmete puhastamine ja ettevalmistamine analüüsiks.
- visualize.py – KPI-de arvutamine ja müügigraafikute loomine.
- pipeline.py – kogu protsessi automatiseerimine ühe käsuga.
- müügi KPI-d
- müügi trend nädalate lõikes
- visualiseeringud Pythonis

#### Äriline järeldus
Automatiseeritud pipeline vähendab ettevõttes käsitsi tehtavat tööd ning tagab, et aruanded põhinevad alati kõige värskematel andmetel. See võimaldab ettevõttel jälgida müügitrende regulaarsemalt ja teha kiiremini andmetel põhinevaid otsuseid.

#### Soovitused
- Kasutada pipeline'i regulaarsete müügiaruannete koostamiseks.
- Ajastada pipeline automaatselt käivituma (näiteks kord nädalas või iga päev), et juhid näeksid alati ajakohaseid tulemusi.
- Laiendada pipeline'i tulevikus täiendavate KPI-de ja visualiseeringutega.

#### AI kasutamine
Kasutasin AI-d Pythoni failide struktuuri planeerimiseks, andmete töötlemise loogika kontrollimiseks ning koodi kirjutamiseks. Kontrollisin, et kõik KPI-d ja visualiseeringud vastaksid Supabase'ist laaditud andmetele.

#### Peamised õppetunnid
- Automatiseerimine vähendab korduvat käsitööd ja säästab aega.
- Projekti jagamine väiksemateks mooduliteks (data_fetcher, transform, visualize, pipeline) muudab koodi loetavamaks ja lihtsamini hooldatavaks.
- Andmepipeline tagab, et analüüs kasutab alati kõige uuemaid andmeid.

#### Failid
- [**WEEK8_Python_Pipeline**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/e5ead99c403af5625cdbe1a06d65bae20d469730/WEEK8_Python_Pipeline.py) - Python skript
- [**WEEK8_Python_Weekly_KPI**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/e5ead99c403af5625cdbe1a06d65bae20d469730/WEEK8_Python_Weekly_KPI.pdf) - Python joonised

[**Week 0**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/0%20Onboarding.md)    [**Week 1**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/1%20SQL%20Basics.md)    [**Week 2**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/2%20SQL%20Data%20Cleaning.md)    [**Week 3**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/3%20SQL%20JOINs.md)    [**Week 4**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/4%20SQL%20Aggregation.md)    [**Week 5**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/5%20Power%20BI.md)    [**Week 6**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/6%20Power%20BI%20Data%20Storytelling%20Dashboard.md)    [**Week 7**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/7%20Python%20RFM%20anal%C3%BC%C3%BCs.md)    [**Week 8**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/671d471828a26044323cb44636f818b07ad58100/8%20Python%20APIs%20%26%20Automation.md)
