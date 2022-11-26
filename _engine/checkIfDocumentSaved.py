from win32com.client import Dispatch
import win32com.client as win32

import getTableData
import readSqlDatabase





def checkIfDocumentSaved():

    dataName='datafillName'

    datafillName = getTableData.GetDataFromDatabase(dataName=dataName)


# ###################################      Imput Data      ########################################

    FilesInDatabaseLocation='FilesInDatabase'
    columnsFileinDatabase=['Job Name', 'File KEY', 'File Saved Location']

    # ###################################      Imput Data      ########################################
    

    OriginalFileNameTable0 = readSqlDatabase.readSqlDatabase(table_name=FilesInDatabaseLocation)
    print(OriginalFileNameTable0)
    OriginalFileNameTable=OriginalFileNameTable0[0]
    print(OriginalFileNameTable)
    print("OriginalFileNameTable")
    OriginalFileNameTable=OriginalFileNameTable[OriginalFileNameTable[columnsFileinDatabase[0]]==datafillName]
    OriFileName0=OriginalFileNameTable[columnsFileinDatabase[2]]
    print(OriFileName0)
    OriFileName=OriFileName0.values[0]
    print(OriFileName)


    wb = openWorkbook(OriFileName)
    wb.Close(True)
    wb = openWorkbook(OriFileName)
    
    # print(os.getcwd())
    
    # documentSaved=False
    # rsp=1
    
    try:
        
        ws = wb.Sheets(1)
        # documentSaved=True
        print("documentSaved")
    except:

        # ##################################       Changed Screen       #############################

        

        # ##################################       Changed Screen       #############################

        print("DocumentNOTSaved")

        

    # if documentSaved:
    #     placeValuesInFile()