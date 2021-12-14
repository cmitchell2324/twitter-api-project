import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Cooper/tickerdata.csv')

values = data['Ticker'].value_counts()

xticks = ['Tesla', 'Honda', 'Ferrari', 'VW']

fig, axe = plt.subplots(figsize=(8,8))

values.plot(kind = 'bar', ax=axe)

axe.yaxis.grid()
axe.set_xticklabels(xticks)
axe.set_ylabel("# of Tweets")
axe.set_title("Frequency of Tweets From 12/11 and 12/12 Discussing Car Stocks")
plt.show()