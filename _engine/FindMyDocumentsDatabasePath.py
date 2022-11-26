import os

import PrintTexListSerial
from importedDataPyinternalLocation import *


def FindMyDocumentsDatabasePath():

    ListToPrint = []

    Folder='AutoFormFillerKey'

    home = os.path.expanduser('~')
        
    # print(home)
    
    location = os.path.join(home, internalLocation, Folder)
    
    # print(location)
    
    # folder_check = os.path.isdir(location)
    
    # print(folder_check)
    
    if not os.path.exists(location):
        os.makedirs(location)
        # print('folder created')
    else:
        # print("folder exists")
        pass


    # print(location)

    ListToPrint.append(location)


    PrintTexListSerial.PrintTexListSerial(ListToPrint=ListToPrint)







FindMyDocumentsDatabasePath()

