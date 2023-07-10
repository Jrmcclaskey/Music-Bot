#!/usr/bin/env python
# coding: utf-8

# In[85]:


# import statements
import os
import numpy as np
import pandas as pd
import seaborn as sns
import plotly as px
import matplotlib.pyplot as plt
import plotly.express as px
import string
import re


# In[132]:


# import csv
df_music = pd.read_csv("train.csv")

# show df
df_music.head()


# In[133]:


# normalizing dataframe headers and replaceing double spaces in vendor name
df_music.columns = df_music.columns.str.lower().str.replace(r'\s+', '_', regex=True)

# show df
df_music.head()


# In[134]:


# defines a function to exract featured artists if there are any
def extract_featured_artist(track_name):
    pattern = r"\(feat\. ([^)]+)\)"  # notates a pattern to match "(feat. artist)"
    match = re.search(pattern, track_name)
   # if statement when we find a match
    if match:
        featured_artist = match.group(1)
        track_name = re.sub(pattern, "", track_name)  # removes the "(feat. artist)" from track_name
        return track_name.strip(), featured_artist.strip()
    
    return track_name.strip(), None
# show df
df_music.head()


# In[135]:


df_music["featured_artist"] = "" # makes a new column in the datafram for featured artists

# sets up a for loop to run our function
for index, row in df_music.iterrows():
    track_name = row["track_name"]
    track_name, featured_artist = extract_featured_artist(track_name)
    df_music.at[index, "track_name"] = track_name
    df_music.at[index, "featured_artist"] = featured_artist.strip() if featured_artist else None 

# show df
df_music.head(30)


# In[136]:


def track_name_cleaner(track_name):
    
    if track_name is not None:
        # Remove all text after the hyphen '-'
        track_name = track_name.split('-')[0].strip()
    
    return track_name
    
# apply the track_name_cleaner function to all rows
df_music["track_name"] = df_music["track_name"].apply(track_name_cleaner)
    
# show df
df_music.head(30)


# In[137]:


# Replace NaN values in "instrumentalness" column with 0's
df_music["instrumentalness"].fillna(0, inplace=True)


# show df
df_music.head(30)


# In[141]:


# Calculate the average song popularity by artist
average_popularity_by_artist = df_music.groupby("artist_name")["popularity"].mean()

# Sort the average popularity values in descending order and select the top ten
top_ten_artists = average_popularity_by_artist.sort_values(ascending=False).head(25)

# Plot the top ten average song popularity by artist
plt.figure(figsize=(12, 6))
top_ten_artists.plot(kind="bar")
plt.xlabel("Artist")
plt.ylabel("Average Song Popularity")
plt.title("Top Twenty-five Average Song Popularity by Artist")
plt.xticks(rotation=90)
plt.show()


# In[142]:


# Calculate the average song popularity by artist
average_popularity_by_artist = df_music.groupby("artist_name")["popularity"].mean()

# Sort the average popularity values in descending order and select the top ten
top_ten_artists = average_popularity_by_artist.sort_values(ascending=True).head(25)

# Plot the top ten average song popularity by artist
plt.figure(figsize=(12, 6))
top_ten_artists.plot(kind="bar")
plt.xlabel("Artist")
plt.ylabel("Average Song Popularity")
plt.title("Bottom twenty-five Average Song Popularity by Artist")
plt.xticks(rotation=90)
plt.show()


# In[ ]:




