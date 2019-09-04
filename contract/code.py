

class Code:
    def source_code():
        contract_source_code = '''
pragma solidity ^0.4.25;


contract RandomContract {

    function RandomArray(uint8[] intArray, uint privatekey, uint blocknumber) public constant returns (uint[]){
        
        uint[] resultArray;
        
        for (uint i2=0;i2<52;i2++){
        
            uint randi2 = randomint(privatekey+i2, 52,blocknumber);
            
            uint randnumber;
            
            for(uint i3=0;i3<52;i3++){
                
                if(intArray[(randi2+i3)%52]!=0){
                    
                    randnumber = (randi2+i3)%52;
                    
                    break;
                    
                }
                
            }
            
            resultArray.push(intArray[randnumber]);
            
            delete intArray[randnumber];
            
        }
        
        return resultArray;
        
    }

    function Poker(uint privatekey, uint blocknumber) public constant returns (uint[]){
        
        uint[] resultArray;
        
        uint8[52] memory intArray= [52,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51];

    for (uint i2=0;i2<52;i2++){
        
            uint randi2 = randomint(privatekey+i2, 52,blocknumber);
            
            uint randnumber;
            
            for(uint i3=0;i3<52;i3++){
                
                if(intArray[(randi2+i3)%52]!=0){
                    
                    randnumber = (randi2+i3)%52;
                    
                    break;
                    
                }
                
            }
            
            resultArray.push(intArray[randnumber]);
            
            delete intArray[randnumber];
            
        }
        
        return resultArray;
        
    }
    
    function Roulette(uint privatekey, uint blocknumber) public constant returns (uint){
        
        return randomint(privatekey+block.timestamp, 38, blocknumber);
        
    }
    /*
    function Dicecup(uint privatekey, uint blocknumber)public constant returns (uint,uint,uint,uint,uint,uint){
        
        return (
            
            randomint(privatekey+block.timestamp+1, 6, blocknumber)+1,
            
            randomint(privatekey+block.timestamp+2, 6, blocknumber)+1,
            
            randomint(privatekey+block.timestamp+3, 6, blocknumber)+1,
            
            randomint(privatekey+block.timestamp+4, 6, blocknumber)+1,
            
            randomint(privatekey+block.timestamp+5, 6, blocknumber)+1,
            
            randomint(privatekey+block.timestamp+6, 6, blocknumber)+1
            
            );
            
    }
    */
    function randomint(uint rand, uint amount, uint blocknumber) internal constant returns (uint){
        
        return uint(keccak256(abi.encodePacked(rand+uint(blockhash(blocknumber)))))%amount;
        
    }
    
}

        '''
        return contract_source_code

