import shutil
import os

import getTableData
import getUniqueAddFileEnd




def copyImageToAppFolder():

    TableDataGotten = getTableData.GetTableData()


    # newFileLocation = TableDataGotten['newFileLocation']



    
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








    LocationToAddFileOnApp = TableDataGotten['LocationToAddFileOnApp']

    # print(newFileLocation)

    # print('newFileLocation above')

    # print(LocationToAddFileOnApp )

    # print('LocationToAddFileOnApp above' )


    CopiedFile = CopiedFileFunction(newFileLocation,LocationToAddFileOnApp)


    # print(CopiedFile)


    if CopiedFile==False:

        try:
            os.remove(LocationToAddFileOnApp)  
        except:
            # print("FileOpened")
            pass
        try:           
            CopiedFile = CopiedFileFunction(newFileLocation,LocationToAddFileOnApp)
            CopiedFile = True
        except:
            # print("FileOpened")
            pass

        # if CopiedFile==False:

        #     #add time
        #     NotCopied = True
        #     while NotCopied:
        #         try:
        #             NewLocationToAddFileOnApp = LocationToAddFileOnApp + getUniqueAddFileEnd.getUniqueAddFileEnd()
        #             CopiedFile = CopiedFileFunction(newFileLocation,NewLocationToAddFileOnApp)
        #             NotCopied = False
        #         except:
        #             pass


        

        # print(CopiedFile)





def CopiedFileFunction(newFileLocation,LocationToAddFileOnApp):

    CopiedFile=False
    try:
        DoneCopyLocation=shutil.copy(newFileLocation, LocationToAddFileOnApp)
        # DoneCopyLocation=shutil.copy(LocationToAddFileOnApp, newFileLocation)

        # print(DoneCopyLocation)
        CopiedFile=True
    except:
        # print("exeption ran")

        # print(LocationToAddFileOnApp)
        # print(newFileLocation)
        pass
    
    return CopiedFile



copyImageToAppFolder()






