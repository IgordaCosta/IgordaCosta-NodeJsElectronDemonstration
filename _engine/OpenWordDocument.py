import win32com.client as win32

from importedDataPyinternalLocation import *
import getTableData
import createSqliteTableFromList
import dropSqlTable
import os
import openWorkbook
import CloseEspecificWorkbook

import closeWordWithHelp
from importedDataPyexcelLocation import *

def OpenWordDocument():

    Dictionary=getTableData.GetTableData()
    # print(Dictionary)

    fileNameOnly=Dictionary['fileNameOnly']

    try:
        newFileLocation=Dictionary['newFileLocation']
    except:
        home = os.path.expanduser('~')
        
        filePath = os.path.join(home, internalLocation ,excelLocation)
        
        newFileLocation=filePath +"\\temp_" + fileNameOnly
        Dictionary['newFileLocation']=newFileLocation

    # print(newFileLocation)

    # print('newFileLocation above')

    # Here it creates a new word document with the name of the old with a 
    # 'temp_' in the beginning and a coded date at the end
    # this document will be created then added information
    # then replace the original document name for input data
    # the temp document could be added to a Temp folder that will later
    # be removed

    closeWordWithHelp.closeWord(fileName=newFileLocation)

    closeWordWithHelp.OpenWord(fileName=newFileLocation)
    

    # CloseEspecificWorkbook.CloseEspecificWorkbook(fileName=newFileLocation) # this is for excel workbook

    # openWorkbook.openWorkbook(xlfile=newFileLocation, Invisable=False) # this is for excel workbook




OpenWordDocument()
            