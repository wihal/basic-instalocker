# Thanks to chatgpt :D
import json

def agents_list(json_file_path):
    object_names = []  # Erstelle eine leere Liste für die Namen der Objekte

    try:
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)

            if isinstance(data, list):
                for obj in data:
                    if isinstance(obj, dict):
                        object_names.extend(obj.keys())  # Füge die Schlüssel zur Liste hinzu
            elif isinstance(data, dict):
                object_names.extend(data.keys())  # Füge die Schlüssel des einzigen Objekts hinzu
            else:
                print("Die JSON-Datei enthält weder eine Liste noch ein Dictionary.")
    
    except FileNotFoundError:
        print(f'Die Datei "{json_file_path}" wurde nicht gefunden.')
    except json.JSONDecodeError:
        print(f'Die Datei "{json_file_path}" ist keine gültige JSON-Datei.')

    return object_names

# Verwende die Funktion, um die Namen der Objekte aus einer JSON-Datei aufzulisten
json_file_path = 'btn_location.json'  # Passe den Dateipfad an