import os
import pandas

import ChangeStartupDirectoryT
import getTableData
import frameStyleByColor
import StringListIntoList

def LoadToSingleFileDetailsP3():

    FinalReturnValue=''

    dictionary=getTableData.GetTableData()
   
    ListUsed = dictionary['ListUsed']

    itemDescription= dictionary['itemDescription'] 

    FileFolder = dictionary['FolderSaveLocation']

    FinalFilename = dictionary['SavedFileName']

    filesInFolder = dictionary['filesInFolder']   

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

    print(itemDescription)

    print('itemDescription before above')

    itemDescription=StringListIntoList.StringListIntoList(StringList=itemDescription,Splitter=" ",SingleListCutAmount=2)


    print(itemDescription)

    print('itemDescription after above')


    print(itemDescription[0])

    print('itemDescription[0] after above')

    print(ListUsed)
    print("ListUsed values at the end")
    
    
    df = pandas.DataFrame(ListUsed, columns =itemDescription)
    df["Save Name"]=filesInFolder
    
    
    itemDescription=["Save Name"]+list(itemDescription)
    
    df=df[itemDescription]
    
    print(df)
    print("dataframe final")
    
    ChangeStartupDirectoryT.ChangeStartupDirectory(Folder=FileFolder)
    FileSaved=False 

    
    writer = pandas.ExcelWriter(FinalFilename)

    df.to_excel(writer,'Sheet1', index=False)
    
    try:
        writer.save()
        FileSaved=True
    except:

        ChangeStartupDirectoryT.ChangeStartupDirectory(Folder='AutoFormFillerKey')

        print("FileNotSaved")

        # FinalReturnValue='FileNotSaved'
    

    if FileSaved:
        frameStyleByColor.frameStyleByColor(path=FinalFilename, columnsList=itemDescription, color='blue')
        os.startfile(FinalFilename)
 
        path=os.path.realpath(FileFolder)
        os.startfile(path)

        ChangeStartupDirectoryT.ChangeStartupDirectory(Folder='AutoFormFillerKey')

        print("OperationCompleted")

        # FinalReturnValue='OperationCompleted'

    
    # print(FinalReturnValue)

    # data=FinalReturnValue
    
    # dataName='FinalReturnValue'


    # getTableData.WriteDataDatabase(data,dataName)






LoadToSingleFileDetailsP3()

    
    