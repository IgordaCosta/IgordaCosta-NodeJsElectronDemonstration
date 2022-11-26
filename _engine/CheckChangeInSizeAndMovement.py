import CreateBlackCross
import RunImportImageMacro
import excelToJpg



def CheckChangeInSizeAndMovement(excelLocation,excelFile,imageLocation,inputImageName,excelIntoImageFileName):

    RunImportImageMacro.RunImportImageMacro(excelLocation=excelLocation,excelFile=excelFile,imageLocation=imageLocation,imageFilename=inputImageName)

    OutputFinalFilename=excelToJpg.excelToJpg(excelFileName=excelFile,FolderLocation=excelLocation,OutputFilename=excelIntoImageFileName)

    return OutputFinalFilename





# imageLocation="C:\\Users\\IgorDC\\Desktop\\"
# excelLocation="C:\\Users\\IgorDC\\Desktop\\"
# excelFile="MacroTest.xlsx"

# inputImageName='BlackCross.jpg'




# excelIntoImageFileName="BlackCrossCheck.jpg"

# CheckChangeInSizeAndMovement(excelLocation,excelFile,imageLocation,inputImageName,excelIntoImageFileName)