#!/bin/bash

function tweet(){
   echo "refresh tweet"
   python3 tweet.py
   sleep 130000
}

function analyse(){
   echo "Analyse"
   python3 Analyse.py
   sleep 13100
}

while : 
do
analyse && tweet
done