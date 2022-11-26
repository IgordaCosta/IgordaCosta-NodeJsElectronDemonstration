import CheckIfPixelColorIsBlack
import resizeImage
import RunImportImageMacro
import imageSizeByMultiplicationValue
import excelToJpg
import placeImageOnTopAnother




# InitialValue=7.9

# Location= "C:\\Users\\IgorDC\\Desktop\\"

# inputImageName="blackTest.png"

# excelLocation=Location

# excelFile="MacroTest.xlsx"

# excelIntoImageFileName="excelIntoImage.png"

# def CheckImageSize(InitialValue,Location,inputImageName,excelImageName,blackShowed=False,Finished=False):
def CheckImageSize(InitialValue,Location,inputImageName,excelLocation,excelFile,excelIntoImageFileName,blackShowed=False,Finished=False):

    # Imagewidth, Imageheight=imageSizeByMultiplicationValue.imageSizeByMultiplicationValue(MultiplicationValue=InitialValue)

    # resizeImage.resizeImage(Location=Location,inputImageName=inputImageName,outputImageName=inputImageName,Imagewidth=Imagewidth,Imageheight=Imageheight)
    resizeImage.resizeImage(InputLocation=Location,SaveLocation=Location,inputImageName = inputImageName,outputImageName=inputImageName)
    ##### here place the allblack image in excel background with a caracter in the upper middle column then
    RunImportImageMacro.RunImportImageMacro(excelLocation=excelLocation,excelFile=excelFile,imageLocation=Location,imageFilename=inputImageName)

    ##### save excel document and make an image of it
    imageName=excelToJpg.excelToJpg(excelFileName=excelFile,FolderLocation=excelLocation,OutputFilename=excelIntoImageFileName)

    # IfBlack=CheckIfPixelColorIsBlack.CheckIfPixelColorIsBlack(Location=Location,imageName=excelImageName)
    IfBlack=CheckIfPixelColorIsBlack.CheckIfPixelColorIsBlack(Location=excelLocation,imageName=imageName)
    
    print('IfBlack: ',IfBlack)
    print("blackShowed: ",blackShowed)
    print("Finished: ",Finished)
    if IfBlack==False:
        if blackShowed:
            # InitialValue=InitialValue+0.1
            InitialValue=((InitialValue*10)+1)/10

            # Imagewidth, Imageheight=imageSizeByMultiplicationValue.imageSizeByMultiplicationValue(MultiplicationValue=InitialValue)
            # resizeImage.resizeImage(Location=Location,inputImageName=inputImageName,outputImageName=inputImageName,Imagewidth=Imagewidth,Imageheight=Imageheight)
            resizeImage.resizeImage(InputLocation=Location,SaveLocation=Location,inputImageName = inputImageName,outputImageName=inputImageName)
            
            Finished=True
        else:
            # InitialValue=InitialValue+0.1
            InitialValue=((InitialValue*10)+1)/10

            blackShowed=False
            Finished=False
    else:
        # InitialValue=InitialValue-0.1
        InitialValue=((InitialValue*10)-1)/10
        blackShowed=True
        Finished=False

    return InitialValue, blackShowed, Finished




# InitialValue, blackShowed, Finished=CheckImageSize(InitialValue,Location,inputImageName,excelLocation,excelFile,excelIntoImageFileName)



# print(InitialValue, blackShowed, Finished)

# print("InitialValue, blackShowed, Finished")



    



