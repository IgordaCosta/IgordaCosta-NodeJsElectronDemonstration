import shutil
import os

import getTableData




def copyImageToAppFolderFromPython():

    TableDataGotten = getTableData.GetTableData()


    LocationToAddFileOnApp = TableDataGotten['LocationToAddFileOnApp']


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


    print(newFileLocation)

    print('newFileLocation above')

    print(LocationToAddFileOnApp )

    print('LocationToAddFileOnApp above' )


    CopiedFile = CopiedFileFunction(newFileLocation,LocationToAddFileOnApp)


    print(CopiedFile)


    if CopiedFile==False:

        try:
            os.remove(LocationToAddFileOnApp)             
            CopiedFile = CopiedFileFunction(newFileLocation,LocationToAddFileOnApp)
            

        except:
            print("FileOpened")

        print(CopiedFile)





def CopiedFileFunction(newFileLocation,LocationToAddFileOnApp):

    CopiedFile=False
    try:
        DoneCopyLocation=shutil.copy(newFileLocation, LocationToAddFileOnApp)
       

        print(DoneCopyLocation)
        CopiedFile=True
    except:
        print("exeption ran")

        print(LocationToAddFileOnApp)

    
    return CopiedFile










# copyImageToAppFolderFromPython()   #### delete after test
