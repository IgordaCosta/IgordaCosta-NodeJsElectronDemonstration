from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import os
import pathlib

# from PIL import ImageFont
# from io import BytesIO



import getTableData
import copyImageToAppFolderFromPython
import MultiplyTextSizeByImageHeight


def CreateImageWithMarker():

    # print(os.getcwd())

    # currentWorkingDirectory=os.getcwd()

    # currentWorkingDirectory=



    # internalLocation='Documents'
    # excelLocation='AutoFormFillerFiles'
    
    # print("ok add file clicked")
    
    # home = os.path.expanduser('~')
    
    # print(home)
    
    # filePath = os.path.join(home, internalLocation ,excelLocation)


    TableGotten = getTableData.GetTableData()

    # print(TableGotten)

    OriginalImageLocation0 = TableGotten['LocationToAddFileOnApp']




    # newFileLocation0 = TableGotten['LocationToAddFileOnApp']

    # OriginalImageLocation1=OriginalImageLocation0.replace("/",'\\')

    # OriginalImageLocation='.\\' + OriginalImageLocation1

    # newFileLocation0 = currentWorkingDirectory + OriginalImageLocation

    # fileExtension=OriginalImageLocation.split('.')[-1]

    # print('fileExtension =',fileExtension)

    # NewImageLocation=OriginalImageLocation.replace('.'+fileExtension,'')

    # print('NewImageLocation =',NewImageLocation)

    # print('OriginalImageLocation =',OriginalImageLocation)

    # # # './_clientImageFiles/TestImageFile_temp.jpg'





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
        # print("Error while deleting file ", OriginalImageLocation0)
        pass

    if ImageRemoved:

        copyImageToAppFolderFromPython.copyImageToAppFolderFromPython()





        # fileNameOnly=TableGotten['fileNameOnly']


        # fileNameOnly='TestImageFile.jpg'


        # newFileLocation=filePath +"\\temp_" + fileNameOnly

        newFileLocation=OriginalImageLocation0



        


        



        # newFileLocation0=filePath +"\\" + fileNameOnly


        # newFileLocation=filePath +"\\temp_" + fileNameOnly


        ImgPosition=TableGotten['ImgPosition']

        # print(ImgPosition)

        # print(TableGotten)

        ImgPositionAsList=ImgPosition.split(',')

        # print(ImgPositionAsList)

        x = int(ImgPositionAsList[0])

        y = int(ImgPositionAsList[1])

        # print('x',x)

        # print('y',y)


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
        #font = ImageFont.truetype("C://Windows//Fonts//Arial//arial.ttf", 30)

        Location = OriginalImageLocation0



        # print(OriginalImageLocation0)


        # print('OriginalImageLocation0')




        multVariable = MultiplyTextSizeByImageHeight.MultiplyTextSizeByImageHeight(Location=Location)

        # print(multVariable)

        font = ImageFont.truetype(DefaultFontLocation , int(multVariable * 30))

        textWidth, textHeight = draw.textsize(TextToPut, font)

        # draw.text((x, y),"Sample Text",(r,g,b))
        draw.text((x, y-textHeight),".XXXXXXX.",(0,0,0),font=font)
        img.save(OriginalImageLocation0)

        # print("Done")


        # newFileLocation

        lastTempLocationPointX= x

        # lastTempLocationPointY= y-textHeight

        lastTempLocationPointY= y



        # data=[newFileLocation, lastTempLocationPointX, lastTempLocationPointY]

        # dataName= ['newFileLocation', 'lastTempLocationPointX', 'lastTempLocationPointY']


        data=[lastTempLocationPointX, lastTempLocationPointY]

        dataName= ['lastTempLocationPointX', 'lastTempLocationPointY']

        

        # TableName=getTableData.GetTableData()

        # try:
        #     TableName.asdfasdf
        # except AttributeError:
        #     print("Table does not exist")

        # print("continued")




        # getTableData.WriteDataDatabase(data,dataName)

        getTableData.MultipleListWriteDataDatabase(dataList=data,dataNameList=dataName)



    






CreateImageWithMarker()
