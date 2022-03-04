# import blockchain library
from blockchain import blockexplorer

# get a particular block
block = blockexplorer.get_block('000000000000000000076f9cb91eebf4d7ac5826626b1bad75ebb8ac6cc99f5c')
print("Block Fee: \n" , block.fee)
print("Block size: \n" , block.size)
print("Block transactions: \n" , block.transactions)
# get the latest block
block = blockexplorer.get_latest_block()

