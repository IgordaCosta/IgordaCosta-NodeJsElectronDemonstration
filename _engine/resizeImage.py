import cv2



def resizeImage(InputLocation,SaveLocation,inputImageName = '',outputImageName='',Imageheight=3000):
    
    heightMax =Imageheight
    if inputImageName == '':
        imageLocation = InputLocation 
    else:
        imageLocation = InputLocation + '\\'+ inputImageName


    if outputImageName == '':
        ResizeSaveFolder = SaveLocation 
    else:
        ResizeSaveFolder = SaveLocation + '\\'+ outputImageName


    
    # print(imageLocation)

    # Read the image using imread function
    image = cv2.imread(imageLocation)



    
    # Get original height and width
    h,w,c = image.shape
    # print("Original Height and Width:", h,"x", w)


    ChangedWidth = int((heightMax/h) * w)
    ChangedHeight = heightMax
    ChangedPoints = (ChangedWidth, ChangedHeight)


    # print("New Height and Width:", ChangedHeight,"x", ChangedWidth)



    reSizeChange = cv2.resize(image, ChangedPoints, interpolation= cv2.INTER_LINEAR)
    

    cv2.imwrite(ResizeSaveFolder,reSizeChange)
 
