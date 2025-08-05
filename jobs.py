from resourcemanager import *
from tech import *
from main import update
import random

#Forage-Button
def forage():
    changeamount("berries",1)
    if random.random() < 0.1:
        changeamount("vegetables",1)
    if random.random() < 0.02:
        changeamount("fruits",1)
    update()
