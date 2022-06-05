#!/bin/bash

# echo "Welcome"
# function test () {
# echo "mis à jour des tweet"
#  python3 tweet.py
# }

# function test2 () {
# echo "This line should only print every 3 seconds..."

# sleep 13
# }


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