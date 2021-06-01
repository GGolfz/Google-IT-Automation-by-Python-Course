#!/usr/bin/python3
import os
from PIL import Image
dir1="/home/student-03-3fec9be30d12/supplier-data"
for filename in os.listdir(dir1+"/images"):
    if ".tiff" in filename:
        Image.open(dir1+"/images/"+filename).convert("RGB").resize((600,400)).save(dir1+"/images/"+filename.split(".")[0]+".jpeg")
