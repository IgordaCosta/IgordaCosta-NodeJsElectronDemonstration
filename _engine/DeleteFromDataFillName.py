import pandas
# import sys

# from . import dropSqlTable
# from . import readSqlDatabase
# from . import writeToSqlite
# from . import getTableData


import dropSqlTable
import readSqlDatabase
import writeToSqlite
import getTableData



def DeleteFromDataFillName():
    
    # columnsFileinDatabase=['Job Name', 'File KEY', 'File Saved Location']


    columnsFileinDatabase=['Job Item', 'Job Name', 'File KEY', 'File Saved Location']

    FilesInDatabaseLocation='FilesInDatabase'

    DatabaseName="AutoFormFiller.db"

    DatabaseNameBACKUP =  writeToSqlite.GetDatePartName(DatabaseNameInput= DatabaseName)

    TableDataGotten = getTableData.GetTableData()

    datafillName0 = TableDataGotten['datafillName']

 
    spaceReplaceDataUserImput = '$%78&*&'

    datafillName = datafillName0.replace(' ', spaceReplaceDataUserImput )


    data = datafillName

    dataName = 'datafillName'


    getTableData.WriteDataDatabase(data=data, dataName=dataName)  

    

    table="KEY_"+datafillName


    dropSqlTable.DropSqlTable(Database=DatabaseName,TableName=table)


    


    ###########################################


    databaseUsed0=readSqlDatabase.readSqlDatabase(table_name=FilesInDatabaseLocation,columns=columnsFileinDatabase)
    databaseUsed=databaseUsed0[0]

    #below checks the ending of the saved file to see if it is of image type
    # databaseToDelete=databaseUsed[(databaseUsed[columnsFileinDatabase[0]]==datafillName)]

    databaseToDelete=databaseUsed[(databaseUsed[columnsFileinDatabase[1]]==datafillName)]

    # print(databaseToDelete)
    

    # print('databaseToDelete above')

    Extension0 = databaseToDelete[columnsFileinDatabase[-1]]

    # print(Extension0)

    Extension1=Extension0.values

    # print(Extension1)

    Extension2=Extension1[0]

    # print(Extension2)

    Extension=Extension2.split(".")[-1]

    # print(Extension)


    # print('Extension above')

    imageExtensions=['jpg', 'jpeg','jpe','jfif','gif','tif','tiff','png','heic','bmp','dib']

    if Extension in imageExtensions:
        ##### in this case the extension is an image extension

        # columnsFileinDatabase2 = ['Job Name', 'File KEY', 'FontName', 'FontSize']

        columnsFileinDatabase2 = ['Job Item', 'Job Name', 'File KEY', 'FontName', 'FontSize', 'FromPdf', 'PdfUsed', 'InPDFdatafillName', 'ExtensionType', 'InPDFdatafillNameUPPER', 'UPPER']

        FilesInDatabaseLocation2='FontAndItsSize'

        DeleteInDatabase(FilesInDatabaseLocation=FilesInDatabaseLocation2,columnsFileinDatabase=columnsFileinDatabase2,datafillName=datafillName, DatabaseName = DatabaseName, DatabaseNameBACKUP= DatabaseNameBACKUP)

        # print("file of image type and all its cached values were deleted")

    
    DeleteInDatabase(FilesInDatabaseLocation= FilesInDatabaseLocation,columnsFileinDatabase= columnsFileinDatabase,datafillName= datafillName, DatabaseName = DatabaseName, DatabaseNameBACKUP= DatabaseNameBACKUP)
    

    # print("DONE file Deletion")
    



def DeleteInDatabase(FilesInDatabaseLocation,columnsFileinDatabase,datafillName,DatabaseName, DatabaseNameBACKUP):
    
    databaseUsed0=readSqlDatabase.readSqlDatabase(table_name=FilesInDatabaseLocation,columns=columnsFileinDatabase)
    databaseUsed=databaseUsed0[0]

    # databaseUsed=databaseUsed[~(databaseUsed[columnsFileinDatabase[0]]==datafillName)]

    databaseUsed=databaseUsed[~(databaseUsed[columnsFileinDatabase[1]]==datafillName)]

    pandas.DataFrame.reset_index(databaseUsed, inplace=True)
    databaseUsed=databaseUsed[columnsFileinDatabase]
    # print(databaseUsed)

    
    writeToSqlite.writeToSqlite(frame=databaseUsed,table_name=FilesInDatabaseLocation,DatabaseName = DatabaseName, DatabaseNameBACKUP= DatabaseNameBACKUP)






DeleteFromDataFillName()





