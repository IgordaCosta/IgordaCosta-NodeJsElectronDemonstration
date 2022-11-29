from os import walk
import pandas
import pprint


def getAllPrintLocations(extensionFilter = '', dataType = '', OtherString = ''):

    

    ContinueNow = False
    if extensionFilter == 'html':
        ContinueNow= True
        extensionChosen = 2
    if extensionFilter == 'js':
        ContinueNow= True
        extensionChosen = 1
    elif extensionFilter == 'py':
        ContinueNow= True
        extensionChosen = 0
    elif extensionFilter == 'results[':
        ContinueNow= True
        extensionChosen = 1

    elif str(extensionFilter) == '0':
        ContinueNow= True
        extensionChosen = 0

    elif str(extensionFilter) == '1':
        ContinueNow= True
        extensionChosen = 1
    elif str(extensionFilter) == '2':
        ContinueNow= True
        extensionChosen = 1
        dataType = 'results['
    elif str(extensionFilter) == '3':
        ContinueNow= True
        extensionChosen = 1
        dataType = 'DataGotten['
    elif str(extensionFilter) == '4':
        ContinueNow= True
        extensionChosen = 2
        dataType = OtherString

    else:
        pass


    # print(extensionFilter)
    
    
    if ContinueNow:
        extensionChoices = ['py','js','html']

        extensionFilter = extensionChoices[extensionChosen]


        mypath0= r'C:\Users\Tigereye\Desktop\pythonFilesBackup'

        mypath2 = r'C:\Users\Tigereye\Desktop\jsFilesBackup\js'

        # mypath = mypath0 + '\\'


        outputtxtPath0 = r'C:\Users\Tigereye\Desktop\PythonJSImportFiles'

        # print(extensionFilter)


        OutputFileName = ''
        if extensionFilter == 'py':
            mypath = mypath0 + '\\'
            OutputFileName= 'PythonUniqueImports.txt'
        elif extensionFilter == 'js':
            mypath = mypath2 + '\\'
            OutputFileName= 'JSuniqueImports.txt'
        elif extensionFilter == 'html':
            mypath = mypath2 + '\\'
            OutputFileName= 'HTMLuniqueImports.txt'
        else:
            pass


        print(extensionFilter)

        print(OutputFileName)



        outputtxtPath = outputtxtPath0 + '\\'



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

        print(ChosenExtensionList)


        importItems = []
        for filenameCheked in ChosenExtensionList:
            file1 = open(mypath + filenameCheked, 'r')
            Lines = file1.readlines()
            
            if extensionFilter == 'py':
                substring = 'print'
                blockedstring = '#'

            elif extensionFilter == 'js':
                if dataType == '':
                    if OtherString == '':
                        substring = 'console.log'

                    else:
                        substring = OtherString
                    
                elif dataType == 'results[':
                    substring = 'results['
                    OutputFileName= 'ResultuniqueImports.txt'

                elif dataType == 'DataGotten[':
                    substring = 'DataGotten['
                    OutputFileName= 'DataGottenuniqueImports.txt'                

                else:
                    pass
                             
                blockedstring = '//'

            elif extensionFilter == 'html':
                
                substring = OtherString
                blockedstring = '//'

            else:
                pass
        

            for line in Lines:
                if substring in line:
                    if blockedstring in line:
                        pass
                    else:
                        CheckValue = line.split(' ')[-1].replace('\n', '')
                        if CheckValue in ChosenItemList:
                            pass
                        else:
                            importItems.append(str(filenameCheked +'    ,     '+ line.strip())+ '\n')

        # pprint.pprint(importItems)

        UniqueDfItemsList = list(pandas.Series(importItems).unique())

        pprint.pprint(UniqueDfItemsList)
        
        # writing to file
        file1 = open(outputtxtPath + OutputFileName, 'w')
        file1.writelines(UniqueDfItemsList)
        file1.close()
        




OtherString = 'require(path'

extensionFilter = 'js'

getAllPrintLocations(extensionFilter = extensionFilter, OtherString = OtherString)
