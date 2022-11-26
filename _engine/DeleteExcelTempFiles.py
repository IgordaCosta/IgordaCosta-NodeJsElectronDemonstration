import os
import pandas

import changeDirectory


def DeleteExcelTempFiles():

    FolderLocation = changeDirectory.ChangeTokey()

    NameToCheck = 'OneFileToMultipleFiles'

    RealfileNameList = os.listdir('.')

    DeleteFileLocations = [x.split('.')[0].split('_')[0]== NameToCheck for x in os.listdir('.')] 

    pdRealfileNameList = pandas.Series(RealfileNameList)[DeleteFileLocations]


    for item in pdRealfileNameList:
        itemToDelete = FolderLocation + '\\' + item

        try:
            os.remove(itemToDelete)
        except:
            pass

