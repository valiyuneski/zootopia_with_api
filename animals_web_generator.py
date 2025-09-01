import data_fetcher


def generate_html(animal_name, info):
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{animal_name} - Animal Info</title>
        <meta charset="UTF-8">
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f7f7f7;
                color: #333;
                margin: 20px;
            }}
            .card {{
                background: white;
                border-radius: 10px;
                padding: 20px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                max-width: 600px;
                margin: auto;
            }}
            h1 {{
                text-align: center;
                color: #2c3e50;
            }}
            h2 {{
                margin-top: 15px;
                color: #16a085;
            }}
            ul {{
                padding-left: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>{info.get("name", animal_name)}</h1>
            <h2>Taxonomy</h2>
            <ul>
                {''.join(f"<li>{k}: {v}</li>" for k, v in info.get("taxonomy", {}).items())}
            </ul>
            <h2>Locations</h2>
            <p>{", ".join(info.get("locations", []))}</p>
            <h2>Characteristics</h2>
            <ul>
                {''.join(f"<li>{k}: {v}</li>" for k, v in info.get("characteristics", {}).items())}
            </ul>
        </div>
    </body>
    </html>
    """
    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(html_content)


def main():
    """Main function to run the program."""
    animal_name = input("Enter a name of an animal: ").strip()
    info = data_fetcher.fetch_data(animal_name)
    if info:
        generate_html(animal_name, info[0])  # Use the first result
        print("Website was successfully generated to the file animals.html.")
    else:
        print("No data found for that animal.")

if __name__ == "__main__":
    main()