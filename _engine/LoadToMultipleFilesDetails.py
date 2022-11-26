# import os
# import pandas
# import glob
# from StyleFrame import StyleFrame, Styler


# from styleframe import StyleFrame, Styler

# import styleframe



# from sqlalchemy import create_engine
# import openpyxl
# from win32com.client import Dispatch
# import win32com.client as win32
# import sys

# from bs4 import BeautifulSoup
# from requests_html import HTML

from importedDataPyAutoFormFiller_OutputFiles import *
import getTableData
import readSqlDatabase

import OpenDeleteRecreateSheet
import changeDirectory
# import dropSqlTable
import GetExcelFilesinLocation
# import PrintTexListSerial
import base93Characterconversion
import DeleteExcelTempFiles
from importedDataPyexcelLocation import *



def LoadToMultipleFilesDetails(datafillName):


    DeleteExcelTempFiles.DeleteExcelTempFiles()







    TimeName = base93Characterconversion.base93Characterconversion()



    filename="OneFileToMultipleFiles_"+ str(TimeName) + ".xlsx"


    

  

    datafillName0 = datafillName

    spaceReplaceDataUserImput = '$%78&*&'

    datafillName = datafillName0.replace(' ', spaceReplaceDataUserImput )

    data = datafillName

    dataName = 'datafillName'

    getTableData.WriteDataDatabase(data=data, dataName=dataName)


    print(datafillName)


    print('datafillName above')

    ListToPrint = []

    changeDirectory.ChangeTokey()



















    # dropSqlTable.DropTable()

    # ###################################      Imput Data      ########################################
    
    FilesInDatabaseLocation='FilesInDatabase'
    columnsFileinDatabase=['Job Name', 'File KEY', 'File Saved Location']

    # ###################################      Imput Data      ########################################

    
    
    # location=filename
    
    # home = os.path.expanduser('~')       
    
    
    # filesInFolder1 = GetExcelFilesinLocation.GetExcelFilesinLocation(location="AutoFormF=illerFiles")
    filesInFolder1 = GetExcelFilesinLocation.GetExcelFilesinLocation(location=excelLocation)
    
    
    filesInFolder2 = GetExcelFilesinLocation.GetExcelFilesinLocation(location=AutoFormFiller_OutputFiles)
    
    listTocheck=[filename]+filesInFolder1+filesInFolder2
    # print(listTocheck)
    

    
    
    # home = os.path.expanduser('~')       
    
    
    databaseUsed0 = readSqlDatabase.readSqlDatabase(table_name="KEY_"+datafillName)
    databaseUsed=databaseUsed0[0]

    # print(databaseUsed0)
    
    OriginalFileNameTable0 = readSqlDatabase.readSqlDatabase(table_name=FilesInDatabaseLocation)
    print(OriginalFileNameTable0)
    
    OriginalFileNameTable=OriginalFileNameTable0[0]
    # print(OriginalFileNameTable)
    # print("OriginalFileNameTable")
    OriginalFileNameTable=OriginalFileNameTable[OriginalFileNameTable[columnsFileinDatabase[0]]==datafillName]
    
    
    OriFileName0=OriginalFileNameTable[columnsFileinDatabase[2]]
    # print(OriFileName0)
    OriFileName=OriFileName0.values[0]
    # print(OriFileName)
    # print("OriFileName after")
    
    # print(databaseUsed)
    itemAddress=databaseUsed.columns.values[1:]
    # print(itemAddress)
    # print("item address above")
    
    itemDescription0=databaseUsed.values[0][1:]
    # print(itemDescription0)


    spaceReplaceData = '$%3&*&'

    itemDescription = str(itemDescription0).replace('[','').replace(']','').replace('"','').replace("'",'').replace(" ",',').replace('\n', '').replace(spaceReplaceData, ' ').split(',')

    # print(itemDescription)



    # print("item Description above")
    itemDescription=["Save Name"]+list(itemDescription)
    # FrameUsed=pandas.DataFrame(columns=itemDescription)

    ###### save variables to database  filename=filename, frame=FrameUsed,columnList=itemDescription

    # DictionaryAdd={'filename':filename, 'frame':FrameUsed,'columnList':itemDescription}

    # DictionaryAdd={'filename':filename,'columnList':itemDescription, 'datafillName':datafillName }
    

    DictionaryAdd={'filename':filename,'columnList':itemDescription}

    getTableData.MultipleDictionaryWriteDataDatabase(DictionaryAdd=DictionaryAdd)

    OpenDeleteRecreateSheet.OpenDeleteRecreateSheet()



# def GetExcelFilesinLocation(location, IncludeFolder=False):
#         home = os.path.expanduser('~') 
        

        
#         print(SelectedFolder)
        
#         print("files in folder with ~$")
        
#         if IncludeFolder==False:
#             filesInFolder = [f.split("\\")[-1] for f in glob.glob(SelectedFolder + "/[!~$]*.xl*", recursive=True)]
            
#             print(filesInFolder)
#             print("files in folder withOUT ~$")
#         if IncludeFolder==True:
#             filesInFolder=glob.glob(SelectedFolder+"\\*.xl*")
        
#         return filesInFolder



# def readSqlDatabase(table_name,columns=None):
#         DatabaseName="AutoFormFiller.db"
#         conn = create_engine('sqlite:///'+DatabaseName)
#         try:
#             df2=pandas.read_sql_table(table_name, conn, columns=columns)
#             #print(df2)
#             TableFound=True
#         except ValueError:
#             df2=None
#             TableFound=False
#         return df2,TableFound

     


# datafillName="file1"


# datafillName=sys.argv[1]








datafillName=getTableData.GetDataFromDatabase(dataName='datafillName')



# datafillName = 'img17'     #block i=this after test


# print('python datafillName: ',datafillName)


LoadToMultipleFilesDetails(datafillName)