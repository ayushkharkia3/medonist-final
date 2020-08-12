import datetime
import pandas as pd
import numpy as np
import sklearn as sks
import nltk
from datetime import timedelta
from datetime import datetime , date
import string
from collections import Counter

from fastapi import FastAPI
from typing import Optional

from pydantic import BaseModel

app = FastAPI()

data_train=pd.read_csv('drugsComTrain_raw.tsv', sep='\t')

class Item(BaseModel):
    name: list = []
    



def test(data_train, item):
    print(type(item))
    data_train['date']=pd.to_datetime(data_train['date'] , infer_datetime_format=True)
    score = data_train.rating * data_train.usefulCount
    data_train['Score'] = score
    sample_data2 = data_train[['drugName' , 'condition','review', 'rating', 'usefulCount','Score' ]]
    result = pd.DataFrame(columns = ['drugName' , 'condition','review' 'rating', 'usefulCount','Score' ])
    resultt1 = []
    resultt2 = []
    user_input = item
    for xx in user_input:
        print(len(user_input))
        print(xx)
        for i in sample_data2 :
            result = sample_data2['condition'].isin([xx])
        dn=pd.DataFrame(sample_data2[result])
        med_count=Counter(dn['drugName'])
        dd = pd.Series(med_count)
        dd.sort_values(ascending=False, inplace=True)
        dn.sort_values(by=['Score'] , ascending=False , inplace=True)
        pat = dn.drop_duplicates(subset ="drugName")
        pat_final=pat.drop(labels = ['condition' , 'usefulCount' ,'rating' , 'review'  ] ,axis=1)
        docc  = dd.to_frame(name="vals")
        docc = docc.vals.iloc[:2]
        docc.to_dict()
        docc = docc.astype('object')
        patt = pat_final.drugName.iloc[:2]
        resultt1.append(docc)
        resultt2.append(patt)
    return(resultt1, resultt2)
        

@app.get('/')
async def create():
    return("OK")

@app.post("/predict/")
async def create_item(item: Item):
    return(test(data_train, item.name))
 

    