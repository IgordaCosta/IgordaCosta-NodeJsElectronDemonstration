import os
from importedDataPyinternalLocation import *

def ChangeStartupDirectory(Folder):
        
        # curentWorkingDirectory = os.getcwd()
        # print(curentWorkingDirectory)
        # print("curentWorkingDirectory")
        
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
         
        os.chdir(location)

        return location
        
        # curentWorkingDirectory = os.getcwd()
        # print(curentWorkingDirectory)
        # print("New curentWorkingDirectory")



def ChangeTokey():

    Folder='AutoFormFillerKey'

    location = ChangeStartupDirectory(Folder=Folder)

    return location



# Folder= 'UserDatabaseBackups'

# print(ChangeStartupDirectory(Folder))

# print('ChangeStartupDirectory(Folder)')


# ChangeTokey()    ### remove this after test