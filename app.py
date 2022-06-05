# import main Flask class and request object
from flask import Flask, make_response, request
import json
import pandas as pd
from os.path import exists
import os.path
from IP import *
import csv
# from tweet import get_tweets
from pathlib import Path


path  = str(Path(__file__).parent)

try:
     os.path.isfile(path+'/Data/ip.json')
     print ("File exist")
except ValueError:
     print ("File not exist")



app = Flask(__name__)



@app.route("/")
def hello_world():
    return "<center><h1>data tweet_bi</h1><h1>tweet-entity</h1><h1>tweet-brut-csv</h1></center>"


@app.route('/tweet-entity')
def tweet_entity():
    setIP()
    with open(path+"/Data/entity.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()
    return jsonObject

# get teet.csv file which contains brut tweet data
@app.route('/tweet-brut-csv')
def form_example():
    dr = pd.read_csv(path+"/Data/tweet.csv")
    resp = make_response(dr.to_csv())
    resp.headers["Content-Disposition"] = "attachment; filename=tweet.csv"
    resp.headers["Content-Type"] = "text/csv"
    setIP()
    return resp


@app.route('/json-example')
def json_example():
    dr = pd.read_csv(path+"/Data/tweet_clean.csv")
    resp = make_response(dr.to_csv())
    resp.headers["Content-Disposition"] = "attachment; filename=tweet_clean.csv"
    resp.headers["Content-Type"] = "text/csv"
    setIP()
    return resp,200




@app.route("/get_ip")
def get_my_ip():
    setIP()
    with open(path+"/Data/ip.json") as jsonFile:   
        return jsonFile.read()
     




if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run()