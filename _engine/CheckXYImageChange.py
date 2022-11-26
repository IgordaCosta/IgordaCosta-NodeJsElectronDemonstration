from PIL import Image, ImageFile

import CheckChangeInSizeAndMovement




def CheckXYImageChange(imageH,ImageW,ChangedImageFolder,ChangedImageName):

    
    # ChangedImageName=CheckChangeInSizeAndMovement.CheckChangeInSizeAndMovement(excelLocation=excelLocation,excelFile=excelFile,imageLocation=inputImageLocation,inputImageName=inputImageName,excelIntoImageFileName=excelIntoImageFileName)

    ImageFile.MAXBLOCK = 2**20

    img = Image.open(ChangedImageFolder+ChangedImageName)
    img = img.convert("RGB")

    pixdata = img.load()

    width, height = img.size

    FirstWhite=True
    FirstBlack=False

    FirstAndLastYList=[]
    for y in range(height):
        (a, b, c)= pixdata[int(ImageW/4), y]
        if a>70 and b >70 and c >70:
            if FirstWhite==False:
                FirstAndLastYList.append(y)
                FirstWhite=True
        else:
            if FirstBlack==False:
                FirstAndLastYList.append(y)
                FirstBlack=True
                FirstWhite=False


    FirstWhite=True
    FirstBlack=False

    FirstAndLastXList=[]
    for x in range(width):
        (a, b, c)= pixdata[x, int(imageH/4)]
        if a>70 and b >70 and c >70:
            if FirstWhite==False:
                FirstAndLastXList.append(x)
                FirstWhite=True
        else:
            if FirstBlack==False:
                FirstAndLastXList.append(x)
                FirstBlack=True
                FirstWhite=False


    print('FirstAndLastXList: ',FirstAndLastXList)

    print("difference X: ",FirstAndLastXList[1]-FirstAndLastXList[0])

    print("FirstAndLastYList: ",FirstAndLastYList)

    print("difference Y: ",FirstAndLastYList[1]-FirstAndLastYList[0])



    print("done")

    return FirstAndLastXList, FirstAndLastYList






# excelLocation="C:\\Users\\IgorDC\\Desktop\\"

# inputImageLocation="C:\\Users\\IgorDC\\Desktop\\"

# ChangedImageFolder="C:\\Users\\IgorDC\\Desktop\\"
# excelFile="MacroTest.xlsx"

# inputImageName='BlackCross.jpg'

# ChangedImageName="BlackCrossCheck.jpg"


# excelIntoImageFileName=ChangedImageName



# imageH=980
# ImageW=758






