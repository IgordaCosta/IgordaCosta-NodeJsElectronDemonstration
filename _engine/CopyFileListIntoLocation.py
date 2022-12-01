import shutil
import os


InputLocation = r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\IgordaCosta-NodeJsElectronDemonstration\_engine'

OutputLocation = r'C:\Users\Tigereye\Desktop\TempFileCopyLocation'

extension = '.py'



InputFileList00= '''getTableData
 sys
             PyPDF2
 pdfToJpg
 os  listdir
 importedDataPyexcelLocation   
 changeDirectory
 base93Characterconversion
 PrintTexListSerial
 importedDataPyinternalLocation   
 importedDataPyupdateNamesFile   
 os path  isfile  join
 importedDataPyFilesInDatabaseLocation   
 getTableData
 importedDataPyimageFolderLocation   
 os
 ListToSentence
 sys
 StringToOrdList
 PrintTexListSerial
 getTableData
 getTableData
 checkIfValueInText
 createSqliteTableFromList
 PrintTexListSerial
 readSqlDatabase
 re
 getTableData
 shutil 
 CreateRow
 writeToSqlite
 DeleteAllFilesInFolder
 pandas 
 readSqlDatabase
 StringListIntoList
 CloseEspecificWorkbook
 os
 getTableData
 copyImageToAppFolderFromPython
 PIL  ImageDraw 
 copyImageToAppFolderFromPython
 MultiplyTextSizeByImageHeight
 pathlib
 PIL  Image
 getTableData
 PIL  ImageFont
 os
 PrintTexListSerial
 importedDataPyinternalLocation   
 os
 GetAllFontNamesFromFolderFunction
 PrintTexListSerial
 DeleteAllTempFiles
 GetDbDataFunction
 createSqliteTableFromList
 getTableData
 dropSqlTable
 os
 DeleteAllTempFiles
 sys
 importedFNUDataPyDTs   
 importedDataPyDTs   
 getTableData
 openWorkbook
 importedDataPyexcelLocation   
 PrintTexListSerial
 importedDataPyinternalLocation   
 CloseEspecificWorkbook
 getTableData
 os
 createSqliteTableFromList
 dropSqlTable
 openWorkbook
 importedDataPyexcelLocation   
 importedDataPyinternalLocation   
 CloseEspecificWorkbook
 closeWordWithHelp
 getTableData
 os
 win32com client as win32
 getTableData
 pdfToJpg
 PIL  ImageDraw 
 copyImageToAppFolderFromPython
 MultiplyTextSizeByImageHeight
 pathlib
 PIL  Image
 RemoveExtraSlashes
 StringListIntoList
 getTableData
 PIL  ImageFont
 os
 PIL  ImageDraw 
 copyImageToAppFolderFromPython
 MultiplyTextSizeByImageHeight
 PIL  Image
 GetFontFilePaths
 getTableData
 PIL  ImageFont
 os
 re
 PrintTexListSerial
 getTableData
 shutil
 sqlite3 dbapi2  Error
 changeDirectory
 PrintTexListSerial
 CloseEspecificWorkbook
 closeWordWithHelp
 os
 ForceCloseSpecificPaintFile
 getTableData
 DeleteObjFromTable
'''

InputFileList0 = InputFileList00.split('\n')


InputFileList = [item + extension for item in InputFileList0]



# fileNameList = []
# for (dirpath, dirnames, filenames) in os.walk(InputLocation):
#     fileNameList.extend(filenames)
#     break

for fileName in InputFileList:

    if fileName == '':
        pass

    else:

        CopyFromLocation = InputLocation + '\\' + fileName

        CopytToLocation = OutputLocation + '\\' + fileName
        try:
            RetunValue= shutil.copy(CopyFromLocation, CopytToLocation)
        
        except:
            pass

print('DONE')


