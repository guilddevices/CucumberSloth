global eatclock, berries_button, berries_counter, brainstorm_button, science_counter, dialogue_label, brainstorm_id, research_there, root, fruit, vegetable
import platform
from ourgameresources import *
from ourvariables import *
import tkinter as tk
from user import *
from dialogue import *
import random
import time
import threading
import state as st
brainstorm_id = None
canceled = False
research_there = False
#Dialogue
dialoguelist = []
root = tk.Tk() 
root.title("Name of our Game")
#define helper functions
def enable(press_button):
    press_button.config(state="normal")

def frame():
    global research_there
    global brainstorm_id
    if research_there == False:
        if getamount("science") >= 2:
            research_button.place(x=root.winfo_screenwidth()/2-root.winfo_screenwidth()/10, y=root.winfo_screenheight()-root.winfo_screenheight()/10*9)
            research_there = True
    now = time.time()
    if not hasattr(st, "last_eat_time"):
        st.last_eat_time = now    
    if int(now) - int(st.last_eat_time) >= int(st.eat_interval):
        if havefood():
            eat()  # This should set st.ranout to "berries", "vegetables", or "fruits"
            if st.ranout == "berries":
                dialogue_pop_up("You have eaten berries.")
            elif st.ranout == "vegetables":
                dialogue_pop_up("You have eaten vegetables.")
            elif st.ranout == "fruits":
                dialogue_pop_up("You have eaten fruits.")
            else:
                dialogue_pop_up("You have eaten food.")
        elif st.printedmessage == True:
            if brainstorm_id is not None:
                root.after_cancel(brainstorm_id)

        else:
            disable(brainstorm_button)
            dialogue_pop_up("You are starving! You can only gather food.")

            st.printedmessage = True
            st.food = False
            st.starving = True
            update()
            st.last_eat_time = now
            return
        st.last_eat_time = now

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

def show_counter(which_counter):
    which_counter.config(fg="White")

def berry_gather():
    number = random.randint(4,6)
    dialogue_pop_up(dialogue["berries"][str(number)])
    disable(berries_button)
    berries_button.after(number*1000-1, lambda: changeamount("berries", 1))
    berries_button.after(number*1000, lambda: berries_button.config(state="normal"))
    berries_button.after(number*1000, lambda: show_counter(berries_counter))

def brainstormfix():
    if havefood():
        brainstorm_button.config(state="normal")
    else:
        pass

def brainstormchange():
    if st.starving:
        return
    else:
        changeamount("science", 1)
        brainstorm_id = None

def brainstorm():
    global brainstorm_id
    brainstorm_number = random.randint(1,3)
    dialogue_pop_up(dialogue["brainstorm"][str(brainstorm_number)])
    disable(brainstorm_button)
    brainstorm_id = brainstorm_button.after(29999, lambda: brainstormchange())
    brainstorm_button.after(30000, lambda: brainstormfix())
    brainstorm_button.after(30001, lambda: show_counter(science_counter))

def research_forage():
    transform(berries_button, forage_button, 0, 100)
    disable(research_button)
    vegetables_counter.place(x=root.winfo_screenwidth()/7.2,y=root.winfo_screenheight()/(60/7)+root.winfo_screenheight()/15)
    fruits_counter.place(x=root.winfo_screenwidth()/7.2,y=root.winfo_screenheight()/(60/7)+root.winfo_screenheight()/7.5)

    

def foragebutton():
    disable(forage_button)
    forage_button.after(4999,lambda: enable(forage_button))
    forage_button.after(5000,lambda: forage())

#Initialize Widgets
berries_button = tk.Button(root, text="Gather Berries", command=berry_gather, bg="#FF6863", fg="Black")
forage_button = tk.Button(root,text="Forage",command=foragebutton)
if platform.system() != "Darwin":
    research_button = tk.Button(root, text="Research: \r Forage: 2 Science", command=research_forage, bg="#0022FF", fg="White")
else:
    research_button = tk.Button(root, text="Research: \r Forage: 2 Science", command=research_forage)
brainstorm_button = tk.Button(root, text="Brainstorm", command=brainstorm, bg="#008080", fg="Black")
science_counter = tk.Label(root, text = "Science: 0")
berries_counter = tk.Label(root, text = "Berries: 0")
dialogue_label = tk.Label(root, text="", justify="left", anchor="nw", bg="Black", fg="White", wraplength=round(root.winfo_screenwidth()/3), width=round(root.winfo_screenwidth()/10), height=round(root.winfo_screenheight()/15))
fruits_counter = tk.Label(root,text="Fruits: 0", bg="Black", fg="White")
vegetables_counter = tk.Label(root,text="Vegetables: 0", bg="Black", fg="White")


def forage():
    changeamount("berries",2)
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
        dialogue_pop_up(dialogue["forage"][str(random.randint(1,2))])

def initialize():
    #dev.start()
    #Berries
    berries_button.place(x=0,y=root.winfo_screenheight()/9)
    berries_counter.place(x=root.winfo_screenwidth()/7.2,y=root.winfo_screenheight()/(60/7))
    berries_counter.config(bg="Black", fg="Black")
        
    #Brainstorm
    brainstorm_button.place(x=0,y=root.winfo_screenheight()/(90/13))
    science_counter.place(x=root.winfo_screenwidth()/7.2,y=root.winfo_screenheight()/(20/3))
    science_counter.config(bg="Black", fg="Black")
    

    #dialogbox
    
    dialogue_label.place(relx=.6, rely=0, anchor='nw')
    root.config(bg="Black")
    root.after(10,game)
    root.mainloop()

"""def devkey():
    key = input("What is the key? ")
    if key != "~":
        return
    else:
        for x in resourcedictionary:
            changeamount(x,10000)
        update()
dev = threading.Thread(target=devkey)"""

def disable(press_button):
    press_button.config(state="disabled")

def update():
    berries_counter.config(text=f"Berries: {getamount('berries')}")
    science_counter.config(text=f"Science: {getamount('science')}")
    fruits_counter.config(text=f"Fruits: {getamount('fruits')}")
    vegetables_counter.config(text=f"Vegetables: {getamount('vegetables')}")

    
def dialogue_pop_up(new_dialogue):
    dialoguelist.insert(0,(f"{new_dialogue}\r\r"))
    #if len(dialoguelist) >= 10:
     #   dialoguelist.pop()
    dialogue_label.config(text="".join(dialoguelist))

def hide(press_button):
    press_button.place_forget()

def showrel(press_button,relative_x,relative_y):
    press_button.place(relx=relative_x,rely=relative_y)

def showdef(press_button,x,y):
    press_button.place(x=x,y=y)

def transform(button1,button2,x,y):
    hide(button1)
    showdef(button2,x,y)