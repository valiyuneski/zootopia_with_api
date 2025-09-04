import requests
import os
from dotenv import load_dotenv
import logging


API_URL = "https://api.api-ninjas.com/v1/animals"

logging.basicConfig(level=logging.ERROR)



# Load environment variables once, at import time
load_dotenv()

def get_api_key():
    """Retrieve the API key from environment variables."""
    return os.getenv("API_KEY")


def fetch_data(animal_name) -> list:
    """Fetch data about the given animal from the API."""
    API_KEY = get_api_key

    if not API_KEY:
        raise ValueError("API_KEY not found! Please set it in the .env file.")

    response = requests.get(
        API_URL,
        headers={"X-Api-Key": API_KEY},
        params={"name": animal_name}
    )
    if response.status_code == 200:
        data = response.json()
        return data if data else []  # always return a list
    else:
        logging.error("Request failed with status code %s", response.status_code)
        return []