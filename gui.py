global eatclcock, berries_button, berries_counter, brainstorm_button, science_counter, dialogue_label, root
from ourgameresources import *
from variables import *
import tkinter as tk
from user import *
from dialogue import *
import random
import time
import threading
import state as st
#Dialogue
dialoguelist = []
root = tk.Tk() 
root.title("Name of our Game")
#define helper functions
def enable(press_button):
    press_button.config(state="normal")
    

def frame():
    st.eatclock -= 1
    if st.eatclock == 0:
        if havefood():
            eat()
            dialogue_pop_up("You have eaten food.")
        else:
            disable(brainstorm_button)
            dialogue_pop_up("You are starving! You can only gather food.")
            st.food = False
            st.starving = True
            update()
            return
        '''if st.ranout == "berries":
            st.eatclock = 1200
        elif st.ranout == "vegetables":
            st.eatclock = 2400
        elif st.ranout == "fruits":
            st.eatclock = 4800'''

    if st.food == False and havefood() == True:
        eat()
        dialogue_pop_up("You have eaten food. You are no longer starving.")
        brainstorm_button.config(state="normal")
        st.food = True
        st.starving = False

    update()
def game():
    dialogue_pop_up("You are in Middle of Nowhere.\nRight now, you can get berries for food, and you need to eat to survive.\nEvery 20 seconds, you will lose one berry.")
    run_frame()

def run_frame():
    frame()
    root.after(17, run_frame)  # roughly 60 frames per second

def berry_gather():
    number = random.randint(4,6)
    dialogue_pop_up(dialogue["berries"][str(number)])
    disable(berries_button)
    berries_button.after(number*1000-1, lambda: changeamount("berries", 1))
    berries_button.after(number*1000, lambda: berries_button.config(state="normal"))

def brainstorm():
    brainstorm_number = random.randint(1,3)
    dialogue_pop_up(dialogue["brainstorm"][str(brainstorm_number)])
    disable(brainstorm_button)
    for i in range(1,600):
        if st.starving:
            dialogue_pop_up("You have lost progress on science!")
            return
        time.sleep(1/20)
    enable(brainstorm_button)
    changeamount("science",1)
    

#Initialize Widgets
berries_counter = tk.Label(root, text = "Berries: 0")
berries_button = tk.Button(root, text="Gather Berries", command=berry_gather)
brainstorm_button = tk.Button(root, text="Brainstorm", command=brainstorm)
science_counter = tk.Label(root, text = "Science: 0")
dialogue_label = tk.Label(root, text="", justify="left", anchor="ne", bg="Black", fg="White", wraplength=round(root.winfo_screenwidth()/3.3), width=round(root.winfo_screenwidth()/30), height=round(root.winfo_screenheight()/9))

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
    dev.start()
    #Berries
    berries_button.place(x=0,y=100)
    berries_counter.place(x=200,y=105)
        
    #Brainstorm
    brainstorm_button.place(x=0,y=130)
    science_counter.place(x=200,y=135)

    #dialogbox
    
    dialogue_label.place(relx=.8, rely=0, anchor='nw')

    root.after(10,game)
    root.mainloop()

def devkey():
    key = input("What is the key? ")
    if key != "~":
        return
    else:
        for x in resourcedictionary:
            changeamount(x,10000)
        update()
dev = threading.Thread(target=devkey)

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
    