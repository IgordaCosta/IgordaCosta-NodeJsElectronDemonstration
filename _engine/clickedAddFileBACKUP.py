import pandas
import sys
import sqlite3
from sqlalchemy import create_engine
import shutil

import CreateRow
import getTableData
import StringListIntoList
import CloseEspecificWorkbook


def clickedAddFile(): #### call on this valuesList from database and remove calling from input

    #### the bellow data is for excel values
    #### it must find which direction to go from by getting the data that says
    #### if it is excel image or word (pdf files will be turned into a ground of image files saved in an location and to continue the user will need to select an image file)

    # valuesList=getTableData.GetDataFromDatabase(dataName='AddToTablevaluesList')

    # ExtensionType = getTableData.GetDataFromDatabase(dataName='ExtensionType')


    TableDataGotten = getTableData.GetTableData()


    ExtensionType = TableDataGotten['ExtensionType']

    valuesList = TableDataGotten['AddToTablevaluesList']


    if ExtensionType=='excel':

        listOfRows = TableDataGotten['listOfRows']

        listOfColumns  = TableDataGotten['listOfColumns']

        listOfRows=StringListIntoList.StringListIntoList(StringList=listOfRows)

        listOfColumns=StringListIntoList.StringListIntoList(StringList=listOfColumns)
    
        # listOfRows =getTableData.GetDataFromDatabase(dataName='listOfRows')

        # listOfColumns=getTableData.GetDataFromDatabase(dataName='listOfColumns')

    if ExtensionType=='image':

        listOfRows = TableDataGotten['finalLocationsY']


        listOfColumns  = TableDataGotten['finalLocationsX']

        listOfRows=StringListIntoList.StringListIntoList(StringList=listOfRows, Splitter=',')

        listOfColumns=StringListIntoList.StringListIntoList(StringList=listOfColumns, Splitter=',')

        # listOfRows=getTableData.GetDataFromDatabase(dataName='finalLocationsY')

        # listOfColumns=getTableData.GetDataFromDatabase(dataName='finalLocationsX')






    


    valuesList=StringListIntoList.StringListIntoList(StringList=valuesList, brakets=False, Splitter=",")


    print(listOfRows)
    print(listOfColumns)

    listOfValueNames=[]
    for i in range(len(listOfRows)):
        
        value="["+ str(listOfRows[i]) +", "+ str(listOfColumns[i])+"]"

        # value=StringListIntoList.StringListIntoList(StringList=value)

        print(value)

        print(type(value)) 

        listOfValueNames.append(value)




    

    print(listOfValueNames)
    print("listOfValueNames above")


    print(valuesList)
    print(type(valuesList))

    print(listOfValueNames[1])
    
    
    print('listOfValueNames[1]')

    print(type(listOfValueNames[1]))

    print('type(listOfValueNames[1])')


    print(valuesList[1])
    print('valuesList[1]')

    print(type(valuesList[1]))
    print('type(valuesList[1])')

    
    columns=listOfValueNames
    row=valuesList


    frame=CreateRow.CreateDataframeWithOneRow(columns=columns,row=row)

    print(frame)

    print("frame above++")


    

    



    newFileSavedLocation=getTableData.GetDataFromDatabase(dataName='newFileLocation0')
    datafillName=getTableData.GetDataFromDatabase(dataName='datafillName')
    
    


    print('newFileSavedLocation',newFileSavedLocation,flush=True)
    print('datafillName',datafillName,flush=True)
    print('listOfValueNames',listOfValueNames,flush=True)

    
    

    Skip=False

    SqlDatase=True

    UseExcel=False
    
    updateNamesFile='updateNamesFile'

    AllTables=getTableData.GetTableData()

    print(AllTables)

    FilesInDatabaseLocation='FilesInDatabase'
    
    # if SqlDatase==True:
    #     updateNamesFile=updateNamesFile.split('.')[0]
    #     FilesInDatabaseLocation=FilesInDatabaseLocation.split('.')[0]
    
    columnsFileinDatabase= ['Job Name', 'File KEY', 'File Saved Location']
    

        
    ExistsNan=True
    rsp=1
    
    # if UseExcel==True:
    #     UpdateValues=pandas.DataFrame(columns=listOfValueNames)
    #     Skip= self.OpenDeleteRecreateSheet(filename=updateNamesFile, frame=UpdateValues,columnList=listOfValueNames, SqlDatase=SqlDatase)
    #     if Skip==False:
    #         self.frameStyleByColor(path=updateNamesFile, columnsList=listOfValueNames, color='blue')
    #         os.startfile(updateNamesFile)
    
    Skip=False
    sizeFrame=len(listOfValueNames)
    # frame=['']*sizeFrame

    print("listOfValueNames bellow")

    print(listOfValueNames)
    
    
    # while rsp==1 and ExistsNan==True and Skip==False:
    #     print(rsp)
    #     print("rsp after while loop")
    #     print(ExistsNan)
    #     print("ExistisNan after while loop")
    #     print(Skip)
    #     print("Skip after while loop")
        
            
        
    #     rsp, frame=addInfoTable(frame=frame, columnNames=listOfValueNames)
    #     ExistsNan=Inframe(frame)

    # print(rsp)
    # print("rsp after while loop end")
    # print(ExistsNan)
    # print("ExistisNan after while loop end")
    # print(Skip)
    # print("Skip after while loop end")

                    
    # if rsp==QtWidgets.QDialog.Accepted:




    print("Ok now it starts updating data")
    
    # SheetName="KEY_" + datafillName.split('.')[0] + '.xlsx'    
    SheetName="KEY_" + datafillName.split('.')[0] 

    # if SqlDatase==True:
    #     SheetName=SheetName.split('.')[0]
    
    print(SheetName)

        
    
    #### TODO create excel file for sheet with only frame names
    print(listOfValueNames)
    print("the above is the list of columns")
    
    # storedValues=pandas.DataFrame(columns=listOfValueNames)
    
    print(frame)
    print('frame before for loop')
    # for i in range(len(listOfValueNames)):
    #     storedValues[listOfValueNames[i]]=[frame[i]]

    storedValues=frame
    
    print(storedValues)
    
    print("this is the endframe just created")
    Skip= OpenDeleteRecreateSheet(filename=SheetName, frame=storedValues,columnList=listOfValueNames, SqlDatase=SqlDatase)
    
    if Skip==False:
        
        InputData=[datafillName,SheetName,newFileSavedLocation]
        
        if SqlDatase==False:
            FilesInDatabaseExists=False
            try:
                FilesInDatabase=pandas.read_excel(FilesInDatabaseLocation)
                FilesInDatabaseExists=True
            except FileNotFoundError:
                print('database DOES NOT exist')
                FilesInDatabaseExists=False

        
        FilesInDatabase , FilesInDatabaseExists = readSqlDatabase(table_name=FilesInDatabaseLocation,columns=columnsFileinDatabase)
            
        if FilesInDatabaseExists==False:
            FilesInDatabase=pandas.DataFrame(columns=[])
            for i in range(len(columnsFileinDatabase)):
                #print(FilesInDatabase[columnsFileinDatabase[i]])
                FilesInDatabase[columnsFileinDatabase[i]]= pandas.Series(InputData[i])
        
        if FilesInDatabaseExists==True:
            # if IgonoreClicked:
            #     FilesInDatabase=FilesInDatabase[~(FilesInDatabase[columnsFileinDatabase[0]]==datafillName)]
            #     IgonoreClicked=False
            
            
            print("database exists")
            TempFilesInDatabase=pandas.DataFrame(columns=[])
            for i in range(len(columnsFileinDatabase)):
                #print(TempFilesInDatabase[columnsFileinDatabase[i]])
                TempFilesInDatabase[columnsFileinDatabase[i]]= pandas.Series(InputData[i])
                
            print(TempFilesInDatabase)
            FilesInDatabase=pandas.concat([FilesInDatabase,TempFilesInDatabase])
            
            FilesInDatabase["UPPER"]=FilesInDatabase[columnsFileinDatabase[0]].str.upper()

            pandas.DataFrame.sort_values(FilesInDatabase, by=["UPPER", columnsFileinDatabase[0],columnsFileinDatabase[1],columnsFileinDatabase[2]], inplace=True)
            
            print(FilesInDatabase)
            
        
        
        Skip= OpenDeleteRecreateSheet(filename=FilesInDatabaseLocation, frame=FilesInDatabase,columnList=columnsFileinDatabase, SqlDatase=SqlDatase)
        
        if Skip==False:

            # copy original file to desired folder location

            fileLocation=getTableData.GetDataFromDatabase(dataName='fileLocation')

            newFileLocation0=getTableData.GetDataFromDatabase(dataName='newFileLocation0')

            try:
                NewfinalSavedLocation=shutil.copy(fileLocation, newFileLocation0)
                print(NewfinalSavedLocation)
            except Exception as e:
                print(e)
                print("file not copied to new location, reason above")
                pass

            #### this closing file is for excel the program will get the variable telling which type of file it is and close the correct one this can be done in an separate python file for easy access
            #### and so this saving mecanism can be used in other areas and changed for all areas easilly
            CloseEspecificWorkbook.CloseEspecificWorkbook(fileName=newFileLocation0)

            
            # uploadDatabase(SqlDatase=True,FilesInDatabaseLocation=FilesInDatabaseLocation,columnsFileinDatabase=columnsFileinDatabase)
            
            print("DONE!!!")



    
