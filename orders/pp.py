import pandas as pd
from os import getcwd, listdir
from os.path import join
import matplotlib.pyplot as plt

cwd = getcwd()

all_files = listdir(cwd)
csv_files = [f for f in all_files if f[-4:] == '.csv']
orders = pd.DataFrame()
for f in csv_files:
    df = pd.read_csv(f)
    df.drop(['Unnamed: 0', 'Ticket', 'Time Frame','Weight', 'Volume', 'SL', 'TP', 'Margin requirment'], axis=1, inplace =True)
    df.rename(columns = {'Porfit':'Profit'}, inplace =True)
    orders = pd.concat([orders, df], axis=0)

orders.index = range(len(orders))
orders['Wealth Index'] = orders['Profit'].cumsum() + 1_000
orders['previous_peaks'] = orders['Wealth Index'].cummax()
orders['drawdowns'] = (orders['Wealth Index'] - orders['previous_peaks'])/orders['previous_peaks']
orders.to_csv('orders.csv')