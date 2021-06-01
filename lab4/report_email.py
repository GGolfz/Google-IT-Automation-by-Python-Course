#!/usr/bin/env python3
import os
from datetime import date
import reports
import emails

dir1="/home/student-03-3fec9be30d12/supplier-data"
message = []
for filename in os.listdir(dir1+"/descriptions"):
    if ".txt" in filename:
        with open(dir1+"/descriptions/"+filename) as f:
            data = f.read().split("\n")
            message.append("name: "+data[0])
            message.append("weight: "+data[1])
            message.append("")
print(message)

reports.generate("/tmp/processed.pdf","Processed Update on "+date.today().strftime("%B %d, %Y"),"<br/>".join(message))
sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
subject = "Upload Completed - Online Fruit Store"
body = "\n".join(message)
mail = emails.generate(sender, receiver, subject, body, "/tmp/processed.pdf")
emails.send(mail)
