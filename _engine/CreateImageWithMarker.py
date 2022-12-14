from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import os
import pathlib

import getTableData
import copyImageToAppFolderFromPython
import MultiplyTextSizeByImageHeight
import resizeImage


def CreateImageWithMarker():


    TableGotten = getTableData.GetTableData()

    OriginalImageLocation00 = TableGotten['LocationToAddFileOnApp']

    ImageRemoved=False
    try:
        os.remove(OriginalImageLocation00)
        ImageRemoved=True
    except:
        pass

    ## if ImageRemoved:      # not needed since a new file name will be used
    OriginalImageLocation0 = copyImageToAppFolderFromPython.copyImageToAppFolderFromPython()

    newFileLocation=OriginalImageLocation0

    ImgPosition=TableGotten['ImgPosition']

    ImgPositionAsList=ImgPosition.split(',')

    x = int(ImgPositionAsList[0])

    y = int(ImgPositionAsList[1])

    TextToPut = ".XXXXXXX."


    try:
        img = Image.open(OriginalImageLocation0)
    
    except:
        resizeImage.resizeImage(InputLocation=OriginalImageLocation0, SaveLocation=OriginalImageLocation0)
        img = Image.open(OriginalImageLocation0)

        
    draw = ImageDraw.Draw(img)

    homedir = pathlib.Path.home()

    homeanchor = homedir.anchor

    WindowsFontsLocation= homeanchor + 'Windows\\Fonts\\'

    DefaultFontLocation = WindowsFontsLocation + "Arial\\arial.ttf"

    Location = OriginalImageLocation0

    multVariable = MultiplyTextSizeByImageHeight.MultiplyTextSizeByImageHeight(Location=Location)

    font = ImageFont.truetype(DefaultFontLocation , int(multVariable * 30))

    textWidth, textHeight = draw.textsize(TextToPut, font)

    draw.text((x, y-textHeight),".XXXXXXX.",(0,0,0),font=font)
    img.save(OriginalImageLocation0)

    lastTempLocationPointX= x

    lastTempLocationPointY= y

    data=[lastTempLocationPointX, lastTempLocationPointY]

    dataName= ['lastTempLocationPointX', 'lastTempLocationPointY']

    getTableData.MultipleListWriteDataDatabase(dataList=data,dataNameList=dataName)










CreateImageWithMarker()
