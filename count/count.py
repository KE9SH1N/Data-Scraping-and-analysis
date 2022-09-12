import pandas as pd
import threading
import os

def highRangedMouse_Count():

    df = pd.read_csv('highRange_mouse.csv')


    counts = pd.value_counts(df['Shop_Name'])


    print(counts)

    filename = "./countfile/highRange_mouse_Count.csv"

    f = open(filename, 'w', encoding='utf-8-sig')

    #headers = "Shop_Name,Counts\n"
    #f.write(headers)
    counts.to_csv("./countfile/highRange_mouse_Count.csv", header=None)

    newread = pd.read_csv("./countfile/highRange_mouse_Count.csv")

    #print(newread)

    finalread = pd.read_csv("./countfile/highRange_mouse_Count.csv",
                            names=['shop name', 'counts'])

    #print(finalread)

    finalread.to_csv("./countfile/highRange_mouse_Count.csv")


threading.Thread(target=highRangedMouse_Count).start()


def midRangedMouse_Count():

    df = pd.read_csv('mediumRange_mouse.csv')

    counts = pd.value_counts(df['Shop_Name'])

    print(counts)

    filename = "./countfile/mediumRange_mouse_Count.csv"

    f = open(filename, 'w', encoding='utf-8-sig')

    #headers = "Shop_Name,Counts\n"
    #f.write(headers)
    counts.to_csv("./countfile/mediumRange_mouse_Count.csv", header=None)

    newread = pd.read_csv("./countfile/mediumRange_mouse_Count.csv")

    #print(newread)

    finalread = pd.read_csv("./countfile/mediumRange_mouse_Count.csv",
                            names=['shop name', 'counts'])

    #print(finalread)

    finalread.to_csv("./countfile/mediumRange_mouse_Count.csv")


threading.Thread(target=midRangedMouse_Count).start()


def lowRangedMouse_Count():

    df = pd.read_csv('lowRange_mouse.csv')

    counts = pd.value_counts(df['Shop_Name'])

    print(counts)

    filename = "./countfile/lowRange_mouse_Count.csv"

    f = open(filename, 'w', encoding='utf-8-sig')

    #headers = "Shop_Name,Counts\n"
    #f.write(headers)
    counts.to_csv("./countfile/lowRange_mouse_Count.csv", header=None)

    newread = pd.read_csv("./countfile/lowRange_mouse_Count.csv")

    #print(newread)

    finalread = pd.read_csv("./countfile/lowRange_mouse_Count.csv",
                            names=['shop name', 'counts'])

    #print(finalread)

    finalread.to_csv("./countfile/lowRange_mouse_Count.csv")


threading.Thread(target=lowRangedMouse_Count).start()





