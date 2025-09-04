import requests
import os
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.ERROR)

API_URL = "https://api.api-ninjas.com/v1/animals"
API_KEY = os.getenv("API_KEY")


def fetch_data(animal_name) -> list:
    """Fetch data about the given animal from the API."""
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