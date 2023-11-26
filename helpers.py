### CS-401 ADA : Project 
### Team: TheSuricates
### November 2023

# This file contain all the helper function 
import requests
import json
import pandas as pd

# Function to convert currency using exchange rate json file
def convert_to_usd(path, amount, currency):

    with open(f"{path}/usd_conversion_rates.json", 'r') as file:
        conversion_rates = json.load(file)

    rate = conversion_rates.get(currency, 1)  # Default to 1 if currency not found
    return float(amount) / float(rate)

def convert_row_currency(path, row):
    if row['currencyCode'] != 'USD':
        row['cost'] = convert_to_usd(path, row['cost'], row['currencyCode'])
        row['boxOffice'] = convert_to_usd(path, row['boxOffice'], row['currencyCode'],)
        row['currencyCode'] = 'USD'

        # Fetch and add the Wikipedia page ID
    row['wikiPageID'] = get_wikipedia_page_id(row['filmLabel'])
    row['costBoxOfficeMultiplier'] = row['boxOffice'] / row['cost']

    return row

def get_wikipedia_page_id(film_name):
    # Replace spaces with underscores for the Wikipedia API format
    film_name_formatted = film_name.replace(' ', '_')

    url = f"https://en.wikipedia.org/w/api.php"

    params = {
        'action': 'query',
        'format': 'json',
        'titles': film_name_formatted
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        try:
            data = response.json()
            page_id = next(iter(data['query']['pages']))
            return page_id
        except KeyError:
            print(f"No page found for {film_name}")
            return None
    else:
        print("Failed to fetch data from Wikipedia")
        return None
    

# Convert our movies release date to datetime
def convert_to_datetime(date_str):
    try:
        return pd.to_datetime(date_str)
    except ValueError:
        # if there is only the year, add a month and day (1st of January)
        return pd.to_datetime(date_str + '-01-01')

