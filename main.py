import time
import sys 
#yesfrom resources import *
global waitnumber
waitnumber = 5
whattodo = input("""You are in Middle of Nowhere.
You have 1 gatherer.
Your gatherer can gather food.
Would you like your gatherer to gather berries?
""")
if whattodo.lower() == "yes":
    for i in range(waitnumber, 0, -1):
        time.sleep(1)
        print(f"Wating: {waitnumber}", end="/r", flush=True)
#print(f"Berries: {getamount(berries)}")