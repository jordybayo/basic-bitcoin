from bitcoin import *


"""
Title - Hello Bitcoin
This program demonstrates the creation of
- private key,
- public key
- an
"""

#Generate Private Key
my_private_key = random_key()
print(my_private_key)

#Generate Public Key
my_public_key = privtopub(my_private_key)
print(my_public_key)


# Create a bitcoin address
my_bitcoin_address = pubtoaddr(my_public_key)

print(my_bitcoin_address)

