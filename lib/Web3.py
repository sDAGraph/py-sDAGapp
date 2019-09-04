from web3 import Web3
import Config
net =  Config.Net.Set()["net"]

web3 = Web3(Web3.HTTPProvider(net))#net))

class w3:
    def block(num):
        return web3.eth.getBlock(num)
    def blockNumber():
        return web3.eth.blockNumber
    def getTransaction(hashs):
        return web3.eth.getTransaction(hashs)
    def getTransactionReceipt(hashs):
        return web3.eth.getTransactionReceipt(hashs)
    def minerList():
        for num in range(4600000, 4713993):#4713877):
            print(num)
            a = []
            a.append(w3.block(num)["miner"])
        fo = open("test.txt", "w")
        fo.write(str(a))
        fo.close()
    def getBalance(hashs):
        return web3.eth.getBalance(hashs)
    def checkAddress(hashs):
        return Web3.toChecksumAddress(hashs)
