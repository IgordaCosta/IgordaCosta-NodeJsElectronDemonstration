import shutil
import os

import getTableData
# import getUniqueAddFileEnd
import DeleteAllFilesInFolder
import base93Characterconversion



def copyImageToAppFolderFromPython(JustSwitchEnding = False):
    LocationToAddFileOnApp = copyImageToAppFolder(JustSwitchEnding = JustSwitchEnding)

    return LocationToAddFileOnApp




def copyImageToAppFolder(JustSwitchEnding = False):

    TableDataGotten = getTableData.GetTableData()
    
    PDFfile = TableDataGotten['PDFfile']

    if PDFfile == 'true':

        newFileLocation = TableDataGotten['newFileLocationImg']
        pass
    elif PDFfile =='false':

        newFileLocation = TableDataGotten['newFileLocation']
        pass
    else:

        newFileLocation = 'Error on true or false values acepted'
        pass


    fileNameOnly = part1 = '\\'.join(newFileLocation.replace('/', '\\').split('\\')[:-1])

   


    LocationToAddFileOnApp0 = TableDataGotten['LocationToAddFileOnApp']


    LocationToPlaceOnWebPage0 = TableDataGotten['LocationToPlaceOnWebPage']

    


    FileEnding = base93Characterconversion.base93Characterconversion()

    # newFileLocation= TempFolderLocation + "\\temp_" + '.'.join(str(fileNameOnly).split('.')[:-1]) + '_' + FileEnding + '.'+ str(fileNameOnly).split('.')[-1]



    ReplaceEndingFunction(TextToChange=LocationToAddFileOnApp0, FileEnding=FileEnding, OriginalFileName=fileNameOnly)

    
    # LocationToAddFileOnApp = '_'.join(('.'.join(str(LocationToAddFileOnApp0).split('.')[:-1])).split('_')[:-1]) + '_' + FileEnding + '.'+ str(LocationToAddFileOnApp0).split('.')[-1]


    # LocationToPlaceOnWebPage = '_'.join(('.'.join(str(LocationToPlaceOnWebPage0).split('.')[:-1])).split('_')[:-1]) + '_' + FileEnding + '.'+ str(LocationToPlaceOnWebPage0).split('.')[-1]

    
    dataList = [LocationToAddFileOnApp, LocationToPlaceOnWebPage]

    dataNameList = ['LocationToAddFileOnApp', 'LocationToPlaceOnWebPage']


    # getTableData.WriteDataDatabase(data=data,dataName=dataName)

    getTableData.MultipleListWriteDataDatabase(dataList=dataList,dataNameList=dataNameList)
    

    LocationToDeleteFIles = '\\'.join(LocationToAddFileOnApp.replace('/','\\').split('\\')[:-1]) + '\\'



    

    DeleteAllFilesInFolder.DeleteAllFilesInFolder(LocationToDeleteFIles=LocationToDeleteFIles)




    

    CopiedFile = CopiedFileFunction(newFileLocation,LocationToAddFileOnApp)

    if CopiedFile==False:

        try:
            os.remove(LocationToAddFileOnApp)  
        except:
            pass
        try:           
            CopiedFile = CopiedFileFunction(newFileLocation,LocationToAddFileOnApp)
            CopiedFile = True
        except:
            pass

    return LocationToAddFileOnApp


def CopiedFileFunction(newFileLocation,LocationToAddFileOnApp):

    CopiedFile=False
    try:
        DoneCopyLocation=shutil.copy(newFileLocation, LocationToAddFileOnApp)
        CopiedFile=True
    except:
        pass
    
    return CopiedFile



def ReplaceEndingFunction(TextToChange, FileEnding, OriginalFileName):

        
    checkUsed = part1 = '\\'.join(TextToChange.replace('/', '\\').split('\\')[:-1])
     
    part21 = (TextToChange.replace('/', '\\').split('\\')[-1])
    
   
    part2 = ''
    if part21 == OriginalFileName:
        part23 = part21
    else:
        part23 = '_'.join(part21.split("_")[:-1])

    try:
        part2 =  part23.split('.')[:-1][0]
        
    except:
        part2 = part23


    part3 = '.' + TextToChange.split('.')[-1]

    partfull= part1 + '\\' + part2 +  '_' + FileEnding  + part3

    return partfull






# copyImageToAppFolderFromPython()   #### delete after test
