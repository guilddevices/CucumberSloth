from ourgameresources import *
from variables import *
import tkinter as tk
from user import *
from dialogue import *
import random
import time
#Dialogue
dialoguelist = []
global berries_button, berries_counter, brainstorm_button, science_counter, dialogue_label

global root
root = tk.Tk() 
root.title("Name of our Game")


#define helper functions

def frame():
    eatclock -= 1
    if eatclock == 0:
        if eat():
            dialogue_pop_up("You have eaten food.")
        else:
            brainstorm_button.config(state="disabled")
    update()
    time.sleep(1/60)

def game():
    dialogue_pop_up("You are in Middle of Nowhere.\nRight now, you can get berries for food, and you need to eat to survive.\nEvery 20 seconds, you will lose one berry.")
    while True:
        frame()

def berry_gather():
    number = random.randint(4,6)
    dialogue_pop_up(dialogue["berries"][str(number)])
    disable(berries_button)
    berries_button.after(number*1000-1, lambda: changeamount("berries", 1))
    berries_button.after(number*1000+1, lambda: berries_button.config(state="normal"))

def brainstorm():
    brainstorm_number = random.randint(1,3)
    dialogue_pop_up(dialogue["brainstorm"][str(brainstorm_number)])
    disable(brainstorm_button)
    brainstorm_button.after(29999, lambda: changeamount("science", 1))
    brainstorm_button.after(30001, lambda: brainstorm_button.config(state="normal"))

#Initialize Widgets
berries_counter = tk.Label(root, text = "Berries: 0")
berries_button = tk.Button(root, text="Gather Berries", command=berry_gather)
brainstorm_button = tk.Button(root, text="Brainstorm", command=brainstorm)
science_counter = tk.Label(root, text = "Science: 0")
dialogue_label = tk.Label(root, text="", justify="left", anchor="ne", bg="Black", fg="White", wraplength=400, width=50, height=100)

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
    berries_counter.place(x=200,y=105)
        
    #Brainstorm
    brainstorm_button.place(x=0,y=130)
    science_counter.place(x=200,y=135)

    #dialogbox
    
    dialogue_label.place(relx=.8, rely=0, anchor='ne')

    root.after(10,game)
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
    dialoguelist.insert(0,(f"{new_dialogue}\r\r"))
    #if len(dialoguelist) >= 10:
     #   dialoguelist.pop()
    dialogue_label.config(text="".join(dialoguelist))
    