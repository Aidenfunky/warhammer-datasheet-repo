import csv
import json
import os

def convert_csv_to_json(csv_file_path, json_file_path):
    """
    Converts a CSV file to a JSON file.
    Each row in the CSV becomes an object in a JSON array.
    Handles potential None values and uses pipe '|' as delimiter.
    """
    data = []
    try:
        # Specify delimiter as '|'
        with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter='|')
            for row in csv_reader:
                cleaned_row = {}
                for k, v in row.items():
                    # Ensure key is a string and clean it
                    cleaned_key = k.strip().replace('\ufeff', '') if k is not None else ''
                    # Ensure value is a string and clean it, handling None
                    cleaned_value = v.strip() if v is not None else ''
                    cleaned_row[cleaned_key] = cleaned_value
                data.append(cleaned_row)
        
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)
        print(f"Successfully converted '{csv_file_path}' to '{json_file_path}'")
    except FileNotFoundError:
        print(f"Error: CSV file not found at '{csv_file_path}'")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")

def main():
    # Define the directory where your downloaded CSVs are located
    csv_input_dir = '.' 
    # Define the directory where you want to save the JSON files
    json_output_dir = 'public/data' 

    # Ensure the output directory exists
    os.makedirs(json_output_dir, exist_ok=True)

    # List of CSV files to convert
    csv_files_to_convert = [
        'Factions',
        'Datasheets', 
        'Source',
        'Stratagems',
        'Abilities',
        'Datasheets_abilities',
        'Datasheets_detachment_abilities',
        'Datasheets_enhancements'
    ]

    for filename_stem in csv_files_to_convert:
        csv_path = os.path.join(csv_input_dir, f"{filename_stem}.csv")
        json_path = os.path.join(json_output_dir, f"{filename_stem}.json")
        convert_csv_to_json(csv_path, json_path)

if __name__ == "__main__":
    main()
