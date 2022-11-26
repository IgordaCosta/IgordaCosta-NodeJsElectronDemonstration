from PIL import Image
import resizeImage 
import time




def ResizeImagesInBulk(Folderlocation, ImagesNameList):

    AppendedValue = str(int(time.time()*10000000))[-8:]

    Folderlocation0 = Folderlocation

    Folderlocation = Folderlocation0 + '\\'

    #get the lowest dimension to make all even size

    AllYSizeValue = []
    for image in ImagesNameList:
        img = Image.open(Folderlocation + image)

        (OldX0, CheckedOldY) = img.size

        AllYSizeValue.append(CheckedOldY)



    # NewY = min(AllYSizeValue)

    NewY = max(AllYSizeValue)

    NewImageNameList = []
    for image in ImagesNameList:

        
        imageNameOnly = '.'.join(image.split('.')[:-1])

        NewImageName = imageNameOnly + '_RS_' + AppendedValue + '.jpg'
        
        try:
            resizeImage.resizeImage(InputLocation=Folderlocation, SaveLocation=Folderlocation,inputImageName = image,outputImageName=NewImageName)
       
            NewImageNameList.append(NewImageName)

        except:
            pass

    
    return NewImageNameList




# ImagesNameList = [Location + 'A13B1.jpg', Location + 'Testingsample_Joined_1652858852545.pdf_74517_3_RS_53049430.jpg']


# print(ResizeImagesInBulk(ImagesNameList))


