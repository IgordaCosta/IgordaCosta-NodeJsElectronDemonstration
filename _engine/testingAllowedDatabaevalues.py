import getTableData 


TableName = 'AB78CDC2'

DictionaryAdd = {'checkedNumber': '1', 'datafillName': 'test$%78&*&b$%78&*&space2', 'dbPath': 'C:\\Users\\Tigereye\\Desktop\\Apps\\CSSAutoFormFiller2\\CSSAutoFormFiller\\js\\AutoFormFiller.db', 'typeOfButton': 'GJD', 'currentWorkingDirectory': 'C:\\Users\\Tigereye\\Desktop\\Apps\\CSSAutoFormFiller2\\CSSAutoFormFiller'}

getTableData.MultipleDictionaryWriteDataDatabase(DictionaryAdd,TableName=TableName)



print(getTableData.GetTableData(TableName=TableName))
