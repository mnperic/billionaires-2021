#################################################
# Import/ call dependencies and Setup
#################################################
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC

import pandas as pd
import datetime as dt
import json
import numpy as np
import humanize
import requests

import warnings
warnings.filterwarnings("ignore")
#################################################
# Visit the page by browser and scrape data for the latest winners information
#################################################
def winners(browser):

    # Set url and browser visit the site
    url = "https://www.forbes.com/real-time-billionaires"
    browser.visit(url)
    html = browser.html
    bs  = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        print(bs.title.text)

        # Scrape winners name & profile URLs and convert to dataframes:
        winner_profile = bs.findAll('div', class_='rtb-wrapper--winner')
        bio = []
        w_name = []
        for item in winner_profile:
            winner_bio = item.find("a")['href'] 
            bio.append(winner_bio)
            w_name.append(item.find("div", "rtb-person-name").text)

        w_name = pd.Series(w_name)
        w_name_df = w_name.to_frame(name="winner_name")

        bio = pd.Series(bio)
        w_profile_df = bio.to_frame(name="winner_profile")

        # Scrape winners winnings & photo URLs and convert to dataframes:
        winner_div = bs.findAll("div", "rtb-avatar-wrapper--winner")
        win = []
        photo = []
        for i in winner_div:
            w_photo = i['style'].split('url("')[1].split('")"')[0]
            photo.append(w_photo)
            win.append(i.text)

        photo = pd.Series(photo)
        w_photo_df = photo.to_frame(name="winner_photo")

        win = pd.Series(win)
        win_df = win.to_frame(name="win")

        # Merge all winners sub dataframes into one dataframe
        winners_df = pd.concat([w_name_df, win_df, w_photo_df, w_profile_df], axis=1, join="inner")
    
        # Save the winners list to json file
        with open('data/winners.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(winners_df.to_dict("records"),ensure_ascii=False,indent=1))

    except AttributeError:
        return None
    
    return winners_df.to_dict("records")
#################################################

#################################################
# Visit the page by browser and scrape data for the latest losers information
#################################################
def losers(browser):

    # Set url and browser visit the site
    url = "https://www.forbes.com/real-time-billionaires"
    browser.visit(url)
    html = browser.html
    bs  = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # Scrape losers name & profile URLs and convert to dataframes:
        loser_profile = bs.findAll('div', class_='rtb-wrapper--loser')
        l_bio = []
        l_name = []
        for item in loser_profile:
            loser_bio = item.find("a")['href'] 
            l_bio.append(loser_bio)
            l_name.append(item.find("div", "rtb-person-name").text)

        l_name = pd.Series(l_name)
        l_name_df = l_name.to_frame(name="loser_name")

        l_bio = pd.Series(l_bio)
        l_profile_df = l_bio.to_frame(name="loser_profile")

        # Scrape losers net lost & photo URLs and convert to dataframes:
        loser_div = bs.findAll("div", "rtb-avatar-wrapper--loser")

        lost = []
        photo = []
        for i in loser_div:
            l_photo = i['style'].split('url("')[1].split('")"')[0]
            photo.append(l_photo)
            lost.append(i.text)

        l_photo = pd.Series(photo)
        l_photo_df = l_photo.to_frame(name="loser_photo")

        lost = pd.Series(lost)
        lost_df = lost.to_frame(name="lost")

        # Merge all losers sub dataframes into one dataframe
        losers_df = pd.concat([l_name_df, lost_df, l_photo_df, l_profile_df], axis=1, join="inner")
    
        # Save the losers list to json file
        with open('data/losers.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(losers_df.to_dict("records"),ensure_ascii=False,indent=1))

    except AttributeError:
        return None
    
    return losers_df.to_dict("records")
#################################################


#################################################
# Visit the page by browser and read json data for all latest billionaires information
#################################################
def all_bills():

    # Read json data via json url
    json_url = "https://forbes400.herokuapp.com/api/forbes400?limit=3000"
    json_read = pd.read_json(json_url, convert_dates=True)

    # Add try/except for error handling
    try:
        
        # Convert json data into "raw" pandas dataframe
        json_df = pd.DataFrame(json_read)

        df = []
        df = json_df[["personName","rank","birthDate","gender","finalWorth","source","industries","countryOfCitizenship","squareImage"]]
        print(f"\n\n------------------>df.head()<----------------\n\n\n",json_df.head())

        # Calculating age from date of birth
        df['birthDate'] = df['birthDate'].astype('datetime64[ns]')
        df["age"]= df["birthDate"].apply(lambda x : (pd.datetime.now().year - x.year))
        df["age"]= df["age"].fillna(0).astype(int)

        # Convert finalworth into networth and humanize the millions/billions numbers
        df["finalWorth"] = (df["finalWorth"]*1000000).astype("int64")
        df['net'] = [humanize.intword(x) for x in df['finalWorth']]
        df['net'] = df['net'].replace({'billion': 'B'},regex=True)
        df['net'] = df['net'].replace({'million': 'M'},regex=True)

        # Get nested json data from "industries"
        df = df.fillna("")
        df= (df["industries"].apply(pd.Series).merge(df,left_index=True, right_index=True))
        df["industries"] = df[0]
        df = df.drop(df.columns[[0]], axis=1)

        # Get the billionaires photo url from squareImage field
        df_tmp = df[df['squareImage'].str.match('//')]      
        df['squareImage'] = np.where(df.squareImage.isin(df_tmp.squareImage), "https:" + df.squareImage, "" + df.squareImage)

        # Create new dataframe with the required columns and fill NaN with blanks
        all_billionaires_df = []
        all_billionaires_df = df[["personName","rank","age","gender","net","source","industries","countryOfCitizenship","squareImage"]]

        # Check dataframe to ensure all fields are filled
        all_billionaires_df.isnull().sum()

        # Check column types
        all_billionaires_df.info()

        # Export the final dataframe to csv files
        # all_billionaires_csv = "data/all_billionaires_" + dt.datetime.today().strftime('%d%m%Y') + ".csv"
        # all_billionaires_df.to_csv(all_billionaires_csv, index=False)

    except AttributeError:
        return None
    
    # return
    return all_billionaires_df.to_dict("records")
#################################################


#################################################
# Perform all scrapping functions and store the data into a dictionary to be loaded on MongoDB
#################################################
def scrape():
   
    # Set the executable path and initialize Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Run all the scraping functions and store results in the dictionary
    data = {
        "winners": winners(browser),
        "losers" : losers(browser),
        "all": all_bills(),
        "last_modified": dt.datetime.now()
    }

    # Close the browser after finished scraping
    browser.quit()
    return data

def jsonifyData():
    data = {
        "all": all_bills()
        }
    return data