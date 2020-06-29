import pandas as pd
from pymongo import MongoClient
import json, requests
import os
from dotenv import load_dotenv
load_dotenv()
import requests
from pandas.io.json import json_normalize
import numpy as np


def transformToGeoPoint(s):
    if np.isnan(s.offices_latitude) or np.isnan(s.offices_longitude):
        return None
    return {
        "type":"Point",
        "coordinates":[s.offices_longitude, s.offices_latitude]
    }

def geoQueryNear(point,radius=10000):
    return {
        "geopoint":{
            "$near": {
                "$geometry": point,
                "$maxDistance": radius,
                "$minDistance": 0
            }
        }
    }

def getFoursquare(search):    
    url = 'https://api.foursquare.com/v2/venues/explore'
    params = dict(
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
    v='20180323',
    ll='37.795531,-122.400598',
    query=search,
    limit=1
    )
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)
    df_api = pd.DataFrame([{
        'query' : data['response']['query'],
        'name': data['response']['groups'][0]['items'][0]['venue']['name'],
        'distance' :data['response']['groups'][0]['items'][0]['venue']['location']['distance'],
        'address': data['response']['groups'][0]['items'][0]['venue']['location']['formattedAddress'][0],
        'postal_code':data['response']['groups'][0]['items'][0]['venue']['location']['postalCode'],
        'latitude' : data['response']['suggestedBounds']['ne']['lat'],
        'longitude' : data['response']['suggestedBounds']['ne']['lng'] }])
    return df_api


def getFoursquareFinal(search):    
    url = 'https://api.foursquare.com/v2/venues/explore'
    params = dict(
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
    v='20180323',
    ll='37.798403,-122.400990',
    query=search,
    limit=1
    )
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)
    df_api = pd.DataFrame([{
        'query' : data['response']['query'],
        'name': data['response']['groups'][0]['items'][0]['venue']['name'],
        'distance' :data['response']['groups'][0]['items'][0]['venue']['location']['distance'],
        'address': data['response']['groups'][0]['items'][0]['venue']['location']['formattedAddress'][0],
        'postal_code':data['response']['groups'][0]['items'][0]['venue']['location']['postalCode'],
        'latitude' : data['response']['suggestedBounds']['ne']['lat'],
        'longitude' : data['response']['suggestedBounds']['ne']['lng'] }])
    return df_api

