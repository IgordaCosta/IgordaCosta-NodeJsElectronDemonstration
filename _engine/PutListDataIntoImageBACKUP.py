import cv2
import re
import shutil
import os
import time
from PIL import Image
from PIL import ImageDraw 
from PIL import ImageFont
import pathlib

# from PIL import ImageFont
# from io import BytesIO

import getTableData
import copyImageToAppFolderFromPython
import StringListIntoList
import MultiplyTextSizeByImageHeight


def PutListDataIntoImage(finalLocationsX, finalLocationsY):



    # print(os.getcwd())

    # currentWorkingDirectory=os.getcwd()

    TableGotten = getTableData.GetTableData()

    OriginalImageLocation0=TableGotten['LocationToAddFileOnApp']

    # OriginalImageLocation1=OriginalImageLocation0.replace("/",'\\')

    # OriginalImageLocation='.\\' + OriginalImageLocation1

    # fileExtension=OriginalImageLocation.split('.')[-1]

    # print('fileExtension =',fileExtension)

    # NewImageLocation=OriginalImageLocation.replace('.'+fileExtension,'')

    # print('NewImageLocation =',NewImageLocation)

    # print('OriginalImageLocation =',OriginalImageLocation)

    # # # './_clientImageFiles/TestImageFile_temp.jpg'

    # newFileLocation = NewImageLocation + '_temp.'+fileExtension

    # newFileLocation0=OriginalImageLocation



    ImageRemoved=False
    try:
        os.remove(OriginalImageLocation0)
        ImageRemoved=True
    except:
        # print("Error while deleting file ", OriginalImageLocation0)
        pass

    

    copyImageToAppFolderFromPython.copyImageToAppFolderFromPython()





    # finalLocationsX = TableGotten['finalLocationsX']

    # finalLocationsY = TableGotten['finalLocationsY']

    # print(finalLocationsX)

    # print('finalLocationsX')

    # print(finalLocationsY)

    # print('finalLocationsY')

    # finalLocationsXList=finalLocationsX.replace("'",'').replace('[','').replace(']','').split(',')

    # finalLocationsYList=finalLocationsY.replace("'",'').replace('[','').replace(']','').split(',')



    finalLocationsXList= finalLocationsX

    finalLocationsYList=finalLocationsY




    # print(finalLocationsXList)

    # print('finalLocationsXList')

    # print(finalLocationsYList)

    # print('finalLocationsYList')

    TextToPut = ".XXXXXXX."

    
    # img = Image.open(currentWorkingDirectory+"\\"+newFileLocation0)
    img = Image.open(OriginalImageLocation0)
    draw = ImageDraw.Draw(img)


    homedir = pathlib.Path.home()

    homeanchor = homedir.anchor

    WindowsFontsLocation= homeanchor + 'Windows\\Fonts\\'

    #"C://Windows//Fonts//Arial//arial.ttf"

    DefaultFontLocation = WindowsFontsLocation + "Arial\\arial.ttf"




    # font = ImageFont.truetype(<font-file>, <font-size>)
    # font = ImageFont.truetype("C://Windows//Fonts//Arial//arial.ttf", 30)


    Location = OriginalImageLocation0


    multVariable = MultiplyTextSizeByImageHeight.MultiplyTextSizeByImageHeight(Location=Location)

    font = ImageFont.truetype(DefaultFontLocation , int(multVariable * 30))



    # font = ImageFont.truetype(DefaultFontLocation, 30)

    textWidth, textHeight = draw.textsize(TextToPut, font)

    # lastTempLocationPointY= y-textHeight

    # print(finalLocationsXList)

    # print(finalLocationsXList[0])

    # finalLocationsXList2 = finalLocationsXList[0]
    try:
        finalLocationsXList = StringListIntoList.StringListIntoList(StringList=finalLocationsXList)
        finalLocationsYList = StringListIntoList.StringListIntoList(StringList=finalLocationsYList)
    except:
        pass

    # print(finalLocationsXList)
    
    # print(type(finalLocationsXList))

    # print('finalLocationsXList after')

    # print(finalLocationsYList)

    # print(type(finalLocationsYList))

    # print('finalLocationsYList after')
    # j = 0

    finalLocationsXList0 = []
    finalLocationsYList0 = []

    for i in range(len(finalLocationsXList)):
        # draw.text((x, y),"Sample Text",(r,g,b))
        # print(i)
        # print(finalLocationsXList[i])
        if finalLocationsXList[i] == '':
            # del finalLocationsXList[j]
            # del finalLocationsYList[j]
            pass


        else:
            draw.text((int(finalLocationsXList[i]), int(finalLocationsYList[i]) - textHeight ),TextToPut,(0,0,0),font=font)
            finalLocationsYList0.append(finalLocationsYList[i])
            finalLocationsXList0.append(finalLocationsXList[i])
            # j=j+1
            


    finalLocationsYList = finalLocationsYList0
    finalLocationsXList = finalLocationsXList0
    
    img.save(OriginalImageLocation0)



    FontSize=30

    # data=FontSize

    # dataName='FontSize'

    dataList = [FontSize, finalLocationsXList, finalLocationsYList ]

    dataNameList = ['FontSize', 'finalLocationsX', 'finalLocationsY' ]



    # getTableData.WriteDataDatabase(data=data,dataName=dataName)

    getTableData.MultipleListWriteDataDatabase(dataList= dataList, dataNameList=dataNameList)

    # print("Done")


















# ########## block all bottom after tests

# TableGotten = getTableData.GetTableData()


# finalLocationsX = TableGotten['finalLocationsX']

# finalLocationsY = TableGotten['finalLocationsY']


# print(finalLocationsX)

# print('finalLocationsX')

# print(finalLocationsY)

# print('finalLocationsY')

# PutListDataIntoImage(finalLocationsX, finalLocationsY)

# ##### PutListDataIntoImage()    # unblock when done