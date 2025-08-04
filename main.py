import time
import sys
from resources import *
import tkinter as tk
from tech import *
from dev import *
root = tk.Tk()
root.title("Name of our Game")

#Dialogue
dialogue1 = ""
dialogue2 = ""
dialogue3 = ""

def dialogue_pop_up(new_dialogue):
    global dialogue1
    global dialogue2
    global dialogue3
    dialogue3 = dialogue2
    dialogue2 = dialogue1
    dialogue1 = new_dialogue
    dialogue1_display = tk.Label(root, text=dialogue1).pack(side=tk.RIGHT, pady=5)
    dialogue2_display = tk.Label(root, text=dialogue2).pack(side=tk.RIGHT, pady=5)
    dialogue3_display = tk.Label(root, text=dialogue3).pack(side=tk.RIGHT, pady=5)

def add_something(item, button, counter):
    changeamount(item, 1)
    button.config(state="normal")
    counter.config(text=f"{item.proper()}: {getamount(item)}")
#Berries
def berry_gather():
    berries_button.config(state="disabled")
    berries_button.after(5000, add_something("berries", berries_button, berries_counter))
    berries_counter.config(text=f"Berries: {getamount("berries")}")
berries_button = tk.Button(root, text="Gather Berries", command=berry_gather)
berries_button.place(x=0,y=100)
berries_counter = tk.Label(root, text = "Berries: 0")
berries_counter.place(x=500,y=100)
#Science
def brainstorm():
    brainstorm_button.config(state="disabled")
    brainstorm_button.after(30000, lambda: brainstorm_button.config(state="normal"))
    changeamount("science",1)
    science_counter.config(text=f"Science: {getamount("science")}")
brainstorm_button = tk.Button(root, text="Brainstorm", command=brainstorm)
brainstorm_button.place(x=0,y=500)
science_counter = tk.Label(root, text = "Science: 0")
science_counter.place(x=100,y=100)

dialogue_pop_up("""You are in Middle of Nowhere.
Right now, you can only get berries for food, and you need to eat to survive.""")


root.mainloop()
devkey()