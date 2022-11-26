import numpy



import getTableData
import readSqlDatabase
import ChangeStartupDirectoryT
import PrintTexListSerial
# import openWorkbook






def GetItemAddressAndDescription():

    ListToPrint = []

    
    Folder="AutoFormFillerKey"

    ChangeStartupDirectoryT.ChangeStartupDirectory(Folder=Folder)

    # print('ok')
    


    TableGotten=getTableData.GetTableData()


    datafillName0=TableGotten['datafillName']

    
    spaceReplaceDataUserImput = '$%78&*&'

    # datafillName = datafillName0.replace(' ', spaceReplaceDataUserImput )

    datafillName = spaceReplaceDataUserImput.join(datafillName0.split(' '))

    data = datafillName

    dataName = 'datafillName'

    getTableData.WriteDataDatabase(data,dataName)

    
    print(datafillName)    


    databaseUsed0 = readSqlDatabase.readSqlDatabase(table_name="KEY_"+datafillName)

    

    databaseUsed=databaseUsed0[0]

    print(databaseUsed)

    itemAddress=list(databaseUsed.columns.values[1:])

    itemDescription0=databaseUsed.values[0][1:]


    spaceReplaceData = '$%3&*&'


    TempspaceReplaceData2 = '$%4&*&'


    

    # itemDescription = numpy.array(str(itemDescription0).replace('"','').replace("'",'').replace('[', '').replace(']', '').replace(' ', TempspaceReplaceData2).replace(spaceReplaceData, ' ').split(TempspaceReplaceData2))

    itemDescription = str(itemDescription0).replace('"','').replace("'",'').replace('[', '').replace(']', '').replace(' ', TempspaceReplaceData2).replace(spaceReplaceData, ' ').replace('\n', '').split(TempspaceReplaceData2)

    # print(itemDescription)

    databaseUsed1 = readSqlDatabase.readSqlDatabase(table_name='FontAndItsSize')

    # print(datafillName)

    # print(databaseUsed1[0])

    # print('databaseUsed1 above is printed')

    # print(databaseUsed1[0]['Job Name'])

    # print(databaseUsed1[0]['Job Name']==datafillName)

    # print(type(databaseUsed1[0]))


    # print(databaseUsed1[0]['Job Name']==datafillName)

    itemLocation = databaseUsed1[0]['Job Name']==datafillName

    # print(itemLocation)

    # print(databaseUsed1)

     

    # print(databaseUsed1[0]['FontName'][itemLocation])

    # print(list(databaseUsed1[0]['FontName'][itemLocation])[0])

    # print(list(databaseUsed1[0]['FontSize'][itemLocation])[0])





    fontName = list(databaseUsed1[0]['FontName'][itemLocation])[0]

    fontSize = list(databaseUsed1[0]['FontSize'][itemLocation])[0]


    PdfUsed = list(databaseUsed1[0]['PdfUsed'][itemLocation])[0]


    InPDFdatafillName0 = list(databaseUsed1[0]['InPDFdatafillName'][itemLocation])[0]
    

    
    
    InPDFdatafillName =  InPDFdatafillName0.replace(spaceReplaceDataUserImput, ' ')



    FromPdf = list(databaseUsed1[0]['FromPdf'][itemLocation])[0]
    

    ExtensionType = list(databaseUsed1[0]['ExtensionType'][itemLocation])[0]


    # FontSizeShow = list(databaseUsed1[0]['FontSizeShow'][itemLocation])[0]

    
    # print(FontSizeShow)
    
    # print(ExtensionType)

    # print(FromPdf)

    # print(PdfUsed)

    # print(InPDFdatafillName)
    
    # print(fontSize)

    # print(fontName)
 
    # print(itemAddress)

    # print(itemDescription)


    spaceReplaceDataUserImput = '$%78&*&'

    InPDFdatafillName0 = InPDFdatafillName

    InPDFdatafillName = ' '.join(InPDFdatafillName0.split(spaceReplaceDataUserImput))


    
    ShappedDatafillName =' '.join(datafillName.split(spaceReplaceDataUserImput))



    ListToPrint.append(ShappedDatafillName)

    # ListToPrint.append(FontSizeShow)
    ListToPrint.append(ExtensionType)
    ListToPrint.append(FromPdf)
    ListToPrint.append(PdfUsed)
    ListToPrint.append(InPDFdatafillName)
    ListToPrint.append(fontSize)
    ListToPrint.append(fontName)
    ListToPrint.append(itemAddress)
    ListToPrint.append(itemDescription)



    PrintTexListSerial.PrintTexListSerial(ListToPrint=ListToPrint)



GetItemAddressAndDescription()