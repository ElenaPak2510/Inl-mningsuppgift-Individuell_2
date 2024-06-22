import csv
import json
import os

def csv_to_json(csv_file, json_file):
    # Specify the full path to the CSV file
    csv_file_path = os.path.join(os.getenv('GITHUB_WORKSPACE', '.'), csv_file)

    # Open the CSV file and read the contents with the correct encoding
    with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    # Specify the full path to the JSON file
    json_file_path = os.path.join(os.getenv('GITHUB_WORKSPACE', '.'), json_file)

    # Write JSON data to the JSON file with UTF-8 encoding
    with open(json_file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

#Specify the path to the CSV and JSON files
csv_file = 'profiles1.csv'
json_file = 'data.json'

#Convert CSV to JSON
csv_to_json(csv_file, json_file)

 