from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import os

# from PIL import ImageFont
from io import BytesIO

import getTableData
import GetFontFilePaths
import copyImageToAppFolderFromPython


def PutListDataIntoImage():

    # print(os.getcwd())

    # currentWorkingDirectory=os.getcwd()



    TableGotten = getTableData.GetTableData()

    FontSize0=TableGotten['newFontSize']

    FontSize=int(FontSize0)     ###### add this to old font size


    newFont=TableGotten['newFont'] ###### add this to old font


    systemFonts = TableGotten['systemFonts']



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












    OriginalImageLocation0=TableGotten['LocationToAddFileOnApp']

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

    

    copyImageToAppFolderFromPython.copyImageToAppFolderFromPython()








    finalLocationsX = TableGotten['finalLocationsX']

    finalLocationsY = TableGotten['finalLocationsY']

    print(finalLocationsX)

    print('finalLocationsX')

    print(finalLocationsY)

    print('finalLocationsY')

    finalLocationsXList=finalLocationsX.split(',')

    finalLocationsYList=finalLocationsY.split(',')

    print(finalLocationsXList)

    print('finalLocationsXList')

    print(finalLocationsYList)

    print('finalLocationsYList')




    TextToPut = ".XXXXXXX."

    
    # img = Image.open(currentWorkingDirectory+"\\"+newFileLocation0)
    img = Image.open(OriginalImageLocation0)
    draw = ImageDraw.Draw(img)

    # # font = ImageFont.truetype(<font-file>, <font-size>)
    # font = ImageFont.truetype("C://Windows//Fonts//Arial//arial.ttf", FontSize)

    font = ImageFont.truetype(fontSelectedPath, FontSize)

    textWidth, textHeight = draw.textsize(TextToPut, font)



    for i in range(len(finalLocationsXList)):
        # # draw.text((x, y),"Sample Text",(r,g,b))
        draw.text((int(finalLocationsXList[i]), int(finalLocationsYList[i]) - textHeight ),TextToPut,(0,0,0),font=font)





    img.save(OriginalImageLocation0)


    # FontSize=int(FontSize0)     ###### add this to old font size

    # newFont=TableGotten['newFont'] ###### add this to old font

    

    # let oldFont = TableGotten['oldFont']

    # let oldFontSize = TableGotten['FontSize']


    dataList= [newFont, FontSize]


    dataNameList = ['oldFont', 'FontSize']




    getTableData.MultipleListWriteDataDatabase(dataList=dataList,dataNameList=dataNameList)


    print("Done")




















PutListDataIntoImage()