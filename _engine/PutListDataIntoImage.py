import os
from PIL import Image
from PIL import ImageDraw 
from PIL import ImageFont
import pathlib

import getTableData
import copyImageToAppFolderFromPython
import StringListIntoList
import MultiplyTextSizeByImageHeight
import RemoveExtraSlashes
# import base93Characterconversion


def PutListDataIntoImage(finalLocationsX, finalLocationsY):

    # TableGotten = getTableData.GetTableData()

    # OriginalImageLocation0=TableGotten['LocationToAddFileOnApp']

    # LocationToAddFileOnApp0=TableGotten['LocationToAddFileOnApp']


   



    # FileEnding = base93Characterconversion.base93Characterconversion()

     
    # OriginalImageLocation0 = '_'.join(('.'.join(str(LocationToAddFileOnApp0).split('.')[:-1])).split('_')[:-1]) + '_' + FileEnding + '.'+ str(LocationToAddFileOnApp0).split('.')[-1]


    


    # ImageRemoved=False
    try:
        TableGotten = getTableData.GetTableData()
        OriginalImageLocation0=TableGotten['LocationToAddFileOnApp']
        os.remove(OriginalImageLocation0)
        # ImageRemoved=True
    except:
        pass
   
    # copyImageToAppFolderFromPython.copyImageToAppFolderFromPython()

    OriginalImageLocation0 = copyImageToAppFolderFromPython.copyImageToAppFolderFromPython()

    # OriginalImageLocation0 = RemoveExtraSlashes.RemoveExtraSlashes(OriginalImageLocation00)

    finalLocationsXList= finalLocationsX

    finalLocationsYList=finalLocationsY

    TextToPut = ".XXXXXXX."

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

    try:
        finalLocationsXList = StringListIntoList.StringListIntoList(StringList=finalLocationsXList)
        finalLocationsYList = StringListIntoList.StringListIntoList(StringList=finalLocationsYList)
    except:
        pass

    finalLocationsXList0 = []
    finalLocationsYList0 = []

    for i in range(len(finalLocationsXList)):
        if finalLocationsXList[i] == '':
            pass

        else:
            draw.text((int(finalLocationsXList[i]), int(finalLocationsYList[i]) - textHeight ),TextToPut,(0,0,0),font=font)
            finalLocationsYList0.append(finalLocationsYList[i])
            finalLocationsXList0.append(finalLocationsXList[i])

    finalLocationsYList = finalLocationsYList0
    finalLocationsXList = finalLocationsXList0
    
    img.save(OriginalImageLocation0)

    FontSize=30

    

    

    dataList = [FontSize, finalLocationsXList, finalLocationsYList]

    dataNameList = ['FontSize', 'finalLocationsX', 'finalLocationsY' ]


    getTableData.MultipleListWriteDataDatabase(dataList= dataList, dataNameList=dataNameList)

