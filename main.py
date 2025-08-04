import time
import sys
from resources import *
import tkinter as tk
from tech import research
root = tk.Tk()
root.title("Name of our Game")
#Berries
def berry_gather():
    berries_button.config(state="disabled")
    berries_counter.config(text=f"Berries: {getamount("berries")}")
    berries_button.after(5000, lambda: berries_button.config(state="normal"))
    changeamount("berries",1)
berries_button = tk.Button(root, text="Gather Berries", command=berry_gather)
berries_button.place(x=0,y=100)
berries_counter = tk.Label(root, text = "Berries: 0")
berries_counter.place(x=500,y=100)
def brainstorm():
    brainstorm.config(state="disabled")
    brainstorn.config(text=f"Science: {getamount("berries")}")
    brainstorm.after(30000, lambda: brainstorm.config(state="normal"))
    changeamount("brainstorm",1)
berries_button = tk.Button(root, text="Gather Berries", command=berry_gather)
berries_button.place(x=0,y=100)
berries_counter = tk.Label(root, text = "Berries: 0")
berries_counter.place(x=500,y=100)
#Dialogue_Section
dialogue = tk.Label(root,text=("""You are in Middle of Nowhere.
Right now, you can only get berries for food, and you need to eat to survive."""))
dialogue.place(x=1000,y=100)
root.mainloop()