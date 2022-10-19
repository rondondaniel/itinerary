import requests
import json
from pathlib import Path
from zipfile import ZipFile

# Create a flow and an application on https://diffuseur.datatourisme.fr/ to get your API key and webservice ID

def get_poi_pipeline(API_KEY, WEBSERVICE_ID):
    # GET POI datafile pipeline
    # Download POI
    try:
        json_link = "https://diffuseur.datatourisme.fr/webservice/{}/{}".format(WEBSERVICE_ID, API_KEY)
        api_response = requests.get(json_link)
    except requests.exceptions.RequestException as e:
        print("Oops!  That was no valid response.  Try again...")
        raise SystemExit(e)
    # Save response to ZIP file
    with open("POI.json.zip", "wb") as zip_file:
        zip_file.write(api_response.content)
    data_path = Path("data/")
    # Check if Data folder already exists
    # If not, create Data folder
    if not data_path.exists:
        data_path.mkdir(parents=True, exist_ok=True)
        print("Folder {} created".format(data_path.name))
    # Unzip into data folder
    with ZipFile("POI.json.zip", "r") as zipObj:
        # Extract all the contents of zip file in current directory
        zipObj.extractall(data_path.name)