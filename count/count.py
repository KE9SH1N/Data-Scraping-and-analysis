import pandas as pd
import threading
import os

def maxRangedGpu_Count():

    df = pd.read_csv('midRange_Gpu.csv')


    counts = pd.value_counts(df['Shop_Name'])


    print(counts)

    filename = "./countfile/maxRangedGpu_Count.csv"

    f = open(filename, 'w', encoding='utf-8-sig')

    #headers = "Shop_Name,Counts\n"
    #f.write(headers)
    counts.to_csv("./countfile/maxRangedGpu_Count.csv", header=None)

    newread = pd.read_csv("./countfile/maxRangedGpu_Count.csv")

    #print(newread)

    finalread = pd.read_csv("./countfile/maxRangedGpu_Count.csv",
                            names=['shop name', 'counts'])

    #print(finalread)

    finalread.to_csv("./countfile/maxRangedGpu_Count.csv")


threading.Thread(target=maxRangedGpu_Count).start()


def maxRangedMouse_Count():

    df = pd.read_csv('lowRange_mouse.csv')

    counts = pd.value_counts(df['Shop_Name'])

    print(counts)

    filename = "./countfile/maxRangedMouse_Count.csv"

    f = open(filename, 'w', encoding='utf-8-sig')

    #headers = "Shop_Name,Counts\n"
    #f.write(headers)
    counts.to_csv("./countfile/maxRangedMouse_Count.csv", header=None)

    newread = pd.read_csv("./countfile/maxRangedMouse_Count.csv")

    #print(newread)

    finalread = pd.read_csv("./countfile/maxRangedMouse_Count.csv",
                            names=['shop name', 'counts'])

    #print(finalread)

    finalread.to_csv("./countfile/maxRangedMouse_Count.csv")


threading.Thread(target=maxRangedMouse_Count).start()


def maxRangedKeyboard_Count():

    df = pd.read_csv('mediumRange_keyboard.csv')

    counts = pd.value_counts(df['Shop_Name'])

    print(counts)

    filename = "./countfile/maxRangedKeyboard_Count.csv"

    f = open(filename, 'w', encoding='utf-8-sig')

    #headers = "Shop_Name,Counts\n"
    #f.write(headers)
    counts.to_csv("./countfile/maxRangedKeyboard_Count.csv", header=None)

    newread = pd.read_csv("./countfile/maxRangedKeyboard_Count.csv")

    #print(newread)

    finalread = pd.read_csv("./countfile/maxRangedKeyboard_Count.csv",
                            names=['shop name', 'counts'])

    #print(finalread)

    finalread.to_csv("./countfile/maxRangedKeyboard_Count.csv")


threading.Thread(target=maxRangedKeyboard_Count).start()


def maxRangedMonitor_Count():

    df = pd.read_csv('maxRange_monitor.csv')

    counts = pd.value_counts(df['Shop_Name'])

    print(counts)

    filename = "./countfile/maxRangedMonitor_Count.csv"

    f = open(filename, 'w', encoding='utf-8-sig')

    #headers = "Shop_Name,Counts\n"
    #f.write(headers)
    counts.to_csv("./countfile/maxRangedMonitor_Count.csv", header=None)

    newread = pd.read_csv("./countfile/maxRangedMonitor_Count.csv")

    #print(newread)

    finalread = pd.read_csv("./countfile/maxRangedMonitor_Count.csv",
                            names=['shop name', 'counts'])

    #print(finalread)

    finalread.to_csv("./countfile/maxRangedMonitor_Count.csv")


threading.Thread(target=maxRangedMonitor_Count).start()


def maxRangedRam_Count():

    df = pd.read_csv('highRange_Ram.csv')

    counts = pd.value_counts(df['Shop_Name'])

    print(counts)

    

    filename = "./countfile/maxRangedRam_Count.csv"

    f = open(filename, 'w', encoding='utf-8-sig')

    #headers = "Shop_Name,Counts\n"
    #f.write(headers)
    counts.to_csv("./countfile/maxRangedRam_Count.csv", header=None)

    newread = pd.read_csv("./countfile/maxRangedRam_Count.csv")

    #print(newread)

    finalread = pd.read_csv("./countfile/maxRangedRam_Count.csv",
                            names=['shop name', 'counts'])

    #print(finalread)

    finalread.to_csv('./countfile/maxRangedRam_Count.csv')


threading.Thread(target=maxRangedRam_Count).start()
