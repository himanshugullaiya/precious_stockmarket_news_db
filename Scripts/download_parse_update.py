import pandas
from datetime import datetime, date, timedelta
import requests
import zipfile
import os

#...zipfilelink = https://nsearchives.nseindia.com/archives/equities/bhavcopy/pr/PR{date_formatted}.zip
#...dateformat = 250225


zips_folder = '../Data/Zips'
files_folder = '../Data/Files'

def formatted_date(dt):
    day = str(dt.day).zfill(2)
    month = str(dt.month).zfill(2)
    year = str(dt.year)[-2:]
    final_date = f'{day}{month}{year}'
    return final_date


def download_zips(starting_date, ending_date):
    global zips_folder, files_folder

    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://www.nseindia.com/",
    "Accept": "*/*",
    }
    
    current_date = starting_date

    while current_date <= ending_date:
        delta = timedelta(days = 1)

        if current_date.weekday() >= 5:
            current_date += delta
            continue

        date_formatted = formatted_date(current_date)
        filelink = f'https://nsearchives.nseindia.com/archives/equities/bhavcopy/pr/PR{date_formatted}.zip'
        print(f'Downloading File : {date_formatted}.zip\n')
        linkdata = requests.get(url = filelink, headers = headers)

        if linkdata.status_code != 200:
            print(f'Skipped {date_formatted}.zip - Holiday / File Not available\n')
            current_date += delta
            continue

        if not os.path.exists('../Data'):
            os.makedirs('../Data')

        if not os.path.exists(zips_folder):
            os.makedirs(zips_folder)

        if not os.path.exists(files_folder):
            os.makedirs(files_folder)

        zip_path = zips_folder + f'/{str(current_date)}.zip'
        with open(zip_path, 'wb') as file:
            file.write(linkdata.content)
        print(f'Saved {current_date} Zip')
                       
        current_date += delta


def parse_zips(starting_date, ending_date):
    global zips_folder, files_folder
    delta = timedelta(days = 1)
    
    all_zips = os.listdir(zips_folder)
    zip_filename = f'{str(starting_date)}.zip'
    current_date = starting_date
    
    while current_date <= ending_date:
        if not zip_filename.endswith('.zip') or zip_filename not in all_zips:
            current_date += delta
            zip_filename = f'{str(current_date)}.zip'
            continue

        zip_path = os.path.join(zips_folder, zip_filename)

        # folder name same as zip name without .zip
        folder_name = zip_filename.replace('.zip', '')

        extract_folder = os.path.join(files_folder, folder_name)

        # create folder if not exists
        if not os.path.exists(extract_folder):
            os.makedirs(extract_folder)

        # extract zip
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_folder)
        print(f'Extracted {zip_filename}')
        
        current_date += delta
        zip_filename = f'{str(current_date)}.zip'
        

def run_inception_code():
    starting_date = date(2026,1,1)
    ending_date  = datetime.now().date()

    if not os.path.exists(zips_folder):
        download_zips(starting_date, ending_date)
        parse_zips(starting_date, ending_date)
        
    elif len(os.listdir(zips_folder)) < int(0.5*(ending_date - starting_date).days):
        
        download_zips(starting_date, ending_date)
        parse_zips(starting_date, ending_date)
        
    else:
        print('Files Present - Inception Not Run')
        
def update_files():
    global zips_folder, files_folder
    new_start_date = datetime.strptime(max(os.listdir(files_folder)), "%Y-%m-%d").date() + timedelta(days = 1)
    download_zips(new_start_date, datetime.now().date())
    parse_zips(new_start_date, datetime.now().date())
    print('Up To Date')
    
    
        
run_inception_code()
update_files()

