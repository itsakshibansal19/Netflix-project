#---------Netflix Stock Analysis

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from datetime import datetime


df= pd.read_csv('D:\\Netflix.csv')
# print(df.head())
# print(df.tail())

df['Date']=pd.to_datetime(df['Date'])
df=df.set_index('Date')
# print(df.head())

# sns.set(rc={'figure.figsize' :(10,5)})
# sns.lineplot(x=df.index, y=df['Volume'],label='Volume')
# plt.title("Netflix Stock Volume Over Time")
# plt.show()

# df.plot(y=['High','Close','Open'],title='Netflix Stock Price Over Time',ylabel='Price')
# plt.show()

# fig,(ax1,ax2,ax3) = plt.subplots(3, figsize=(5,15))
# df.groupby(df.index.day).mean().plot(y ='Volume' ,ax=ax1, xlabel='Day')
# df.groupby(df.index.month).mean().plot(y ='Volume', ax=ax2, xlabel='Month')
# df.groupby(df.index.year).mean().plot(y ='Volume', ax=ax3, xlabel='Year')
# plt.show()

#--------Dates with highest STOCK PRICE

# a = df.sort_values(by = 'High',ascending = False).head(5)
# print(a['High'])

#--------Dates with lowest STOCK PRICE

# b = df.sort_values(by = 'Low',ascending =True).head(5)
# print(b['Low'])

# fig,axes = plt.subplots(nrows=1,ncols=2, sharex=True, figsize =(12,5))
# fig.suptitle('High & Low values stock per period of time',fontsize=18)
# sns.lineplot(ax=axes[0], y=df['High'], x=df.index, color='green')
# sns.lineplot(ax=axes[1],y=df['Low'], x=df.index, color='red')
# plt.show()