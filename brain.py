import json
import pyautogui as pg
import json
import keyboard
from time import sleep
import os
import sys

# Thanks Bro https://stackoverflow.com/a/31966932/16335953
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    result = os.path.join(base_path, relative_path)
    print(f"Resource Path: {result}")  # Debug-Ausgabe hinzufügen
    return result



'''if not os.path.exists(f".vlocker"):
    os.makedirs(f".vlocker")
    print(f"Folder .vlocker created successfully.")
else:
    print(f"Folder .vlocker already exists.")

def create_json(file_path, data=None):
    file_path = resource_path(file_path)
    if not os.path.exists(file_path):
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"JSON file '{file_path}' created.")
    else:
        print(f"JSON file '{file_path}' already exists. To update it, use a different function.")

create_json(".vlocker\\agents.json")
create_json(".vlocker\\settings.json")'''

def agents_list(json_file_path: str):
    json_file_path = resource_path(json_file_path)
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

def get_value(key:str, json_file_path: str):
    json_file_path = resource_path(json_file_path)
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

def update_value(key, new_value, json_file_path: str):
    json_file_path = resource_path(json_file_path)
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


def start(startkey: str, stopkey: str, agent: str):

    agent_pos = get_value(agent, ".vlocker\\agents.json")
    button_pos = get_value("Button", ".vlocker\\settings.json")
    print("StartKey: "+ startkey + "\n StopKey: " + stopkey + "\n Agent: " + agent)
    
    while True:
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed(startkey):  # if key 'q' is pressed 
                while True:
                    pg.mouseDown(agent_pos[0], agent_pos[1], duration=0.1)
                    sleep(0.2)
                    pg.mouseUp(agent_pos[0], agent_pos[1], duration=0.1)
                    sleep(0.1)
                    
                    pg.mouseDown(button_pos[0], button_pos[1], duration=0.1)
                    sleep(0.2)
                    pg.mouseUp(button_pos[0], button_pos[1], duration=0.1)
                    sleep(0.1)
                    
                    try:  # used try so that if user pressed other than the given key error will not be shown
                        if keyboard.is_pressed(stopkey):  # if key 'q' is pressed 
                            break
                    except:
                        print("Stop Key not pressed yet!")
        except:
            print("Start Key not pressed yet!")

def add_value(agent: str, json_file_path: str, key: str = "q"):
    json_file_path = resource_path(json_file_path)
    while True:
        mousep = pg.position()
        print(mousep)
        sleep(0.1)
        try:
            if keyboard.is_pressed(key):
                update_value(agent, mousep, json_file_path)
                return True  # Rückgabe, um anzuzeigen, dass die Aktualisierung erfolgreich war
        except:
            print("Key not pressed yet!")
            return False  # Rückgabe, um anzuzeigen, dass ein Fehler aufgetreten ist

def remove_agent(json_file_path):
    json_file_path = resource_path(json_file_path)
    try:
        # Create an empty dictionary to clear the JSON data
        json_data = {}

        # Save the empty data back to the file
        with open(json_file_path, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)

        print("All agents deleted successfully.")
    except FileNotFoundError:
        print(f"File '{json_file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

