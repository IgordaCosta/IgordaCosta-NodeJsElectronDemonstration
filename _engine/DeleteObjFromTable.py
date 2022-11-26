import getTableData
import dropSqlTable




def DeleteObjFromTable(ObjectToDelete,TableName='qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq'):

    IsList=False
    # this checks if obj is list or not
    if type(ObjectToDelete) is list: 
        # print("your object is a list") 
        IsList=True
    else: 
        # print("your object is not a list") 
        pass

    ObjExists=False
    TableExists=False
    # this gets the table from database
    try:
        TableData = getTableData.GetTableData(TableName=TableName,ErrorIfNotFound=True)
        TableExists=True
    except:
        # print("Table does NOT Exist in Table")
        pass

    if TableExists:
        try:
            if IsList:
                for i in range(len(ObjectToDelete)):
                    ObjectToDeleteValue=TableData[ObjectToDelete[i]]
                ObjExists=True
            else:
                ObjectToDeleteValue=TableData[ObjectToDelete]
                ObjExists=True
        except:
            # print("One or more objects does NOT exist in table")
            pass

    if ObjExists:
        # print("Object Exists in Table")
        # print(ObjectToDeleteValue)

        # this deletes the key from the dictionary
        if IsList:
            for i in range(len(ObjectToDelete)):
                del TableData[ObjectToDelete[i]]
        else:
            del TableData[ObjectToDelete]

        # print(TableData)
        # this drops the table
        dropSqlTable.DropSqlTable(TableName=TableName)

        # this writes the new table
        getTableData.MultipleDictionaryWriteDataDatabase(DictionaryAdd=TableData, TableName=TableName)

        # print('Done')








# ObjectToDelete=['finalLocationsX','finalLocationsY']

# DeleteObjFromTable(ObjectToDelete,TableName='qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq')