from ourgameresources import *
global eatclock
eatclock = 1200
def eat():
    if getamount("berries") > 0:
        changeamount("berries",-1)
        eatclock = 12000
        return True
    elif getamount("vegetables") > 0:
        changeamount("vegetables",-1)
        eatclock = 2400
        return True
    elif getamount("fruits") > 0:
        changeamount("fruits",-1)
        eatclock = 4800
        return True
    else:
        return False
        