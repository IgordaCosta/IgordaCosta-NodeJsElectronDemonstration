import getTableData



TableGotten = getTableData.GetTableData()

fileLocation = TableGotten['fileLocation']


# print(fileLocation)


fileNameOnly  = fileLocation.split('\\')[-1]

# print(fileNameOnly)


FolderSaveLocation  = '\\'.join(fileLocation.split('\\')[:-1]) + '\\'


dataNameList = ['fileNameOnly', 'FolderSaveLocation']


dataList = [fileNameOnly , FolderSaveLocation]



getTableData.MultipleListWriteDataDatabase(dataList=dataList,dataNameList=dataNameList)