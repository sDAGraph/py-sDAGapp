import threading
import binascii
import pymongo
import json
import sys

#from contract.Sol import Solidity
from transaction.sign import Sign 
#from contract.contract import Contract 
from lib.Web3 import w3


def sol_exp():
    #print(Solidity.Gunabizero("lotterybalance_L1"))
    print("Poker：",Solidity.Gunabitwo("Poker",0x12,1))
def deploymain_exp():
    signtx = Sign.SignTx(
            Sign.ContractTx(Sign.Nonce("0x47ED2C6cAE34FDB231B82Ec8D666646085ea3A92"),
                Contract.compile()["bin"]), 
            "116f08538a9373d8bc0b174f65bea2744aca4f0fc41eecea15d5851c4b19c02c")
    #print(binascii.hexlify(signtx).decode())
    txid = Sign.Broadcast(signtx)
    print(txid)
    print(binascii.hexlify(txid).decode())
#過濾交易資訊
def block_data():
    myclient = pymongo.MongoClient("mongodb://192.168.51.202:27017")
    mydb = myclient["testdatabase"]
    mycol = mydb["topcollection"]
    for i in range(5000000,6000000):
        print(i)
        transactionArray = []
        blockResult = w3.block(i)
        for tx in blockResult["transactions"]:
            txResult = binascii.hexlify(tx).decode()
            #txResult["logsBloom"] = binascii.hexlify(txResult["logsBloom"]).decode()
            #txResult["transactionHash"] = binascii.hexlify(txResult["transactionHash"]).decode()
            #txResult["blockHash"] = binascii.hexlify(txResult["blockHash"]).decode()
            transactionResult = w3.getTransactionReceipt(txResult)
            #print(transactionResult["AttributeDict"])
            #transactionResult.logsBloom1 = binascii.hexlify(transactionResult["logsBloom"]).decode()
            transactionJson={
                    'blockHash':binascii.hexlify(transactionResult["blockHash"]).decode(),
                    'blockNumber':transactionResult["blockNumber"],
                    'contractAddress':transactionResult["contractAddress"],
                    'cumulativeGasUsed':transactionResult["cumulativeGasUsed"],
                    'from':transactionResult["from"],
                    'gasUsed':transactionResult["gasUsed"],
                    'logs':transactionResult["logs"],
                    'logsBloom':binascii.hexlify(transactionResult["logsBloom"]).decode(),
                    #'root':transactionResult["root"],
                    'to':transactionResult["to"],
                    'transactionHash':binascii.hexlify(transactionResult["transactionHash"]).decode(),
                    'transactionIndex':transactionResult["transactionIndex"]
                    }
            transactionArray.append(transactionJson)#{"transactions":transactionJson})
        if(len(transactionArray)>0):
            mycol.insert_many(transactionArray)
def insertBlock():
    myclient = pymongo.MongoClient("mongodb://192.168.51.202:27017")
    mydb = myclient["testdatabase"]
    mycol = mydb["blockInfo"]
    for i in range(6446370,6700000):
        blockResult = w3.block(i)
        #print(blockResult)
        trans = []
        for r in blockResult["transactions"]:
            trans.append(binascii.hexlify(r).decode())
        unc = []
        for r in blockResult["transactions"]:
            unc.append(binascii.hexlify(r).decode())

        block = {
                'number':blockResult['number'],
                'timestamp':blockResult['timestamp'],
                'transactions':trans,#blockResult['transactions'],
                'uncles':unc,#blockResult['uncles'],
                'hash':blockResult['hash'],
                'miner':blockResult['miner']
        }
        print(i)
        #db.blockInfo.find().sort({"number":-1}).limit(1)
        try:
            mycol.insert(block)
        except:
            print("error key")
def blockUpdate():
    myclient = pymongo.MongoClient("mongodb://192.168.51.202:27017")
    mydb = myclient["testdatabase"]
    mycol = mydb["blockInfo"]
    x = mycol.find().sort([("number",pymongo.DESCENDING)]).limit(1)
    while True:
        if x[0]["number"] < w3.blockNumber()-100:
            blockResult = w3.block(x[0]["number"]+1)
            trans = []
            for r in blockResult["transactions"]:
                trans.append(binascii.hexlify(r).decode())
            unc = []
            for r in blockResult["transactions"]:
                unc.append(binascii.hexlify(r).decode())

            block = {
                'number':blockResult['number'],
                'timestamp':blockResult['timestamp'],
                'transactions':trans,#blockResult['transactions'],
                'uncles':unc,#blockResult['uncles'],
                'hash':blockResult['hash'],
                'miner':blockResult['miner']
            }
            print("blockNumber:",block['number'])
            try:
                mycol.insert(block)
                updateTransaction(mydb,block['number'])#x[0]["number"]+1)
                print("stay one second")
                sleep(1)
            except:
                print("pass")

