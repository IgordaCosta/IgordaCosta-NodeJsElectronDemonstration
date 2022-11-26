import getTableData



def TestIfTableValueExists(ValueToCheck,TableName='',ErrorIfNotFound=False):
    
    
    dictValue=getTableData.GetTableData(TableName='qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq',ErrorIfNotFound=True)

    # print(dictValue)

    try:
        
        dictValue[ValueToCheck]
        # print("the value exists")
        return True

    except KeyError:

        # print("the value doese not exist")

        return False




# ItExistsHere=TestIfTableValueExists(ValueToCheck='datafillName')


# print(ItExistsHere)

# print('ItExistsHere above')