import time as tm
import json
import pyautogui as pg
import settings
import build as build

def start(StartKey: str = settings.get_value("start_key"), StopKey: str = settings.get_value("end_key"), Remember: bool = False):
    if Remember:
        settings.update_value("start_key", StartKey)
        settings.update_value("end_key",StopKey)

    print("StartKey: ", StartKey, "StopKey: ", StopKey)
    #while True:
        #if pg.keyDown(StartKey):
            #tm.sleep(1)
        #if pg.keyDown(StopKey):
            #break

def main():
    build.root()

if __name__ == "__main__":
    main()