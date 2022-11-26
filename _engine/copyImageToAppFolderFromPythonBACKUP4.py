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


def copyImageToAppFolderFromPython(JustSwitchEnding = False):
    LocationToAddFileOnApp = copyImageToAppFolder(JustSwitchEnding = JustSwitchEnding)
    
    # LocationToAddFileOnApp = RemoveExtraSlashes.RemoveExtraSlashes(LocationToAddFileOnApp0)
    
    return LocationToAddFileOnApp




# def copyImageToAppFolder(JustSwitchEnding = False):

#     FileEnding = base93Characterconversion.base93Characterconversion()


def copyImageToAppFolder(JustSwitchEnding = False):

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
    



    LocationToAddFileOnApp0 = TableDataGotten['LocationToAddFileOnApp']


    LocationToPlaceOnWebPage0 = TableDataGotten['LocationToPlaceOnWebPage']

    # LocationNameOnly = TableDataGotten['LocationNameOnly']
    try:
        LocationNameOnly = TableDataGotten['fileNameOnly']
    except :
        LocationNameOnly = TableDataGotten['LocationNameOnly']

    print(LocationToAddFileOnApp0)
    print('LocationToAddFileOnApp0')
    print(LocationToPlaceOnWebPage0)

    print('LocationToPlaceOnWebPage0')
    


    

    
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

    

    # # # # DeleteAllFilesInFolder.DeleteAllFilesInFolder(LocationToDeleteFIles=LocationToDeleteFIles)


    # print(LocationToDeleteFIles)

    if JustSwitchEnding:
        newFileLocation2 = LocationToAddFileOnApp0
    else:
        DeleteAllFilesInFolder.DeleteAllFilesInFolder(LocationToDeleteFIles=LocationToDeleteFIles)
        newFileLocation2 = newFileLocation

    # newFileLocation2 = newFileLocation
    # print(newFileLocation2)

    # print('newFileLocation2')
    # print(LocationToAddFileOnApp)

    # print('LocationToAddFileOnApp')
    # print('CopiedFileFunction')
    # CopiedFile = CopiedFileFunction(newFileLocation2,LocationToAddFileOnApp)

    currentWorkingDirectory = FilePathFromPython.FilePathFromPython() + '\\'

    # if JustSwitchEnding:

    #     try:
    #         LocationToDeleteFIles = currentWorkingDirectory + '\\' + imageFolderLocation + '\\'
    #         DeleteAllFilesInFolder.DeleteAllFilesInFolder(LocationToDeleteFIles=LocationToDeleteFIles)
    #         # os.remove(LocationToAddFileOnApp0)  
    #         # os.remove(LocationToCopyFile)

    #     except:
    #         pass

    

#     # LocationToCopyFile = LocationToPlaceOnWebPage     #This works best for AddToDatabase Option

#     LocationToCopyFile = LocationToAddFileOnApp   #This option is for ViewDados , this is the whole location

#     CopiedFile = CopiedFileFunction(newFileLocation = newFileLocation2,LocationToCopyFile = LocationToCopyFile)


#     # if JustSwitchEnding:
#     #     try:
#     #         DeleteAllFilesInFolder.DeleteAllFilesInFolder()
#     #         # os.remove(LocationToAddFileOnApp0)  
#     #         # os.remove(LocationToCopyFile)
#     #     except:
#     #         pass

#     if CopiedFile==False:

#         try:
#             LocationToDeleteFIles = currentWorkingDirectory + '\\' + imageFolderLocation + '\\'
#             DeleteAllFilesInFolder.DeleteAllFilesInFolder(LocationToDeleteFIles=LocationToDeleteFIles)

#             # os.remove(LocationToAddFileOnApp)  
#             # os.remove(LocationToCopyFile)
            
#         except:
#             pass
#         try:           
#             # CopiedFile = CopiedFileFunction(newFileLocation2,LocationToAddFileOnApp)
#             CopiedFile = CopiedFileFunction(newFileLocation2,LocationToCopyFile)
#             CopiedFile = True
#         except:
#             pass

#     # return LocationToAddFileOnApp
#     return LocationToCopyFile


# def CopiedFileFunction(newFileLocation,LocationToCopyFile):

#     LocationToAddFileOnApp = LocationToCopyFile

#     print(newFileLocation)
#     print('source location')

#     print(LocationToAddFileOnApp)

#     print('destination location')

#     CopiedFile=False
#     try:
#         DoneCopyLocation=shutil.copy(newFileLocation, LocationToAddFileOnApp)
#         CopiedFile=True
#     except:
#         pass
    
#     return CopiedFile




# def ReplaceEndingFunction(TextToChange, FileEnding, OriginalFileName):

#     # print(OriginalFileName)

#     # print('OriginalFileName')

#     # print(TextToChange)

#     # print('TextToChange')
        
#     checkUsed = part1 = '\\'.join(TextToChange.replace('/', '\\').split('\\')[:-1])

#     part21 = (TextToChange.replace('/', '\\').split('\\')[-1])

#     # print(part21)

#     part2 = ''
#     if part21 == OriginalFileName:
#         part23 = part21
#     else:
#         part23 = '_'.join(part21.split("_")[:-1])
    
#     try:
#         part2 =  part23.split('.')[:-1][0]
        
#     except:
#         part2 = part23

#     # print(part2)
#     part3 = '.' + TextToChange.split('.')[-1]
#     # print(3)
#     partfull= part1 + '\\' + part2 +  '_' + FileEnding  + part3

#     return partfull




# copyImageToAppFolderFromPython(JustSwitchEnding = True)   #### block this after test
