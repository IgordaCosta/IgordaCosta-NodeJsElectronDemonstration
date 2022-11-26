import sys
# import base64

import getTableData
import StringToOrdList
import PrintTexListSerial





# stringOfChars = sys.argv[1]

# StringList = str(stringOfChars).replace("'",'').replace('"','').replace('[', '').replace(']', '').split(', ')

# TableName = StringList[0]

# Database = StringList[1]



TableName = ''

Database = ''

ListToPrint = []

Datalist, names = getTableData.GetTableDataFromTable(Database=Database,TableName=TableName, InPythonFunction=True)

# make ord list here from the data then when in javascript get the data and use it to code it back to string
# using the string to ord and python ord to string functions


# print(StringToOrdList.StringToOrdList(Datalist))

# print(StringToOrdList.StringToOrdList(names))


OrdListDatalist = StringToOrdList.StringToOrdList(Datalist)

OrdListnames = StringToOrdList.StringToOrdList(names)




ListToPrint.append(OrdListDatalist)

ListToPrint.append(OrdListnames)




PrintTexListSerial.PrintTexListSerial(ListToPrint=ListToPrint)




