import matplotlib.pyplot as plot

import pandas as pd


plot.style.use('bmh')
df = pd.read_csv(
    'D:\Programming\Cse 498R\bar chart and min max functions\highRange_Ram.csv')

print(df.shape[0])


y = df['counts']
x = df['shop name']



plot.ylabel('Counts', fontsize=14)
plot.xlabel('Shop Name', fontsize=14)


plot.bar(x, y)


plot.show()
