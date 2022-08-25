import pandas as pd
import threading


def mouseRange():
    df = pd.read_csv('productbyMouse.csv')


    #FINDING MAX AND MIN
    max = df['G-Price'].max()
    min = df['G-Price'].min()

    print(max)
    print(min)

    mid = (max-min)/2
    print(mid)


    low = max/3
    medium = 2*low
    high = max

    print(low)
    print(medium)
    print(high)


    def midRange():
        midRange = df[df['G-Price'].between(min, mid)]

        #print(midrange)

        filename = "midRange_mouse.csv"

        f = open(filename, 'w', encoding='utf-8-sig')

        midRange.to_csv("midRange_mouse.csv")

        #df = pd.read_csv('testmouse.csv')


    threading.Thread(target=midRange).start()


    def maxRange():
        maxRange = df[df['G-Price'].between(mid, max)]

        #print(midrange)

        filename = "maxRange_mouse.csv"

        f = open(filename, 'w', encoding='utf-8-sig')

        maxRange.to_csv("maxRange_mouse.csv")

        #df = pd.read_csv('testmouse.csv')


    threading.Thread(target=maxRange).start()


    def lowRange():
        lowRange = df[df['G-Price'].between(min, low)]

        #print(midrange)

        filename = "lowRange_mouse.csv"

        f = open(filename, 'w', encoding='utf-8-sig')

        lowRange.to_csv("lowRange_mouse.csv")

        #df = pd.read_csv('testmouse.csv')


    threading.Thread(target=lowRange).start()


    def mediumRange():
        mediumRange = df[df['G-Price'].between(low, medium)]

        #print(midrange)

        filename = "mediumRange_mouse.csv"

        f = open(filename, 'w', encoding='utf-8-sig')

        mediumRange.to_csv("mediumRange_mouse.csv")

        #df = pd.read_csv('testmouse.csv')


    threading.Thread(target=mediumRange).start()


    def highRange():
        highRange = df[df['G-Price'].between(medium, high)]

        #print(midrange)

        filename = "highRange_mouse.csv"

        f = open(filename, 'w', encoding='utf-8-sig')

        highRange.to_csv("highRange_mouse.csv")

        #df = pd.read_csv('testmouse.csv')


    threading.Thread(target=highRange).start()
    

threading.Thread(target=mouseRange).start()


def keyboardRange():
    df = pd.read_csv('productbyKeyboard.csv')

    #FINDING MAX AND MIN
    max = df['G-Price'].max()
    min = df['G-Price'].min()

    print(max)
    print(min)

    mid = (max-min)/2
    print(mid)

    low = max/3
    medium = 2*low
    high = max

    print(low)
    print(medium)
    print(high)

    def midRange():
        midRange = df[df['G-Price'].between(min, mid)]

        #print(midrange)

        filename = "midRange_keyboard.csv"

        f = open(filename, 'w', encoding='utf-8-sig')

        midRange.to_csv("midRange_keyboard.csv")

        #df = pd.read_csv('testmouse.csv')

    threading.Thread(target=midRange).start()

    def maxRange():
        maxRange = df[df['G-Price'].between(mid, max)]

        #print(midrange)

        filename = "maxRange_keyboard.csv"

        f = open(filename, 'w', encoding='utf-8-sig')

        maxRange.to_csv("maxRange_keyboard.csv")

        #df = pd.read_csv('testmouse.csv')

    threading.Thread(target=maxRange).start()

    def lowRange():
        lowRange = df[df['G-Price'].between(min, low)]

        #print(midrange)

        filename = "lowRange_keyboard.csv"

        f = open(filename, 'w', encoding='utf-8-sig')

        lowRange.to_csv("lowRange_keyboard.csv")

        #df = pd.read_csv('testmouse.csv')

    threading.Thread(target=lowRange).start()

    def mediumRange():
        mediumRange = df[df['G-Price'].between(low, medium)]

        #print(midrange)

        filename = "mediumRange_keyboard.csv"

        f = open(filename, 'w', encoding='utf-8-sig')

        mediumRange.to_csv("mediumRange_keyboard.csv")

        #df = pd.read_csv('testmouse.csv')

    threading.Thread(target=mediumRange).start()

    def highRange():
        highRange = df[df['G-Price'].between(medium, high)]

        #print(midrange)

        filename = "highRange_keyboard.csv"

        f = open(filename, 'w', encoding='utf-8-sig')

        highRange.to_csv("highRange_keyboard.csv")

        #df = pd.read_csv('testmouse.csv')

    threading.Thread(target=highRange).start()


threading.Thread(target=keyboardRange).start()


