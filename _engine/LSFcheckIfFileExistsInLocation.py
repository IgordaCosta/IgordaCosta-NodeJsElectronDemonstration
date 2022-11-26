import os.path

import FixExcelExtension
import PrintTexListSerial
import getTableData



def LSFcheckIfFileExistsInLocation():

    # folder=getTableData.GetDataFromDatabase(dataName='FolderSaveLocation')

    # file=getTableData.GetDataFromDatabase(dataName='SavedFileName')

    dictValue=getTableData.GetTableData()

    # print(dictValue)

    folder=dictValue['FolderSaveLocation']

    file=dictValue['SavedFileName']


    file=FixExcelExtension.FixExcelExtension(fileName=file)

    finalPath=os.path.join(folder,file)

    FileExists=os.path.exists(finalPath)


    ListToPrint = []

    # print(FileExists)

    ListToPrint.append(FileExists)
    PrintTexListSerial.PrintTexListSerial(ListToPrint = ListToPrint)

    return FileExists



LSFcheckIfFileExistsInLocation()







