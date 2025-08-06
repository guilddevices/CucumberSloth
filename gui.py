from ourgameresources import *
from variables import *
import tkinter as tk
from dialogue import *
import random
#Dialogue
dialoguelist = []
global berries_button, berries_counter, brainstorm_button, science_counter, dialogue_label

global root
root = tk.Tk() 
root.title("Name of our Game")


#define helper functions


def berry_gather():
    number = random.randint(4,6)
    disable(berries_button)
    berries_button.after(number*1000-1, lambda: changeamount("berries", 1))
    berries_counter.after(number*1000, lambda: update())
    berries_button.after(number*1000+1, lambda: berries_button.config(state="normal"))

def brainstorm():
    disable(brainstorm_button)
    brainstorm_button.after(29999, lambda: changeamount("science", 1))
    science_counter.after(30000, lambda: update())
    brainstorm_button.after(30001, lambda: brainstorm_button.config(state="normal"))

#Initialize Widgets
berries_counter = tk.Label(root, text = "Berries: 0")
berries_button = tk.Button(root, text="Gather Berries", command=berry_gather)
brainstorm_button = tk.Button(root, text="Brainstorm", command=brainstorm)
science_counter = tk.Label(root, text = "Science: 0")
dialogue_label = tk.Label(root, text="", justify="left", anchor="ne", bg="Black", fg="White", wraplength=400, width=50, height=10)

def forage():
    changeamount("berries",1)
    if random.random() < 0.1:
        vegetable = True
        changeamount("vegetables",1)
    if random.random() < 0.02:
        fruit = True
        changeamount("fruits",1)
    if fruit and vegetable:
        dialogue_pop_up(dialogue["forage"]["vegetable_fruit"])
    elif vegetable:
        dialogue_pop_up(dialogue["forage"]["vegetable"])
    elif fruit:
        dialogue_pop_up(dialogue["forage"]["fruit"])
    else:
        dialogue_pop_up(dialogue["forage"][random.randint(1,2)])

def initialize():
    #Berries
    berries_button.place(x=0,y=100)
    berries_counter.place(x=500,y=100)
        
    #Brainstorm
    brainstorm_button.place(x=0,y=500)
    science_counter.place(x=100,y=100)

    #dialogbox
    
    dialogue_label.place(relx=.8, rely=0, anchor='ne')

    #root.after(500,devkey)
    root.mainloop()

"""def devkey():
    key = input("What is the key? ")
    if key != "~":
        return
    else:
        for x in resourcedictionary:
            changeamount(x,10000)
        update()"""

def disable(press_button):
    press_button.config(state="disabled")

def update():
    berries_counter.config(text=f"Berries: {getamount("berries")}")
    science_counter.config(text=f"Science: {getamount("science")}")

    
def dialogue_pop_up(new_dialogue):
    dialoguelist.insert(0,new_dialogue)
    #if len(dialoguelist) >= 10:
     #   dialoguelist.pop()
    dialogue_label.config(text=dialoguelist)
    