import pymongo

import sys
sys.path.append("../")
from lib.Web3 import w3


myclient = pymongo.MongoClient("mongodb://192.168.51.202:27017")

mydb = myclient["testdatabase"]
mycol = mydb["topcollection"]
mycol2 = mydb["topcollection2"]


#x = mycol.find({})
#print(x)
#bal = []
#bal.append("add")
#print(x[1])

#print(x[40000000])
result = []
i=0
for x in mycol.find():
    if(i >= int(sys.argv[1]) and i<int(sys.argv[2])):
        result.append(x)
    i = i+1
    print(i)
#for i in range(int(sys.argv[1]),int(sys.argv[2])):
for d in result:
    print(d)
    try:
        bala = w3.getBalance(w3.checkAddress(d["address"]))
        mycol2.insert({"address":d["address"].lower(), "balance":str(bala)})
    except:
        print("error address")
