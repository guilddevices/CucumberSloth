import tkinter as tk
from resources import *
root = tk.Tk()
root.title("Name of our Game")
#Berries
def berry_gather():
    changeamount("berries",1)
    berries_counter.config(text=f"Berries: {getamount("berries")}")
berries_button = tk.Button(root, text="Gather Berries", command=berry_gather)
berries_button.place(x=0,y=100)
berries_counter = tk.Label(root, text = "Berries: 0")
berries_counter.place(x=100,y=100)
root.mainloop()