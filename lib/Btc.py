from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import logging

logging.basicConfig()
logging.getLogger("BitcoinRPC").setLevel(logging.DEBUG)

rpc_connection = AuthServiceProxy("http://xxx:xxx@192.168.51.202:8332")
print(rpc_connection.getinfo())
