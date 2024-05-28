import json

def load_data(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def sort_data(data, key):
    return sorted(data, key=lambda x: x[key])

def filter_data(data, key, value):
    return [item for item in data if item[key] == value]

def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    # Load data from JSON
    data = load_data('../scrapers/json/forex_news.json')
    
    # Sort data by impact (for example)
    sorted_data = sort_data(data, 'impact')
    
    # Optionally filter data (for example, only high impact events)
    filtered_data = filter_data(sorted_data, 'impact', 'high')
    
    # Save sorted/filtered data back to JSON
    save_to_json(filtered_data, 'forex_news_parsed.json')
    
    # Print data to console for verification
    print(json.dumps(filtered_data, indent=4))

if __name__ == "__main__":
    main()
