import csv
from collections import OrderedDict
import pandas as pd
from random import randint
import numpy as np
from sklearn.utils import _list_indexing
import math
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

def get_recommendations(metadata, cosine_sim, day=1, category=['Alam', 'Budaya dan Sejarah'], budget=50000):
    # Get indices
    indices = pd.Series(metadata.index, index=metadata['nama']).drop_duplicates()
    # Calculate mean of vote average column
    C = metadata['vote_average'].mean()
    # Calculate the minimum number of votes required to be in the chart, m
    m = metadata['vote_count'].quantile(0.02)

    def weighted_rating(x, m=m, C=C):
        v = x['vote_count']
        R = x['vote_average']
        # Calculation based on the IMDB formula
        return (v/(v+m) * R) + (m/(m+v) * C)
    
    filtered = metadata.copy().loc[metadata['vote_count'] >= m]

    filtered['score'] = filtered.apply(weighted_rating, axis=1)

    filtered['htm_weekday'] = filtered['htm_weekday'].fillna(0) # filtered: metadata yg vote_count > m
    metadata['htm_weekday'] = metadata['htm_weekday'].fillna(0) # dan udah diweighted masuk ke 'score'

    #Sort destionation based on score calculated above
    filtered = filtered.sort_values('score', ascending=False) # sorting filtered bdsk 'score'

    df = filtered.to_dict('records')
    meta_dict = metadata.to_dict('records')

    if day > len(df):
        day = 1
    elif day < 1:
        day = 1
    
    each = math.ceil((day * 2) / len(category))

    count = 0

    while count < 5:
        name_dest = []
        for i in category:
            filtered_df = filtered.copy().loc[filtered['type'] == i]
            filtered_dict = filtered_df.to_dict('records')
            each_no = get_similiar(filtered_dict[randint(0,len(filtered_dict))-1]['nama'], cosine_sim, indices, day)[:each]
            # name_dest.append(filter_df[randint(0,len(filter_df))-1]['nama'])
            for j in each_no:
                name_dest.append(meta_dict[j])

        # sorted_name_dest = sorted(name_dest, key=lambda i: i['htm_weekday']) # Ascending

        # Count total_htm by iterating the list
        total_htm=0
        for dest in name_dest:
            total_htm += dest['htm_weekday']
        
        # If total htm below the budget, then break the loop
        if total_htm <= budget:
            break
        # If not, then start looping until total_htm below the budget
        count += 1

    content = []
    for dest in range(0, len(name_dest), 2):
        day = {'schedule': [name_dest[dest], name_dest[dest+1]]}
        content.append(day)
    
    return content, total_htm


# DIBAWAH UNTUK NGE TEST
# UNCOMMENT UNTUK TEST

# # Import TfIdfVectorizer and linear_kernel from scikit-learn
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import linear_kernel

# metadata = pd.read_csv("inventory/dataset.csv", low_memory=False)
# tfidf = TfidfVectorizer()

# #Replace NaN with an empty string
# metadata['description'] = metadata['description'].fillna('')

# #Construct the required TF-IDF matrix by fitting and transforming the data
# tfidf_matrix = tfidf.fit_transform(metadata['description'])

# # Compute the cosine similarity matrix
# cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# # parameter (dataframe, cosine_sim, day)
# budget = 50000
# category = ["Alam", "Pantai"]
# df, total_htm, count = get_recommendations(metadata, cosine_sim, 2, category, budget)

# print("count", count)
# print("budgetnya", budget)
# print("total_htm:", total_htm)
# # print(min_vote)
# # print(df[1])

# # print(len(df))
# for schedule_day_dict in df:
#     for key_of_list in schedule_day_dict:
#         for dict_of_places in schedule_day_dict[key_of_list]:
#             print(dict_of_places['nama'], end=' ')
#             print(dict_of_places['htm_weekday'])