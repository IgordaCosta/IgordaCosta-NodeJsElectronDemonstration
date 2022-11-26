import os

from importedDataPyinternalLocation import *
from importedDataPyAutoFormFiller_OutputFiles import *
import getTableData 

LocationAsked = getTableData.GetDataFromDatabase(dataName='FolderSaveLocation')

if LocationAsked == '':

        location=AutoFormFiller_OutputFiles


        home = os.path.expanduser('~')       
        filePath = os.path.join(home, internalLocation,location)


path=os.path.realpath(filePath)
os.startfile(path)