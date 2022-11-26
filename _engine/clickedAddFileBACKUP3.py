import pandas 
# import sys
import sqlite3
# from sqlalchemy import create_engine
import shutil 
import os

import CreateRow
import getTableData
import StringListIntoList
import CloseEspecificWorkbook

import changeDirectory
import readSqlDatabase
import writeToSqlite


def clickedAddFile(): #### call on this valuesList from database and remove calling from input

    #### the bellow data is for excel values
    #### it must find which direction to go from by getting the data that says
    #### if it is excel image or word (pdf files will be turned into a ground of image files saved in an location and to continue the user will need to select an image file)

 
    TableDataGotten = getTableData.GetTableData()

   
    ExtensionType = TableDataGotten['ExtensionType']

    valuesList = TableDataGotten['AddToTablevaluesList']


    if ExtensionType=='excel':

        listOfRows = TableDataGotten['listOfRows']

        listOfColumns  = TableDataGotten['listOfColumns']

        listOfRows=StringListIntoList.StringListIntoList(StringList=listOfRows)

        listOfColumns=StringListIntoList.StringListIntoList(StringList=listOfColumns)
    

    if ExtensionType=='image':


        listOfRows0 = TableDataGotten['finalLocationsYList']
  

        listOfColumns0  = TableDataGotten['finalLocationsXList']


        newFontSize = TableDataGotten['FontSize']

        newFont = TableDataGotten['newFont']


        # FontSizeShow = TableDataGotten['FontSizeShow']


        listOfRows = listOfRows0.replace("[",'').replace(" ",'').replace("]",'').replace("'",'').split(',')

        listOfColumns = listOfColumns0.replace("[",'').replace(' ','').replace("]",'').replace("'",'').split(',')


        
    valuesList=StringListIntoList.StringListIntoList(StringList=valuesList, brakets=False, Splitter=",")


    listOfValueNames=[]
    for i in range(len(listOfRows)):
        
        value="["+ str(listOfRows[i]) +", "+ str(listOfColumns[i])+"]"


        listOfValueNames.append(value)

    columns=listOfValueNames
    row=valuesList

    frame=CreateRow.CreateDataframeWithOneRow(columns=columns,row=row)


    newFileSavedLocation=getTableData.GetDataFromDatabase(dataName='newFileLocation0')
    datafillName=getTableData.GetDataFromDatabase(dataName='datafillName')


    UPPERdf = datafillName.upper()


    PDFfile=getTableData.GetDataFromDatabase(dataName='PDFfile')


    # print(PDFfile)


    Skip=False

    SqlDatase=True

    AllTables=getTableData.GetTableData()


    FilesInDatabaseLocation='FilesInDatabase'


    if ExtensionType=='image':
        
        if PDFfile == 'false':

            InPDFdatafillName = ''
            InPDFdatafillNameUPPER = ''
        

        if PDFfile == 'true':

            InPDFdatafillName=getTableData.GetDataFromDatabase(dataName='InPDFdatafillName')

            InPDFdatafillNameUPPER = InPDFdatafillName.upper()

           
    
    columnsFileinDatabase= ['Job Item', 'Job Name', 'File KEY', 'File Saved Location']

    Skip=False
 
     
    SheetName="KEY_" + datafillName.split('.')[0] 
    
    # print(SheetName)


    storedValues=frame
    
    # print(storedValues)
    
    Skip= OpenDeleteRecreateSheet(filename=SheetName, frame=storedValues,columnList=listOfValueNames, SqlDatase=SqlDatase)

    # print(Skip)

    # print(ExtensionType)

    # print(PDFfile)
    
    if Skip==False:

        if ExtensionType=='image':

                if PDFfile == 'false':

                    #this is where the Files in database table is created

                    PdfUsed =''

                    InPDFdatafillName = ''

                    JobItem = InPDFdatafillName + ' / ' + datafillName

                    InputDataList=[JobItem, datafillName,SheetName,newFileSavedLocation]

                    TableName=FilesInDatabaseLocation

                    columnsInDatabase=columnsFileinDatabase


                    # print(TableName)

                    # print(columnsInDatabase)

                    # print('columnsInDatabase above')


                    Skip = AddTabletoSql(InputDataList=InputDataList,TableName=TableName,columnsInDatabase=columnsInDatabase)


                if PDFfile == 'true':
                    

                    PdfUsed = getTableData.GetDataFromDatabase(dataName='PdfLocation') 

                    InPDFdatafillName=getTableData.GetDataFromDatabase(dataName='InPDFdatafillName')


                    JobItem = InPDFdatafillName + ' / ' + datafillName


                    InputDataList=[JobItem, datafillName,SheetName,newFileSavedLocation]

                    TableName=FilesInDatabaseLocation

                    columnsInDatabase=columnsFileinDatabase


                    # print(InputDataList)

                    # print(TableName)

                    # print(columnsInDatabase)


                    Skip = AddTabletoSql(InputDataList=InputDataList,TableName=TableName,columnsInDatabase=columnsInDatabase)


                else:
                    # print('something wrong PDFfile can only be true or false')
                    pass


        if Skip==False:
            if ExtensionType=='image':


                if PDFfile == 'false':

                    FromPdf = 'No'

                    InPDFdatafillName= ''


                    InPDFdatafillNameUPPER = ''

                    JobItem = InPDFdatafillName + ' / ' + datafillName



                    # print(FontSizeShow)

                    # print('FontSizeShow here above')


                    # InputDataList2=[JobItem, datafillName,SheetName,newFont,newFontSize, FromPdf, PdfUsed, InPDFdatafillName,ExtensionType, InPDFdatafillNameUPPER, FontSizeShow, UPPERdf]

                    InputDataList2=[JobItem, datafillName,SheetName,newFont,newFontSize, FromPdf, PdfUsed, InPDFdatafillName,ExtensionType, InPDFdatafillNameUPPER, UPPERdf]

                    TableName2='FontAndItsSize'

                    # columnsInDatabase2 =  ['Job Item', 'Job Name', 'File KEY', 'FontName', 'FontSize', 'FromPdf', 'PdfUsed', 'InPDFdatafillName','ExtensionType', 'InPDFdatafillNameUPPER', 'FontSizeShow', 'UPPER']

                    columnsInDatabase2 =  ['Job Item', 'Job Name', 'File KEY', 'FontName', 'FontSize', 'FromPdf', 'PdfUsed', 'InPDFdatafillName','ExtensionType', 'InPDFdatafillNameUPPER', 'UPPER']


                    Skip = AddTabletoSql(InputDataList=InputDataList2,TableName=TableName2,columnsInDatabase=columnsInDatabase2)
                    

                if PDFfile=='true':

                    FromPdf = 'Yes'


                    InPDFdatafillNameUPPER = InPDFdatafillName.upper()

                    
                    JobItem = InPDFdatafillName + ' / ' + datafillName


                    # print(datafillName)

                    # print('datafillName above')


                    # print(UPPERdf)


                    # print('UPPERdf above')


                    # InputDataList2=[JobItem, datafillName,SheetName,newFont,newFontSize, FromPdf, PdfUsed, InPDFdatafillName,ExtensionType, InPDFdatafillNameUPPER, FontSizeShow, UPPERdf]

                    InputDataList2=[JobItem, datafillName,SheetName,newFont,newFontSize, FromPdf, PdfUsed, InPDFdatafillName,ExtensionType, InPDFdatafillNameUPPER, UPPERdf]

                    TableName2='FontAndItsSize'

                    # columnsInDatabase2 =  ['Job Item', 'Job Name', 'File KEY', 'FontName', 'FontSize', 'FromPdf', 'PdfUsed', 'InPDFdatafillName','ExtensionType', 'InPDFdatafillNameUPPER', 'FontSizeShow', 'UPPER']

                    columnsInDatabase2 =  ['Job Item', 'Job Name', 'File KEY', 'FontName', 'FontSize', 'FromPdf', 'PdfUsed', 'InPDFdatafillName','ExtensionType', 'InPDFdatafillNameUPPER', 'UPPER']


                    Skip = AddTabletoSql(InputDataList=InputDataList2,TableName=TableName2,columnsInDatabase=columnsInDatabase2)
                
                

            if ExtensionType=='excel':


                # add for extension excel must have infill data = '' in the ones that does not apply


                pass

            if ExtensionType=='word':


                # add for extension word


                pass




                
            if Skip==False:

                # copy original file to desired folder location

                TableDataGotten = getTableData.GetTableData()




                if PDFfile=='true':
                    fileLocation = TableDataGotten['newFileLocationImg']


                    # print('pdfFIleSim')
                
                elif PDFfile=='false':
                    fileLocation = TableDataGotten['fileLocation']
                    # print('pdfFIleNo')
                else:
                    
                    fileLocation = TableDataGotten['fileLocation']

                    # print('pdfFIleError')


                # print("PDFfile? above")



                newFileLocation0 = TableDataGotten['newFileLocation0']

                try:
                    LocationToAddFileOnApp = TableDataGotten['LocationToAddFileOnApp']
                except KeyError:
                    pass


                # print(fileLocation)

                # print('fileLocation above')



                # print(newFileLocation0)

                # print('newFileLocation0 above')



                try:
                    NewfinalSavedLocation=shutil.copy(fileLocation, newFileLocation0)
                    # print(NewfinalSavedLocation)

                    # print(fileLocation)

                    # print('fileLocation svaed file above')
                except Exception as e:
                    # print(e)
                    # print("file not copied to new location, reason above")
                    pass

                #### this closing file is for excel the program will get the variable telling which type of file it is and close the correct one this can be done in an separate python file for easy access
                #### and so this saving mecanism can be used in other areas and changed for all areas easilly
                CloseEspecificWorkbook.CloseEspecificWorkbook(fileName=newFileLocation0)

                try:
                    #this is the image or pdf file being used temporatily to add data
                    #pdf will not be added here in this function
                    os.remove(LocationToAddFileOnApp)  
                except UnboundLocalError:
                    pass

                except FileNotFoundError:
                    pass


                # print("DONE!!!")




