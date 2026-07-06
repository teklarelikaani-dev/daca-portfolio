## Week 7 – Python & Pandas: UrbanStyle RFM kliendianalüüs
Koostasin Pythoni ja Pandase abil UrbanStyle'i klientide RFM (Recency, Frequency, Monetary) analüüsi, et segmenteerida kliendid nende ostukäitumise põhjal ning teha soovitusi turundus- ja kliendisuhete parandamiseks. Ühendasin selleks sales (10118 rida ja 12 veergu) ja customers (3150 rida ja 9 veergu) tabelid. Peale puhastamist 8950 rida ja 20 veergu. 

#### Kasutatud tehnoloogiad
- Python
- Jupyter Notebook (VS Code)
- Supabase (PostgreSQL)

#### RFM analüüs

| Kliendisegment | Soovitused |
| :--- | :--- |
| **Potential (29,88%) - ettevõtte suurim kasvuvõimalus** | Tervitus- ja lojaalsusprogrammid; personaalsed pakkumised; motiveerida teist ja kolmandat ostu tegema. |
| **Loyal (26,73%) - ettevõtte selgroog** | Lojaalsusprogramm; eksklusiivsed pakkumised; kliendirahulolu regulaarne mõõtmine. |
| **At Risk (20,83%) - suurim riskikoh** | "Tule tagasi" pakkumised; uurida lahkumise põhjuseid; personaalsed meeldetuletused |
| **VIP Champions (17,91%) - suur osa käibest** |  VIP-programmid; personaalne teenindus; varajane ligipääs toodetele; tänukampaaniad; erisoodustused.|
| **Lost (4,65%) - kaotatud kliendid** | Üks viimane reaktivatsioonikampaania ning kui tulemust pole, siis vähendada turunduskulusid nende peale. |

#### Äriline järeldus
- RFM analüüs näitas, et ettevõttel on tugev lojaalsete klientide baas (Loyal + VIP Champions = 44,6%), mis loob stabiilse müügitulu.
- Ligi 30% klientidest Potential segmendi, mis on ettevõtte suurim kasvuvõimalus.
- Kõige suurem risk on At Risk segment (20,83%), sest nende klientide kaotamine võib oluliselt vähendada tulevast käivet.

#### AI kasutamine
Kasutasin AI-d Pandase funktsioonide ja RFM arvutuste kontrollimiseks ning koodi kirjutamiseks. Kontrollisin kõik vahetulemused Jupyter Notebookis ning võrdlesin segmentide jaotust arvutatud RFM näitajatega.

#### Peamised õppetunnid
- Andmete ühendamine (merge) on kliendianalüüsi alus, sest võimaldab siduda ostud konkreetsete klientidega.
- Enne analüüsi tuleb andmed puhastada, et vältida vigaseid tulemusi.
- Pandas võimaldab töödelda suuri andmehulkasid kiiresti ja efektiivselt.
- RFM analüüs aitab muuta toorandmed praktilisteks turundus- ja kliendihalduse otsusteks.

#### Failid
- [**WEEK7_Python_RFM_analüüs**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/2823447a2e40a38cc6d2221d137143c0edc33d69/WEEK7_Python_RFM.py) - Python skript
- [**WEEK7_Python_RFM_analüüs_visual**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/2823447a2e40a38cc6d2221d137143c0edc33d69/WEEK7_Python_RFM_visual.pdf) - Python joonised

[**Järgmine Week 8**](https://github.com/teklarelikaani-dev/daca-portfolio/blob/f85716dde9191dacb7159a812fc6c2f003364344/8%20Python%20APIs%20%26%20Automation.md)
