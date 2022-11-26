import pathlib

import CheckImageSize
import RunPageConfigurationMacro




def getImagePixelToBorder(InitialValue,Location,inputImageName,excelLocation,excelFile,excelIntoImageFileName):
    
    blackShowed=False
    Finished=False

    RunPageConfigurationMacro.RunPageConfigurationMacro(excelFile=excelFile,Location=excelLocation)

    numberOfStepsTaken=0

    while Finished==False:
        
        InitialValue, blackShowed, Finished= CheckImageSize.CheckImageSize(InitialValue,Location,inputImageName,excelLocation,excelFile,excelIntoImageFileName,blackShowed=blackShowed,Finished=Finished)

        numberOfStepsTaken=numberOfStepsTaken+1

        print('numberOfStepsTaken',numberOfStepsTaken)

        print('InitialValue',InitialValue)

    print('Last Value: ',InitialValue)

    print("Finished")






InitialValue=7.9

# InitialValue=8.5

#Location="C:\\Users\\IgorDC\\Desktop\\"


homedir = pathlib.Path.home()

Location = str(homedir) + '\\Desktop\\'


inputImageName="blackTest.png"

excelLocation=Location

excelFile="MacroTest.xlsx"

excelIntoImageFileName="excelIntoImage.png"



getImagePixelToBorder(InitialValue,Location,inputImageName,excelLocation,excelFile,excelIntoImageFileName)