import hashlib as hasher
import datetime as time


class Block:
    def __init__(self,index,timeStamp,data,previousHash):
        self.index = index
        self.timeStamp = timeStamp
        self.data = data
        self.previousHash = previousHash
        self.hash = self.hashBlock()
    

    def hashBlock(self):
        sha = hasher.sha256()
        hashString =(str(self.index)
                   +str(self.timeStamp)
                   +str(self.previousHash)
                   +str(self.data))
        sha.update(hashString.encode('utf-8'))  # Encode the string to bytes
        return sha.hexdigest()
    
def genesis():


        return Block(0,time.datetime.now(),'GenesisBlock','0')
    

    
def next_block(last_block):
         this_index = last_block.index + 1
         this_timestamp = time.datetime.now()
         this_data = "Hey! I'm block " + str(this_index)
         this_hash = last_block.hash
         return Block(this_index, this_timestamp, this_data, this_hash)
    

    # Create the blockchain and add the genesis block
blockchain = [genesis()]
previous_block = blockchain[0]

# How many blocks should we add to the chain
# after the genesis block
num_of_blocks_to_add = 20

# Add blocks to the chain
         
for i in range(0, num_of_blocks_to_add):
         block_to_add = next_block(previous_block)
         blockchain.append(block_to_add)
         previous_block = block_to_add
  # Tell everyone about it!
         print("Block #{} has been added to the blockchain!".format(block_to_add.index))
         print( "Hash: {}\n".format(block_to_add.hash))

 