resourcedictionary = {
    wood: 0
    stone: 0
    food: 0
}

def getamount(resource):
    if resource in resourcedictionary:
        return resourcedictionary[resource]
    else:
        return "GetResourceAmountError"

def changeamount(resource,change):
    if resource in resourcedictionary:
        resourcedictionary[resource] = resourcedictionary[resource] + change
    else:
        return "ChangeResourceAmountError"

def setamount(resource,amount):
    if resource in resourcedictionary:
        resourcedictionary[resource] = amount
    else:
        return "SetResourceAmountError"     

