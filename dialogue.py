from main import *

dialogue = tk.Label(root,text=("""You are in Middle of Nowhere.
Right now, you can only get berries for food, and you need to eat to survive."""))
dialogue.place(x=1000,y=100)

dialogue1 = ""
dialogue2 = ""
dialogue3 = ""

def dialogue(new_dialogue):
    dialogue1 = new_dialogue
    dialogue2 = dialogue1
    dialogue3 = dialogue2
    dialogue1_display = tk.Label(root,text=dialogue1).pack(side=tk.RIGHT, pady=5)
    dialogue2_display = tk.Label(root,text=dialogue2).pack(side=tk.RIGHT, pady=5)
    dialogue3_display = tk.Label(root,text=dialogue3).pack(side=tk.RIGHT, pady=5)

