import json

def load_data(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    # Ensure all items have an 'impact' key with a default value
    for item in data:
        if 'impact' not in item:
            item['impact'] = 'low'  # Default value
    return data

def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def sort_data(data, key):
    return sorted(data, key=lambda x: x.get(key, ''))

def filter_data(data, key, value):
    return [item for item in data if item.get(key) == value]

def main():
    try:
        # Load data from JSON
        data = load_data('../scrapers/json/forex_news.json')
        
        # Debugging: Print the data loaded from JSON
        print("Loaded data:")
        print(json.dumps(data, indent=4))

        # Sort data by impact (for example)
        sorted_data = sort_data(data, 'impact')

        # Optionally filter data (for example, only high impact events)
        filtered_data = filter_data(sorted_data, 'impact', 'high')

        # Save sorted/filtered data back to JSON
        save_to_json(filtered_data, '../scrapers/json/processed_data.json')

        # Print data to console for verification
        print("Filtered data:")
        print(json.dumps(filtered_data, indent=4))
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
    except KeyError as e:
        print(f"KeyError: {e}. Please check the data structure.")
    except json.JSONDecodeError:
        print("Error decoding JSON. Please check the file format.")

if __name__ == "__main__":
    main()
