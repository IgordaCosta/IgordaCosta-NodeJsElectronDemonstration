import os



FolderLocation = r'C:\Users\Tigereye\Desktop\TempFileCopyLocation'

FileName = 'CheckIfNameExists'

extension = '.js'


# print(os.listdir(FolderLocation))

ListOfFileNames = os.listdir(FolderLocation)


for FileName in ListOfFileNames:
    LocationToDeleteComments = FolderLocation + '\\' + FileName

    dataList2 = []
    with open(LocationToDeleteComments, 'r') as file:    
        dataList = file.readlines()

        for data in dataList:
            if r'//' in data:
                data = ''

            dataList2.append(data)


    with open(LocationToDeleteComments, 'w') as file:
        file.writelines( dataList2 )