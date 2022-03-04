'''
Title - Bitcoin Transaction History
This program demonstrates listing history of a bitcoin address.
'''
# import bitcoin
from bitcoin import *
#View address transaction history
a_valid_bitcoin_address = '16RPTdEKvPdmvuNSsq9rhjD5ArHK4ZLjYA'

history_ofa = history(a_valid_bitcoin_address)

print(history_ofa)