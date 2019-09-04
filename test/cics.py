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
import random
import requests
#os.fork()
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")
mydb = myclient["sDAGf"]
mycol = mydb["pixelPhoto"]
infocol = mydb["pixelInfo"]
config =  Config.Net.Main()

web3 = Web3(Web3.HTTPProvider(config["net"]))
greeter = web3.eth.contract(
	address=config["contract"],
	abi=abi,
)

#web3 = Web3(Web3.HTTPProvider("http://192.168.51.212:9999"))
#greeter = web3.eth.contract(
#        address = "0xbe908eB8F90619F751Dd13F19Ce2446bdc05e225",
#        abi = abi,
#)
data = {}
a = 0
#ImageData
contractInput = "0xca144fa300000000000000000000000000000000000000000000000000000000000000"

#os.fork()
while(True):
    #time.sleep(3)
    #print("web3 Version:",web3.version.api)

    coor= hex(a).replace("0x","")
    
    if len(coor) < 2:
        coor = "0" + coor
    print("coor",coor)
    increase = contractInput + coor
    print("Input",increase)

    postData = {"from": "23471aa344372e9c798996aaf7a6159c1d8e3eac","to": "0xbe908eB8F90619F751Dd13F19Ce2446bdc05e225","balance": "0","nonce": 99,"input":increase, "type":"VvmDCall"}
    response = requests.post('http://125.227.132.130:5214/esGas',json=postData)

    out = "0x" + response.json()["ret"]
    print("response.ret",out)

    postDecode = {"args":["string","string","address","uint256","uint256"],"str":out}

    resDecode = requests.post('http://13.75.117.140:3368/casigo/sDAGdecode',json=postDecode)
    decoded = resDecode.json()

    print("decoded",decoded)

    #print("url",decoded["0"])
    #print("introduction",decoded["1"])
    #print("owner",decoded["2"])
    #print("time",int(decoded["3"]["_hex"],0))
    #print("dyn",int(decoded["4"]["_hex"],0))

    #output = greeter.functions["ImageData"](a).call()
    #print("output",output)
    #outputDecode = greeter.decode_function_input('0x'+response.json()["ret"])
    data["url"] = decoded["0"]
    data["introduction"] = decoded["1"]
    data["owner"] = decoded["2"]
    data["time"] = int(decoded["3"]["_hex"],0)
    data["price"] = int(decoded["4"]["_hex"],0)
    
    #data["price"] = str(greeter.functions["imagePrice"](a).call()*2)
    #data["sort"] = a
    #data["dyn"] = str(data["dyn"])
    data["address"] = config["contract"]
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
		#time.sleep(5000)




