from resources import *
from main import *
from dialogue_handling import *

science_tree = {
    "lumberjack": {
        "Science": 2
    }
}
have_science = {
    "lumberjack": False
}

def research(item):
    if item in science_tree:
        for resource in science_tree[item]:
            if science_tree[item][resource] < getamount(resource):
                dialogue_pop_up("Not enough resources!")
        for resource in science_tree[item]:
            changeamount(resource,-science_tree[item][resource])
        have_science[item] = True
        update()
        dialogue_pop_up(f"Succesfully researched {item}")
    else:
        return "ResearchError"