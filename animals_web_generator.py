import requests

API_URL = "https://api.api-ninjas.com/v1/animals"
API_KEY = "n7IqvzqjRPFKD7v17+FsDg==ggBAIzwOejjz8ehL"

import requests

API_URL = "https://api.api-ninjas.com/v1/animals"
API_KEY = "YOUR_API_KEY"  # replace with your actual key

def fetch_data(animal_name: str) -> list:
    """Fetch animal information from the API (raw results)"""
    response = requests.get(
        API_URL,
        headers={"X-Api-Key": API_KEY},
        params={"name": animal_name}
    )
    if response.status_code == 200:
        return response.json()  # full list of matches
    else:
        print("Error fetching data:", response.status_code)
        return []

def generate_html(animal_data: list, query: str):
    """Generate an HTML page for the animal(s) or show error message"""
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Animal Info - {query}</title>
        <meta charset="UTF-8">
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; background: #f9f9f9; }}
            .card {{ background: white; padding: 20px; margin: 20px auto; border-radius: 10px;
                     box-shadow: 0 4px 6px rgba(0,0,0,0.1); max-width: 700px; }}
            h1 {{ color: #2c3e50; }}
            h2 {{ color: #e74c3c; }}
            ul {{ padding-left: 20px; }}
            p {{ font-size: 16px; }}
        </style>
    </head>
    <body>
        <h1>Result for "{query}"</h1>
    """

    if not animal_data:
        # Show friendly error message
        html_content += f'<h2>The animal "{query}" doesn\'t exist.</h2>'
    else:
        # Show all exact matches
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
    query = input("Enter a name of an animal: ").strip()
    
    # fetch all API results
    all_results = fetch_data(query)
    
    # filter here for exact match only (case-insensitive)
    exact_matches = [a for a in all_results if a.get("name", "").lower() == query.lower()]
    
    # generate HTML (either results or error message)
    generate_html(exact_matches, query)
    
    print("Website was successfully generated to the file animals.html.")

if __name__ == "__main__":
    main()