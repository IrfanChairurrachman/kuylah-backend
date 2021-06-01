import csv
from collections import OrderedDict
import pandas as pd
from random import randint
import numpy as np
from sklearn.utils import _list_indexing

# from django.urls import path, include


# def get_data():
#     metadata = pd.read_csv('inventory/dataset.csv', low_memory=False)
#     return metadata

# print("MASOK")

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

# Function that takes in movie title as input and outputs most similar destination
def get_similiar(title, cosine_sim, indices, day=1):
    # Get the index of the dest that matches the name
    idx = indices[title]

    # Get the pairwsie similarity scores of all destination with input dest
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the similar destionation
    total = (day * 2) + 1
    sim_scores = sim_scores[:total]

    # Get the destination indices
    dest_indices = [i[0] for i in sim_scores]

    return dest_indices

def get_recommendations(metadata, cosine_sim, day=1, category=['Alam', 'Budaya dan Sejarah']):
    # Get indices
    indices = pd.Series(metadata.index, index=metadata['nama']).drop_duplicates()
    # Calculate mean of vote average column
    C = metadata['vote_average'].mean()
    # Calculate the minimum number of votes required to be in the chart, m
    m = metadata['vote_count'].quantile(0.5)

    def weighted_rating(x, m=m, C=C):
        v = x['vote_count']
        R = x['vote_average']
        # Calculation based on the IMDB formula
        return (v/(v+m) * R) + (m/(m+v) * C)
    
    filtered = metadata.copy().loc[metadata['vote_count'] >= m]

    filtered['score'] = filtered.apply(weighted_rating, axis=1)

    filtered['htm_weekday'] = filtered['htm_weekday'].fillna(0)
    metadata['htm_weekday'] = metadata['htm_weekday'].fillna(0)

    #Sort destionation based on score calculated above
    filtered = filtered.sort_values('score', ascending=False)

    df = filtered.to_dict('records')
    meta_dict = metadata.to_dict('records')

    if day > len(df):
        day = 1
    elif day < 1:
        day = 1
    
    each = int((day * 2) / len(category))

    name_dest = []
    for i in category:
        filtered = metadata.copy().loc[metadata['type'] == i]
        filter_df = filtered.to_dict('records')
        each_no = get_similiar(filter_df[randint(0,len(filter_df))-1]['nama'], cosine_sim, indices, day)[:each]
        # name_dest.append(filter_df[randint(0,len(filter_df))-1]['nama'])
        for j in each_no:
            name_dest.append(meta_dict[j])
    
    content = []
    for dest in range(0, len(name_dest), 2):
        day = {'schedule': [name_dest[dest], name_dest[dest+1]]}
        content.append(day)

    # FUNGSI SEBELUM MENGGUNAKAN SKLEARN
    # for i in range(day):
    #     dest_list = {"schedule":[df[randint(0,len(df))-1] for j in range(2)]}
    #     content.append(dest_list)
    # content = [{"schedule": [df[randint(0,len(df) - 1)] for j in range(2)] for i in range(day)}]

    total_htm = 0

    for schedule_day_dict in content:
        for key_of_list in schedule_day_dict:
            for dict_of_places in schedule_day_dict[key_of_list]:
                total_htm += dict_of_places['htm_weekday']
    
    return content, total_htm


# DIBAWAH UNTUK NGE TEST
# UNCOMMENT UNTUK TEST

# #Import TfIdfVectorizer from scikit-learn
# from sklearn.feature_extraction.text import TfidfVectorizer
# # Import linear_kernel
# from sklearn.metrics.pairwise import linear_kernel
# # Create your views here.

# metadata = pd.read_csv("dataset.csv", low_memory=False)

# tfidf = TfidfVectorizer()

# # metadata = pd.read_csv('dataset.csv', low_memory=False)

# #Replace NaN with an empty string
# metadata['description'] = metadata['description'].fillna('')

# #Construct the required TF-IDF matrix by fitting and transforming the data
# tfidf_matrix = tfidf.fit_transform(metadata['description'])

# # Compute the cosine similarity matrix
# cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# # parameter (dataframe, cosine_sim, day)
# df, budget = get_recommendations(metadata, cosine_sim, 2)

# print("budgetnya", budget)
# # print(df[1])

# # print(len(df))
# for schedule_day_dict in df:
#     for key_of_list in schedule_day_dict:
#         for dict_of_places in schedule_day_dict[key_of_list]:
#             print(dict_of_places['nama'], end=' ')
#             print(dict_of_places['htm_weekday'])