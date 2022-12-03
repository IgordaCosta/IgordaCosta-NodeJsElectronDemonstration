import os
from importedDataPyFAutoForm_FillerFiles import *
from importedDataPyimageFolderLocation import *
from importedDataPyinternalLocation import *
from importedDataPyAutoFormFillerKey import *

import DeleteAllFilesInFolder
import FilePathFromPython
import CreateFolderInFolder



def DeleteAllTempFiles():
    # currentWorkingDirectory = os.getcwd() +'\\'

    currentWorkingDirectory = str(FilePathFromPython.FilePathFromPython()) +'\\'
    home = os.path.expanduser('~')

    AutoForm_FillerFilesAddLocation = os.path.join(home, internalLocation, AutoForm_FillerFiles,'Temp') + '\\'

    
    CreateFolderInFolder.CreateFolderInFolder(AutoForm_FillerFilesAddLocation)


    LocationToDeleteFIlesList= [

            currentWorkingDirectory,
            currentWorkingDirectory  + imageFolderLocation + '\\' ,
                        
            AutoForm_FillerFilesAddLocation

        ]


    for locationToDelete in LocationToDeleteFIlesList:
        print(locationToDelete)
        DeleteAllFilesInFolder.DeleteAllFilesInFolder(locationToDelete)



    KeepDBLocation = os.path.join(home, internalLocation, AutoForm_FillerKey) + '\\'

    DeleteAllFilesInFolder.DeleteAllFilesInFolder(KeepDBLocation, KeepDB=True)


    
DeleteAllTempFiles()
