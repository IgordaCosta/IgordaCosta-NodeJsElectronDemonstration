import pathlib

import shiftImage
import CheckDifferenceInExcelImage




def checkAndFixExcelImageDifference(FolderLocation,excelFileName,OutputImageFilename,imageH,ImageW,inputImageName,outputImageName,shiftImageOutputImageName):

    shiftX, shiftY, OutputFinalFilename = CheckDifferenceInExcelImage.CheckDifferenceInExcelImage(excelFileName=excelFileName,FolderLocation=FolderLocation,OutputFilename=OutputImageFilename,imageH=imageH,ImageW=ImageW,ChangedImageFolder=FolderLocation,inputImageName=inputImageName,outputImageName=outputImageName)

    shiftImage.shiftImage(inputImageFilename=OutputFinalFilename,inputImageFileLocation=FolderLocation,outputImageName=shiftImageOutputImageName,shiftX=shiftX,shiftY=shiftY)

    print("Done check and fix excel image difference")




# FolderLocation="C:\\Users\\IgorDC\\Desktop\\"

homedir = pathlib.Path.home()

FolderLocation = str(homedir) + '\\Desktop\\'

excelFileName="MacroTest2.xlsx"
OutputImageFilename="ExcelBlackCrossPaintCheck.jpg"
imageH=980
ImageW=758
inputImageName='BlackCross.jpg'
outputImageName='BlackCross1700x2200.jpg'
shiftImageOutputImageName="ExcelBlackCrossPaintCheckShifted.jpg"


checkAndFixExcelImageDifference(FolderLocation,excelFileName,OutputImageFilename,imageH,ImageW,inputImageName,outputImageName,shiftImageOutputImageName)