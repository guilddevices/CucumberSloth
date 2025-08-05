from tech import *
from ourgameresources import *
import random

#Forage-Button
def forage():
    changeamount("berries",1)
    if random.random() < 0.1:
        changeamount("vegetables",1)
    if random.random() < 0.02:
        changeamount("fruits",1)