import getTableData
import openWorkbook

import StringListIntoList

def LoadToSingleFileDetailsP2():

    dictionary=getTableData.GetTableData()
    
    rw = int(dictionary['rw'])

    numberOfRows = int(dictionary['numberOfRows'])

    if rw < numberOfRows:

        itemAddress = dictionary['itemAddress']

        rowList = dictionary['rowList']

        columnList= dictionary['columnList']

        ListUsed = dictionary['ListUsed']

        filesInFolder = dictionary['filesInFolder']

        Folder=dictionary['FolderFileGottenLocation']

        print(ListUsed)

        print('ListUsed above before')

        StringList=ListUsed

        DoublesSeparator1="], ["

        DoublesSeparator2=", "

        ListUsed=StringListIntoList.StringListIntoList(StringList=StringList,DoubleListCutAmount=2,DoublesSeparator1=DoublesSeparator1,DoublesSeparator2=DoublesSeparator2,DoubleList=True)

        print(ListUsed)

        print('ListUsed above')

        print(ListUsed[0][0])

        print('ListUsed[0][0] above')

        print(filesInFolder)

        print('filesInFolder above')

        filesInFolder=StringListIntoList.StringListIntoList(StringList=filesInFolder,Splitter=", ",SingleListCutAmount=2)

        print(filesInFolder)

        print('filesInFolder above')

        print(filesInFolder[0])

        print('filesInFolder[0] above')

        print('New filesInFolder above')


        print(ListUsed)

        print('ListUsed after made list above')

        ListUsed.append([])

        print(ListUsed)

        print("New ListUsed")

        print('rw =',rw)

        print(itemAddress)

        print('itemAddress before')


        DoublesSeparator1="], ["

        DoublesSeparator2=", "


        StringList=itemAddress

        
        itemAddress=StringListIntoList.StringListIntoList(StringList=StringList,brakets=True,Splitter=", ",SingleListCutAmount=2,DoubleListCutAmount=2,DoublesSeparator1=DoublesSeparator1, DoublesSeparator2=DoublesSeparator2,DoubleList=True)
        
        print(itemAddress)

        print("itemAddress after above")

        print(itemAddress[0][0])

        print('itemAddress[0][0] above')

        print(len(itemAddress))

        print("len(itemAddress) above")


        print(rowList)

        print('rowList before above')

        StringList=rowList

        rowList=StringListIntoList.StringListIntoList(StringList=StringList,brakets=True,Splitter=", ",SingleListCutAmount=1,DoubleListCutAmount=2,DoublesSeparator1="'], ['", DoublesSeparator2="', '",DoubleList=False)


        print(rowList)

        print('rowList after above')

        print(rowList[0])

        print('rowList[0] above')

        print(columnList)

        print('columnList before')

        StringList=columnList

        columnList=StringListIntoList.StringListIntoList(StringList=columnList,brakets=True,Splitter=", ",SingleListCutAmount=1,DoubleListCutAmount=2,DoublesSeparator1="'], ['", DoublesSeparator2="', '",DoubleList=False)
        
        print(columnList)

        print('columnList after')

        print(columnList[0])

        print('columnList[0] after')

        print(rw)

        print('rw above')

    
        xlfile=filesInFolder[rw]

        print(Folder)
        
        wb,excel,noError = openWorkbook.openWorkbook(Folder + xlfile)
        ws = wb.Sheets(1)

        if wb!=None:
            
            for cl in range(len(itemAddress)):

                print(cl)

                print('cl above')

                i=rowList[cl]
                c=columnList[cl]

                print(i)

                print('i above')

                print(c)

                print('c above')
                
                ValueSaved=ws.Cells(int(i),int(c)).Value

                if ValueSaved==None:
                    ValueSaved=''
                
                ListUsed[rw].append(ValueSaved)
            
            wb.Close(True)

        print(ListUsed)

        print('ListUsed above')
        
        rw=rw+1

        if rw<numberOfRows:
            NextFileToCome=filesInFolder[rw]
        else:
            NextFileToCome="Saving data to a file"

        numberOfStepsTotal=numberOfRows+1

        percentileComplete=int((rw/numberOfStepsTotal)*100)

        dataList= [rw, ListUsed, percentileComplete, NextFileToCome ]
        dataNameList= ['rw', 'ListUsed', 'percentileComplete', 'NextFileToCome' ]

        getTableData.MultipleListWriteDataDatabase(dataList,dataNameList)

        print('rw = ',rw)

        if numberOfRows==rw:

            print(NextFileToCome)

            print(rw)

            print(numberOfStepsTotal)

            print(percentileComplete)

            print("DoneGettingFileData")

        else:

            print(NextFileToCome)

            print(rw)

            print(numberOfStepsTotal)

            print(percentileComplete)

            print("InformationAdded")

    else:

        print(FinalSaveLocation)

        print(rw)

        print(numberOfStepsTotal)

        print(percentDone)

        print("DoneGettingFileData")







LoadToSingleFileDetailsP2()