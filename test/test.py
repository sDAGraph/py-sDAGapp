abi = [
	{
		"constant": False,
		"inputs": [
			{
				"name": "bal",
				"type": "uint256"
			}
		],
		"name": "getBalance",
		"outputs": [
			{
				"name": "result",
				"type": "bool"
			}
		],
		"payable": True,
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [
			{
				"name": "coor",
				"type": "uint256"
			}
		],
		"name": "imagePrice",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "price",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"name": "coor",
				"type": "uint256"
			},
			{
				"name": "coimage",
				"type": "string"
			},
			{
				"name": "introduction",
				"type": "string"
			}
		],
		"name": "buyCoordinator",
		"outputs": [],
		"payable": True,
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"name": "ImageData",
		"outputs": [
			{
				"name": "image",
				"type": "string"
			},
			{
				"name": "introduction",
				"type": "string"
			},
			{
				"name": "owner",
				"type": "address"
			},
			{
				"name": "time",
				"type": "uint256"
			},
			{
				"name": "dyn",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	}
]
import Config
from web3 import Web3
from random import *
import pymongo
import os
import time
<<<<<<< HEAD
import random
#os.fork()
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")
mydb = myclient["sDAGf"]
mycol = mydb["pixelPhoto"]
infocol = mydb["pixelInfo"]
=======
#os.fork()
myclient = pymongo.MongoClient("mongodb://192.168.51.203:27017")
mydb = myclient["sDAGf"]
mycol = mydb["pixelPhoto"]

>>>>>>> 7c8920216ced3946c0119580954fb262281fcae6
config =  Config.Net.Main()

web3 = Web3(Web3.HTTPProvider(config["net"]))
greeter = web3.eth.contract(
	address=config["contract"],
	abi=abi,
)
data = {}
a = 0
#os.fork()
while(True):
<<<<<<< HEAD
    #time.sleep(3)
    print("index",a)
    data["url"],data["introduction"], data["owner"],data["time"],data["dyn"] = greeter.functions["ImageData"](a).call()
    data["price"] = str(greeter.functions["imagePrice"](a).call()*2)
    data["sort"] = a
    data["dyn"] = str(data["dyn"])
    data["address"] = config["contract"]
    print(data["address"])
    print(data)
    if data["url"]=="":
        print(str(randrange(300, 800, 2)))
        data["url"] = "https://picsum.photos/id/"+str(randrange(1, 1000, 1))+"/600/600"#str(randrange(300, 800, 2))
        #data["price"] = "1000"
        data["introduction"] = "default image"
    mycol.update({'sort':a}, {'$set': data}, upsert=True)
    try:
        findinfo = infocol.find()[0]
        #findinfo["TFHuser"]+1
        #findinfo["TFHtransaction"]+1
        u = random.randint(1,101)
        t = random.randint(1,101)
        infocol.update({}, {'$set': {"TFHuser":u,"totaluser":findinfo["totaluser"]+u,"contactBalance":230.5, "TFHtransaction":t,"totalTransaction":findinfo["totalTransaction"]+t}}, upsert=True)
    except:
        infocol.update({}, {'$set': {"TFHuser":0,"totaluser":0,"contactBalance":230.5, "TFHtransaction":0,"totalTransaction":0}}, upsert=True)
    a=a+1	
    if a >200:
        a = 0
=======
	#time.sleep(3)
	print("index",a)
	data["url"],data["introduction"], data["owner"],data["time"],data["dyn"] = greeter.functions["ImageData"](a).call()
	data["price"] = str(greeter.functions["imagePrice"](a).call()*2)
	data["sort"] = a
	data["dyn"] = str(data["dyn"])
	print(data)
	if data["url"]=="":
		print(str(randrange(300, 800, 2)))
		data["url"] = "https://picsum.photos/id/"+str(randrange(300, 800, 2))+"/1000/1000"
		#data["price"] = "1000"
		data["introduction"] = "1000"
	mycol.update({'sort':a}, {'$set': data}, upsert=True)
	a=a+1	
	if a >200:
		a = 0
>>>>>>> 7c8920216ced3946c0119580954fb262281fcae6
		#time.sleep(5000)




