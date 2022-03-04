
import pandas as pd
import matplotlib.pyplot as plt

pd.options.mode.chained_assignment = None

# %matplotlib inline

price = pd.read_csv('BTC_USD_2020-12-08_2021-12-07-CoinDesk.csv')

print(price.head())


