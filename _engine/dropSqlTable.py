import os
import sqlite3

import changeDirectory
import GetKeyfileNameType
import GetWriteDBTableSecured
# import FilePathFromPython
import DeleteAllFilesInFolder



# Adapt to delete teh Database so the values will reset
# in case of the secured database option
# adapting just this DropSqlTable funtion will fix both
def DropSqlTable(Database="AutoFormFiller.db", TableName="qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq"):

    # CurrentWorkingPath = FilePathFromPython.FilePathFromPython() +'\\'

   

    conn  = sqlite3.connect(Database)

    c = conn.cursor()

    TableOptions = ['FontAndItsSize','FilesInDatabase','qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq','KEY_']

    TableNameUsed = ''

    if TableName == 'FontAndItsSize':
        TableNameUsed = TableOptions[0]

    elif TableName == 'FilesInDatabase':
        TableNameUsed = TableOptions[1]

    elif TableName == 'qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq':
        TableNameUsed = TableOptions[2]

    elif TableName[:4] == 'KEY_':

        changeDirectory.ChangeTokey()

        KeyFilename = TableName
        TableNameUsed = GetKeyfileNameType.GetKeyfileNameType(KeyFilename)

    else:
        pass

    if TableNameUsed == 'qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq':
        
        # pass
        # GetWriteDBTableSecured.DeleteDb()

       currentWorkingDirectory = os.getcwd()

       DeleteAllFilesInFolder.DeleteAllFilesInFolder(currentWorkingDirectory)



    else:

        changeDirectory.ChangeTokey()

        try:

            c.execute("DROP TABLE " + TableNameUsed)

            # print("Table Dropped Sucessfully")
        except Exception as e:
            # print(e)
            pass

        c.close() 
        conn.close() 

# do not change
def DropTable(TableName="qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq"):


    TableName=TableName
    Database="AutoFormFiller.db"

    
    DropSqlTable(Database=Database, TableName=TableName)


# DropTable()