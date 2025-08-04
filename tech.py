from resources import *
from main import *

science_tree = {
    "lumberjack": {
        "Science": 2
    }
}
have_science = {
    "lumberjack": False
}

def research(item):
    for resource in science_tree[item]:
        if science_tree[item][resource] < getamount(resource):
            return("Not Enough Resources")
    for resource in science_tree[item]:
        changeamount(resource,-science_tree[item][resource])
    have_science[item] = True
    update()
    return "Succesfully Bought"