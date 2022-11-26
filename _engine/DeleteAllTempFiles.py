import os
from importedDataPyFAutoForm_FillerFiles import *
from importedDataPyimageFolderLocation import *
from importedDataPyinternalLocation import *
from importedDataPyAutoFormFillerKey import *

import DeleteAllFilesInFolder
import FilePathFromPython



def DeleteAllTempFiles():
    # currentWorkingDirectory = os.getcwd() +'\\'

    currentWorkingDirectory = str(FilePathFromPython.FilePathFromPython()) +'\\'
    home = os.path.expanduser('~')

    LocationToDeleteFIlesList= [

            currentWorkingDirectory,
            currentWorkingDirectory  + imageFolderLocation + '\\' ,

            os.path.join(home, internalLocation, AutoForm_FillerFiles,'Temp') + '\\'

        ]


    for locationToDelete in LocationToDeleteFIlesList:
        DeleteAllFilesInFolder.DeleteAllFilesInFolder(locationToDelete)



    KeepDBLocation = os.path.join(home, internalLocation, AutoForm_FillerKey) + '\\'

    DeleteAllFilesInFolder.DeleteAllFilesInFolder(KeepDBLocation, KeepDB=True)


    
# DeleteAllTempFiles()
