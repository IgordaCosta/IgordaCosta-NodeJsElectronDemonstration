import os
import CreateFolderInFolder
 

KDbFileExtensionListToDelete = [

    'xmv',
    'xlsx', 'xlsm', 'xlsb', 'xlam', 'xltx', 'xltm', 'xls', 'xla', 'xlt', 'xlm', 'xlw', 'csv',
    'jpg', 'jpeg', 'jpe', 'jfif', 'gif', 'tif', 'tiff', 'png', 'heic', 'bmp', 'dib',
    'pdf',
    'doc', 'docx', 'docm', 'dotx', 'dotm', 'dot', 'xps', 'rtf', 'odt'

]

FileExtensionListToDelete = [

    'db',
    'xmv',
    'xlsx', 'xlsm', 'xlsb', 'xlam', 'xltx', 'xltm', 'xls', 'xla', 'xlt', 'xlm', 'xlw', 'csv',
    'jpg', 'jpeg', 'jpe', 'jfif', 'gif', 'tif', 'tiff', 'png', 'heic', 'bmp', 'dib',
    'pdf',
    'doc', 'docx', 'docm', 'dotx', 'dotm', 'dot', 'xps', 'rtf', 'odt'

]

def DeleteAllFilesInFolder(LocationToDeleteFIles, KeepDB = False):
    if str(KeepDB) =='True':
        ExtensionToDelete = KDbFileExtensionListToDelete
    elif str(KeepDB) == 'False':
        ExtensionToDelete = FileExtensionListToDelete
    else:
        raise Exception("value not supported")

    CreateFolderInFolder.CreateFolderInFolder(LocationToDeleteFIles)

    for fileToDelete in os.listdir(LocationToDeleteFIles):
        if fileToDelete.split('.')[-1] in ExtensionToDelete:
            # print(fileToDelete)
            try:
                os.remove(os.path.join(LocationToDeleteFIles, fileToDelete))

            except PermissionError:
                pass
    




# LocationToDeleteFIles = r'C:\Users\Tigereye\Desktop\testDeleteFiles' +'\\'
# DeleteAllFilesInFolder(LocationToDeleteFIles)



