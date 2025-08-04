import tkinter as tk
from resources import *
root = tk.Tk()
root.title("Name of our Game")
def gather_berries:
    changeamount(berries,1)
berries_button = tk.Button(root, text="Gather Berries", command=gather_berries)
beries_button.place(X=-50,y=100)