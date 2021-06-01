#! /usr/bin/env python3
import os
import json
import requests
dir1="/home/student-03-3fec9be30d12/supplier-data"
for filename in os.listdir(dir1+"/descriptions"):
    if ".txt" in filename:
        with open(dir1+"/descriptions/"+filename) as f:
            data = f.read().split("\n")
            dic = {"name":data[0],"weight":int(data[1].split(" ")[0]),"description":data[2],"image_name": filename.split(".")[0]+".jpeg"}
            dic = json.dumps(dic)
            r = requests.post("http://34.70.80.33/fruits",data=dic)
            print(dic)
