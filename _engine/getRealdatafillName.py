import pandas
# import pprint

import getTableData
import PrintTexListSerial




def getRealdatafillName():


    TableDataGotten = getTableData.GetTableData()

    checkedNumber = TableDataGotten['checkedNumber']

    ListToPrint = []

    # print(checkedNumber)


    # JobItemGotten = TableDataGotten['JobItemGotten']

    # pprint.pprint(JobItemGotten)

    TableName='FilesInDatabase'

    TableNumber = ''
    

    TableDataGotten2 = getTableData.GetTableDataFromTable(TableName=TableName ,TableNumber=TableNumber)

    # pprint.pprint(TableDataGotten2[0])
    # pprint.pprint(TableDataGotten2[0][0][1])


    # print(len(TableDataGotten2[0]))

    # pprint.pprint(TableDataGotten2[0][1][2])

    # pprint.pprint(TableDataGotten2[0][1][1]

    # print(datafillName)

    # print(type(TableDataGotten2))

    # df = pandas.DataFrame(TableDataGotten2[0])
    # print(df)

    # print(TableDataGotten2[1])

    columns = TableDataGotten2[1]

    df = pandas.DataFrame(TableDataGotten2[0], columns=columns)

    print(df)

    # print(df['Job Item'])

    # print(df['Job Item']==JobItemGotten)

    # ValueChecked = df['Job Item']==JobItemGotten


    # datafillName = df['Job Name'][ValueChecked].values[0]


    # datafillName = df['Job Name'][checkedNumber].values[0]

    # print(datafillName)


    datafillName = list(df['Job Name'])[int(checkedNumber)]

    Extension = str(list(df['File Saved Location'])[int(checkedNumber)].split('.')[-1]).lower()

    print(Extension)

    if Extension == 'pdf':
        PDFfile = 'true'
    
    else:
        PDFfile = 'false'

    data = PDFfile
    dataName = 'PDFfile'

    getTableData.WriteDataDatabase(data, dataName=dataName)

    

    # print(datafillName)

    ListToPrint.append(datafillName)


    PrintTexListSerial.PrintTexListSerial(ListToPrint=ListToPrint)










getRealdatafillName()