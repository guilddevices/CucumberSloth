from gui import *
from tech import *
from user import *
import time
#variable setting
initialize()
dialogue_pop_up("""You are in Middle of Nowhere.
Right now, you can only get berries for food, and you need to eat to survive.""")
def frame():
    update()
    eatclock -= 1
    if eatclock == 0:
        eat()
    time.sleep(1/60)
while True do:
    frame()

#gameloop


