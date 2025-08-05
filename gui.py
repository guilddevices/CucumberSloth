from ourgameresources import *
import tkinter as tk
#Dialogue
global berries_button, berries_counter, brainstorm_button, science_counter
dialogue_history = []
dialogue_labels = []
MAX_DIALOGUES = 10
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
    global dialogue_history, dialogue_labels, root, MAX_DIALOGUES
    dialogue_history.append(new_dialogue)
    if len(dialogue_history) > MAX_DIALOGUES:
        dialogue_history.pop(0)
    for label in dialogue_labels:
        label.destroy()
    dialogue_labels.clear()
    dialogue_area_width = 300
    padding_from_right_edge = 20
    dialogue_start_y = 10
    line_height = 25
    x_pos = root.winfo_width() - dialogue_area_width - padding_from_right_edge
    for i, dialogue_text in enumerate(reversed(dialogue_history)):
        target_y = dialogue_start_y + (i * line_height)
        label = tk.Label(root, text=dialogue_text,
                         width=dialogue_area_width // 7,
                         wraplength=dialogue_area_width - (2 * 5),
                         bg="#282828", fg="#E0E0E0",
                         font=("Inter", 10),
                         anchor="nw", 
                         justify="left",
                         relief="flat",
                         padx=5, pady=2)
        label.place(x=x_pos, y=target_y)
        dialogue_labels.append(label)
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