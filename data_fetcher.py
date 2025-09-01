import requests
import os
from dotenv import load_dotenv

API_URL = "https://api.api-ninjas.com/v1/animals"

def fetch_data(animal_name) -> list:
    """Fetch data about the given animal from the API."""
    load_dotenv()
    
    API_KEY = os.getenv('API_KEY')

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
        print("Error:", response.status_code)
        return []