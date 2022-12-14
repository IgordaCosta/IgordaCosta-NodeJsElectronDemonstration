import getTableData
import pdfToJpg



def OPFSelectImageFileTitleAndData():

    TableDataGotten=getTableData.GetTableData()

    FolderImageSaveLocation=TableDataGotten['FolderImageSaveLocation']

    newFileLocation = TableDataGotten['newFileLocation']
    
    fileName = newFileLocation.split('\\')[-1]

    FolderLocation=newFileLocation.replace(fileName, "")

    OutputFilename=fileName.replace('temp_', "")

    # print(FolderLocation)
    # print('FolderLocation')

    # print(fileName)
    # print('fileName')

    # print(FolderImageSaveLocation)
    # print('FolderImageSaveLocation')

    # print(OutputFilename)
    # print('OutputFilename')

    

    FilesMadeList = pdfToJpg.pdfToJpg(FolderLocation=FolderLocation,PdfFileName=fileName,FolderSaveLocation=FolderImageSaveLocation, OutputFilename = OutputFilename)

    

    # print(FilesMadeList)

    tableTitles=''
    for i in range(len(FilesMadeList)):
        tableTitles=tableTitles+'''<th scope='col'>'''+str(FilesMadeList[i])+'''</th>'''

    tableData=''
    for i in range(len(FilesMadeList)):
        tableData=tableData+'''<td><div class='form-group thirdsize'><button type='button' id=' ''' +str(i)+ ''' ' class='btn2 btn-primary' onClick='ChoosenImage(this.id)'>''''Click to select '+str(FilesMadeList[i])+'''</button></div></td>'''

    dataList= [tableTitles, tableData]
    
    dataNameList= ['tableTitles', 'tableData']

    getTableData.MultipleListWriteDataDatabase(dataList=dataList,dataNameList=dataNameList)












if __name__ == "__main__":  #added this

    OPFSelectImageFileTitleAndData()