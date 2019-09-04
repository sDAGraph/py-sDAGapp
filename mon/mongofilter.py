import pymongo

import sys
sys.path.append("../")
from lib.Web3 import w3


myclient = pymongo.MongoClient("mongodb://192.168.51.202:27017")

mydb = myclient["testdatabase"]
mycol = mydb["accountFilter"]
mycol6 = mydb["aF1"]
mycol2 = mydb["accountO4"]
mycol3 = mydb["accountO1"]
mycol4 = mydb["accountO2"]
mycol5 = mydb["accountO3"]

result = []
i=0
for x in mycol.find():
    i= i+1
    print(i)
    #print(x)
    result.append(x)
for d in result:
    print(d)
    #try:
    #if len(d["balance"]) > 15 and len(d["balance"]) < 18:
        #mycol2.insert({d})
    #try:
    if len(d["balance"]) >= 20:
        mycol6.insert(d)
    #except:
        #print("error")
    """
    if len(d["balance"]) >= 18 and len(d["balance"]) < 19:
        mycol3.insert(d)
    elif len(d["balance"]) >= 19 and len(d["balance"]) < 20:
        mycol4.insert(d)
    elif len(d["balance"]) >= 20 and len(d["balance"]) < 21:
        mycol5.insert(d)
    else:
        mycol2.insert(d)
    """
