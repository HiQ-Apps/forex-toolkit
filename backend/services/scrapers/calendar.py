import requests
from bs4 import BeautifulSoup
from utils import save_to_csv, save_to_json, print_as_json

def fetch_page_source(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch the page... CODE: {response.status_code}")

def parse_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    print(f"Page Title: {soup.title.string.strip()}")

    calendar_rows = soup.find_all('tr', class_='calendar__row')
    print(f"Found {len(calendar_rows)} calendar rows")

    data = []

    for row in calendar_rows:
        try:
            date_td = row.find_previous('td', class_='calendar__cell calendar__date')
            date_text = date_td.get_text(strip=True) if date_td else 'N/A'
            
            time_td = row.find('td', class_='calendar__cell calendar__time')
            time_text = time_td.get_text(strip=True) if time_td else 'N/A'

            currency_td = row.find('td', class_='calendar__cell calendar__currency')
            currency_text = currency_td.get_text(strip=True) if currency_td else 'N/A'

            impact_td = row.find('td', class_='calendar__cell calendar__impact')
            impact_span = impact_td.find('span', class_='icon')
            if impact_span:
                impact_class = impact_span.get('class', [])
                if 'icon--ff-impact-red' in impact_class:
                    impact_text = 'high'
                elif 'icon--ff-impact-ora' in impact_class:
                    impact_text = 'medium'
                elif 'icon--ff-impact-yel' in impact_class:
                    impact_text = 'low'
                else:
                    impact_text = 'N/A'
            else:
                impact_text = 'N/A'

            event_detail = row.find('td', class_='calendar__cell calendar__event')
            event_text = event_detail.get_text(strip=True) if event_detail else 'N/A'

            actual = row.find('td', class_='calendar__cell calendar__actual')
            actual_text = actual.get_text(strip=True) if actual else 'N/A'

            forecast = row.find('td', class_='calendar__cell calendar__forecast')
            forecast_text = forecast.get_text(strip=True) if forecast else 'N/A'

            previous = row.find('td', class_='calendar__cell calendar__previous')
            previous_text = previous.get_text(strip=True) if previous else 'N/A'
            
            data.append({
                "date": date_text,
                "time": time_text,
                "currency": currency_text,
                "impact": impact_text,
                "event": event_text,
                "actual": actual_text,
                "forecast": forecast_text,
                "previous": previous_text
            })

        except Exception as e:
            print(f"Error processing the data... {e}")

    return data

def main():
    url = "https://www.forexfactory.com"
    page_source = fetch_page_source(url)
    data = parse_content(page_source)

    if data:
        save_to_csv(data, 'data/csv/forex_news.csv')
        save_to_json(data, 'data/json/forex_news.json')
        print_as_json(data)
    else:
        print("No data to save")

if __name__ == "__main__":
    main()
