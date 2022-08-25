import io
from operator import index
from textwrap import indent
import pandas as pd
from io import StringIO

df = pd.read_csv('allData.csv')

#FINDING MAX AND MIN
max = df['G-Price'].max()
min = df['G-Price'].min()

print(max)
print(min)

mid = (max-min)/2


print(mid)

#filtered by only price to avoid unnecessary  row

filtered = df[df['G-Price'].between(min, max)]

print(filtered)


filename = "filteredAllData.csv"

f = open(filename, 'w', encoding='utf-8-sig')

filtered.to_csv("filteredAllData.csv")

#filtered.reset_index(drop=True)
