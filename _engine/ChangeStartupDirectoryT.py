import os
# import path

from importedDataPyinternalLocation import *

def ChangeStartupDirectory(Folder,midFolder=internalLocation):
        
        home = os.path.expanduser('~')

        location = os.path.join(home, midFolder, Folder)
        
        if not os.path.exists(location):
            os.makedirs(location)

        else:

            pass
         
        os.chdir(location)