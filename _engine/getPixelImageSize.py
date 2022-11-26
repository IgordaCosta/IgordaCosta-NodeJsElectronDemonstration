from PIL import Image
import os.path

def getPixelImageSize(Location,filename):

    img = Image.open(Location+filename)
    width, height = img.size
    print ("Dimensions:", img.size, "Total pixels:", width * height)

    return img.size



# filename="ContractOutput.png"

# Location="C:\\Users\\IgorDC\\Desktop\\"

# filename2="emptyExcelJPGFile_1.jpg"


# width, height=getPixelImageSize(Location=Location,filename=filename)

# print('filename: ',filename)

# print('width: ',width)

# print('height: ',height)


# width, height=getPixelImageSize(Location=Location,filename=filename2)

# print('filename2: ',filename2)

# print('width: ',width)

# print('height: ',height)
