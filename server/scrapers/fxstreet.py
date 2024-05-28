import requests
from bs4 import BeautifulSoup
import csv
import json

def fetch_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    return response.text

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    calendar_rows = soup.select('tr[data-event-date-id]')
    events = []
    
    for row in calendar_rows:
        time = row.select_one('td.fxs_c_item.fxs_c_time span').text.strip()
        country = row.select_one('td.fxs_c_item.fxs_c_flag span')['title']
        currency = row.select_one('td.fxs_c_item.fxs_c_currency span').text.strip()
        event_name = row.select_one('td.fxs_c_item.fxs_c_name span').text.strip()
        impact = row.select_one('td.fxs_c_item.fxs_c_impact span')['class'][1] if row.select_one('td.fxs_c_item.fxs_c_impact span') else None
        actual = row.select_one('td.fxs_c_item.fxs_c_actual strong').text.strip()
        deviation = row.select_one('td.fxs_c_item.fxs_c_deviation').text.strip()
        consensus = row.select_one('td.fxs_c_item.fxs_c_consensus').text.strip()
        previous = row.select_one('td.fxs_c_item.fxs_c_previous').text.strip()
        
        if impact in ['fxs_c_impact-med', 'fxs_c_impact-high']:
            events.append({
                'time': time,
                'country': country,
                'currency': currency,
                'event_name': event_name,
                'impact': impact,
                'actual': actual,
                'deviation': deviation,
                'consensus': consensus,
                'previous': previous
            })
    
    return events

def save_to_csv(data, filename):
    if not data:
        print("No data to save")
        return
    
    keys = data[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as output_file:
        json.dump(data, output_file, ensure_ascii=False, indent=4)

def main():
    url = 'https://www.fxstreet.com/economic-calendar'
    html = fetch_html(url)
    events = parse_html(html)
    
    print(f"Found {len(events)} impactful calendar rows")
    print(json.dumps(events, indent=4))
    
    save_to_csv(events, 'fxstreet_news.csv')
    save_to_json(events, 'fxstreet_news.json')

if __name__ == "__main__":
    main()
