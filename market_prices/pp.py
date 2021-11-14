import pandas as pd
from os import getcwd, listdir
from os.path import join

cwd = getcwd()

all_files = listdir(cwd)
csv_files = [f for f in all_files if f[-4:] == '.csv']
prices = pd.DataFrame()
for f in csv_files:
    df = pd.read_csv(f)
    df.index = pd.to_datetime(df['time'])
    df.index.name = 'Date'
    df['Difference'] = df['close']-df['open']
    df['Pair'] = [f[:6],]*len(df)
    df.drop(['Unnamed: 0', 'time', 'high', 'low', 'tick_volume', 'spread', 'real_volume'], axis=1, inplace =True)
    prices = pd.concat([prices, df], axis=0)
prices.to_csv('prices.csv')