def Inframe(frame):
        if '' in frame:
            ExistsNan=True
        else:
            ExistsNan=False
        return ExistsNan

def addInfoTable(frame, columnNames):
    DInfoTable = QtWidgets.QDialog()
    self.ui4 = Ui_DInfoTable()
    self.ui4.setupUi(DInfoTable)
    DInfoTable.show()
    
    
    self.ui4.tableWidget.setColumnCount(0)
    numColumn=len(columnNames)
    self.ui4.tableWidget.setColumnCount(numColumn)
    
    
    print(columnNames)
    print("columnNames in for loop")
    
    self.ui4.tableWidget.setHorizontalHeaderLabels(columnNames)
    for i in range(len(columnNames)):
        self.ui4.tableWidget.setItem(0, i, QTableWidgetItem(frame[i]))
    
    
    rsp=DInfoTable.exec_()
    
    if rsp==QtWidgets.QDialog.Accepted:
        frame=[]
        for i in range(len(columnNames)):
            print(self.ui4.tableWidget.item(0,i).text())
            CellValue=self.ui4.tableWidget.item(0,i).text()
            
            CellValue=CellValue.split()
            CellValue=" ".join(CellValue)
            
            frame.append(CellValue)
            
        print(frame)
        
        return rsp, frame
    else:
        return rsp, frame
    
    pass





    
