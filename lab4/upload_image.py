#!/usr/bin/env python3
import requests
import os
# This example shows how a file can be uploaded using
# The Python Requests module
dir1="/home/student-03-3fec9be30d12/supplier-data"
for filename in os.listdir(dir1+"/images"):
    url = "http://localhost/upload/"
    if ".jpeg" in filename:
        if len(filename.split(".")) == 2:
            with open(dir1+"/images/"+filename, 'rb') as opened:
                r = requests.post(url, files={'file': opened})
