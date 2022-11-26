import subprocess

import wordToPdf
import ExcelToPdf
import jpgToPdf
import getTableData



TableGotten = getTableData.GetTableData()

ExtensionType = TableGotten['ExtensionType']

fileLocation = TableGotten['fileLocation']


fileLocationList = fileLocation.split('\\')

fileNameANdExtension = fileLocationList[-1]


filenameOnly ='.'.join(fileNameANdExtension.split('.')[:-1])

Location =  '\\'.join(fileLocation.split('\\')[:-1]) +'\\'



# print(fileNameANdExtension)

# print('fileNameANdExtension')

# print(filenameOnly)

# print('filenameOnly')

# print(Location)

# print('Location')



if ExtensionType == 'excel':

    excelFileName = fileNameANdExtension

    pdfFileName =  filenameOnly + '.pdf'

    excelFolderSavePath = Location

    pdfFolderSavePath = Location

    ExcelToPdf.ExcelToPdf(excelFileName,pdfFileName,excelFolderSavePath,pdfFolderSavePath)

elif ExtensionType == 'word':

    WordFileName = fileNameANdExtension
    
    PdfFileName =  filenameOnly + '.pdf'
    
    FolderLocation = Location

    wordToPdf.wordToPdf(WordFileName,PdfFileName,FolderLocation)



elif ExtensionType == 'image':

    ImageName = fileNameANdExtension
    
    PdfSaveName =  filenameOnly + '.pdf'
    
    FolderLocation = Location

    jpgToPdf.jpgToPdf(ImageName=ImageName,Folderlocation=FolderLocation, PdfSaveName=PdfSaveName)

    
else:
    # print('error extension not supported')
    pass




dataList = [filenameOnly, Location]

dataNameList = ['nameOfNewFile', 'FolderSaveLocation']


getTableData.MultipleListWriteDataDatabase(dataList=dataList, dataNameList=dataNameList)


subprocess.Popen(r'explorer /open, ' + Location)