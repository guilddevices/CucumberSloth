from ourgameresources import *

science_tree = {
    "foraging": {
        "description": "Foraging unlocks the replacement of gathering with foraging. It does the same thing except has a chancce to give other food.",
        "science": 2
    },
    "wood collecting" :{
        "description": "Wood Collecting unlocks the collect wood button giving you wood.",
        "science": 2
    }
}
have_science = {
    "foraging": False,
    "wood collecting": False
}

def research(item):
    if item in science_tree:
        for resource in science_tree[item]:
            if resource != "description":
                if science_tree[item][resource] < getamount(resource):
                    return("Not enough resources!")

        for resource in science_tree[item]:
            if resource != "description":
                changeamount(resource,-science_tree[item][resource])
        have_science[item] = True
        return(f"Succesfully researched {item}")
    else:
        return "ResearchError"