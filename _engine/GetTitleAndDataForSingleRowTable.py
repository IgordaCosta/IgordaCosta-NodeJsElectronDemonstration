import getTableData



def GetTitleAndDataForSingleRowTable():



    TableDataGotten=getTableData.GetTableData()

    # print(TableDataGotten)

    finalLocationsX=TableDataGotten['finalLocationsX']

    # print(finalLocationsX)

    finalLocationsX=finalLocationsX.split(',')

    # print(finalLocationsX)

    # NumberOfItens=len(finalLocationsX)

    # print(NumberOfItens)

    tableTitles=''
    for i in range(len(finalLocationsX)):
        tableTitles=tableTitles+'''<th scope='col'>'''+str(i+1)+'''*</th>'''

    # print(tableTitles)


    tableData=''
    for i in range(len(finalLocationsX)):
        tableData=tableData+'''<td><div class='form-group thirdsize'><input type='text' class='form-control' id='validationTooltip0'''+str(i+1)+'''' placeholder='Type here the identifier'></div></td>'''

    # print(tableData)

    dataList= [tableTitles, tableData]
    
    dataNameList= ['tableTitles2', 'tableData2']



    getTableData.MultipleListWriteDataDatabase(dataList=dataList,dataNameList=dataNameList)














GetTitleAndDataForSingleRowTable()