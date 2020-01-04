# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.1
#   kernelspec:
#     display_name: cv-hw
#     language: python
#     name: cv-hw
# ---

# import the necessary packages
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
import glob
import cv2
import os


cols = ["bedrooms", "bathrooms", "area", "zipcode", "price"]
df = pd.read_csv("keras-regression/Houses-dataset/Houses Dataset/HousesInfo.txt", sep=" ", names=cols)
df.head()

# +
# determine (1) the unique zip codes and (2) the number of data
# points with each zip code

zipcodes = df["zipcode"].value_counts().keys().tolist()
counts = df["zipcode"].value_counts().tolist()

# +
zipcode_drop = []

for zipcode, count in df["zipcode"].value_counts().items():
    if count <25:
        zipcode_drop.append(zipcode)

# -

len(zipcode_drop)

df = df.query("zipcode != @zipcode_drop")
print("ran as script")


# +
def process_house_attributes(train, test, y_col):
    # initialize the column names of the continuous data
    continuous = ["bedrooms", "bathrooms", "area"]

    # performin min-max scaling each continuous feature column to
    # the range [0, 1]
    cs = MinMaxScaler()
    train.loc[:,continuous] = cs.fit_transform(train[continuous])
    test.loc[:,continuous] = cs.transform(test[continuous])
    
    train["zipcode"] = train["zipcode"].astype(str)
    test["zipcode"] = test["zipcode"].astype(str)
    
    # one-hot encode the zip code categorical data (by definition of
    # one-hot encoing, all output features are now in the range [0, 1])
    trainX = pd.get_dummies(train.drop(columns=y_col))
    testX = pd.get_dummies(test.drop(columns=y_col))
    
    return (trainX, testX)
    


# -

def load_house_attributes(inputPath):
    cols = ["bedrooms", "bathrooms", "area", "zipcode", "price"]
    df = pd.read_csv(inputPath, sep=" ", names=cols)
    
    zipcodes = df["zipcode"].value_counts().keys().tolist()
    counts = df["zipcode"].value_counts().tolist()
    zipcode_drop = []

    for zipcode, count in df["zipcode"].value_counts().items():
        if count <25:
            zipcode_drop.append(zipcode)
    df = df.query("zipcode != @zipcode_drop")
    return df
