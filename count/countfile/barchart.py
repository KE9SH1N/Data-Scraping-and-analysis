import matplotlib.pyplot as plot
import threading
import pandas as pd



#def gpuChart():
plot.style.use('bmh')
df = pd.read_csv('mediumRange_mouse_Count.csv')

#print(df.shape[0])
y = df['counts']


x = df['shop name']

plot.ylabel('Stock Counts', fontsize=14)

plot.xlabel('Shop Name', fontsize=14)

plot.bar(x, y)

plot.text(0.0, 60.5, 'Price Range Medium')
    
plot.show()

#threading.Thread(target=gpuChart).start()




