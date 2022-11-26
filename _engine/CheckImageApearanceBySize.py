import pathlib

import imageSizeByMultiplicationValue
import resizeImage
import RunImportImageMacro
import excelToJpg
import ExcelToPdf

def CheckImageApearanceBySize(InitialValue,imageLocation,inputImageName,excelLocation,excelFile,excelIntoImageFileName):

    # Imagewidth, Imageheight=imageSizeByMultiplicationValue.imageSizeByMultiplicationValue(MultiplicationValue=InitialValue)

    # resizeImage.resizeImage(Location=imageLocation,inputImageName=inputImageName,outputImageName=inputImageName,Imagewidth=Imagewidth,Imageheight=Imageheight)

    
    RunImportImageMacro.RunImportImageMacro(excelLocation=excelLocation,excelFile=excelFile,imageLocation=imageLocation,imageFilename=inputImageName)

    excelToJpg.excelToJpg(excelFileName=excelFile,FolderLocation=excelLocation,OutputFilename=excelIntoImageFileName)

    # ExcelToPdf.ExcelToPdf(excelFileName=excelFile,pdfFileName=pdfFileName,excelFolderSavePath=excelLocation,pdfFolderSavePath=imageLocation)

    print("Done image check")

InitialValue=7.9


homedir = pathlib.Path.home()

Location = str(homedir) + '\\Desktop\\'


#imageLocation="C:\\Users\\IgorDC\\Desktop\\"
imageLocation= Location

inputImageName="BlackBox.jpg"
#excelLocation="C:\\Users\\IgorDC\\Desktop\\"
excelLocation= Location

excelFile="MacroTest.xlsx"
pdfFileName="ImageApearance.pdf"

excelIntoImageFileName="BlackBoxCheck.jpg"


CheckImageApearanceBySize(InitialValue,imageLocation,inputImageName,excelLocation,excelFile,excelIntoImageFileName)