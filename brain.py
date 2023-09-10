import time as tm
import json
import pyautogui as pg
import json
from pynput.keyboard import Key, Listener
import keyboard
from time import sleep

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

def update_value(key, new_value, json_file_path: str = 'settings.json'):
    try:
        # Open the JSON file for reading
        with open(json_file_path, 'r') as file:
            data = json.load(file)

        # Update the value for the specified key
        data[key] = new_value

        # Open the JSON file for writing
        with open(json_file_path, 'w') as file:
            json.dump(data, file, indent=4)
        
        print(f"Updated '{key}' to '{new_value}' in {json_file_path}")
    
    except FileNotFoundError:
        print(f"Error: {json_file_path} not found.")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in {json_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


def start(startkey: str = get_value("start_key"), stopkey: str = get_value("end_key"), Remember: bool = False, agent: str = get_value("default_agent")):
    if Remember:
        update_value("default_agent", agent)
        update_value("start_key", startkey)
        update_value("end_key", stopkey)

    print("StartKey: "+ startkey + "\n StopKey: " + stopkey + "\n Agent: " + agent)
    #while True:
        #if pg.keyDown(StartKey):
            #tm.sleep(1)
        #if pg.keyDown(StopKey):
            #break

def add_agent(agent: str):
    while True:
        mousep = pg.position()
        print(mousep)
        sleep(0.1)
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('q'):  # if key 'q' is pressed 
                update_value(agent, mousep, 'agents.json')
                break  # finishing the loop
        except:
            update_value(agent, mousep, 'agents.json')
            break  # if user pressed a key other than the given key the loop will break

def remove_agent(file_path):
    try:
        # Create an empty dictionary to clear the JSON data
        json_data = {}

        # Save the empty data back to the file
        with open(file_path, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)

        print("All agents deleted successfully.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
