import urllib.request
import os
import bs4 as bs
import pandas as pd

def dowload():
    """ Download all the csv data available """

    source = urllib.request.\
        urlopen("https://www.eia.gov/totalenergy/data/monthly/index.php")
    soup = bs.BeautifulSoup(source)

    for link in soup.select("a[href*=csv]"):
        current_link = link.get("href")
        title = link.get("title")
        response = urllib.request.\
            urlopen('https://www.eia.gov' + current_link)
        data = pd.read_csv(response)
        data.to_csv(title + '.csv' if title != None
                    else current_link.split('=')[1])


def single_table():
    """ Join all tables in a single one """

    data = pd.DataFrame()
    for file in os.listdir('data'):
        data_par = pd.read_csv(os.path.join('data', file))
        data = pd.concat([data, data_par], ignore_index=True)
