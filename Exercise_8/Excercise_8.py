"""

Healthy Programmer
    1. Water in Every 30 mints
    2. Eyes in Every 30 Mints
    3. Movement in Every 45 mints

"""

from asyncore import write
from datetime import datetime
from time import time;
from pygame import mixer
from os.path import exists

# Setting up time for the events
interval_water = 20*60 
interval_eyes = 30*60
interval_exercise = 45*60

events = {
    1: "water",
    2: "eyes",
    3: "exercise",
    4: "general"
}

alarms = {
    "water": "water.mp3",
    "eyes": "eyes.mp3",
    "exercise": "exercise.mp3"
}

def write_log(str, event = 4):
    fn = events.get(event)
    fileName = fn + ".log"

    with open(fileName, "a") as f:
        log_time = datetime.now().strftime("%m/%d/%y, %H:%M:%S")
        f.write(f"{log_time}: {str}\n")

def music_on_loop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()

    stoppers = ["drank", "eydone", "exdone"]

    while True:
        a = input()
        if(a.lower() not in stoppers):
            print("Please provide valid inpur")
        
        if(a.lower() == stopper.lower()):
            break

def check_files():
    for key, value in alarms.items():
        if(not exists(value)):
            print(f"Sound of {key} doesn't exists")

if __name__ == "__main__":
    check_files()
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    write_log("Started ... ")
    while True:
        curr_time = time()
        if (curr_time - init_water) > interval_water:
            print("Time to drink water. Enter 'Drank' to stop the alarm.")
            write_log("Time to drink water. Enter 'Drank' to stop the alarm.", 1)
            music_on_loop(alarms.get("water"), "Drank")
            init_water = time()
            write_log("Water drank", 1)

        if(curr_time - init_eyes) > interval_eyes:
            print("Time for eye exercise. Enter 'EyDone' to stop the alarm.")
            write_log("Time for eye exercise", 2)
            music_on_loop(alarms.get("eyes"), "EyDone")
            init_eyes = time()
            write_log("Eye exercise done", 2)

        if(curr_time - init_exercise) > interval_exercise:
            print("Time for exercise. Enter 'ExDone' to stop the alarm.")
            write_log("Time for exercise", 3)
            music_on_loop(alarms.get("exercise"), "ExDone")
            init_exercise = time()
            write_log("Exercise done", 3)
            