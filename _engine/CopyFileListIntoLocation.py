import shutil
import os


InputLocation = r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\IgordaCosta-NodeJsElectronDemonstration\_engine'

OutputLocation = r'C:\Users\Tigereye\Desktop\TempFileCopyLocation'

extension = '.py'



InputFileList00= '''getTableData
  sys
  edDataPyimageFolderLocation    
  edDataPyexcelLocation    
  edDataPyinternalLocation    
  pdfToJpg
  PrintTexListSerial
              PyPDF2
 os   listdir
  edDataPyFilesInDatabaseLocation    
  os
  ListToSentence
  changeDirectory
 os path   isfile  join
  base93Characterconversion
  getTableData
  edDataPyupdateNamesFile    
  PrintTexListSerial
  sys
  StringToOrdList
  getTableData
  getTableData
  checkIfValueInText
  PrintTexListSerial
  createSqliteTableFromList
  re
  getTableData
  readSqlDatabase
  shutil 
  CloseEspecificWorkbook
  CreateRow
  StringListIntoList
  os
  writeToSqlite
  DeleteAllFilesInFolder
  getTableData
  pandas 
  readSqlDatabase
  copyImageToAppFolderFromPython
 PIL   Image
  copyImageToAppFolderFromPython
 PIL   ImageDraw 
  os
  pathlib
  MultiplyTextSizeByImageHeight
  getTableData
 PIL   ImageFont
  PrintTexListSerial
  os
  edDataPyinternalLocation    
  PrintTexListSerial
  GetAllFontNamesFromFolderFunction
  GetDbDataFunction
  DeleteAllTempFiles
  os
  getTableData
  createSqliteTableFromList
  dropSqlTable
  sys
  edFNUDataPyDTs    
  edDataPyDTs    
  getTableData
  DeleteAllTempFiles
  CloseEspecificWorkbook
  edDataPyexcelLocation    
  edDataPyinternalLocation    
  PrintTexListSerial
  openWorkbook
  os
  getTableData
  CloseEspecificWorkbook
  edDataPyexcelLocation    
  edDataPyinternalLocation    
  closeWordWithHelp
  openWorkbook
  createSqliteTableFromList
  dropSqlTable
  os
  getTableData
  win32com client as win32
  getTableData
  pdfToJpg
 PIL   Image
  RemoveExtraSlashes
  copyImageToAppFolderFromPython
 PIL   ImageDraw 
  StringListIntoList
  os
  pathlib
  MultiplyTextSizeByImageHeight
  getTableData
 PIL   ImageFont
  GetFontFilePaths
 PIL   Image
  copyImageToAppFolderFromPython
  os
 PIL   ImageDraw 
  MultiplyTextSizeByImageHeight
  getTableData
 PIL   ImageFont
  PrintTexListSerial
  getTableData
  re
  CloseEspecificWorkbook
  closeWordWithHelp
  PrintTexListSerial
 sqlite3 dbapi2   Error
  ForceCloseSpecificPaintFile
  os
  shutil
  changeDirectory
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


