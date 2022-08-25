import pandas as pd

df = pd.read_csv('mousedata.csv')


#FINDING MAX AND MIN
max = df['G-Price'].max()
min = df['G-Price'].min()

print(max)
print(min)

mid = (max-min)/2


print(mid)


midrange = df[df['G-Price'].between(min, mid)]

#print(midrange)


filename = "testmouse.csv"

f = open(filename, 'w', encoding='utf-8-sig')

midrange.to_csv("testmouse.csv")

df = pd.read_csv('testmouse.csv')

counts = pd.value_counts(df['Availability'])


#print(counts)


filename = "testcount.csv"

f = open(filename, 'w', encoding='utf-8-sig')

#headers = "Shop_Name,Counts\n"
#f.write(headers)
counts.to_csv("testcount.csv", header=None)

newread = pd.read_csv("testcount.csv")

#print(newread)

finalread = pd.read_csv("testcount.csv" , names=['shop name', 'counts'])

#print(finalread)

finalread.to_csv("testcount.csv")





hdf = pd.read_csv('mousedata.csv')

highrange = hdf[hdf['G-Price'].between(mid, max)]

print(highrange)

filename = "highrangemouse.csv"

f = open(filename, 'w', encoding='utf-8-sig')

highrange.to_csv("highrangemouse.csv")

hdf = pd.read_csv('highrangemouse.csv')

highcounts = pd.value_counts(hdf['Availability'])

print(highcounts)


highcounts.to_csv("highrangemouse.csv", header=None)

highread = pd.read_csv("highrangemouse.csv")

print(highread)

finalhighread = pd.read_csv("highrangemouse.csv", names=['shop name', 'counts'])

print(finalhighread)

finalhighread.to_csv("highrangemouse.csv")












