



def MakeLinesInTxtUnique(Location,filenameChanged):
    file1 = open(Location + filenameChanged, 'r')
    ListOfTextLInes = file1.readlines()

    AcceptedLineList= list(set(ListOfTextLInes))

    file1 = open(Location + filenameChanged, 'w')
    file1.writelines(AcceptedLineList)
    file1.close()




outputtxtPath = r'C:\Users\Tigereye\Desktop\PythonJSImportFiles' + '\\'

OutputFileName = 'UniqueImportsShort.txt'

Location = outputtxtPath

filenameChanged = OutputFileName

MakeLinesInTxtUnique(Location,filenameChanged)