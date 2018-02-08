#!/usr/bin/python3

import json
import requests
import shutil
import time
import os

api_key = "B2FD274279214B0AA4BEE21468CC7BC9"
timelapse_source = "/home/pi/.octoprint/timelapse/"
timelapse_destination = "/mnt/server1/junk/octoprint_timelapse/"

sleep_time = 600
url = "http://octopi/api/job"
headers = {'x-api-key': api_key}
response_json = requests.get(url, headers=headers).json()
printer_progress = response_json["progress"]["completion"]
printer_state = response_json["state"]

def tl_push():

    def tl_mover():
        for filename in os.listdir(timelapse_source):
            if filename.endswith('.mpg'):
                full_filename = timelapse_source + filename
                shutil.move(full_filename, timelapse_destination)

        print("Files Moved to NAS.")


    if printer_state == "Operational":
        print("Printer is online.")

        while printer_progress != None:
            sleep_minutes = int(sleep_time / 60)
            print("Printer is online and printing.  Rechecking in {} minutes.".format(sleep_minutes))
            time.sleep(1)

        else:
            print("Printer is not printing.  Moving files to NAS.")
            tl_mover()


    else:
        print("Printer is offline. Stopping script.")

print("Printer State is : {}".format(printer_state))
print("Printer Progress is : {}".format(printer_progress))
tl_push()
