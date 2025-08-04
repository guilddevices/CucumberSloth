import tkinter as tk
from main import root
dialogue1 = ""
dialogue2 = ""
dialogue3 = ""

def dialogue_pop_up(new_dialogue):
    dialogue1 = new_dialogue
    dialogue2 = dialogue1
    dialogue3 = dialogue2
    dialogue1_display = tk.Label(root, text=dialogue1).pack(side=tk.RIGHT, pady=5)
    dialogue2_display = tk.Label(root, text=dialogue2).pack(side=tk.RIGHT, pady=5)
    dialogue3_display = tk.Label(root, text=dialogue3).pack(side=tk.RIGHT, pady=5)

