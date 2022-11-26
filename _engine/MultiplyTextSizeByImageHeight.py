import cv2
import re
import shutil
import os
import time

import getTableData


def MultiplyTextSizeByImageHeight(Location, ImageName = ''):

    # print(Location + ImageName)

    # print('Location + ImageName')



    LocationToAddFileOnApp = getTableData.GetTableData()['LocationToAddFileOnApp']



    CompleteLocation = Location + ImageName


    NewCompleteLocationFileName0 = CompleteLocation.split('\\')[-1]


  
    timeInMili = int(round(time.time() * 1000))


    NewCompleteLocationFileName = str(timeInMili) + '_' + re.sub("[^A-Za-z0-9.]","",NewCompleteLocationFileName0) 

    NewLocation = '\\'.join(LocationToAddFileOnApp.split('\\')[:-1]) + '\\'

    NewCompleteLoation = NewLocation + NewCompleteLocationFileName

    # print(NewCompleteLoation)


    shutil.copyfile(CompleteLocation, NewCompleteLoation)



    imageGotten = cv2.imread(NewCompleteLoation)

    ImHeight, ImWidth, _ = imageGotten.shape
    # print('width: ', ImWidth)
    # print('height:', ImHeight)

    MuLImageTextSize = round(int(ImHeight)/2200,2)


    os.remove(NewCompleteLoation)
     
    return MuLImageTextSize




# ImageName = 'A2ç   B1.jpg'




# print(MultiplyTextSizeByImageHeight(Location, ImageName))