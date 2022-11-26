import shutil






FileList = [

'oswalk',
'pandas',
'pprint',
'oslistdir',
'ospathisfile,join',
'getTableData',
'getAddressesFromColumn',
'readSqlDatabase',
'openWorkbook',
'StringListIntoList',
'sys',
'win32comclientaswin32',
'PrintTexListSerial',
'shutil',
'os',
'DeleteAllFilesInFolder',
'base93Characterconversion',
'sqlite3',
'changeDirectory',
'GetKeyfileNameType',
'RegularExpressionTextOrList',
'GetWriteDBTableSecured',
'importedDataPyFAutoForm_FillerFiles',
'importedDataPyimageFolderLocation',
'importedDataPyinternalLocation',
'importedDataPyAutoFormFillerKey',
'FilePathFromPython',
'sqlite3',
'ChangeStartupDirectoryT',
'GSn',
'cv2',
're',
'time',
'os',
're',
'sys',
'shutil',
'win32com',
'win32comclient',
'pdf2imageexceptions',
'pdf2imageconvert_from_path',
'PyPDF2',
'sqlalchemycreate_engine',
'PandasDfIntoSecureDb',
'IfSingleListMakeDoubleList',
'string',
'random',
'docxDocument',
'bs4BeautifulSoup',
'ForceCloseExcelFunction',
'createSqliteTableFromList',
'importedDataPyexcelLocation',
'CloseEspecificWorkbook',
'checkIfValueInText',
'dropSqlTable',
'closeWordWithHelp',
'DeleteAllTempFiles',
'importedDataPyFilesInDatabaseLocation',
'importedDataPyupdateNamesFile',
'ListToSentence',
'pdfToJpg',
'PyPDF2',
'StringToOrdList',
'copyImageToAppFolderFromPython',
'PILImage',
'PILImageFont',
'PILImageDraw',
'pathlib',
'MultiplyTextSizeByImageHeight',
'GetDbDataFunction',
'importedFNUDataPyDTs',
'importedDataPyDTs',
'sqlite3dbapi2Error',
'ForceCloseSpecificPaintFile'

]


LocationToCopy = r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\_engine'

OutputLocation = r'C:\Users\Tigereye\Desktop\TempFileCopyLocation'


for fileToCopy in FileList:
    try:
        shutil.copy(LocationToCopy +'\\' + fileToCopy + '.py', OutputLocation +'\\' + fileToCopy + '.py')
    
    except:
        pass

