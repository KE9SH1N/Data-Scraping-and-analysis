import pandas as pd
import matplotlib.pyplot as plot
import numpy as np

df = pd.read_csv('G:\CSE498R\Final\count\lowRange_Ram.csv')

new_df= df[["Shop_Name", "Availability"]]


condition = [
    (new_df['Availability'] == 'In Stock') & (
        new_df['Shop_Name'] == 'TECHLAND'),
    (new_df['Availability'] == 'In Stock') & (
        new_df['Shop_Name'] == 'RYANS'),
    (new_df['Availability'] == 'In Stock') & (
        new_df['Shop_Name'] == 'STARTECH'),
    (new_df['Availability'] == 'In Stock') & (
        new_df['Shop_Name'] == 'COMPUTER VILLAGE'),
    (new_df['Availability'] == 'In Stock') & (
        new_df['Shop_Name'] == 'Skyland'),
]

values = ['Techland','Ryans','Startech','Computer Village', 'Skyland']

new_df['Stock Group'] = np.select(condition, values)

#print(new_df.tail(100))


counts = pd.value_counts(new_df['Stock Group'])

print(counts)

counts.to_csv('stockCount.csv',  header=None)
finalcounts = pd.read_csv("stockCount.csv",names=['shop name', 'Stock Counts'])

finalcounts.to_csv('stockCount.csv')
finalcounts.drop(3, axis=0, inplace=True)
finalcounts.to_csv('stockCount.csv')

y = finalcounts['Stock Counts']


x = finalcounts['shop name']

plot.ylabel('Stock Counts', fontsize=14)

plot.xlabel('Shop Name', fontsize=14)

plot.bar(x, y)

plot.text(0.0, 320.0, 'Barchart of Shop vs Stock count from low price ram data')

plot.show()



