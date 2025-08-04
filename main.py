import time
import sys
from resources import *
from dialogue import *
import tkinter as tk
from tech import *
root = tk.Tk()
root.title("Name of our Game")
#Berries

def berry_gather():
    berries_button.config(state="disabled")
    berries_counter.config(text=f"Berries: {getamount("berries")}")
    berries_button.after(5000, changeamount("berries",1))
    berries_button.config(state="normal")
berries_button = tk.Button(root, text="Gather Berries", command=berry_gather)
berries_button.place(x=0,y=100)
berries_counter = tk.Label(root, text = "Berries: 0")
berries_counter.place(x=500,y=100)
def brainstorm():
    brainstorm_button.config(state="disabled")
    brainstorm_button.config(text=f"Science: {getamount("science")}")
    brainstorm_button.after(30000, lambda: brainstorm_button.config(state="normal"), changeamount("Science",1))
brainstorm_button = tk.Button(root, text="Brainstorm", command=brainstorm)
brainstorm_button.place(x=0,y=500)
science_counter = tk.Label(root, text = "Science: 0")
science_counter.place(x=100,y=100)

adddialogue("""You are in Middle of Nowhere.
Right now, you can only get berries for food, and you need to eat to survive.""")

root.mainloop()