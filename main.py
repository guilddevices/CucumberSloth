import time
import sys
from resources import *
import tkinter as tk
root = tk.Tk()
root.title("Name of our Game")
#Berries
def berry_gather():
    changeamount("berries",1)
    berries_counter.config(text=f"Berries: {getamount("berries")}")
berries_button = tk.Button(root, text="Gather Berries", command=berry_gather)
berries_button.place(x=0,y=100)
berries_counter = tk.Label(root, text = "Berries: 0")
berries_counter.place(x=500,y=100)
#Dialogue_Section
dialogue = tk.Label(root,text=("""You are in Middle of Nowhere.
You can get berries to eat, and you need berries"""))
dialogue.place(x=1000,y=100)
root.mainloop()
global waitnumber
waitnumber = 5
whattodo = input("""You are in Middle of Nowhere.
You have 1 gatherer.
Your gatherer can gather berries for food.
Would you like your gatherer to gather berries?
""")
if whattodo.lower() == "yes":
    for x in range(waitnumber):
        print(f"Waiting: {waitnumber}", end="\r", flush=True)
        time.sleep(1)
        waitnumber -= 1
    changeamount("berries", 2)
    print(f"Berries: {getamount("berries")}")
whattodo = input("""You need to pay your gatherer in 5 berries """)
