from ourgameresources import *
import state as st
def eat():
    import state as st
    if getamount("berries") > 0:
        changeamount("berries",-1)
        #st.eatclock = 1200
        st.ranout = "berries"
        return True
    elif getamount("vegetables") > 0:
        changeamount("vegetables",-1)
        #st.eatclock = 2400
        st.ranout = "vegetables"
        return True
    elif getamount("fruits") > 0:
        changeamount("fruits",-1)
        #st.eatclock = 4800
        st.ranout = "fruits"
        return True
    else:
        return False
    
def havefood():
    if getamount("berries") > 0 or getamount("vegetables") > 0 or getamount("fruits") > 0:
        return True
    else:
        return False
        