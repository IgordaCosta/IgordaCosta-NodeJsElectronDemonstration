import getTableData

import readSqlDatabase





def getDatafillName():

    dataName='datafillName'

    datafillName=getTableData.GetDataFromDatabase(dataName=dataName)


    OriTable="FilesInDatabase"

    columnsFileinDatabase=['Job Name', 'File KEY', 'File Saved Location']

    FilesInDatabase , FileExists = readSqlDatabase.readSqlDatabase(table_name=OriTable,columns=columnsFileinDatabase)


    

    # print(FilesInDatabase)

    # print('FilesInDatabase above')

    


    database=FilesInDatabase

    ItemSingularToCompare=datafillName

    columnsFileinDatabase=['Job Name', 'File KEY', 'File Saved Location']


    itemToCompareFromTable=columnsFileinDatabase[0]

    ColumnToGetItem=columnsFileinDatabase[2]


    returnedValue=getItemFromSameLineDb(itemToCompareFromTable,ItemSingularToCompare, ColumnToGetItem,database)


    return returnedValue



def getItemFromSameLineDb(itemToCompareFromTable,ItemSingularToCompare, ColumnToGetItem,database):


    
    # print(database)

    # print('database')


    jobNameColumn=database[itemToCompareFromTable]

    # print(jobNameColumn)

    # print('jobNameColumn above')

    JobNameSameLocation=jobNameColumn==ItemSingularToCompare

    # print(JobNameSameLocation)

    # print('JobNameSameLocation above')

    FilesaveLocation=database[ColumnToGetItem]

    # print(FilesaveLocation)

    # print('FilesaveLocation above')

    FilesaveLocationForsame=FilesaveLocation[JobNameSameLocation]

    FilesaveLocationForsame0=FilesaveLocation[JobNameSameLocation]

    

    # print(FilesaveLocationForsame0)

    FilesaveLocationForsame = list(FilesaveLocationForsame0)[0]

    # print(FilesaveLocationForsame)

    # print('FilesaveLocationForsame above')

    return FilesaveLocationForsame







# returnedValue=getDatafillName()



# print(returnedValue)

# print('returnedValue is above')



# print(getDatafillName())     # block after testing