def transaction_data():
    myclient = pymongo.MongoClient("mongodb://192.168.51.202:27017")
    mydb = myclient["testdatabase"]
    mycol = mydb["topcollection"]
    for i in range(int(sys.argv[2]),int(sys.argv[3])+1):
        print(i)
        transactionArray = []
        #blockResult = w3.block(i)
        mycol.insert_one({"miner":blockResult["miner"]})
        for tx in blockResult["transactions"]:
            print(tx)
        """
            txResult = binascii.hexlify(tx).decode()
            transactionResult = w3.getTransactionReceipt(txResult)
            transactionJson={
                    'transactionHash':binascii.hexlify(transactionResult["transactionHash"]).decode(),
                    'from':transactionResult["from"],
                    'contractAddress':transactionResult["contractAddress"],
                    'to':transactionResult["to"],
                    }
            transactionArray.append(transactionJson)#{"transactions":transactionJson})
        if(len(transactionArray)>0):
            mycol.insert_many(transactionArray)
        """
def updateTransaction(mydb,i):
    blockinfo = mydb["blockInfo"]
    transinfo = mydb["transInfo"]
    blockResult = blockinfo.find_one({"number":i})
    for tx in blockResult["transactions"]:
        transactionResult = w3.getTransactionReceipt(tx)
        trans = {
                'blockHash':binascii.hexlify(transactionResult["blockHash"]).decode(),
                'blockNumber':transactionResult["blockNumber"],
                'contractAddress':transactionResult["contractAddress"],
                'cumulativeGasUsed':transactionResult["cumulativeGasUsed"],
                'from':transactionResult["from"],
                'gasUsed':transactionResult["gasUsed"],
                'logs':transactionResult["logs"],
                'logsBloom':binascii.hexlify(transactionResult["logsBloom"]).decode(),
                #'status':transactionResult["status"],
                'to':transactionResult["to"],
                'transactionHash':binascii.hexlify(transactionResult["transactionHash"]).decode(),
                'transactionIndex':transactionResult["transactionIndex"]
        }
        transinfo.insert(trans)
def insertTransaction():
    myclient = pymongo.MongoClient("mongodb://192.168.51.202:27017")
    mydb = myclient["testdatabase"]
    blockinfo = mydb["blockInfo"]
    transinfo = mydb["transInfo"]
    for i in range(int(sys.argv[2]),int(sys.argv[3])+1):
        print(i)
        transactionArray = []
        blockResult = blockinfo.find_one({"number":i})
        #print(blockResult["number"])
        
        for tx in blockResult["transactions"]:
            transactionResult = w3.getTransactionReceipt(tx)
            trans = {
                'blockHash':binascii.hexlify(transactionResult["blockHash"]).decode(),
                'blockNumber':transactionResult["blockNumber"],
                'contractAddress':transactionResult["contractAddress"],
                'cumulativeGasUsed':transactionResult["cumulativeGasUsed"],
                'from':transactionResult["from"],
                'gasUsed':transactionResult["gasUsed"],
                'logs':transactionResult["logs"],
                'logsBloom':binascii.hexlify(transactionResult["logsBloom"]).decode(),
                #'status':transactionResult["status"],
                'to':transactionResult["to"],
                'transactionHash':binascii.hexlify(transactionResult["transactionHash"]).decode(),
                'transactionIndex':transactionResult["transactionIndex"]
            }
            try:
                transinfo.insert(trans)
            except:
                print("exist key")
            #print(trans)
        
def blockCheck():
    myclient = pymongo.MongoClient("mongodb://192.168.51.202:27017")
    mydb = myclient["testdatabase"]
    blockinfo = mydb["blockInfo"]
    transinfo = mydb["transInfo"]
    for i in range(int(sys.argv[2]),int(sys.argv[3])+1):
        #print(i)
        transactionArray = []
        blockResult = blockinfo.find_one({"number":i})
        print(blockResult["number"])

