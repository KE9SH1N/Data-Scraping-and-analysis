import io
from operator import index
from textwrap import indent
import threading
import pandas as pd
from io import StringIO

#df = pd.read_csv('filteredAllData.csv')

#read = df.groupby(['Category']).mean()

#print(read)

#newread = df[df['Category'].str.contains("Keyboard")]

#print(newread)

#newread = newread.drop('Unnamed: 0', axis=1)


#filename = "productbyKeyboard.csv"

#f = open(filename, 'w', encoding='utf-8-sig')

#newread.to_csv("productbyCategory.csv" , index_col=[0])

#read2 = pd.read_csv(io.StringIO(newread.to_csv()), index_col=[0])
#newfile = newread.to_csv('productbyKeyboard.csv', index=False)


def productbyKeyboard():
    
    df = pd.read_csv('filteredAllData.csv')


    read = df.groupby(['Category']).mean()

    #print(read)

    newread = df[df['Category'].str.contains("Keyboard")]

    print(newread)

    newread = newread.drop('Unnamed: 0', axis=1)


    filename = "productbyKeyboard.csv"

    f = open(filename, 'w', encoding='utf-8-sig')

    #newread.to_csv("productbyCategory.csv" , index_col=[0])

    read2 = pd.read_csv(io.StringIO(newread.to_csv()), index_col=[0])
    newfile = newread.to_csv('productbyKeyboard.csv', index=False)


def productbyMouse():

    df = pd.read_csv('filteredAllData.csv')

    read = df.groupby(['Category']).mean()

    #print(read)

    newread = df[df['Category'].str.contains("Mouse")]

    print(newread)

    newread = newread.drop('Unnamed: 0', axis=1)

    filename = "productbyMouse.csv"

    f = open(filename, 'w', encoding='utf-8-sig')

    #newread.to_csv("productbyCategory.csv" , index_col=[0])

    read2 = pd.read_csv(io.StringIO(newread.to_csv()), index_col=[0])
    newfile = newread.to_csv('productbyMouse.csv', index=False)


def productbyMonitor():

    df = pd.read_csv('filteredAllData.csv')

    read = df.groupby(['Category']).mean()

    #print(read)

    newread = df[df['Category'].str.contains("Monitor")]

    print(newread)

    newread = newread.drop('Unnamed: 0', axis=1)

    filename = "productbyMonitor.csv"

    f = open(filename, 'w', encoding='utf-8-sig')

    #newread.to_csv("productbyCategory.csv" , index_col=[0])

    read2 = pd.read_csv(io.StringIO(newread.to_csv()), index_col=[0])
    newfile = newread.to_csv('productbyMonitor.csv', index=False)


def productbyRam():

    df = pd.read_csv('filteredAllData.csv')

    read = df.groupby(['Category']).mean()

    #print(read)

    newread = df[df['Category'].str.contains("Ram")]

    print(newread)

    newread = newread.drop('Unnamed: 0', axis=1)

    filename = "productbyRam.csv"

    f = open(filename, 'w', encoding='utf-8-sig')

    #newread.to_csv("productbyCategory.csv" , index_col=[0])

    read2 = pd.read_csv(io.StringIO(newread.to_csv()), index_col=[0])
    newfile = newread.to_csv('productbyRam.csv', index=False)


def productbyGPU():

    df = pd.read_csv('filteredAllData.csv')

    read = df.groupby(['Category']).mean()

    #print(read)

    newread = df[df['Category'].str.contains("GPU")]

    print(newread)

    newread = newread.drop('Unnamed: 0', axis=1)

    filename = "productbyGpu.csv"

    f = open(filename, 'w', encoding='utf-8-sig')

    #newread.to_csv("productbyCategory.csv" , index_col=[0])

    read2 = pd.read_csv(io.StringIO(newread.to_csv()), index_col=[0])
    newfile = newread.to_csv('productbyGpu.csv', index=False)


threading.Thread(target=productbyGPU).start()

threading.Thread(target=productbyRam).start()

threading.Thread(target=productbyMonitor).start()

threading.Thread(target=productbyMouse).start()

threading.Thread(target=productbyKeyboard).start()
