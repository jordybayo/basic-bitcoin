# import blockchain library
from blockchain import statistics
# get the stats object
stats = statistics.get()
# get and print Bitcoin trade volume
print("Bitcoin Trade Volume: \n", stats.trade_volume_btc)

# get and print Bitcoin mined
print("Bitcoin mined: \n" , stats.btc_mined)


# get and print Bitcoin market price in usd
print("Bitcoin market price: \n" , stats.market_price_usd)