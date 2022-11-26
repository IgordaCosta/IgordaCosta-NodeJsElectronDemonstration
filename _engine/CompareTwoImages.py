import pathlib

import CheckXYImageChange



def CompareTwoImages(imageH,ImageW,ChangedImageFolder,ChangedImageName1,ChangedImageName2):
    FromExcelXList, FromExcelYList=CheckXYImageChange.CheckXYImageChange(imageH=imageH,ImageW=ImageW,ChangedImageFolder=ChangedImageFolder,ChangedImageName=ChangedImageName1)

    RealImageXList, RealImageYList=CheckXYImageChange.CheckXYImageChange(imageH=imageH,ImageW=ImageW,ChangedImageFolder=ChangedImageFolder,ChangedImageName=ChangedImageName2)



    print('FromExcelXList: ',FromExcelXList)

    FromExcelXListDifference=FromExcelXList[1]-FromExcelXList[0]
    print('FromExcelXListDifference: ',FromExcelXListDifference)

    print('FromExcelYList: ',FromExcelYList)

    FromExcelYListDifference=FromExcelYList[1]-FromExcelYList[0]
    print('FromExcelYListDifference: ',FromExcelYListDifference)

    print("RealImageXList: ",RealImageXList)
    
    RealImageXListDifference=RealImageXList[1]-RealImageXList[0]

    print("RealImageXListDifference: ",RealImageXListDifference)

    print('RealImageYList: ',RealImageYList)
    
    RealImageYListDifference=RealImageYList[1]-RealImageYList[0]

    print("RealImageYListDifference: ", RealImageYListDifference)

    DifferenceYBothImages=RealImageYListDifference-FromExcelYListDifference

    print("DifferenceYBothImages: ",DifferenceYBothImages)

    XDifferenceBothImages=RealImageXListDifference-FromExcelXListDifference

    print("XDifferenceBothImages: ", XDifferenceBothImages)


    percentYtoIncreaseImage=(DifferenceYBothImages/RealImageYListDifference)*100

    print('percentYtoIncreaseImage: ',percentYtoIncreaseImage,"%")

    IncreaseXbyPercent=(XDifferenceBothImages/RealImageXListDifference)*100

    print("IncreaseXbyPercent: ",IncreaseXbyPercent,"%")

    upperYSubtration=RealImageYList[0]-FromExcelYList[0]

    print("upperYSubtration: ", upperYSubtration)

    lowerYSubtration=RealImageYList[1]-FromExcelYList[1]

    print("lowerYSubtration: ", lowerYSubtration)

    upperXSubtration=RealImageXList[1]-FromExcelXList[1]

    print('upperXSubtration: ',upperXSubtration)

    lowerXSubtration=RealImageXList[0]-FromExcelXList[0]

    print('lowerXSubtration: ',lowerXSubtration)

    RealYSubtraction=int((upperYSubtration+lowerYSubtration)/2)

    print('RealYSubtraction: ',RealYSubtraction)

    RealXSubtraction=int((upperXSubtration+lowerXSubtration)/2)

    print('RealXSubtraction: ',RealXSubtraction)

    return RealXSubtraction, RealYSubtraction






imageH=980
ImageW=758
#ChangedImageFolder="C:\\Users\\IgorDC\\Desktop\\"


homedir = pathlib.Path.home()

ChangedImageFolder = str(homedir) + '\\Desktop\\'


ChangedImageName1="ExcelBlackCrossPaintCheckShifted.jpg"
ChangedImageName2="BlackCross1700x2200.jpg"



CompareTwoImages(imageH,ImageW,ChangedImageFolder,ChangedImageName1,ChangedImageName2)