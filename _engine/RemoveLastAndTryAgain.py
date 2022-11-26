import getTableData





TableGotten = getTableData.GetTableData()

finalLocationsX0 = TableGotten['finalLocationsX']

finalLocationsY0 = TableGotten['finalLocationsY']



# finalLocationsX0 = "1a, 2a, 3a, 4a, 5a"

# finalLocationsY0 = "1b, 2b, 3b, 4b, 5b"




commaReplace = '%$%&*'

finalLocationsX1 = str(finalLocationsX0).replace(', ', commaReplace).replace(',', commaReplace).split(commaReplace)

finalLocationsY1 = str(finalLocationsY0).replace(', ', commaReplace).replace(',', commaReplace).split(commaReplace)


finalLocationsX2 = finalLocationsX1[:-1]

finalLocationsY2 = finalLocationsY1[:-1]


finalLocationsX = str(finalLocationsX2).replace('[','').replace(']','').replace('"','').replace("'",'')

finalLocationsY = str(finalLocationsY2).replace('[','').replace(']','').replace('"','').replace("'",'')


# print(finalLocationsX)

# print(finalLocationsY)

dataList = [finalLocationsX, finalLocationsY]

dataNameList = ['finalLocationsX', 'finalLocationsY']

getTableData.MultipleListWriteDataDatabase(dataList=dataList,dataNameList=dataNameList)