import shutil
import os

from importedDataPyimageFolderLocation import *
import getTableData
# import getUniqueAddFileEnd
import DeleteAllFilesInFolder
import base93Characterconversion
import FilePathFromPython

# import RemoveExtraSlashes

import pprint


def copyImageToTempFolderFromPython(JustSwitchEnding = False, FromBase=False):
    LocationToAddFileOnApp = copyImageToTempFolder(JustSwitchEnding = JustSwitchEnding, FromBase= FromBase)
    
    # LocationToAddFileOnApp = RemoveExtraSlashes.RemoveExtraSlashes(LocationToAddFileOnApp0)
    
    return LocationToAddFileOnApp




# def copyImageToAppFolder(JustSwitchEnding = False):

#     FileEnding = base93Characterconversion.base93Characterconversion()


def copyImageToTempFolder(JustSwitchEnding = False, FromBase = False):

    FileEnding = base93Characterconversion.base93Characterconversion(TimeBased=True, OtherNumer='',OnlyUpper=False)

    TableDataGotten = getTableData.GetTableData()
    
    PDFfile = TableDataGotten['PDFfile']

    if PDFfile == 'true':

        newFileLocation = TableDataGotten['newFileLocationImg']
        pass
    elif PDFfile =='false':
        # try:
        newFileLocation = TableDataGotten['newFileLocation']
        # pass
    else:

        newFileLocation = 'Error on true or false values acepted'
        pass

    
    print(newFileLocation)

    print('newFileLocation')
    



    LocationToAddFileOnApp = TableDataGotten['LocationToAddFileOnApp']


    LocationToPlaceOnWebPage = TableDataGotten['LocationToPlaceOnWebPage']

    # LocationNameOnly = TableDataGotten['LocationNameOnly']
    try:
        LocationNameOnly = TableDataGotten['fileNameOnly']
    except :
        LocationNameOnly = TableDataGotten['LocationNameOnly']

  
    
    # LocationToAddFileOnApp = '_'.join(('.'.join(str(LocationToAddFileOnApp0).split('.')[:-1])).split('_')[:-1]) + '_' + FileEnding + '.'+ str(LocationToAddFileOnApp0).split('.')[-1]


    # LocationToPlaceOnWebPage = '_'.join(('.'.join(str(LocationToPlaceOnWebPage0).split('.')[:-1])).split('_')[:-1]) + '_' + FileEnding + '.'+ str(LocationToPlaceOnWebPage0).split('.')[-1]

    dataList = [LocationToAddFileOnApp, LocationToPlaceOnWebPage]

    dataNameList = ['LocationToAddFileOnApp', 'LocationToPlaceOnWebPage']


    # getTableData.WriteDataDatabase(data=data,dataName=dataName)

    getTableData.MultipleListWriteDataDatabase(dataList=dataList,dataNameList=dataNameList)

   
    currentWorkingDirectory = FilePathFromPython.FilePathFromPython() + '\\'

    if  FromBase == False: 

        newFileLocation2 = LocationToAddFileOnApp #switched here

        LocationToCopyFile = newFileLocation #switched here the location to copy is in the newfileLocation
    
    else:
        NewLocation = '\\'.join(LocationToAddFileOnApp.replace('/', '\\').split('\\')[:-2])
 
        FileName = LocationToAddFileOnApp.replace('/','\\').split('\\')[-1]
       
        BlankPageLocation = NewLocation + '\\' + FileName

        newFileLocation2 = BlankPageLocation #switched here

        LocationToCopyFile = newFileLocation #switched here the location to copy is in the newfileLocation



    CopiedFile = CopiedFileFunction(newFileLocation = newFileLocation2,LocationToCopyFile = LocationToCopyFile)


    # if JustSwitchEnding:
    #     try:
    #         DeleteAllFilesInFolder.DeleteAllFilesInFolder()
    #         # os.remove(LocationToAddFileOnApp0)  
    #         # os.remove(LocationToCopyFile)
    #     except:
    #         pass

    if CopiedFile==False:

        try:
            LocationToDeleteFIles = currentWorkingDirectory + '\\' + imageFolderLocation + '\\'
            DeleteAllFilesInFolder.DeleteAllFilesInFolder(LocationToDeleteFIles=LocationToDeleteFIles)

            # os.remove(LocationToAddFileOnApp)  
            # os.remove(LocationToCopyFile)
            
        except:
            pass
        try:           
            # CopiedFile = CopiedFileFunction(newFileLocation2,LocationToAddFileOnApp)
            CopiedFile = CopiedFileFunction(newFileLocation2,LocationToCopyFile)
            CopiedFile = True
        except:
            pass

    # return LocationToAddFileOnApp
    return LocationToCopyFile


def CopiedFileFunction(newFileLocation,LocationToCopyFile):

    LocationToAddFileOnApp = LocationToCopyFile

    print(newFileLocation)
    print('source location')

    print(LocationToAddFileOnApp)

    print('destination location')

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


