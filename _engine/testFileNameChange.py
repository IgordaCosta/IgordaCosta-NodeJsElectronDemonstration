import base93Characterconversion



TempFolderLocation = r'C:\Users\Tigereye\Documents\AutoFormFillerFiles'
fileNameOnly = 'file.jpg'
FileEnding = base93Characterconversion.base93Characterconversion()


print(TempFolderLocation + "\\temp_" + '.'.join(str(fileNameOnly).split('.')[:-1]) + '_' + FileEnding + '.'+ str(fileNameOnly).split('.')[-1])