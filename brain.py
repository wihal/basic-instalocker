import json
import pyautogui as pg
import json
import keyboard
from time import sleep
import os
import sys

# Funktioniert einfach keine ahnung wie. Danke Bro https://stackoverflow.com/a/31966932/16335953
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2 # Noch nie davon gehört
    except Exception:
        base_path = os.path.abspath(".")

    result = os.path.join(base_path, relative_path)
    return result 

def agents_list(path: str):
    path = resource_path(path)
    object_names = []  # Erstelle eine leere Liste für die Namen der Objekte

    with open(path, 'r') as json_file:
        data = json.load(json_file)

        if isinstance(data, list):
            for obj in data:
                if isinstance(obj, dict):
                    object_names.extend(obj.keys())  # Füge die Schlüssel zur Liste hinzu
        elif isinstance(data, dict):
                object_names.extend(data.keys())  # Füge die Schlüssel des einzigen Objekts hinzu

    return object_names

def get_value(item:str, path: str):
    path = resource_path(path)
    try:
        with open(path, 'r') as json_file:
            data = json.load(json_file)

            # Überprüfe, ob der Schlüssel (key) in den JSON-Daten existiert
            if item in data:
                return data[item]
            else:
                pass

    except FileNotFoundError:
        print(f'Die Datei "{path}" wurde nicht gefunden.')
    except json.JSONDecodeError:
        print(f'Die Datei "{path}" ist keine gültige JSON-Datei.')

def update_item(item: str, value, path: str):
    path = resource_path(path)
    try:
        with open(path, 'r') as file:
            data = json.load(file)

        data[item] = value

        with open(path, 'w') as file:
            json.dump(data, file, indent=4)
        
        print(f"Updated '{item}' to '{value}' in {path}")
    
    except FileNotFoundError:
        print(f"Error: {path} not found.")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in {path}")
    except Exception as e:
        print(f"An error occurred: {e}")


def start(startkey: str, stopkey: str, agent: str):

    agent_pos = get_value(agent, ".vlocker\\agents.json")
    button_pos = get_value("Button", ".vlocker\\settings.json")
    print("StartKey: "+ startkey + "\n StopKey: " + stopkey + "\n Agent: " + agent)
    
    while True:
        try: 
            if keyboard.is_pressed(startkey):
                while True:
                    pg.mouseDown(agent_pos[0], agent_pos[1], duration=0.1)
                    pg.mouseUp(agent_pos[0], agent_pos[1], duration=0.1)
                    
                    pg.mouseDown(button_pos[0], button_pos[1], duration=0.1)
                    
                    pg.mouseUp(button_pos[0], button_pos[1], duration=0.1)
                    
                    try: 
                        if keyboard.is_pressed(stopkey):
                            return True
                    except:
                        pass
        except:
            pass

def add_item(agent: str, json_file_path: str, key: str = "q"):
    json_file_path = resource_path(json_file_path)
    while True:
        mousep = pg.position()
        sleep(0.1)
        try:
            if keyboard.is_pressed(key):
                update_item(agent, mousep, json_file_path)
                return True  # Rückgabe, um anzuzeigen, dass die Aktualisierung erfolgreich war
        except:
            return False  # Rückgabe, um anzuzeigen, dass ein Fehler aufgetreten ist

def reset_json(path: str):
    path = resource_path(path)
    try:
        # leere JSON-Datei erstellen
        json_data = {}

        with open(path, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)

    except FileNotFoundError:
        print(f"File '{path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        
# Löscht ein JSON object
def remove_item(agent: str, path: str):
    path = resource_path(path)
    try:
        with open(path, "r") as file:
            counter_data = json.load(file)
        del counter_data[agent]
        with open(path, "w") as file:
            json.dump(counter_data, file)
    except FileNotFoundError:
        print(f"File '{path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")