import os

import getTableData
import PrintTexListSerial





def CheckIfFileChanged(Newstamp):

    ListToPrint = []

    oldStamp=GetDataFromDatabase(dataName='oldStamp')

    # print(oldStamp,'oldStamp')

    # print(Newstamp,'Newstamp')

    # Newstamp=GetDataFromDatabase(dataName='Newstamp')

    if str(Newstamp) == str(oldStamp):
        # print("NOTchanged")
        ListToPrint.append('NOTchanged')
    else:
        # print("FileChanged")
        ListToPrint.append('FileChanged')

    
    PrintTexListSerial.PrintTexListSerial(ListToPrint = ListToPrint)



def GetDataFromDatabase(dataName):
    dictValue=getTableData.GetTableData()

    data=dictValue[dataName]

    return data


# CheckIfFileChanged()


    


    
