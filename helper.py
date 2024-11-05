
import requests
import os
from bs4 import BeautifulSoup as bs
from tqdm.auto import tqdm
import math

def init_platforms_dict(base_url):
    # Init Platform-ID dict
    platform_id_dict = {}
    response = requests.get(base_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = bs(response.content, "html.parser") 

        platform_options = soup.find(id="uuid")
        options = platform_options.find_all("option")[2:]
        for option in options:
            platform_id_dict[option.get_text().strip(" ")] = option.get("value")

        # Print platform options
        #print("Platforms for wich you can download data:")
        print(platform_id_dict.keys())
        
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")


    return platform_id_dict



def scraper(platform_name, from_date, to_date, download_directory,full=True, chunksize=8192):

    base_url = "https://transparency.dsa.ec.europa.eu/data-download"

    platform_id_dict = init_platforms_dict(base_url)
    platform = platform_id_dict[platform_name]
    page = 1
    more_pages = True
    while more_pages == True:

        ###
        request_link = f"{base_url}?from_date={from_date}&to_date={to_date}&uuid={platform}&page={page}"
        response = requests.get(request_link)

        if response.status_code == 200:
            # Parse the HTML content
            soup = bs(response.content, "html.parser") 

            # probe for multi pages
            overview = soup.find("p", class_="blocktext ecl-u-type-paragraph")
            if overview:
                n_results = overview.find_all("span")[2].get_text()
                n_pages = math.ceil(int(n_results)/50)
                # iterate page number by one if currently not on last page
                if n_pages > page:
                    page += 1
                # otherwise make sure while loop ends after this go through    
                else:
                    more_pages == False
                print("More than one page (its max. 50 per page), this one might take longer! Sit back and relax.")
                print(f"Number of days returned by request: {n_results}")
                print(f"Number of page to go through: {n_pages}")
            else:
                print("Less than 50 entries. This one will be fast.")

            # get data file list
            daily_data_list = soup.find_all("tr", class_="ecl-table__row dayarchive-row")

            if len(daily_data_list) == 0:
                print("Upsi, no data at all! Double check your input.")
                print("Check what your input does manually here:")
                print(request_link)


            for day in tqdm(daily_data_list):
                if full == True:
                        ref = day.select("td:nth-child(3) > a:nth-child(1)")[0].get("href")
                else:
                        ref = day.select("td:nth-child(5) > a:nth-child(1)")[0].get("href")

                ## download csv
                        
                response = requests.get(ref, stream=True)  # stream=True for large files

                # Check if the request was successful
                if response.status_code == 200:
                    # Get the filename from the URL (you might need to adjust this)
                    filename = ref.split("/")[-1] 
                    save_to = os.path.join(download_directory, filename)

                    # Save the file
                    with open(save_to, "wb") as f:
                        for chunk in response.iter_content(chunk_size=chunksize):  # Download in chunks
                            f.write(chunk)
                    #print(f"File downloaded: {filename}")
                else:
                    print(f"Failed to download the file. Status code: {response.status_code}")

    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")


