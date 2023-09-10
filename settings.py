import json

def get_value(key, json_file_path='settings.json'):
    try:
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)

            # Überprüfe, ob der Schlüssel (key) in den JSON-Daten existiert
            if key in data:
                return data[key]
            else:
                print(f'Der Schlüssel "{key}" wurde nicht in der JSON-Datei gefunden.')

    except FileNotFoundError:
        print(f'Die Datei "{json_file_path}" wurde nicht gefunden.')
    except json.JSONDecodeError:
        print(f'Die Datei "{json_file_path}" ist keine gültige JSON-Datei.')

def update_value(key, new_value):
    try:
        # Open the JSON file for reading
        with open('settings.json', 'r') as file:
            data = json.load(file)

        # Update the value for the specified key
        data[key] = new_value

        # Open the JSON file for writing
        with open('settings.json', 'w') as file:
            json.dump(data, file, indent=4)
        
        print(f"Updated '{key}' to '{new_value}' in settings.json")
    
    except FileNotFoundError:
        print("Error: settings.json not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON in settings.json")
    except Exception as e:
        print(f"An error occurred: {e}")
