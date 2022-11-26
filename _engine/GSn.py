# import os
import numpy


from SnL import *
from importedWindowTitle import *






def getWindowPid():  #Block this function after production and adapt the code
    import win32gui,win32process

    hwnd = win32gui.FindWindow(None, WIndowTitle)
    threadid,pid = win32process.GetWindowThreadProcessId(hwnd)
    return pid



  
def DefConst():
   
    # IDS =os.getpid()
    try:
        IDS = int(getWindowPid())    #Block this function after production

    except:
        import ctypes

        IDS = int(ctypes.windll.user32.GetForegroundWindow())



    #Data Senha
    DSn = str(IDS)    

    #ListL ocation
    LL = int(DSn[-2:])

    #Location Choosen
    LC = SnL[LL]            

    #Small List Choosen
    SLC = list(LC[34:57])
    try:
        numpy.random.seed(IDS)
    except:
        IDS = 54823
        numpy.random.seed(IDS)
    numpy.random.shuffle(SLC)

    # Aleatorio Small String Choosen
    ASSC = ''.join(SLC)

    #Small List Choosen 2
    SLC2 = list(LC[72:83])

    numpy.random.seed(IDS)
    numpy.random.shuffle(SLC2)

    # Aleatorio Small String Choosen
    ASSC2 = ''.join(SLC2) + '.db'


    return ASSC2, ASSC



ASSC2, ASSC = DefConst()



# import ctypes
# window = ctypes.windll.user32.GetForegroundWindow()

# print(window)