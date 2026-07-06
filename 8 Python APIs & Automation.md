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
