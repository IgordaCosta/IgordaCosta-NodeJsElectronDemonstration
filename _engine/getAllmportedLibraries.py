from os import walk
import pandas
import pprint


mypath0= r'C:\Users\Tigereye\Desktop\pythonFilesBackup'

mypath = mypath0 + '\\'


outputtxtPath0 = r'C:\Users\Tigereye\Desktop\PythonImportFiles'

outputtxtPath = outputtxtPath0 + '\\'

extensionFilter = 'py'

fileNameList = []
for (dirpath, dirnames, filenames) in walk(mypath):
    fileNameList.extend(filenames)
    break

ChosenItemList = []
ChosenExtensionList = []
for item in filenames:
    if item.split('.')[-1] == extensionFilter:
        ChosenExtensionList.append(item)
        ChosenItemList.append(item.split('.')[-2])

# print(ChosenExtensionList)


importItems = []
for filenameCheked in ChosenExtensionList:
    file1 = open(mypath + filenameCheked, 'r')
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
  


