import numpy as np
import pandas as pd
import re
import urllib
from urllib.request import Request, urlopen
import csv
import json


def get_additional_info(ID):
    idx =  re.search("[0-9]*", ID)
    req = Request('http://www.politifact.com//api/v/2/statement/'+idx.group()+'/?format=json', headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
    a = json.loads(response)
    return a

datapath = 'data/liar_dataset/'

columns = ['ID',
           'Label',
           'Statement',
           'Subject',
           'Speaker',
           'Job title',
           'Home State',
           'Party Affiliations',
           'Barely True Counts',
           'False Counts',
           'Half True Counts',
           'Mostly True Counts',
           'Pants on Fire Counts',
           'Context']
liar_train = pd.read_csv(datapath + 'train.tsv',delimiter='\t',encoding='utf-8', names = columns)
liar_test = pd.read_csv(datapath + 'test.tsv',delimiter='\t',encoding='utf-8', names = columns)
liar_valid = pd.read_csv(datapath + 'valid.tsv',delimiter='\t',encoding='utf-8', names = columns)

liar_df = pd.concat([liar_train, liar_test, liar_valid])

date = liar_df[["ID"]].copy()

date["statement_date"] = pd.Series(np.zeros(len(date)))

with open('date.csv', mode='r') as date_file:
    csv_reader = csv.reader(date_file, delimiter=',')

    line_count = 0
    for row in csv_reader:
        line_count+=1
        #print(line_count)

with open('date.csv', mode='a') as date_file:

    csv_writer = csv.writer(date_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for i in range(line_count,len(date)):
        print(i, date.iloc[i,0])
        date.iloc[i,1] = get_additional_info(date.iloc[i,0])["statement_date"]
        csv_writer.writerow(date.iloc[i].values)
