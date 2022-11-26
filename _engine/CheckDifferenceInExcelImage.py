import ComparingImages
import excelToJpg

def CheckDifferenceInExcelImage(excelFileName,FolderLocation,OutputFilename,imageH,ImageW,ChangedImageFolder,inputImageName,outputImageName):

    OutputFinalFilename=excelToJpg.excelToJpg(excelFileName=excelFileName,FolderLocation=FolderLocation,OutputFilename=OutputFilename)

    RealXSubtraction, RealYSubtraction=ComparingImages.ComparingImages(imageH=imageH,ImageW=ImageW,ChangedImageFolder=FolderLocation,ChangedImageName=OutputFinalFilename,inputImageLocation=FolderLocation,inputImageName=inputImageName,outputImageName=outputImageName)

    return RealXSubtraction, RealYSubtraction, OutputFinalFilename















# # OutputFilename="ExcelBlackCrossCheck.jpg"


# OutputFilename="ExcelBlackCrossPaintCheck.jpg"

# # excelFileName="CrossExcelJoin.xlsx"

# excelFileName="MacroTest2.xlsx"

# FolderLocation="C:\\Users\\IgorDC\\Desktop\\"
# ChangedImageFolder="C:\\Users\\IgorDC\\Desktop\\"
# inputImageLocation="C:\\Users\\IgorDC\\Desktop\\"
# inputImageName='BlackCross.jpg'
# outputImageName='BlackCross1700x2200.jpg'

# imageH=980
# ImageW=758




# CheckDifferenceInExcelImage(excelFileName,FolderLocation,OutputFilename,imageH,ImageW,ChangedImageFolder,inputImageLocation,inputImageName,outputImageName)