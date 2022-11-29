import shutil






FileList = [

"bootstrap.min",
"FileAlreadyExists",
"spinner",
"img",
"NoClick",
"bootstrap.min",
"DragnDrop",
"img",
"NoClick",
"AlertBox",
"spinner",
"bootstrap.min",
"FileAlreadyExists",
"NoClick",
"img",
"spinner2",
"NoClick",
"spinner",
"img",
"bootstrap.min",
"AlertBox",
"GetImageCoordinates",
"bootstrap.min",
"AlertBox",
"GetImageCoordinatesStep2",
"NoClick",
"img",
"spinner",
"bootstrap.min",
"mystyle",
"img",
"gotResultsIndexOut",
"NoClick",
"spinner",
"bootstrap.min",
"OpenedPdfFiles",
"spinner",
"img",
"NoClick",
"bootstrap.min",
"LMFchooseFolder",
"AlertBox",
"spinner",
"img",
"NoClick",
"bootstrap.min",
"addInfoToTheDocument",
"AlertBox",
"GetImageCoordinatesStep5mystyle",
"OPFSelectImageFile",
"NoClick",
"spinner",
"img",
"bootstrap.min",
"TypeJobName",
"AlertBox",
"NoClick",
"spinner"


]


LocationToCopy = r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2_AddToDatabase\CSSAutoFormFiller\IgordaCosta-NodeJsElectronDemonstration\css'

OutputLocation = r'C:\Users\Tigereye\Desktop\TempFileCopyLocation'

extensionUsed= '.css'


for fileToCopy in FileList:
    try:
        shutil.copy(LocationToCopy +'\\' + fileToCopy + extensionUsed, OutputLocation +'\\' + fileToCopy + extensionUsed)
    
    except:
        pass

