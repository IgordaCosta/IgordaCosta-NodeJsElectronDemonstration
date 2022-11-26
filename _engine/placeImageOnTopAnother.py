from PIL import Image




def placeImageOnTopAnother(bottomImagefolderLocation,topImagefolderLocation,bottomImage,imagePlacedOnTop,OutputImageName):

    im1 = Image.open(bottomImagefolderLocation+bottomImage)
    im2 = Image.open(topImagefolderLocation+imagePlacedOnTop)

    back_im = im1.copy()
    back_im.paste(im2, (0, 0), im2)
    back_im.save(folderLocation+OutputImageName, "PNG")

    print("done")




# folderLocation="C:\\Users\\IgorDC\\Desktop\\"
# bottomImage="LibreOfficeMac.jpg"
# imagePlacedOnTop="ContractOutput.png"
# OutputImageName="JoinedImage.png"




# placeImageOnTopAnother(folderLocation,bottomImage,imagePlacedOnTop,OutputImageName)