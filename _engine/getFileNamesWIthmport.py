import re
# from os import walk
import os
import shutil
import glob
import pprint






def PlaceNewDataInLocation(CopyFolder,extension):
    #risk of data damage
    SaveTempLocaion = r'C:\Users\Tigereye\Desktop\FileSearcholder\LocationOfFIles' + '\\' #  DO NOT CHANGE THIS

    outputTexPath = '\\'.join(str(SaveTempLocaion).split('\\')[:-2])+'\\TextLocation\\'
    try:
        shutil.rmtree(SaveTempLocaion)
    except:
        pass
    
    try:
        os.mkdir(SaveTempLocaion)
    except:
        pass

    try:
        os.mkdir(outputTexPath)
    except:
        pass

    # shutil.copytree(CopyFolder, SaveTempLocaion, dirs_exist_ok=True)


    files = glob.iglob(os.path.join(CopyFolder, "*."+ extension))
    for file in files:
        if os.path.isfile(file):
            shutil.copy2(file, SaveTempLocaion)

    return outputTexPath




# outputtxtPath0 = r'C:\Users\Tigereye\Desktop\PythonImportFiles'


# outputtxtPath0 = r'C:\Users\Tigereye\Desktop\JavascriptImportFIles'

# outputtxtPath = outputtxtPath0 + '\\'


# outputtxtPath = SaveTempLocaion

# extensionFilter = 'py'




def getFileNamesWIthmport (extensionFilter, TexToSearchOnAllFilleType):

    ImportLibrary=TexToSearchOnAllFilleType

    OktoGo = False
    #python folder location (original files location)
    if extensionFilter == 'py':
        OktoGo = True
        # PythonFle = True
        # mypath0= r'C:\Users\Tigereye\Desktop\pythonFilesBackup'
        CopyFolder0 =  r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2\CSSAutoFormFiller\_engine' #can change

        CopyFolder = CopyFolder0 + '\\'
        
    #javascript folder location (original files location)
    elif extensionFilter == 'js':
        OktoGo = True
        # PythonFle = False
        # mypath0= r'C:\Users\Tigereye\Desktop\jsFilesBackup\js'
        CopyFolder0 = r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2\CSSAutoFormFiller\js' # can change

        CopyFolder = CopyFolder0 + '\\'


    elif extensionFilter == 'html':

        OktoGo = True
        # PythonFle = False
        # mypath0= r'C:\Users\Tigereye\Desktop\jsFilesBackup\js'
        CopyFolder0 = r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2\CSSAutoFormFiller' # can change

        CopyFolder = CopyFolder0 + '\\'

    else:
        pass
        
    if OktoGo:
        outputtxtPath = PlaceNewDataInLocation(CopyFolder=CopyFolder,extension=extensionFilter)

        # mypath = mypath0 + '\\'


        mypath = CopyFolder

        IgnoreBlocks = True


        


        print(ImportLibrary)




        fileNameList = []
        for (dirpath, dirnames, filenames) in os.walk(mypath):
            fileNameList.extend(filenames)
            break


        # print(fileNameList)

        # print(extensionFilter)


        ChosenExtensionList = []
        for item in filenames:
            if item.split('.')[-1] == extensionFilter:
                ChosenExtensionList.append(item)

        # print(ChosenExtensionList)

        importItems = []
        for filenameCheked in ChosenExtensionList:
            file1 = open(mypath + filenameCheked, 'r')
            Lines = file1.readlines()
            
        
            # if PythonFle:
            if extensionFilter == 'py':
                blockedstring = '#'
            elif extensionFilter == 'js':
                blockedstring = '//'
            elif extensionFilter == 'html':
                blockedstring = '<!--'

            else:
                pass
            for line in Lines:
                if ImportLibrary in line:
                    if blockedstring in line:               
                        if IgnoreBlocks:
                            importItems.append(filenameCheked + '\n')
                        else:
                            pass              
                    else:
                        importItems.append(filenameCheked + '\n')

        pprint.pprint(importItems)


        
        # writing to file

        outputtxtPath

        file1 = open(outputtxtPath + 'docxImportsFiles.txt', 'w')
        file1.writelines(importItems)
        file1.close()


    




extensionFilter = 'js'



TexToSearchOnAllFilleType = 'CreateImageWithMarkerReturn'



getFileNamesWIthmport (extensionFilter, TexToSearchOnAllFilleType)