resourcedictionary = {
    wood: 0,
    stone: 0
}
fooddictionary = {
    berries: 0,
    meat: {
    raw: 0,
    fried: 0,
    roasted: 0,
},
    fish: {
    raw: 0,
    fried: 0,
    roasted: 0,
},
    vegetables: 0,
    fruits: 0
}
#Nothing can be in food dictionary and resource dictionary.

def resourcegetamount(resource,condition=""):
    if resource in resourcedictionary:
        return resourcedictionary[resource]
    elif resource in fooddictionary:
        if type(fooddictionary[resource]) is dict:
            if condition is "raw" or "fried" or "roasted"
                return fooddictionary[resource][condition]
            else:
                return "FoodTypeError"
        else:
            return fooddictionary[resource]
        
    else:
        return "GetResourceAmountError"

def resourcechangeamount(resource,change):
    if resource in resourcedictionary:
        resourcedictionary[resource] = resourcedictionary[resource] + change
    else:
        return "ChangeResourceAmountError"

def foodchangeamount(resource,change):
    if resource in resourcedictionary:
        resourcedictionary[resource] = resourcedictionary[resource] + change
    else:
        return "ChangeResourceAmountError"

def foodsetamount(resource,amount):
    if resource in resourcedictionary:
        resourcedictionary[resource] = amount
    else:
        return "SetResourceAmountError"   
