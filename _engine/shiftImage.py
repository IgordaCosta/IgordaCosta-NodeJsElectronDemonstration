import cv2 
import numpy as np 

def shiftImage(inputImageFilename, inputImageFileLocation,outputImageName,shiftX,shiftY):
  
    FILE_NAME = inputImageFileLocation+inputImageFilename
    # Create translation matrix. 
    # If the shift is (x, y) then matrix would be 
    # M = [1 0 x] 
    #     [0 1 y] 
    
    M = np.float32([[1, 0, shiftX], [0, 1, shiftY]]) 
    
    try: 
    
        # Read image from disk. 
        img = cv2.imread(FILE_NAME) 
        (rows, cols) = img.shape[:2] 
    
        # warpAffine does appropriate shifting given the 
        # translation matrix. 
        res = cv2.warpAffine(img, M, (cols, rows)) 
    
        # Write image back to disk. 
        cv2.imwrite(inputImageFileLocation+outputImageName, res) 
    
    except IOError: 
        print ('Error while reading files !!!') 

    print("Done")



# inputImageFilename="ExcelBlackCrossCheck.jpg"

# inputImageFileLocation="C:\\Users\\IgorDC\\Desktop\\"

# outputImageName="ExcelBlackCrossCheckShifted.jpg"

# shiftX=0

# shiftY=-143




# shiftImage(inputImageFilename, inputImageFileLocation,outputImageName,shiftX,shiftY)
