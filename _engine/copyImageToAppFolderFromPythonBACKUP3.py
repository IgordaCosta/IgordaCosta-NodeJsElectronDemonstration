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

    
    



    LocationToAddFileOnApp0 = TableDataGotten['LocationToAddFileOnApp']


    LocationToPlaceOnWebPage0 = TableDataGotten['LocationToPlaceOnWebPage']

    try:
        LocationNameOnly = TableDataGotten['LocationNameOnly']
    
    except:
         LocationNameOnly = TableDataGotten['fileNameOnly']


    print(LocationToAddFileOnApp0)
    print(LocationToPlaceOnWebPage0)
    


    FileEnding = base93Characterconversion.base93Characterconversion()

    
    LocationToAddFileOnApp = ReplaceEndingFunction(TextToChange=LocationToAddFileOnApp0, FileEnding=FileEnding, OriginalFileName=LocationNameOnly)

    LocationToPlaceOnWebPage = ReplaceEndingFunction(TextToChange=LocationToPlaceOnWebPage0, FileEnding=FileEnding, OriginalFileName=LocationNameOnly)


    
    # LocationToAddFileOnApp = '_'.join(('.'.join(str(LocationToAddFileOnApp0).split('.')[:-1])).split('_')[:-1]) + '_' + FileEnding + '.'+ str(LocationToAddFileOnApp0).split('.')[-1]


    # LocationToPlaceOnWebPage = '_'.join(('.'.join(str(LocationToPlaceOnWebPage0).split('.')[:-1])).split('_')[:-1]) + '_' + FileEnding + '.'+ str(LocationToPlaceOnWebPage0).split('.')[-1]

    dataList = [LocationToAddFileOnApp, LocationToPlaceOnWebPage]

    dataNameList = ['LocationToAddFileOnApp', 'LocationToPlaceOnWebPage']


    # getTableData.WriteDataDatabase(data=data,dataName=dataName)

    getTableData.MultipleListWriteDataDatabase(dataList=dataList,dataNameList=dataNameList)

    print(LocationToAddFileOnApp)
    

    LocationToDeleteFIles = '\\'.join(LocationToAddFileOnApp.replace('/','\\').split('\\')[:-1]) + '\\'

    print(LocationToDeleteFIles)

    

    # DeleteAllFilesInFolder.DeleteAllFilesInFolder(LocationToDeleteFIles=LocationToDeleteFIles)



    if JustSwitchEnding:
        newFileLocation2 = LocationToAddFileOnApp0
    else:
        DeleteAllFilesInFolder.DeleteAllFilesInFolder(LocationToDeleteFIles=LocationToDeleteFIles)
        newFileLocation2 = newFileLocation


    CopiedFile = CopiedFileFunction(newFileLocation2,LocationToAddFileOnApp)


    if JustSwitchEnding:
        try:
            os.remove(LocationToAddFileOnApp0)  
        except:
            pass

    if CopiedFile==False:

        try:
            os.remove(LocationToAddFileOnApp)  
        except:
            pass
        try:           
            CopiedFile = CopiedFileFunction(newFileLocation2,LocationToAddFileOnApp)
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

    # print(OriginalFileName)

    # print('OriginalFileName')

    # print(TextToChange)

    # print('TextToChange')
        
    checkUsed = part1 = '\\'.join(TextToChange.replace('/', '\\').split('\\')[:-1])

    part21 = (TextToChange.replace('/', '\\').split('\\')[-1])

    # print(part21)

    part2 = ''
    if part21 == OriginalFileName:
        part23 = part21
    else:
        part23 = '_'.join(part21.split("_")[:-1])
    
    try:
        part2 =  part23.split('.')[:-1][0]
        
    except:
        part2 = part23

    # print(part2)
    part3 = '.' + TextToChange.split('.')[-1]
    # print(3)
    partfull= part1 + '\\' + part2 +  '_' + FileEnding  + part3

    return partfull




copyImageToAppFolderFromPython()   #### delete after test
