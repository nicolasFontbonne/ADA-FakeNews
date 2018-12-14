import numpy as np
import pandas as pd
import re
import urllib
from urllib.request import Request, urlopen
import csv
import json
import requests

#https://www.politifact.com//api/v/2/statementlist/?order_by=-ruling_date&offset=1&limit=1&format=json
def get_data(i):
    response = requests.get('https://www.politifact.com//api/v/2/statementlist/?order_by=-ruling_date&offset='+str(i)+'&limit=1&format=json')
    a = json.loads(response.text)['objects']
    return a


with open('politifact.csv', mode='r') as date_file:
    csv_reader = csv.reader(date_file, delimiter=',')

    line_count = 0
    for row in csv_reader:
        line_count+=1
        #print(line_count)


with open('politifact.csv', mode='a') as date_file:
    csv_writer = csv.writer(date_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    if line_count == 0:
        csv_writer.writerow(["Date", "Label", "Speaker", "Political Party", "Subject", "Photo"])

    for i in range(line_count,20000):
        print(i)
        data = get_data(i)
        for d in data:
            try:
                date = d['statement_date']
                label = d['ruling']['advalue']
                speaker = d['speaker']['first_name'] +" "+ d['speaker']['last_name']
                political_party = d['speaker']['party']['party']
                subjects = [sub['subject'] for sub in d['subject']]
                photo = d['speaker']['photo']
                row = [date,label,speaker,political_party, ';'.join(subjects), photo]
            #print(row)
                csv_writer.writerow(row)
                break
            except UnicodeEncodeError:
                pass
