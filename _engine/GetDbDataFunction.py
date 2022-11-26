# import os
# import sqlite3

import pandas
# from sqlalchemy import create_engine

import ChangeStartupDirectoryT
import readSqlDatabase
import PrintTexListSerial
import StringListIntoList

# this will not change
def ChangeStartupDirectory(Folder):
    
    ChangeStartupDirectoryT.ChangeStartupDirectory(Folder)

# this will not change
# does not apply to secured database
def uploadDatabase():

    FileKey=[]
    FileSavedLocation=[]
    ListToPrint = []

    # CurrentWorkingPath = ''

    ChangeStartupDirectoryT.ChangeStartupDirectory(Folder='AutoFormFillerKey')

    FilesInDatabaseLocation='FilesInDatabase'

    columnsFileinDatabase=['Job Item', 'File KEY', 'File Saved Location']
  
    FileExists=False
    
    
    try:
        FilesInDatabase=pandas.read_excel(FilesInDatabaseLocation)
        FileExists=True

    
    except FileNotFoundError:
        FileExists=False
        FilesInDatabase , FileExists = readSqlDatabase.readSqlDatabase(table_name=FilesInDatabaseLocation,columns=columnsFileinDatabase)
        # print("file not found")
        ListToPrint.append("file not found")

    pass
    
    if FileExists:
        FilesInDatabase , FileExists = readSqlDatabase.readSqlDatabase(table_name=FilesInDatabaseLocation,columns=columnsFileinDatabase)
        
    if FileExists:           
        
        FilesInDatabase=FilesInDatabase[columnsFileinDatabase]
        
        NumbRowsPandas=len(FilesInDatabase.index)
        
        if NumbRowsPandas ==0:
            # print("file not found")
            ListToPrint.append("file not found")
            pass

        else:

            # print(FilesInDatabase[columnsFileinDatabase[0]])
            # print(type(FilesInDatabase[columnsFileinDatabase[0]]))


            spaceReplaceDataUserImput = '$%78&*&'

            # ' '.join(datafillName.split(spaceReplaceDataUserImput))/

            # JobItem=list(FilesInDatabase[columnsFileinDatabase[0]].replace(spaceReplaceDataUserImput, ' '  )) 


            JobItem0=list(FilesInDatabase[columnsFileinDatabase[0]])

            JobItem1 = str(JobItem0)

            JobItem2 = ' '.join(JobItem1.split(spaceReplaceDataUserImput))

            JobItem = StringListIntoList.StringListIntoList(StringList = JobItem2)

            FileKey=list(FilesInDatabase[columnsFileinDatabase[1]])
            FileSavedLocation=list(FilesInDatabase[columnsFileinDatabase[2]])


            # print("blablablabablablz")      

            returnedValues=[str(JobItem), str(FileKey), str(FileSavedLocation)]

            # print(FileKey)
            # print(FileSavedLocation)

            listOfCharCodes=[]
            for x in range(len(returnedValues)):
                listOfCharCodes.append([])
                for c in range(len(returnedValues[x])):
                    listOfCharCodes[x].append(ord(returnedValues[x][c]))

            # print(listOfCharCodes)

            # print("below are the 3 lists of charcodes")

            # print(str(listOfCharCodes[0])[1:-1])
            # print(str(listOfCharCodes[1])[1:-1])
            # print(str(listOfCharCodes[2])[1:-1])

            # print("FILE FOUND")

            ListToPrint.append(str(listOfCharCodes[0])[1:-1])
            ListToPrint.append(str(listOfCharCodes[1])[1:-1])
            ListToPrint.append(str(listOfCharCodes[2])[1:-1])

            ListToPrint.append("FILE FOUND")
                          
    PrintTexListSerial.PrintTexListSerial(ListToPrint=ListToPrint)    

# def readSqlDatabase(table_name,columns=None):
#     DatabaseName="AutoFormFiller.db"
#     conn = create_engine('sqlite:///'+DatabaseName)
#     try:
#         df2=pandas.read_sql_table(table_name, conn, columns=columns)
#         #print(df2)
#         TableFound=True
#     except ValueError:
#         df2=None
#         TableFound=False

#     print(df2)
#     return df2,TableFound





# uploadDatabase() #block this when done testing


# print(returnedvalues)
