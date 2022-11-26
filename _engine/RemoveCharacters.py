import re

import getTableData
import PrintTexListSerial


dataName = 'AddToTablevaluesList'

AddToTablevaluesList1 = getTableData.GetDataFromDatabase(dataName=dataName)         ##unblock this after testing



ListToPrint = []




#AddToTablevaluesList1 = "['first', '  the second', ' this is third', 'this is the      fourth', 'this is the     fifth', 'this is the    sixth', 'this is the  seventh', 'this is the eigth    ', 'this is the nineth   ', 'this is the tenght  ', 'this is the eleventh     ' ]"       # block this after testing




AddToTablevaluesList000 = re.sub("[^A-Za-z0-9,\s]","",AddToTablevaluesList1)


# AddToTablevaluesList001 = AddToTablevaluesList000.replace('  ', ' ')


# AddToTablevaluesList00 = AddToTablevaluesList001.replace('\n', '')



spaceReplaceData = '$%3&*&'


AddToTablevaluesList0001 = ' '.join(str(AddToTablevaluesList000).split())
AddToTablevaluesList = AddToTablevaluesList0001.replace('[','').replace(']','').replace('"','').replace("'",'').replace(", ",',').replace(" ,",',').replace(' ', spaceReplaceData)


# AddToTablevaluesList = AddToTablevaluesList00.replace(' ', '$%3&*&')

# print(AddToTablevaluesList)


SplitAddToTablevaluesList = AddToTablevaluesList.split(',')

# print(SplitAddToTablevaluesList)

MissingValues = False
for i in SplitAddToTablevaluesList:
    if len(i) == 0:
        MissingValues = True


# print(AddToTablevaluesList)

if MissingValues:
    pass

else:
    data = AddToTablevaluesList
    

    getTableData.WriteDataDatabase(data=data, dataName=dataName)



# print(MissingValues)


ListToPrint.append(MissingValues)


PrintTexListSerial.PrintTexListSerial(ListToPrint=ListToPrint)