def address_data():
    myclient = pymongo.MongoClient("mongodb://192.168.51.202:27017")
    mydb = myclient["testdatabase"]
    mycol = mydb["topcollection"]
    init = int(sys.argv[2])
    final = int(sys.argv[3])
    print(int(final))
    
    for i in range(int(init),int(final)):
        print(i)
        transactionArray = []
        blockResult = w3.block(i)
        transactionArray.append({'address':blockResult["miner"]})
        for tx in blockResult["transactions"]:
            txResult = binascii.hexlify(tx).decode()
            transactionResult = w3.getTransactionReceipt(txResult)
            transactionArray.append({'address':transactionResult["from"]})
            transactionArray.append({'address':transactionResult["contractAddress"]})
            transactionArray.append({'address':transactionResult["to"]})
        if(len(transactionArray)>0):
            for array in transactionArray:
                try:
                    mycol.insert_one(array)
                except:
                    print("not unique:",array["address"])
    
def update_address():
    myclient = pymongo.MongoClient("mongodb://192.168.51.202:27017")
    mydb = myclient["testdatabase"]
    mycol = mydb["topcollection"]
    init = int(sys.argv[2])
    final = int(sys.argv[3])
    print(int(final))

    for i in range(int(init),int(final)):
        print(i)
        transactionArray = []
        blockResult = w3.block(i)
        transactionArray.append({'address':blockResult["miner"]})
        for tx in blockResult["transactions"]:
            txResult = binascii.hexlify(tx).decode()
            transactionResult = w3.getTransactionReceipt(txResult)
            #transactionArray.append({'address':transactionResult["from"]})
            #transactionArray.append({'address':transactionResult["contractAddress"]})
            transactionArray.append({'address':transactionResult["to"]})
        if(len(transactionArray)>0):
            for array in transactionArray:
                try:
                    mycol.insert_one(array)
                except:
                    print("not unique:",array["address"])
"""
def address_data():
    myclient = pymongo.MongoClient("mongodb://192.168.51.202:27017")
    mydb = myclient["testdatabase"]
    mycol = mydb["topcollection"]
    for i in range(int(sys.argv[1]),int(sys.argv[2])+1):
        print(i)
        transactionArray = []
        blockResult = w3.block(i)
        transactionArray.append({'address':blockResult["miner"]})
        for tx in blockResult["transactions"]:
            txResult = binascii.hexlify(tx).decode()
            transactionResult = w3.getTransactionReceipt(txResult)
            transactionArray.append({'address':transactionResult["from"]})
            transactionArray.append({'address':transactionResult["contractAddress"]})
            transactionArray.append({'address':transactionResult["to"]})
        if(len(transactionArray)>0):
            #for array in transactionArray:
            mycol.insert_many(transactionArray)
"""
def miningData():
    myclient = pymongo.MongoClient("mongodb://192.168.51.202:27017")
    mydb = myclient["testdatabase"]
    mycol = mydb["aF1"]
    #x = mycol.find().sort([("number",pymongo.DESCENDING)]).limit(1)
    content = mycol.find()
    result = []
    init = """
package main

func EthData()[]string{

    return []string{
    """
    end = """
            }

}
    """
    fo = open("data.go", "r+")
    fo.write(init +"\n")
    for con in content:
        fo.write('"'+str(con["address"])+'",' +"\n")
        #init = init + str(con["address"]) +"\n"
    #result.append(init)
    fo.write(end)
    fo.close()
def backupData():
    myclient = pymongo.MongoClient("mongodb://192.168.51.202:27017")
    mydb = myclient["testdatabase"]
    mycol = mydb["account"]
    #backupcol = mydb["aF1_test"]
    backclient = pymongo.MongoClient("mongodb://192.168.0.200:27017")
    backdb = backclient["main"]
    backcol = backdb["alladdress"]

    #x = mycol.find().sort([("number",pymongo.DESCENDING)]).limit(1)
    content = mycol.find()
    result = []
    for con in content:
        print(con)
        #result.append(con)
        try:
            backcol.insert(con)
        except:
            print("except")


if __name__ == '__main__':
    
    if sys.argv[1] == "1":
        t1 = threading.Thread(target=miningData)
        t1.start()
    if sys.argv[1] == "2":
        t2 = threading.Thread(target=backupData)
        t2.start()
    if sys.argv[1] == "3":
        t3 = threading.Thread(target=w3.minerList)
        t3.start()
    if sys.argv[1] == "4":
        t4 = threading.Thread(target=address_data())
        t4.start()
    if sys.argv[1] == "5":
        t5 = threading.Thread(target=insertBlock())
        t5.start()
    if sys.argv[1] == "6":
        t6 = threading.Thread(target=blockUpdate())
        t6.start()
    if sys.argv[1] == "7":
        t7 = threading.Thread(target=insertTransaction())
        t7.start()
    if sys.argv[1] == "8":
        t8 = threading.Thread(target=update_address())
        t8.start()
    if sys.argv[1] == "9":
        t9 = threading.Thread(target=blockCheck())
        t9.start()