def monitorRange():
    df = pd.read_csv('productbyMonitor.csv')

    #FINDING MAX AND MIN
    max = df['G-Price'].max()
    min = df['G-Price'].min()

    print(max)
    print(min)

    mid = (max-min)/2
    print(mid)

    low = max/3
    medium = 2*low
    high = max

    print(low)
    print(medium)
    print(high)

    def midRange():
        midRange = df[df['G-Price'].between(min, mid)]

        #print(midrange)

        filename = "midRange_monitor.csv"

        f = open(filename, 'w', encoding='utf-8-sig')

        midRange.to_csv("midRange_monitor.csv")

        #df = pd.read_csv('testmouse.csv')

    threading.Thread(target=midRange).start()

    def maxRange():
        maxRange = df[df['G-Price'].between(mid, max)]

        #print(midrange)

        filename = "maxRange_monitor.csv"

        f = open(filename, 'w', encoding='utf-8-sig')

        maxRange.to_csv("maxRange_monitor.csv")

        #df = pd.read_csv('testmouse.csv')

    threading.Thread(target=maxRange).start()

    def lowRange():
        lowRange = df[df['G-Price'].between(min, low)]

        #print(midrange)

        filename = "lowRange_monitor.csv"

        f = open(filename, 'w', encoding='utf-8-sig')

        lowRange.to_csv("lowRange_monitor.csv")

        #df = pd.read_csv('testmouse.csv')

    threading.Thread(target=lowRange).start()

    def mediumRange():
        mediumRange = df[df['G-Price'].between(low, medium)]

        #print(midrange)

        filename = "mediumRange_monitor.csv"

        f = open(filename, 'w', encoding='utf-8-sig')

        mediumRange.to_csv("mediumRange_monitor.csv")

        #df = pd.read_csv('testmouse.csv')

    threading.Thread(target=mediumRange).start()

    def highRange():
        highRange = df[df['G-Price'].between(medium, high)]

        #print(midrange)

        filename = "highRange_monitor.csv"

        f = open(filename, 'w', encoding='utf-8-sig')

        highRange.to_csv("highRange_monitor.csv")

        #df = pd.read_csv('testmouse.csv')

    threading.Thread(target=highRange).start()


threading.Thread(target=monitorRange).start()


def ramRange():
    df = pd.read_csv('productbyMonitor.csv')

    #FINDING MAX AND MIN
    max = df['G-Price'].max()
    min = df['G-Price'].min()

    print(max)
    print(min)

    mid = (max-min)/2
    print(mid)

    low = max/3
    medium = 2*low
    high = max

    print(low)
    print(medium)
    print(high)

    def midRange():
        midRange = df[df['G-Price'].between(min, mid)]

        #print(midrange)

        filename = "midRange_Ram.csv"

        f = open(filename, 'w', encoding='utf-8-sig')

        midRange.to_csv("midRange_Ram.csv")

        #df = pd.read_csv('testmouse.csv')

    threading.Thread(target=midRange).start()

    def maxRange():
        maxRange = df[df['G-Price'].between(mid, max)]

        #print(midrange)

        filename = "maxRange_Ram.csv"

        f = open(filename, 'w', encoding='utf-8-sig')

        maxRange.to_csv("maxRange_Ram.csv")

        #df = pd.read_csv('testmouse.csv')

    threading.Thread(target=maxRange).start()

    def lowRange():
        lowRange = df[df['G-Price'].between(min, low)]

        #print(midrange)

        filename = "lowRange_Ram.csv"

        f = open(filename, 'w', encoding='utf-8-sig')

        lowRange.to_csv("lowRange_Ram.csv")

        #df = pd.read_csv('testmouse.csv')

    threading.Thread(target=lowRange).start()

    def mediumRange():
        mediumRange = df[df['G-Price'].between(low, medium)]

        #print(midrange)

        filename = "mediumRange_Ram.csv"

        f = open(filename, 'w', encoding='utf-8-sig')

        mediumRange.to_csv("mediumRange_Ram.csv")

        #df = pd.read_csv('testmouse.csv')

    threading.Thread(target=mediumRange).start()

    def highRange():
        highRange = df[df['G-Price'].between(medium, high)]

        #print(midrange)

        filename = "highRange_Ram.csv"

        f = open(filename, 'w', encoding='utf-8-sig')

        highRange.to_csv("highRange_Ram.csv")

        #df = pd.read_csv('testmouse.csv')

    threading.Thread(target=highRange).start()


threading.Thread(target=ramRange).start()


def gpuRange():
    df = pd.read_csv('productbyMonitor.csv')

    #FINDING MAX AND MIN
    max = df['G-Price'].max()
    min = df['G-Price'].min()

    print(max)
    print(min)

    mid = (max-min)/2
    print(mid)

    low = max/3
    medium = 2*low
    high = max

    print(low)
    print(medium)
    print(high)

    def midRange():
        midRange = df[df['G-Price'].between(min, mid)]

        #print(midrange)

        filename = "midRange_Gpu.csv"

        f = open(filename, 'w', encoding='utf-8-sig')

        midRange.to_csv("midRange_Gpu.csv")

        #df = pd.read_csv('testmouse.csv')

    threading.Thread(target=midRange).start()

    def maxRange():
        maxRange = df[df['G-Price'].between(mid, max)]

        #print(midrange)

        filename = "maxRange_Gpu.csv"

        f = open(filename, 'w', encoding='utf-8-sig')

        maxRange.to_csv("maxRange_Gpu.csv")

        #df = pd.read_csv('testmouse.csv')

    threading.Thread(target=maxRange).start()

    def lowRange():
        lowRange = df[df['G-Price'].between(min, low)]

        #print(midrange)

        filename = "lowRange_Gpu.csv"

        f = open(filename, 'w', encoding='utf-8-sig')

        lowRange.to_csv("lowRange_Gpu.csv")

        #df = pd.read_csv('testmouse.csv')

    threading.Thread(target=lowRange).start()

    def mediumRange():
        mediumRange = df[df['G-Price'].between(low, medium)]

        #print(midrange)

        filename = "mediumRange_Gpu.csv"

        f = open(filename, 'w', encoding='utf-8-sig')

        mediumRange.to_csv("mediumRange_Gpu.csv")

        #df = pd.read_csv('testmouse.csv')

    threading.Thread(target=mediumRange).start()

    def highRange():
        highRange = df[df['G-Price'].between(medium, high)]

        #print(midrange)

        filename = "highRange_Gpu.csv"

        f = open(filename, 'w', encoding='utf-8-sig')

        highRange.to_csv("highRange_Gpu.csv")

        #df = pd.read_csv('testmouse.csv')

    threading.Thread(target=highRange).start()


threading.Thread(target=gpuRange).start()
