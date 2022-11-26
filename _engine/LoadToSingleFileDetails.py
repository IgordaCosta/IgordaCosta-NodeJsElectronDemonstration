from os import listdir
from os.path import isfile, join

import getTableData
import getAddressesFromColumn
import readSqlDatabase
import openWorkbook
import StringListIntoList




def LoadToSingleFileDetails():

    excelExtensions=['xlsx' ,'xlsm', 'xlsb', 'xlam' ,'xltx', 'xltm', 'xls', 'xla', 'xlt', 'xlm' ,'xlw']

    dictionary=getTableData.GetTableData()

    Folder=dictionary['FolderFileGottenLocation']

    datafillName=dictionary['datafillName']

    
    onlyfiles = [f for f in listdir(Folder) if isfile(join(Folder, f))]

    ExcelExtensionFile=[]

    for i in range(len(onlyfiles)):
        IsExcelExtension=any(x == onlyfiles[i].split(".")[-1] for x in excelExtensions)
        if IsExcelExtension:
            ExcelExtensionFile.append(onlyfiles[i])

    print(onlyfiles)

    print(ExcelExtensionFile)

    filesInFolder=ExcelExtensionFile

    print(filesInFolder)
    
    numberOfFilesinFolder=len(filesInFolder)
    print(numberOfFilesinFolder)
    
    databaseUsed0=readSqlDatabase.readSqlDatabase(table_name="KEY_"+datafillName)
    databaseUsed=databaseUsed0[0]
    
    print(databaseUsed)
    
    print("databaseUsed")
    
    itemAddress=databaseUsed.columns.values[1:]    
    print(itemAddress)
    
    itemDescription=databaseUsed.values[0][1:]
    print(itemDescription) 
    
    rowList, columnList=getAddressesFromColumn.getAddressesFromColumn(itemAddress=itemAddress)
    
    numberOfRows=numberOfFilesinFolder

    print(numberOfRows)

    ListUsed=[]

    rw=0


    print("open file in row to extract data")


    ListUsed.append([])
    
    xlfile=filesInFolder[rw]

    print(Folder)
    
    wb,excel,noError = openWorkbook.openWorkbook(Folder + xlfile)
    ws = wb.Sheets(1)

    
    itemAddress=str(itemAddress)

    StringList=itemAddress

    print(itemAddress)

    print('itemAddress before')

    
    itemAddress=StringListIntoList.StringListIntoList(StringList,brakets=True,Splitter=", ",SingleListCutAmount=2,DoubleListCutAmount=3,DoublesSeparator1="]' '[", DoublesSeparator2=", ",DoubleList=True)
    print(itemAddress)

    print("itemAddress above")
  
    print(len(itemAddress))

    print('len(itemAddress)')

    print(wb)

    print('wb')

    
    if wb!=None:
        print("wb!=None")
    
        for cl in range(1,len(itemAddress)+1):

            i=rowList[cl-1]
            c=columnList[cl-1]
            
            ValueSaved=ws.Cells(i,c).Value

            if ValueSaved==None:
                ValueSaved=''
            
            ListUsed[rw].append(ValueSaved)
        
        wb.Close(True)

    print(ListUsed)

    print('ListUsed above')

    rw=1

    NextFileToCome=filesInFolder[rw]

    numberOfStepsTotal=numberOfRows+1

    percentileComplete=int((rw/numberOfStepsTotal)*100)

    dataList= [filesInFolder, itemAddress, itemDescription, numberOfRows, rowList, columnList, rw, ListUsed, numberOfStepsTotal, percentileComplete, NextFileToCome ]
    dataNameList= ['filesInFolder', 'itemAddress', 'itemDescription', 'numberOfRows', 'rowList', 'columnList', 'rw', 'ListUsed', 'numberOfStepsTotal', 'percentileComplete', 'NextFileToCome' ]

    getTableData.MultipleListWriteDataDatabase(dataList,dataNameList)



LoadToSingleFileDetails()