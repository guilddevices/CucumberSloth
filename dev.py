from resourcemanager import *

def devkey():
    key = input("What is the key? ")
    if key != "~":
        return
    else:
        for x in resourcedictionary:
            changeamount(x,10000)
        update()