from ourgameresources import *
import tkinter as tk
#Dialogue
dialoguelist = []
global berries_button, berries_counter, brainstorm_button, science_counter
global root
root = tk.Tk() 
root.title("Name of our Game")
def initialize():
    #Berries
    berries_button.place(x=0,y=100)
    berries_counter.place(x=500,y=100)
        
    #Brainstorm
    brainstorm_button.place(x=0,y=500)
    science_counter.place(x=100,y=100)

    root.after(500,devkey)
    root.mainloop()

def devkey():
    key = input("What is the key? ")
    if key != "~":
        return
    else:
        for x in resourcedictionary:
            changeamount(x,10000)
        update()

def disable(press_button):
    press_button.config(state="disabled")

def update():
    berries_counter.config(text=f"Berries: {getamount("berries")}")
    science_counter.config(text=f"Science: {getamount("science")}")

def dialogue_pop_up(new_dialogue):
    dialoguelist.insert(0,new_dialogue)
    if dialoguelist >= 10:
        dialoguelist[9] = ""
    new_dialogue = Label(root, text = new_dialogue)
    new_dialogue.place(relx=1, rely=0, anchor='ne')
    

def berry_gather():
    disable(berries_button)
    berries_button.after(4999, lambda: changeamount("berries", 1))
    berries_counter.after(5000, lambda: update())
    berries_button.after(5001, lambda: berries_button.config(state="normal"))

def brainstorm():
    disable(brainstorm_button)
    brainstorm_button.after(29999, lambda: changeamount("science", 1))
    science_counter.after(30000, lambda: update())
    brainstorm_button.after(30001, lambda: brainstorm_button.config(state="normal"))

#Berries
berries_counter = tk.Label(root, text = "Berries: 0")
berries_button = tk.Button(root, text="Gather Berries", command=berry_gather)
brainstorm_button = tk.Button(root, text="Brainstorm", command=brainstorm)
science_counter = tk.Label(root, text = "Science: 0")