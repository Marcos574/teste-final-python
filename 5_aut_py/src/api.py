import hashlib
import hmac
import requests
import json
import os

from dotenv import load_dotenv

def create_url():
    load_dotenv()
    meteo_blue_api_key = os.getenv("METEO_BLUE_API_KEY")

    lat=-15.7797
    lon=-47.9297

    sharedSecret = "MySharedSecret"
    query = f"/packages/basic-1h?lat={lat}&lon={lon}&apikey={meteo_blue_api_key}"

    sig = hmac.new(sharedSecret.encode(), query.encode(), hashlib.sha256).hexdigest()

    signedUrl = f"https://my.meteoblue.com{query}&sig={sig}"

    return signedUrl

def request(url):
    response = requests.get(url)

    data = response.json()

    with open("dados/response_data.json", "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
