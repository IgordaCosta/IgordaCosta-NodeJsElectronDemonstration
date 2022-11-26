from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import os
import pandas

import getTableData
import GetFontFilePaths
import copyImageToAppFolderFromPython
import GetAllFontNamesFromFolderFunction
import MultiplyTextSizeByImageHeight


def PutListDataIntoImage(TextToPut = ".XXXXXXX.", DataInputOption = True):

    TableGotten = getTableData.GetTableData()

    if DataInputOption:

        systemFonts = TableGotten['systemFonts']

        finalLocationsX = TableGotten['finalLocationsX']

        finalLocationsY = TableGotten['finalLocationsY']

        OriginalImageLocation0=TableGotten['LocationToAddFileOnApp']

        Location = OriginalImageLocation0

        multVariable = MultiplyTextSizeByImageHeight.MultiplyTextSizeByImageHeight(Location=Location)

        FontSize0=TableGotten['newFontSize']

        FontSize = int(int(FontSize0) * multVariable)     ###### add this to old font size

        FontSizeShow=int(FontSize0) 

        newFont=TableGotten['newFont'] ###### add this to old font

    else:
        systemFonts = GetAllFontNamesFromFolderFunction.GetAllFontNamesFromFolder()
        
        currentWorkingDirectory = TableGotten['currentWorkingDirectory']        

        FilesInDatabaseTable = getTableData.GetTableDataFromTable(TableName='FilesInDatabase')

        FontAndItsSizeTable = getTableData.GetTableDataFromTable(TableName='FontAndItsSize')

        FilesInDatabaseTableDf = pandas.DataFrame(FilesInDatabaseTable[0] , columns=FilesInDatabaseTable[1])

        imageFolderLocation='_clientImageFiles\\'

        datafillName0 = TableGotten['datafillName']

        spaceReplaceDataUserImput = '$%78&*&'

        datafillName = datafillName0.replace(' ', spaceReplaceDataUserImput )

        data = datafillName

        dataName = 'datafillName'

        getTableData.WriteDataDatabase(data=data, dataName=dataName)

        rowLoacation = FilesInDatabaseTableDf[FilesInDatabaseTableDf['Job Name']== datafillName]

        newFileLocation1 = rowLoacation['File Saved Location'].values[0]

        LocationNameOnly = rowLoacation['File Saved Location'].values[0].split('\\')[-1]

        LocationToPlaceOnWebPage= imageFolderLocation + LocationNameOnly

        OriginalImageLocation0 = currentWorkingDirectory + '\\'  + LocationToPlaceOnWebPage

        SaveLocation = LocationToPlaceOnWebPage

        KeyFile = rowLoacation['File KEY'].values[0]

        KeyFileTable = getTableData.GetTableDataFromTable(TableName=KeyFile)

        FontAndItsSizeTableDf = pandas.DataFrame(FontAndItsSizeTable[0] , columns=FontAndItsSizeTable[1])

        rowLoacationTable2 = FontAndItsSizeTableDf[FontAndItsSizeTableDf['Job Name']== datafillName]

        FontSize0 = rowLoacationTable2['FontSize'].values[0]

        FontSize=int(FontSize0) 

        FontSizeShow=int(FontSize0) 

        newFont = rowLoacationTable2['FontName'].values[0]

        FromPdf = rowLoacationTable2['FromPdf'].values[0]

        dataList = [OriginalImageLocation0, 'false', newFileLocation1 ]
        
        dataNameList =['LocationToAddFileOnApp', 'PDFfile', 'newFileLocation']

        getTableData.MultipleListWriteDataDatabase(dataList=dataList,dataNameList=dataNameList)

    systemFontsList=systemFonts.split('|')

    indexOfItemInListOfFonts=systemFontsList.index(newFont)

    fontFilePaths=GetFontFilePaths.GetFontFilePaths()

    fontSelectedPath= fontFilePaths[indexOfItemInListOfFonts]

    ImageRemoved=False
    try:
        os.remove(OriginalImageLocation0)
        ImageRemoved=True
    except:
        # print("Error while deleting file ", OriginalImageLocation0)
        pass
    
    cwd = os.getcwd()

    copyImageToAppFolderFromPython.copyImageToAppFolderFromPython()

    if DataInputOption:

        finalLocationsXList=finalLocationsX.replace('[','').replace(" ",'').replace(']','').replace("'",'').split(',')

        finalLocationsYList=finalLocationsY.replace('[','').replace(" ",'').replace(']','').replace("'",'').split(',')

    img = Image.open(OriginalImageLocation0)
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype(fontSelectedPath, FontSize)

    textWidth, textHeight = draw.textsize(TextToPut, font)

    if DataInputOption:

        for i in range(len(finalLocationsXList)):
            if finalLocationsXList[i] == '':
                pass
            
            else:
                draw.text((int(finalLocationsXList[i]), int(finalLocationsYList[i]) - textHeight ),TextToPut,(0,0,0),font=font)

    else:    
        spaceReplaceData = '$%3&*&'

        TextTopPut00 = str(KeyFileTable[0][0]).replace('[','').replace(']','').replace('"','').replace("'",'').replace(", ",',').replace(" ,",',')
        
        TextTopPut0= (' '.join(TextTopPut00.split(spaceReplaceData))).split(',')

        data = LocationToPlaceOnWebPage

        dataName = 'LocationToPlaceOnWebPage'

        getTableData.WriteDataDatabase(data=data,dataName=dataName)

        ListValues00 = KeyFileTable[1]

        for j in range(len( TextTopPut0 ) - 1 ): 
            i = j + 1

            ListValues = ListValues00[i].replace('[', '').replace(']', '').strip().replace(', ', ',').replace(' ,', ',').split(',')
            
            print(ListValues)

            TextToPut = TextTopPut0[i]

            draw.text((int(ListValues[1]), int(ListValues[0]) - textHeight ),TextToPut,(0,0,0),font=font)

    img.save(OriginalImageLocation0)
   
    if DataInputOption:

        dataList= [newFont, FontSize, finalLocationsXList, finalLocationsYList, FontSizeShow]
        dataNameList = ['oldFont', 'FontSize', 'finalLocationsXList', 'finalLocationsYList', 'FontSizeShow']

        getTableData.MultipleListWriteDataDatabase(dataList=dataList,dataNameList=dataNameList)
