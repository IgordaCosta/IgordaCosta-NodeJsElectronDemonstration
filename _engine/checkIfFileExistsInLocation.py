import os.path

import FixExcelExtension

import getTableData



def checkIfFileExistsInLocation(folder,file):

    # folder=getTableData.GetDataFromDatabase(dataName='')

    # file=getTableData.GetDataFromDatabase(dataName='')

    file=FixExcelExtension.FixExcelExtension(fileName=file)

    finalPath=os.path.join(folder,file)

    FileExists=os.path.exists(finalPath)

    print(FileExists)

    return FileExists