def OpenDeleteRecreateSheet(filename,frame,columnList, SqlDatase=True, noColumnList=False):
    
    if SqlDatase==True:
        writeToSqlite(frame=frame, table_name=filename)
        Skip=False
        
    return Skip


def writeToSqlite(frame,table_name):
    DatabaseName="AutoFormFiller.db"

    conn = sqlite3.connect(DatabaseName)
    print(frame)
    frame.to_sql(table_name, conn, if_exists="replace")


def readSqlDatabase(table_name,columns=None):
    DatabaseName="AutoFormFiller.db"
    conn = create_engine('sqlite:///'+ DatabaseName)
    try:
        df2=pandas.read_sql_table(table_name, conn, columns=columns)
        #print(df2)
        TableFound=True
    except ValueError:
        df2=None
        TableFound=False
    return df2,TableFound




def uploadDatabase(SqlDatase,FilesInDatabaseLocation,columnsFileinDatabase):


    # FilesInDatabaseLocation=self.FilesInDatabaseLocation
    # columnsFileinDatabase=self.columnsFileinDatabase
    
        
    FileExists=False
    
        
    if SqlDatase==True:
        FilesInDatabase , FileExists = readSqlDatabase(table_name=FilesInDatabaseLocation,columns=columnsFileinDatabase)
        
    
    if FileExists==False:
        self.ui0.tableWidget.setRowCount(0)
        self.ui0.tableWidget.setRowCount(7)
        
        header=self.ui0.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Fixed)
        self.ui0.tableWidget.horizontalHeader().setDefaultSectionSize(132)
    
    if FileExists==True:
# =============================================================================
#             FilesInDatabase["UPPER"]=FilesInDatabase[columnsFileinDatabase[0]].str.upper()
#             
#             pandas.DataFrame.sort_values(FilesInDatabase, by=["UPPER", columnsFileinDatabase[0],columnsFileinDatabase[1],columnsFileinDatabase[2]], inplace=True)
#             FilesInDatabase=FilesInDatabase[columnsFileinDatabase]
# =============================================================================
        
        
        FilesInDatabase=FilesInDatabase[columnsFileinDatabase]
        
        NumbRowsPandas=len(FilesInDatabase.index)
        print(len(FilesInDatabase.index))
        print("len(FilesInDatabase.index)")
        
        if NumbRowsPandas ==0:
            #self.ui0.tableWidget.clearContents()
            self.ui0.tableWidget.setRowCount(0)
            self.ui0.tableWidget.setRowCount(7)
            
            header=self.ui0.tableWidget.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.Fixed)
            self.ui0.tableWidget.horizontalHeader().setDefaultSectionSize(132)

        else:
            print(FilesInDatabase)
            
            #self.ui.tableWidget.setRowCount(0)
            self.ui0.tableWidget.setRowCount(0)
            #self.ui.tableWidget.setRowCount(0)
            
            for rowNumber, rowData in enumerate(FilesInDatabase.values):
                self.ui0.tableWidget.insertRow(rowNumber)
                for columnNumber , data in enumerate(rowData):
                    #self.ui.tableWidget.insertColumn(columnNumber)
                    self.ui0.tableWidget.setItem(rowNumber, columnNumber, QtWidgets.QTableWidgetItem(str(data)))
            
            header=self.ui0.tableWidget.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
            
    pass










# valuesList = sys.argv[1]

clickedAddFile()