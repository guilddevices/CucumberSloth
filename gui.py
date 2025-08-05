from ourgameresources import *
import tkinter as tk
#Dialogue
global berries_button, berries_counter, brainstorm_button, science_counter, root
root=tk.Tk()
dialogue1 = ""
dialogue2 = ""
dialogue3 = ""
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
    global root
    dialogue3 = dialogue2
    dialogue2 = dialogue1
    dialogue1 = new_dialogue
    dialogue1_display = tk.Label(root, text=dialogue1,width=20,wraplength=100).place(relx=1.0, rely=0.0, anchor="ne").pack(side=tk.TOP, pady=5)
    dialogue2_display = tk.Label(root, text=dialogue2,width=20,wraplength=100).place(relx=1.0, rely=0.0, anchor="ne").pack(side=tk.TOP, pady=5)
    dialogue3_display = tk.Label(root, text=dialogue3,width=20,wraplength=100).place(relx=1.0, rely=0.0, anchor="ne").pack(side=tk.TOP, pady=5)

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


def initialize():
    root = tk.Tk()
    root.title("Name of our Game")
    #Berries
    berries_button.place(x=0,y=100)
    berries_counter.place(x=500,y=100)
        
    #Brainstorm
    brainstorm_button.place(x=0,y=500)
    science_counter.place(x=100,y=100)

    root.after(500,devkey)
    root.mainloop()