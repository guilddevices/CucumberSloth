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

def resourcegetamount(resource):
    if resource in resourcedictionary:
        return resourcedictionary[resource]
    else:
        return "GetResourceAmountError"

def resourcechangeamount(resource,change):
    if resource in resourcedictionary:
        resourcedictionary[resource] = resourcedictionary[resource] + change
    else:
        return "ChangeResourceAmountError"

def resourcesetamount(resource,amount):
    if resource in resourcedictionary:
        resourcedictionary[resource] = amount
    else:
        return "SetResourceAmountError"    

def foodgetamount(resource):
    if resource in resourcedictionary:
        return resourcedictionary[resource]
    else:
        return "GetResourceAmountError"

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
