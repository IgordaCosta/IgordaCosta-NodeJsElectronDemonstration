import shutil






FileList = [

"AddtoTablePromise",
"CreateImageWithMarkerStep5Return",
"CreateImageWithMarkerStep5Return",
"DragnDropMid",
"DragnDropMid",
"DragnDropMid0",
"DragnDropMid0",
"DragnDropMid0",
"getDbDataSimple",
"GetOldWordStamp",
"OPFSelectImageFile3",
"OPFSelectImageFile3",
"RunPythonFile",
"RunPythonFile",
"RunPythonFile",
"runReturnFromSameFileInside",
"runReturnFromSameFileInside",


]


LocationToCopy = r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\IgordaCosta-NodeJsElectronDemonstration\js'

OutputLocation = r'C:\Users\Tigereye\Desktop\TempFileCopyLocation'

extensionUsed= '.js'


for fileToCopy in FileList:
    try:
        shutil.copy(LocationToCopy +'\\' + fileToCopy + extensionUsed, OutputLocation +'\\' + fileToCopy + extensionUsed)
    
    except:
        pass

