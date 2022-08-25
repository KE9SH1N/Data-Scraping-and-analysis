import matplotlib.pyplot as plot
import threading
import pandas as pd



#def gpuChart():
plot.style.use('bmh')
df = pd.read_csv('maxRangedRam_Count.csv')

#print(df.shape[0])
y = df['counts']


x = df['shop name']

plot.ylabel('Counts', fontsize=14)

plot.xlabel('Shop Name', fontsize=14)

plot.bar(x, y)

plot.text( 0.0, 3.5, 'Barchart of Max price ranged mouse provided in the market and its quantities')
    
plot.show()

#threading.Thread(target=gpuChart).start()




