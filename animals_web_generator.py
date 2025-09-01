import requests

API_URL = "https://api.api-ninjas.com/v1/animals"
API_KEY = "n7IqvzqjRPFKD7v17+FsDg==ggBAIzwOejjz8ehL"

def fetch_data(animal_name: str) -> list:
    """Fetch animal information from the API"""
    response = requests.get(
        API_URL,
        headers={"X-Api-Key": API_KEY},
        params={"name": animal_name}
    )
    if response.status_code == 200:
        return response.json()  # returns a list of results
    else:
        print("Error fetching data:", response.status_code)
        return []

def generate_html(animal_data: list):
    """Generate an HTML page from the API results"""
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Animal Info</title>
        <meta charset="UTF-8">
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; background: #f9f9f9; }
            .card { background: white; padding: 20px; margin: 20px auto; border-radius: 10px;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1); max-width: 700px; }
            h1 { color: #2c3e50; }
            h2 { color: #16a085; }
            ul { padding-left: 20px; }
        </style>
    </head>
    <body>
    <h1>Animals Information</h1>
    """

    for animal in animal_data:
        html_content += f"""
        <div class="card">
            <h2>{animal.get("name", "Unknown")}</h2>
            <h3>Taxonomy</h3>
            <ul>
                {''.join(f"<li>{k}: {v}</li>" for k,v in animal.get("taxonomy", {}).items())}
            </ul>
            <h3>Locations</h3>
            <p>{", ".join(animal.get("locations", []))}</p>
            <h3>Characteristics</h3>
            <ul>
                {''.join(f"<li>{k}: {v}</li>" for k,v in animal.get("characteristics", {}).items())}
            </ul>
        </div>
        """

    html_content += "</body></html>"

    with open("animals.html", "w", encoding="utf-8") as f:
        f.write(html_content)

def main():
    # Instead of reading JSON file → fetch from API
    data = fetch_data("Fox")
    if data:
        generate_html(data)
        print("Website was successfully generated to the file animals.html.")
    else:
        print("No animal data found.")

if __name__ == "__main__":
    main()