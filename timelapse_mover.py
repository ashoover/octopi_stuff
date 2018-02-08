#!/usr/bin/python3

import json
import requests
import shutil
import time
import os

api_key = "B2FD274279214B0AB4BEE21368CC7BC1"
timelapse_source = "/home/pi/.octoprint/timelapse/"
timelapse_destination = "/mnt/server/octoprint_timelapse/"

sleep_time = 600
url = "http://octopi/api/job"
headers = {'x-api-key': api_key}
response_json = requests.get(url, headers=headers).json()

def tl_push():

    def tl_mover():
        for filename in os.listdir(timelapse_source):
            if filename.endswith('.mpg'):
                full_filename = timelapse_source + filename
                shutil.move(full_filename, timelapse_destination)

    if printer_state == "Operational":
        while printer_progress != None:
            time.sleep(sleep_time)

        else:
            tl_mover()


    else:
        print("Printer is offline. Stopping script.")

tl_push()
