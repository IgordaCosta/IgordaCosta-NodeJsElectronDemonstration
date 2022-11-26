import getTableData

import PrintTexListSerial


dataName = 'rw'

rw = getTableData.GetDataFromDatabase(dataName= dataName)
ListToPrint = []

if str(rw) == '0':
    ListToPrint.append('False')
    
else:
    ListToPrint.append('True')

PrintTexListSerial.PrintTexListSerial(ListToPrint = ListToPrint)