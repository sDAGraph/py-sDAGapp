from web3 import Web3
web3 = Web3(Web3.HTTPProvider("https://ropsten.infura.io"))


class Net:
    def Main():
        return {
                "mongo":"mongodb://192.168.51.202:27017",
                #"net":"http://192.168.51.203:9999",
                #"net":"http://127.0.0.1:9999",
                "net":"http://192.168.51.203:19999",
                "contract": Web3.toChecksumAddress("0xfB05FF4F0cA7940ED801AA164af81D40cB567a7F")
                }
    def Ropsten():
        return {
                "net":"https://ropsten.infura.io/",
                #"contract": Web3.toChecksumAddress("0x103d7643540dd48800d97a29048a7058542680dbc6b105c98f469d5f3862c3ec")
                "contract": Web3.toChecksumAddress("0xfB05FF4F0cA7940ED801AA164af81D40cB567a7F")
                }
    def Testrpc():
        return {
                "net":"http://127.0.0.1:8545",
                "contract": Web3.toChecksumAddress("0x67687cfca900305f64e0efb4fe5545c842fac9f8")
                }
    def BYBrpc():
        return {
                "net":"http://10.0.7.16:9500",
                "contract": Web3.toChecksumAddress("0x67687cfca900305f64e0efb4fe5545c842fac9f8")
                }
    def Set():
        return Net.Main()
        #return Net.Ropsten()
        #return Net.Testrpc()