def AddTabletoSql(InputDataList,TableName,columnsInDatabase):

    InputData=InputDataList

    SqlDatase=True

    FilesInDatabase , FilesInDatabaseExists = readSqlDatabase.readSqlDatabase(table_name=TableName,columns=columnsInDatabase)

    # print(FilesInDatabase)

    # print(FilesInDatabaseExists)


    print(InputDataList)

    print('InputDataList above')

    print(TableName)

    print('TableName above')

    print(columnsInDatabase)

    print('columnsInDatabase above')



    if FilesInDatabaseExists==False:
        FilesInDatabase=pandas.DataFrame(columns=[])
        for i in range(len(columnsInDatabase)):

            FilesInDatabase[columnsInDatabase[i]]= pandas.Series(InputData[i])


        # print(FilesInDatabase)
    
    if FilesInDatabaseExists==True:
        
        # print("database exists")
        TempFilesInDatabase=pandas.DataFrame(columns=[])
        for i in range(len(columnsInDatabase)):

            TempFilesInDatabase[columnsInDatabase[i]]= pandas.Series(InputData[i])
            
        # print(TempFilesInDatabase)
        FilesInDatabase=pandas.concat([FilesInDatabase,TempFilesInDatabase])
        

        pandas.DataFrame.sort_values(FilesInDatabase, by=['Job Item']+columnsInDatabase,ignore_index=True, inplace=True)
        
        # print(FilesInDatabase)
        
    
    # print(TableName)

    # print(FilesInDatabase)

    # print(columnsInDatabase)

    # print(SqlDatase)
    
    Skip= OpenDeleteRecreateSheet(filename=TableName, frame=FilesInDatabase,columnList=columnsInDatabase, SqlDatase=SqlDatase)

    return Skip


    
def OpenDeleteRecreateSheet(filename,frame,columnList, SqlDatase=True, noColumnList=False):
    
    if SqlDatase==True:
        writeToSqlite.writeToSqlite(frame=frame, table_name=filename)
        Skip=False
        
    return Skip


# def writeToSqlite(frame,table_name):
#     DatabaseName="AutoFormFiller.db"

#     changeDirectory.ChangeTokey()

#     conn = sqlite3.connect(DatabaseName)
    
#     frame.to_sql(table_name, conn, if_exists="replace")










clickedAddFile()