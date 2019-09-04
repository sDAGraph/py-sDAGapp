
class Abi:
    def Gunabi():
        return {
[
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
		#"type": "function"
	}
]

}
