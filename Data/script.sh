#!/bin/bash

function tweet(){
   echo "refresh tweet"
   python3 tweet.py
   sleep 43200
}

function analyse(){
   echo "Analyse"
   
   python3 Analyse.py
   sleep 43230
}

# boucle infint qui rexecute les deux fonctions toutes les 
while : 
   do
      tweet && analyse
done