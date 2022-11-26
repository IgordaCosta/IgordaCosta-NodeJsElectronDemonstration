import os
from os import listdir 
from os.path import isfile, join
import pandas
import pprint




def getFileListInLocationWithExtension(Location, extension):
    

    onlyFilesSpecified = [f for f in listdir(Location) if isfile(join(Location, f)) if f.split('.')[-1]==extension]

    # print(onlyFilesSpecified)

    return onlyFilesSpecified




def DeleteTheFirstOfTenTypeFiles(Location, extension):

    ListOfFiles = getFileListInLocationWithExtension(Location, extension)

    PdListOfFiles  = pandas.Series(ListOfFiles).sort_values().reset_index()


    PdAfterTenList = PdListOfFiles[:-10]

    # print(PdAfterTenList)

    # print(len(PdAfterTenList))

    if len(PdAfterTenList)>0:

        # print(len(PdAfterTenList))

        AfterTenList = PdAfterTenList[0].values.tolist()

        # pprint.pprint(AfterTenList)

        for item in AfterTenList:
            try:
                os.remove(Location + item)
            except:
                pass

    







# extension =  'txt'


# pprint.pprint(DeleteTheFirstOfTenTypeFiles(Location, extension))

