from ourgameresources import *
import tkinter as tk
#Dialogue
dialogue1 = ""
dialogue2 = ""
dialogue3 = ""
root = tk.Tk()
root.title("Name of our Game")

def update():
    berries_counter.config(text=f"Berries: {getamount("berries")}")
    science_counter.config(text=f"Science: {getamount("science")}")

def dialogue_pop_up(new_dialogue):
    global dialogue1
    global dialogue2
    global dialogue3
    dialogue3 = dialogue2
    dialogue2 = dialogue1
    dialogue1 = new_dialogue
    dialogue1_display = tk.Label(root, text=dialogue1,width=20,wraplength=100).pack(side=tk.TOP, pady=5)
    dialogue2_display = tk.Label(root, text=dialogue2,width=20,wraplength=100).pack(side=tk.TOP, pady=5)
    dialogue3_display = tk.Label(root, text=dialogue3,width=20,wraplength=100).pack(side=tk.TOP, pady=5)

#Berries
def berry_gather():
    berries_button.config(state="disabled")
    berries_button.after(4999, lambda: changeamount("berries", 1))
    berries_counter.after(5000, lambda: update(berries_counter, science_counter))
    berries_button.after(5001, lambda: berries_button.config(state="normal"))
berries_button = tk.Button(root, text="Gather Berries", command=berry_gather)
berries_button.place(x=0,y=100)
berries_counter = tk.Label(root, text = "Berries: 0")
berries_counter.place(x=500,y=100)
#Brainstorm
def brainstorm():
    brainstorm_button.config(state="disabled")
    brainstorm_button.after(29999, lambda: changeamount("berries", 1))
    science_counter.after(30000, lambda: update(berries_counter, science_counter))
    brainstorm_button.after(30001, lambda: berries_button.config(state="normal"))
brainstorm_button = tk.Button(root, text="Brainstorm", command=brainstorm)
brainstorm_button.place(x=0,y=500)
science_counter = tk.Label(root, text = "Science: 0")
science_counter.place(x=100,y=100)

dialogue_pop_up("""You are in Middle of Nowhere.
Right now, you can only get berries for food, and you need to eat to survive.""")

root.after(500,devkey)
root.mainloop()