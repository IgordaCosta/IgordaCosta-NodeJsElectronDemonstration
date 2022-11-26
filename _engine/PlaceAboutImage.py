import PutListDataIntoImageWithFontSizeFunction
import getTableData
from importedDataPyimageFolderLocation import *




data = imageFolderLocation


print(data)
dataName = 'imageFolderLocation'

getTableData.WriteDataDatabase(data=data, dataName=dataName)



PutListDataIntoImageWithFontSizeFunction.PutListDataIntoImage(DataInputOption = False)