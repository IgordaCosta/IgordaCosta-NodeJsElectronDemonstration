import os




def CreateFolderInFolder(FolderLocation):

    FolderLocation2= FolderLocation.replace('/', '\\').split(':\\')[1].split('\\')


    DriveLocation = FolderLocation.replace('/', '\\').split(':\\')[0]
    # print(FolderLocation2)

    FolderSize = len(FolderLocation2)


    LocationToMake = ''
    for LoationToAdd in FolderLocation2:
        # print(DriveLocation + '\\' + LoationToAdd)
        if LoationToAdd == '':
            pass

        else:
            LocationToMake = LocationToMake + '\\' + LoationToAdd

            # print(LocationToMake)
            try:
                os.mkdir(LocationToMake)
            except:
                pass




# FolderLocation = 'C:\\Users/Tigereye\\Documents\\AutoFormFillerFiles\\Temp\\Temp1\\Temp2\\Temp3\\Temp4\\Temp5\\'

# CreateFolderInFolder(FolderLocation)



# TestFolderLocation = 'C:\\Users\\Tigereye\\Documents\\AutoFormFillerFiles\\Temp\\Temp1\\Temp2\\Temp3\\Temp4\\Temp5'


# os.mkdir(TestFolderLocation)