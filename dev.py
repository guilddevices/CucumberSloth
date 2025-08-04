from resources import *

def devkey():
    key = input("What is the key")
    if key != "~":
        break
    else:
        for x in resourcedictionary:
            changeamount(x,10000)