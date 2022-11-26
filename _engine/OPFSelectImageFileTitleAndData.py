import getTableData
import pdfToJpg



def OPFSelectImageFileTitleAndData():



    TableDataGotten=getTableData.GetTableData()


    FolderImageSaveLocation=TableDataGotten['FolderImageSaveLocation']


    newFileLocation = TableDataGotten['newFileLocation']

    
    fileName = newFileLocation.split('\\')[-1]


    # print('fileName: ', fileName)


    FolderLocation=newFileLocation.replace(fileName, "")


    # print('FolderLocation: ', FolderLocation)


    OutputFilename=fileName.replace('temp_', "")


    # print('OutputFilename: ',OutputFilename)
    
    # print('FolderImageSaveLocation :', FolderImageSaveLocation)


    FilesMadeList = pdfToJpg.pdfToJpg(FolderLocation=FolderLocation,PdfFileName=fileName,FolderSaveLocation=FolderImageSaveLocation, OutputFilename = OutputFilename)

    # print('FilesMadeList: ',FilesMadeList)



















    # finalLocationsX=TableDataGotten['finalLocationsX']

    # # print(finalLocationsX)

    # finalLocationsX=finalLocationsX.split(',')

    # print(finalLocationsX)

    # # NumberOfItens=len(finalLocationsX)

    # # print(NumberOfItens)





    # tableTitles=''
    # for i in range(len(finalLocationsX)):
    #     tableTitles=tableTitles+'''<th scope='col'>'''+str(i+1)+'''*</th>'''

    # # print(tableTitles)



    tableTitles=''
    for i in range(len(FilesMadeList)):
        tableTitles=tableTitles+'''<th scope='col'>'''+str(FilesMadeList[i])+'''</th>'''

    # print(tableTitles)








    # tableData=''
    # for i in range(len(finalLocationsX)):
    #     tableData=tableData+'''<td><div class='form-group thirdsize'><input type='text' class='form-control' id='validationTooltip0'''+str(i+1)+'''' placeholder='Type here the identifier'></div></td>'''

    # # print(tableData)




    tableData=''
    for i in range(len(FilesMadeList)):
        tableData=tableData+'''<td><div class='form-group thirdsize'><button type='button' id=' ''' +str(i)+ ''' ' class='btn2 btn-primary' onClick='ChoosenImage(this.id)'>''''Click to select '+str(FilesMadeList[i])+'''</button></div></td>'''

    # print(tableData)













    dataList= [tableTitles, tableData]
    
    dataNameList= ['tableTitles', 'tableData']



    getTableData.MultipleListWriteDataDatabase(dataList=dataList,dataNameList=dataNameList)














OPFSelectImageFileTitleAndData()