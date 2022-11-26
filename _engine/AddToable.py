import sys


import getTableData





stringOfChars = sys.argv[1]


# print(stringOfChars)


# stringOfChars = r'[["pdf", "C:\Users\Tigereye\Desktop\PASSOS PARA ATIVAÇÃO DO …9 (2) (2) (1) (4) (1) (1) (1) (1) (4) (1) (1).pdf"], ["ExtensionType", "PdfLocation"], "None", "None", "C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2\CSSAutoFormFiller"]'

# stringOfChars = r'[["pdf", "C:\Users\Tigereye\Desktop\PASSOS PARA ATIVAÇÃO DO …9 (2) (2) (1) (4) (1) (1) (1) (1) (4) (1) (1).pdf"],["ExtensionType", "PdfLocation"], "None", "None", "C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2\CSSAutoFormFiller"]'


# stringOfChars = r"pdf,C:\Users\Tigereye\Desktop\PASSOS PARA ATIVA��O DO SEU OFFICE 2019 (2) (2) (1) (4) (1) (1) (1) (1) (4) (1) (1).pdf,ExtensionType,PdfLocation,None,None,C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2\CSSAutoFormFiller"




# stringOfChars = r'["C:\Users\Tigereye\Desktop\PASSOS PARA ATIVAÇÃO DO SEU OFFICE 2019 (2) (2) (1) (4) (1) (1) (1) (1) (4) (1) (1).pdf", "fileLocation", "None", "None", "C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2\CSSAutoFormFiller"]'



# stringOfChars = "[['data', 'data2'], ['dataName', dataName2'], 'TableName', 'Database', 'CurrentWorkingPath']"

# StringList = str(stringOfChars).replace("'",'').replace('"','').split('], ')

StringList = str(stringOfChars).replace("'",'').replace('"','').replace('], ','%*&@').replace('],','%*&@').split('%*&@')

# print(StringList)

ListSize = len(StringList)

# print(ListSize)

ValueList = ''
if ListSize == 1:

    StringList1 = StringList[0]

    StringList = StringList1.replace('[','').replace(']','').replace(', ', '#$@*').replace(',', '#$@*').split('#$@*')

    data = StringList[0]

    dataName = StringList[1]

    TableName = StringList[2]

    Database = StringList[3]

    # CurrentWorkingPath = StringList[4]

    ValueList = False

    # print(StringList)

    # print(StringList[4])


    # print(data)

    # print(dataName)

    # print(TableName) 

    # print(Database)

    # print(CurrentWorkingPath)




elif ListSize > 1:
    ValueList = True

    data = StringList[0].replace('[','').replace(', ', '#$@*').replace(',', '#$@*').split('#$@*')

    dataName = StringList[1].replace('[','').replace(', ', '#$@*').replace(',', '#$@*').split('#$@*')

    DataList = StringList[2].replace(']','').replace(', ', '#$@*').replace(',', '#$@*').split('#$@*')

    TableName = DataList[0]
    
    Database = DataList[1]

    # CurrentWorkingPath = DataList[2]

    # print(data)
    # print(dataName)

    # print(TableName)

    # print(Database)

    if len(dataName) == 1:
        # print(len(data))
        
        data1 = data

        data = data[0]
        dataName = dataName[0]

        ValueList = False

        if len(data1) > 1:
        
            data = ','.join(data1)


  
else:
    pass






# print(data)

# print(data[0])

# print(data[1])

# print(dataName)

# print(dataName[0])

# print(dataName[1])

# print(TableName) 

# print(Database)

# print(CurrentWorkingPath)

# print(ValueList)



if ValueList:

    dataNameList = dataName
    dataList = data


    getTableData.MultipleListWriteDataDatabase(dataList=dataList,dataNameList=dataNameList)

elif ValueList == False:


    getTableData.WriteDataDatabase(data=data,dataName=dataName)
    
else:
    pass






# print(data)
# print(dataName)

# print(TableName)

# print(Database)

            


