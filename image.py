#!/usr/bin/python3
import os
from PIL import Image
dir1="/home/student-02-2c346389f1b9"
for filename in os.listdir(dir1+"/images"):
    Image.open(dir1+"/images/"+filename).convert("RGB").rotate(270).resize((128, 128)).save("/opt/icons/"+filename+".jpg")
