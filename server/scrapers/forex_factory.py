import requests
from bs4 import BeautifulSoup
import csv
import json

def fetch_page_source(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch the page. Status code: {response.status_code}")

def parse_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    # Debug: print the title of the page
    print(f"Page Title: {soup.title.string}")

    # Find the calendar rows
    calendar_rows = soup.find_all('tr', class_='calendar__row')
    print(f"Found {len(calendar_rows)} calendar rows")

    data = []

    for row in calendar_rows:
        try:
            # Extracting currency
            currency = row.find('td', class_='calendar__cell calendar__currency')
            currency_text = currency.get_text(strip=True) if currency else 'N/A'

            # Extracting event title
            event_detail = row.find('td', class_='calendar__cell calendar__event')
            event_text = event_detail.get_text(strip=True) if event_detail else 'N/A'

            # Extracting actual value
            actual = row.find('td', class_='calendar__cell calendar__actual')
            actual_text = actual.get_text(strip=True) if actual else 'N/A'

            # Extracting forecast value
            forecast = row.find('td', class_='calendar__cell calendar__forecast')
            forecast_text = forecast.get_text(strip=True) if forecast else 'N/A'

            # Extracting previous value
            previous = row.find('td', class_='calendar__cell calendar__previous')
            previous_text = previous.get_text(strip=True) if previous else 'N/A'

            # Add the row to the data list
            data.append({
                "currency": currency_text,
                "event": event_text,
                "actual": actual_text,
                "forecast": forecast_text,
                "previous": previous_text
            })

        except Exception as e:
            print(f"Error processing row: {e}")

    return data

def save_to_csv(data, filename):
    keys = data[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

def print_as_json(data):
    print(json.dumps(data, indent=4))

def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as output_file:
        json.dump(data, output_file, ensure_ascii=False, indent=4)

def main():
    url = "https://www.forexfactory.com"
    page_source = fetch_page_source(url)
    data = parse_content(page_source)

    # Save to CSV
    save_to_csv(data, 'csv/forex_news.csv')
    save_to_json(data, 'json/forex_news.json')

    # Print as JSON
    print_as_json(data)

if __name__ == "__main__":
    main()
