from web3 import Web3
import Config
net =  Config.Net.Set()["net"]
web3 = Web3(Web3.HTTPProvider(net))

class Sign:
    def ExpTransactionTx(nonce,amount):
        return {
            'to':Config.Net.Set()["contract"],
            'value': amount,
            'gas': 3000000,
            'gasPrice': 10**10,
            'nonce':nonce
        }
    def ContractTx(nonce,bytecode):
        return {
            'value': 0,
            'gas': 2000000,
            'gasPrice': 10**10,
            'nonce':nonce,
            'data':bytecode
        }
    def SignTx(transaction, key):
        signed = web3.eth.account.signTransaction(transaction, key)
        return signed.rawTransaction
    def Broadcast(raw):
        try:
            return web3.eth.sendRawTransaction(raw)
        except Exception as e:
            return e
    def Nonce(address):
        reAddress = web3.toChecksumAddress(address)
        return web3.eth.getTransactionCount(reAddress)


