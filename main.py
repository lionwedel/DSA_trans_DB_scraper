from helper import scraper

# To enter:
from_date = "01-05-2024" #DD-MM-YYYY
to_date = "30-09-2024" #DD-MM-YYYY
full = True #choose full or light csv (full contians for columns/ information but is larger)
download_directory = "/Users/lion.wedel/Documents/DSA_transparency_DB"
chunksize = 8192*4
platform_name = "TikTok"

scraper(platform_name, from_date, to_date, download_directory,full=True, chunksize=chunksize)