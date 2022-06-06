

# from logging import error
import os.path
import json
from flask import Flask
from flask import request

from pathlib import Path


# on obtient dynamiquement le chemin des fichiers
path  = str(Path(__file__).parent)
# Obtenir la liste des adresses IP et leur nombre de connexion
def setIP():
    # On importe le fichier pour écrire sur la dernière version du fichier
    if os.path.isfile(path+'/file/ip.json'):
        print ("File exist")
        with open(path+"/file/ip.json") as fp:
            iplist = json.load(fp)
        
        ip_found = False
        count  = 1
        # cherche dans a liste si l'ip existe si
        # si oui up_found pass a True
        for i in range(len(iplist)):
        
        #
            if iplist[i]["ip"] == request.remote_addr:
                count = iplist[i]["nombre de connexion"] + 1
                iplist[i]["nombre de connexion"] = count
                ip_found = True
        # l'adresse ip n'est pas dans le fichier on initilise le nombre de connexion à 0
        if(ip_found == False):
            iplist.append({'ip': request.remote_addr, "nombre de connexion": count})
            

        with open(path+"/file/ip.json", 'w') as json_file:
            json.dump(iplist, json_file, )
     
    
    
       
    else:
        pass
        