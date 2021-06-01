#! /usr/bin/env python3
import os
import json
import requests
for filename in os.listdir("/data/feedback"):
    with open("/data/feedback/"+filename) as f:
        data = f.read().split("\n")
        dic = {"title":data[0],"name":data[1],"date":data[2],"feedback":data[3]}
        dic = json.dumps(dic)
        r = requests.post("http://35.226.150.155/feedback",data=dic)
        print(r)
