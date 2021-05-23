import csv
from collections import OrderedDict
import pandas as pd
from random import randint
import numpy as np

# from django.urls import path, include


# def get_data():
#     metadata = pd.read_csv('inventory/dataset.csv', low_memory=False)
#     return metadata

def get_wisata():
    wisata = []
    with open('inventory/dataset.csv','r') as f:
    # with open('dataset.csv','r') as f:
        r = csv.DictReader(f)
        for row in r:
            print(row)
            wisata.append(row)
        # od = collections.OrderedDict(r)
    return wisata


def get_popular(metadata, day=1):
    
    # Calculate mean of vote average column
    C = metadata['vote_average'].mean()
    # Calculate the minimum number of votes required to be in the chart, m
    m = metadata['vote_count'].quantile(0)

    def weighted_rating(x, m=m, C=C):
        v = x['vote_count']
        R = x['vote_average']
        # Calculation based on the IMDB formula
        return (v/(v+m) * R) + (m/(m+v) * C)
    
    filtered = metadata.copy().loc[metadata['vote_count'] >= m]

    filtered['score'] = filtered.apply(weighted_rating, axis=1)

    filtered['htm_weekday'] = filtered['htm_weekday'].fillna(0)

    #Sort movies based on score calculated above
    filtered = filtered.sort_values('score', ascending=False)

    df = filtered.to_dict('records')
    # df = filtered.to_dict('records', into=OrderedDict)

    if day > len(df):
        day = 1
    
    content = {i+1: [df[randint(0,len(df) - 1)] for i in range(2)] for i in range(day)}

    total_htm = 0

    for i in content:
        for j in content[i]:
            total_htm += j['htm_weekday']
    
    return content

# metadata = pd.read_csv('dataset.csv', low_memory=False)
# df, budget = get_popular(metadata, 2)
# # df_baru = df.to_dict(into=OrderedDict)