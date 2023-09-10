import time as tm
import json
import pyautogui as pg

import main as main
import json

def agents_list(json_file_path):
    object_names = []  # Erstelle eine leere Liste für die Namen der Objekte

    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

        if isinstance(data, list):
            for obj in data:
                if isinstance(obj, dict):
                    object_names.extend(obj.keys())  # Füge die Schlüssel zur Liste hinzu
        elif isinstance(data, dict):
                object_names.extend(data.keys())  # Füge die Schlüssel des einzigen Objekts hinzu

    return object_names

# Verwende die Funktion, um die Namen der Objekte aus einer JSON-Datei aufzulisten
json_file_path = 'agents.json'  # Passe den Dateipfad an

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


def start(StartKey: str = get_value("start_key"), StopKey: str = get_value("end_key"), Remember: bool = False):
    if Remember:
        update_value("start_key", StartKey)
        update_value("end_key",StopKey)

    print("StartKey: ", StartKey, "StopKey: ", StopKey)
    #while True:
        #if pg.keyDown(StartKey):
            #tm.sleep(1)
        #if pg.keyDown(StopKey):
            #break

def status():
    print("Good")

if __name__ == "__main__":
    main()