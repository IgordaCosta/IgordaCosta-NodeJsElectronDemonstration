import os
import pandas
from pathlib import Path
import shutil
import subprocess
import re

import getTableData

def SortFilesIntoFolders():

    DataGotten = getTableData.GetTableData()

    MinRange = DataGotten['MinRange']

    MaxRange = DataGotten['MaxRange']

    fileNameOnly = DataGotten['fileNameOnly']

    FolderSaveLocation0 = DataGotten['FolderSaveLocation']


    FolderSaveLocation = FolderSaveLocation0 + '\\'


    filenameNoExtension = '.'.join(fileNameOnly.split('.')[:-1])

    MaxAllowedFileSize = len(filenameNoExtension)

    if MaxAllowedFileSize < int(MaxRange):
        MaxRange = MaxAllowedFileSize

    
    FileListUsed = []

    for filename in os.listdir(FolderSaveLocation):
        if '.' in filename:
            FileListUsed.append(filename)
            

    # print(FileListUsed)
    df = pandas.DataFrame(FileListUsed,columns=['folderFiles'])

    # print(df)


    # print(df['folderFiles'].str.slice(start=int(MinRange),stop=int(MaxRange)))


    df['SplitParameters'] = df['folderFiles'].str.slice(start=int(MinRange),stop=int(MaxRange))

    # print(df)

    # print(df['SplitParameters'].nunique())

    # print(df['SplitParameters'].unique())


    # print(df['folderFiles'][df['SplitParameters'] == df['SplitParameters'].unique()[0]].tolist())


    # print(df['folderFiles'][df['SplitParameters'] == df['SplitParameters'].unique()[1]].tolist())
        


    NumberOfUniqueValues = df['SplitParameters'].nunique()

    UniqueValueNames = df['SplitParameters'].unique()



    UniqueValueNames2 = []
    for i in range(NumberOfUniqueValues):

        UniqueValuesInList = df['folderFiles'][df['SplitParameters'] == df['SplitParameters'].unique()[i]].tolist()

        

        InnerFolderName0 = str(UniqueValueNames[i]) 


        InnerFolderName1 = InnerFolderName0.replace(' ', '_').replace('\\', '_').replace('/', '_').replace('|', '_').replace(':', '_').replace('*', '_').replace('?', '_').replace('>', '_').replace('<', '_').replace('"', '_').replace("'", '_').replace(".", '_')

        InnerFolderName = InnerFolderName1 + '\\'



        UniqueValueNames2.append(InnerFolderName1)




        WholeFolderLocation = FolderSaveLocation + InnerFolderName

        # print(WholeFolderLocation)

        
        Path(WholeFolderLocation).mkdir(parents=True, exist_ok=True)

        for r in range(len(UniqueValuesInList)):

            OldfileLocationAndName = FolderSaveLocation + UniqueValuesInList[r]

            # print(OldfileLocationAndName)


            NewFileToCopiedAndLocation = WholeFolderLocation + UniqueValuesInList[r]

            # print(NewFileToCopiedAndLocation)


            shutil.copyfile(OldfileLocationAndName, NewFileToCopiedAndLocation)




    # data = str(UniqueValueNames)



    # UniqueValueNames3 = str(UniqueValueNames2).replace('-', '&#8211;')

    # UniqueValueNames3 = str(UniqueValueNames2).replace('-', 'T')

    # UniqueValueNames20 = str(UniqueValueNames2).replace(', ', ',')

    # UniqueValueNames3=re.sub("[^A-Za-z0-9,]","_", str(UniqueValueNames2))


   

    UniqueValueNames3 = ''
    for textToAdd in UniqueValueNames2:

        itemToAdd = '''<td><div class="form-group thirdsize"><h1>''' + textToAdd + '''</h1></div></td>'''


        UniqueValueNames3 = UniqueValueNames3 + itemToAdd


    data = UniqueValueNames3

    dataName = 'nameOfNewFile'


    getTableData.WriteDataDatabase(data = data, dataName=dataName)


    subprocess.Popen(r'explorer /open, ' + FolderSaveLocation)

            


            #copy file to the locatio and file name above



            # add file from folder Loation to a folder that has the name of the area of the file


    # search on how to do string manipulation on pandas column '










SortFilesIntoFolders()




           
