from os import walk
import pandas
import pprint


# mypath0= r'C:\Users\Tigereye\Desktop\pythonFilesBackup'

# mypath = mypath0 + '\\'


outputtxtPath0 = r'C:\Users\Tigereye\Desktop\PythonImportFiles'

outputtxtPath = outputtxtPath0 + '\\'

extensionFilter = 'py'

filenames = [

r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\getAllmportedLibrariesFromFileList.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\getAllmportedLibraries.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\LoadToSingleFileDetails.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\AddToable.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\closeWordWithHelp.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\copyImageToAppFolderFromPython.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\createSqliteTableFromList.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\DeleteAllTempFiles.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\dropSqlTable.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\ForceCloseSpecificPaintFile.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\GetDbDataFunction.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\importedDataPyDTs.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\importedDataPyexcelLocation.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\importedDataPyFilesInDatabaseLocation.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\importedDataPyimageFolderLocation.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\importedDataPyinternalLocation.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\importedDataPyupdateNamesFile.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\importedFNUDataPyDTs.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\ListToSentence.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\MultiplyTextSizeByImageHeight.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\openWorkbook.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\pdfToJpg.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\PrintTexListSerial.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\readSqlDatabase.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\StringListIntoList.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\StringToOrdList.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\base93Characterconversion.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\changeDirectory.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\checkIfValueInText.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\CloseEspecificWorkbook.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\CheckJobNameRedo.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\OpenExcelDocument.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\CheckIfLocationWordinDoc.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\getAllmportedLibrariesFromFileList.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\GetOldStamp.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\OpenWordDocument.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\getRealdatafillName.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\RunDeleteAllTempFilesFromApp.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\AddToDatabase.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\CallgetDbData.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\copyImageToAppFolder.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\CreateImageWithMarker.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\GetDbData.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\insertIntoDatabase.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\getAllPrintLocations.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\FindMyDocumentsDatabasePath.py',
r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine\ReturnFromSameFileInside.py',

]



ChosenItemList = []
ChosenExtensionList = []
for item in filenames:
    if item.split('.')[-1] == extensionFilter:
        ChosenExtensionList.append(item)
        ChosenItemList.append(item.split('.')[-2])

# print(ChosenExtensionList)


importItems = []
for filenameCheked in ChosenExtensionList:
    file1 = open(filenameCheked, 'r')
    Lines = file1.readlines()
    
    
    substring = 'import '
    blockedstring = '#'
    for line in Lines:
        if substring in line:
            if blockedstring in line:
                pass
            else:
                CheckValue = line.split(' ')[-1].replace('\n', '')
                if CheckValue in ChosenItemList:
                    pass
                else:
                    importItems.append(line)

# pprint.pprint(importItems)

UniqueDfItemsList = list(pandas.Series(importItems).unique())

pprint.pprint(UniqueDfItemsList)
  
# writing to file
file1 = open(outputtxtPath + 'PythonUniqueImports.txt', 'w')
file1.writelines(UniqueDfItemsList)
file1.close()
  


