import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm


days_projection = 30 # predict next month of data 
iterations = 25

#data of mongodb  https://finance.yahoo.com/quote/MDB/history?p=MDB

df = pd.read_csv("MDB.csv",index_col=0,usecols=['Date', 'Adj Close'])
df.plot(figsize=(10, 6))
plt.title(" adj close for Mongo DB values are ")
plt.show()

log_data = np.log(1 + df.pct_change())
log_data.plot(figsize = (10, 6))
plt.show(" log values for the MongoDB  for simplicity are ")
plt.show()


u = log_data.mean()
var = log_data.var()
drift = u - (0.5 * var) #what if we got 0.5 decrease drift ?
stdev = log_data.std() 

"""
    simulation of monto carlo simulations 
    assume that we may go with exp values either + or -ve 

"""

daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(days_projection, iterations))) 

#exponentional trends

start_of_projection = df.iloc[-1] #starting point of projection from this day , we can fix this , think of this "as-of now"
mc_values= np.zeros_like(daily_returns)
mc_values[0] = start_of_projection
print(start_of_projection)

for t in range(1, days_projection):
    mc_values[t] = mc_values[t - 1] * daily_returns[t]

plt.figure(figsize=(10,6))
plt.title("Monto Carlo Simualation for next 30 days starting from today (2020-03-20)")
plt.plot(mc_values)
plt.show()