resourcedictionary = {
    "wood": 0,
    "stone": 0,
    "money": 0,
    "science": 0
}
fooddictionary = {
    "berries": 0,
    "meat": {
    "raw": 0,
    "fried": 0,
    "roasted": 0
},
    "fish": {
    "raw": 0,
    "fried": 0,
    "roasted": 0
},
    "vegetables": 0,
    "fruits": 0
}
# Nothing can be in food dictionary and resource dictionary.

def update():
    berries_counter.config(text=f"Berries: {getamount("berries")}")
    brainstorm.config(text=f"Science: {getamount("berries")}")


def getamount(resource,condition=""):
    if resource in resourcedictionary:
        return resourcedictionary[resource]
    elif resource in fooddictionary:
        if type(fooddictionary[resource]) is dict:
            if condition == "raw" or condition == "fried" or condition == "roasted":
                return fooddictionary[resource][condition]
            else:
                return "FoodTypeError"
        else:
            return fooddictionary[resource]
        
    else:
        return "GetResourceAmountError"

def changeamount(resource,change,condition=""):
    if resource in resourcedictionary:
        resourcedictionary[resource] = resourcedictionary[resource] + change
    elif resource in fooddictionary:
        if type(fooddictionary[resource]) is dict:
            if condition == "raw" or condition == "fried" or condition == "roasted":
                fooddictionary[resource][condition] = fooddictionary[resource][condition] + change
            else:
                return "FoodTypeError"
        else:
            fooddictionary[resource] = fooddictionary[resource] + change
    else:
        return "ChangeResourceAmountError"

def setamount(resource,amount,condition =""):
    if resource in resourcedictionary:
        resourcedictionary[resource] = amount
    elif resource in fooddictionary:
        if type(fooddictionary[resource]) is dict:
            if condition == "raw" or condition == "fried" or condition == "roasted":
                fooddictionary[resource][condition] = amount
            else:
                return "FoodTypeError"
        else:
            fooddictionary[resource] = amount
    else:
        return "SetResourceAmountError"
