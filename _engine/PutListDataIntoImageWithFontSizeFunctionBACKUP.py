from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import os

# from PIL import ImageFont
# from io import BytesIO
import pandas

import getTableData
import GetFontFilePaths
import copyImageToAppFolderFromPython

import GetAllFontNamesFromFolderFunction


def PutListDataIntoImage(TextToPut = ".XXXXXXX.", DataInputOption = True):

    # print(os.getcwd())

    # currentWorkingDirectory=os.getcwd()



    TableGotten = getTableData.GetTableData()


    # print(TableGotten)


    


    if DataInputOption:

        systemFonts = TableGotten['systemFonts']

        finalLocationsX = TableGotten['finalLocationsX']

        finalLocationsY = TableGotten['finalLocationsY']

        OriginalImageLocation0=TableGotten['LocationToAddFileOnApp']

        FontSize0=TableGotten['newFontSize']

        FontSize=int(FontSize0)     ###### add this to old font size


        newFont=TableGotten['newFont'] ###### add this to old font

       






        # finalLocationsX = str(finalLocationsX).replace('[','').replace(']','').replace("'",'').replace('"','').split(',')

        # finalLocationsY = str(finalLocationsY).replace('[','').replace(']','').replace("'",'').replace('"','').split(',')



        print(finalLocationsX)

        print('finalLocationsX above')

        print(finalLocationsY)

        print('finalLocationsY above')


    else:

        systemFonts = GetAllFontNamesFromFolderFunction.GetAllFontNamesFromFolder()

        
        currentWorkingDirectory = TableGotten['currentWorkingDirectory']        

        print(currentWorkingDirectory)


        FilesInDatabaseTable = getTableData.GetTableDataFromTable(TableName='FilesInDatabase')

        FontAndItsSizeTable = getTableData.GetTableDataFromTable(TableName='FontAndItsSize')

        print(FilesInDatabaseTable[0])

        print('FilesInDatabaseTable above')

        print(FilesInDatabaseTable[1])

        FilesInDatabaseTableDf = pandas.DataFrame(FilesInDatabaseTable[0] , columns=FilesInDatabaseTable[1])

        print(FilesInDatabaseTableDf)

        # newFileLocation1



        imageFolderLocation='_clientImageFiles\\'


        datafillName = TableGotten['datafillName']

        print(datafillName)


        rowLoacation = FilesInDatabaseTableDf[FilesInDatabaseTableDf['Job Name']== datafillName]

        print(rowLoacation)

        print(rowLoacation['File Saved Location'].values[0])

        print("rowLoacation['File Saved Location']")

        newFileLocation1 = rowLoacation['File Saved Location'].values[0]

        LocationNameOnly = rowLoacation['File Saved Location'].values[0].split('\\')[-1]

        print(newFileLocation1)


        # LocationToPlaceOnWebPage=currentWorkingDirectory + '\\' + imageFolderLocation + LocationNameOnly

        LocationToPlaceOnWebPage= imageFolderLocation + LocationNameOnly

        print(LocationToPlaceOnWebPage)

        OriginalImageLocation0 = currentWorkingDirectory + '\\'  + LocationToPlaceOnWebPage

        SaveLocation = LocationToPlaceOnWebPage
        

        KeyFile = rowLoacation['File KEY'].values[0]
        print(KeyFile)


        KeyFileTable = getTableData.GetTableDataFromTable(TableName=KeyFile)

        print(KeyFileTable)


        print(FontAndItsSizeTable)

        FontAndItsSizeTableDf = pandas.DataFrame(FontAndItsSizeTable[0] , columns=FontAndItsSizeTable[1])

        print(FontAndItsSizeTableDf)

        rowLoacationTable2 = FontAndItsSizeTableDf[FontAndItsSizeTableDf['Job Name']== datafillName]

        # print(rowLoacationTable2)


        FontSize0 = rowLoacationTable2['FontSize'].values[0]

        print(FontSize0)

        FontSize=int(FontSize0) 


        newFont = rowLoacationTable2['FontName'].values[0]

        print(newFont)

        FromPdf = rowLoacationTable2['FromPdf'].values[0]

        print(FromPdf)





        print('======================')


        print(newFileLocation1)



        print(OriginalImageLocation0)


        print('=========================')


        print(newFileLocation1)




        dataList = [OriginalImageLocation0, 'false', newFileLocation1 ]

        
        dataNameList =['LocationToAddFileOnApp', 'PDFfile', 'newFileLocation']


        getTableData.MultipleListWriteDataDatabase(dataList=dataList,dataNameList=dataNameList)


        




    # print(newFont)

    # print('newFont above')


    # newFont='Times+New+Roman+Bold'   ### delete this after tests


    # print(FontSize)

    # print('FontSize above')

    # print(systemFonts)

    # print('systemFonts above')


    systemFontsList=systemFonts.split('|')


    # print(systemFontsList)


    # print('systemFontsList above')


    indexOfItemInListOfFonts=systemFontsList.index(newFont)

    print(indexOfItemInListOfFonts)



    fontFilePaths=GetFontFilePaths.GetFontFilePaths()

    # print(fontFilePaths)

    # print('fontFilePaths above')



    fontSelectedPath= fontFilePaths[indexOfItemInListOfFonts]


    # print(fontSelectedPath)

    # print('fontSelectedPath above')












    # OriginalImageLocation0=TableGotten['LocationToAddFileOnApp']

    # OriginalImageLocation1=OriginalImageLocation0.replace("/",'\\')

    # OriginalImageLocation='.\\' + OriginalImageLocation1



    # fileExtension=OriginalImageLocation.split('.')[-1]

    # print('fileExtension =',fileExtension)

    # NewImageLocation=OriginalImageLocation.replace('.'+fileExtension,'')

    # print('NewImageLocation =',NewImageLocation)

    # print('OriginalImageLocation =',OriginalImageLocation)

    # # './_clientImageFiles/TestImageFile_temp.jpg'





    # newFileLocation = NewImageLocation + '_temp.'+fileExtension

    # newFileLocation0=OriginalImageLocation



    # try:
    #     os.remove(newFileLocation)
    # except:
    #     print("Error while deleting file ", newFileLocation)

    ImageRemoved=False
    try:
        os.remove(OriginalImageLocation0)
        ImageRemoved=True
    except:
        print("Error while deleting file ", OriginalImageLocation0)

    
    cwd = os.getcwd()

    print(cwd)

    copyImageToAppFolderFromPython.copyImageToAppFolderFromPython()








    # finalLocationsX = TableGotten['finalLocationsX']

    # finalLocationsY = TableGotten['finalLocationsY']

    # print(finalLocationsX)

    # print('finalLocationsX')

    # print(finalLocationsY)

    # print('finalLocationsY')


    if DataInputOption:


        # finalLocationsX = str(finalLocationsX0).replace('[','').replace(']','').replace("'",'').split(',')

        # finalLocationsY = str(finalLocationsY0).replace('[','').replace(']','').replace("'",'').split(',')


        finalLocationsXList=finalLocationsX.replace('[','').replace(" ",'').replace(']','').replace("'",'').split(',')


        finalLocationsYList=finalLocationsY.replace('[','').replace(" ",'').replace(']','').replace("'",'').split(',')



    


    # print(finalLocationsXList)

    # print('finalLocationsXList')

    # print(finalLocationsYList)

    # print('finalLocationsYList')




    # TextToPut = ".XXXXXXX."

    
    # img = Image.open(currentWorkingDirectory+"\\"+newFileLocation0)
    img = Image.open(OriginalImageLocation0)
    draw = ImageDraw.Draw(img)

    # # font = ImageFont.truetype(<font-file>, <font-size>)
    # font = ImageFont.truetype("C://Windows//Fonts//Arial//arial.ttf", FontSize)

    font = ImageFont.truetype(fontSelectedPath, FontSize)

    textWidth, textHeight = draw.textsize(TextToPut, font)


    if DataInputOption:

        # for i in range(len(finalLocationsXList)):

        # j = 0
        for i in range(len(finalLocationsXList)):
            # draw.text((x, y),"Sample Text",(r,g,b))
            print(i)
            print(finalLocationsXList[i])
            if finalLocationsXList[i] == '':
                # del finalLocationsXList[j]
                # del finalLocationsYList[j]
                # # draw.text((x, y),"Sample Text",(r,g,b))
                pass
            
            else:
                draw.text((int(finalLocationsXList[i]), int(finalLocationsYList[i]) - textHeight ),TextToPut,(0,0,0),font=font)

                # draw.text((int(finalLocationsXList[j]), int(finalLocationsYList[j]) - textHeight ),TextToPut,(0,0,0),font=font)
                # j=j+1

    else:
    

        print(KeyFileTable)

        print('KeyFileTable above')

        # print(type(KeyFileTable[1]))

        print(KeyFileTable[0][0]) # this is the description list

        print(KeyFileTable[0][0][1]) # this is the first item in the description list

        print(len(KeyFileTable[0][0]))

        # print(KeyFileTable[1][1])


        data = LocationToPlaceOnWebPage

        dataName = 'LocationToPlaceOnWebPage'


        getTableData.WriteDataDatabase(data=data,dataName=dataName)



        # LocationToPlaceOnWebPage



        for j in range(len( KeyFileTable[0][0] ) - 1 ):
            # # draw.text((x, y),"Sample Text",(r,g,b))
            i = j + 1
            print((KeyFileTable[1][i]))

            # print(type((KeyFileTable[1][i])))
            ListValues = KeyFileTable[1][i].replace('[', '').replace(']', '').strip().split(',')


            print(ListValues[0])

            print(ListValues[1])


            print(KeyFileTable[0][0][i])


            TextToPut = KeyFileTable[0][0][i]



            draw.text((int(ListValues[1]), int(ListValues[0]) - textHeight ),TextToPut,(0,0,0),font=font)








    img.save(OriginalImageLocation0)
    

    # if DataInputOption:

    #     img.save(OriginalImageLocation0)

    #     pass

    # else:
        
    #     # img.save(SaveLocation)

    #     pass


    # FontSize=int(FontSize0)     ###### add this to old font size

    # newFont=TableGotten['newFont'] ###### add this to old font

    

    # let oldFont = TableGotten['oldFont']

    # let oldFontSize = TableGotten['FontSize']

    if DataInputOption:

        dataList= [newFont, FontSize, finalLocationsXList, finalLocationsYList ]
        dataNameList = ['oldFont', 'FontSize', 'finalLocationsXList', 'finalLocationsYList']

        getTableData.MultipleListWriteDataDatabase(dataList=dataList,dataNameList=dataNameList)


    print("Done")




















# PutListDataIntoImage(DataInputOption = False)     # block this after testing

# PutListDataIntoImage()     # block this after testing