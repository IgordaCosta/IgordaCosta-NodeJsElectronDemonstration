from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import os

import getTableData
import GetFontFilePaths
import copyImageToAppFolderFromPython
import MultiplyTextSizeByImageHeight


def PutListDataIntoImage():

    currentWorkingDirectory=os.getcwd()

    TableGotten = getTableData.GetTableData()

    FontSize0=TableGotten['newFontSize']

    FontSize=int(FontSize0)     ###### add this to old font size


    newFont=TableGotten['newFont'] ###### add this to old font


    systemFonts = TableGotten['systemFonts']

    systemFontsList=systemFonts.split('|')

    indexOfItemInListOfFonts=systemFontsList.index(newFont)

    fontFilePaths=GetFontFilePaths.GetFontFilePaths()

    fontSelectedPath= fontFilePaths[indexOfItemInListOfFonts]

    OriginalImageLocation00=TableGotten['LocationToAddFileOnApp']

    ImageRemoved=False
    try:
        os.remove(OriginalImageLocation00)
        ImageRemoved=True
    except:
        pass

    OriginalImageLocation0 = copyImageToAppFolderFromPython.copyImageToAppFolderFromPython()

    finalLocationsX = TableGotten['finalLocationsX']

    finalLocationsY = TableGotten['finalLocationsY']

    finalLocationsXList=finalLocationsX.replace('[','').replace(" ",'').replace(']','').replace("'",'').split(',')

    finalLocationsYList=finalLocationsY.replace('[','').replace(" ",'').replace(']','').replace("'",'').split(',')

    img = Image.open(OriginalImageLocation0)

    draw = ImageDraw.Draw(img)

    Location = OriginalImageLocation0

    multVariable = MultiplyTextSizeByImageHeight.MultiplyTextSizeByImageHeight(Location=Location)

    font = ImageFont.truetype(fontSelectedPath , int(multVariable * FontSize))

    textWidth, textHeight = draw.textsize("5*", font)

    for i in range(len(finalLocationsXList)):
        draw.text((int(finalLocationsXList[i]), int(finalLocationsYList[i]) - textHeight ),str(i+1)+"*",(0,0,0),font=font)

    img.save(OriginalImageLocation0)




PutListDataIntoImage()