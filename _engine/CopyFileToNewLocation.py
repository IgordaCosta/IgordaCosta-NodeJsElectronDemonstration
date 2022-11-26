import shutil
import os


def CopyFileToNewLocation(getFileLocation, CopyToLocaion, TimeNameFull):

    BaseFileLocation2 =getFileLocation
    BaseFileLocation = CopyToLocaion

    currentDirectory = BaseFileLocation.split(':')[0]+ ':/'

    os.chdir(currentDirectory)
    noError= False
    NOTCopy = True
    while NOTCopy:
    
        RetunValue= shutil.copy(BaseFileLocation2, TimeNameFull)

        # print('fileNotCopied')

        if os.path.exists(str(TimeNameFull)):
            # print(TimeNameFull)
            NOTCopy =False
            # print('file just copied')
            noError = True

       

    return noError, RetunValue

