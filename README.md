#### Quick Start

1. Download/clone main.py and helper.py. Make sure both are in the same directory.
2. Make sure the following packages are installed: requests, os, bs4, tqdm, math

To scrape, open main.py and adjust the necessary variables.
Example:

```python
from helper import scraper

# To enter:
from_date = "01-05-2024" #DD-MM-YYYY
to_date = "30-09-2024" #DD-MM-YYYY
full = True #choose full or light csv (full contians for columns/ information but is larger), default True
download_directory = "/Users/XXXX/XXXX/XXXXX"
chunksize = 8192 ### the higher the faster the download, but perhaps less stable, default 8192
platform_name = "TikTok"

```
An overview of the platforms that can be scraped and how to write them is provided at the end of this page or in the main.py file.

To start scraping, run the main.py file, making sure the scraper function:

```python
scraper(platform_name, from_date, to_date, download_directory)
```

If you have customized the chunk_size and full variables, make sure to specify them in the function call in main.py:
```python
scraper(platform_name, from_date, to_date, download_directory, full = full, chunksize = chunksize)
```

Complete list of platforms and the way they would have to be written (as of 5.11.24)

A: Akciós-újság.hu | AliExpress | Amazon Store | App Store | Auctronia
B: Badoo | BlaBlaCar | Bolha.com | Booking.com | Bumble
C: Campfire | Canva | Cdiscount | Chrome Web Store | Conrad
D: Daft.ie | Discord Netherlands B.V. | Doctolib | DoneDeal.ie
E: EMAG.BG | EMAG.HU | EMAG.RO | EMimino.cz
F: Facebook | Fashiondays.ro | Flights | Flourish
G: Glassdoor | Google Maps | Google Play | Google Shopping | Groupon
H: Használtautó.hu | Hírstart | Horizon | Hotels
I: Idealo | IMDb | Imovirtual | Ingatlan.com | Instagram
K: Kaggle | Kleinanzeigen
L: La Redoute | Ligaportal | LinkedIn
M: Meetic SAS | Mobile.de | Nebenan.de
N: Njuškalo.hr | Nosalty
O: OLX | OTTO Market
P: Parship | Pinterest | Pornhub | Pub.dev
Q: Quest Store
R; Rajče | Rakuten | Reddit | Roblox
S: SFDC Ireland Limited | Shein | SIA "JOOM" | Snapchat | Standvirtual | Startlap | Stripchat
T: TAZZ | Telia Yhteisö | Temu | Tenor | Threads | TikTok | Tripadvisor | Trustpilot
U: Uber
V: Vacation Rentals | Vareni.cz | Vinted UAB | VSCO
W: Wallapop | Waze | WhatsApp Channels | Willhaben internet service GmbH & Co KG
X: X
Y: YouTube
Z: Zalando
