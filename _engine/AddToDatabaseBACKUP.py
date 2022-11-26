import os
# import glob
# import shutil
import sys

from os import listdir
from os.path import isfile, join

import changeDirectory
# import dropSqlTable
# import createSqliteTableFromList

import getTableData

import ListToSentence
# import FilePathFromPython

# import RemoveExtension


def AddToDatabase(fname=""):

    changeDirectory.ChangeTokey()



    # import pathlib
    
    # # print(pathlib.Path(__file__).parent.resolve())

    # # print('current working file path is above')

    # PyPath = pathlib.Path(__file__).parent.resolve()

    # CurrentWorkingPath = '\\'.join(str(PyPath).split('\\')[:-1])

    # # print(str(PyPath))

    # print(CurrentWorkingPath)

    # print('CurrentWorkingPath in python above')

    






    print(fname, flush=True)
    print('fname', flush=True)
    
    # UseExcel=False
    SqlDatase=True
    
    updateNamesFile='updateNamesFile.xlsx'
    
    FilesInDatabaseLocation='FilesInDatabase.xlsx'
    
    if SqlDatase==True:
        updateNamesFile=updateNamesFile.split('.')[0]
        FilesInDatabaseLocation=FilesInDatabaseLocation.split('.')[0]
    
    # columnsFileinDatabase=['Job Name', 'File KEY', 'File Saved Location']
    
    internalLocation='Documents'
    excelLocation='AutoFormFillerFiles'
    
    print("ok add file clicked")
    
    home = os.path.expanduser('~')
    
    print(home)
    
    filePath = os.path.join(home, internalLocation ,excelLocation)
    
    # location = os.path.join(home, internalLocation)
    
    
    # StartswithTemp=True
    
    # rsp=1

    print("done up to before qfiledialog")
    
    # ### this is the filename that was got from whe drag and drop window this data is not gotten here
    # while StartswithTemp==True and rsp==1:
        
    #     fname, _ = QFileDialog.getOpenFileName(self, 'Open a file to add to the database',location , "Excel Files (*.xl* *.xlsx *.xlsm *.xlsb *.xlam *.xltx *.xltm *.xls *.xla *.xlt *.xlm *.xlw)")
        
    #     print(fname)
        

    # ### this is data that was got from whe drag and drop window this data is not gotten here
    #     StartswithTemp=self.funcStartswithTemp(filename=fname)
        
    #     if StartswithTemp:
    #         rsp=self.FileCanNotStartWith()
    #         if rsp==0:
    #             fname=''



    ##### unblock from here below
    
    if fname !='':
        
        print(fname, flush=True)
        
        print("fname", flush=True)







        
        
        fname=fname.replace("\\","/")
        
        fileNameOnly=fname.split("/")[-1]
        # fileNameOnly=fname.split("\\")[-1]
        print(fileNameOnly, flush=True)
        print('fileNameOnly', flush=True)
        
        
        # filePath = os.path.join(home, 'Documents','AutoFormFillerFiles')

        InFileLocation, SenteceOpenFiles=CheckIfInFileLocation(fileToCheck=fileNameOnly, location=excelLocation)
        # CheckIfInFileLocation(fileToCheck=fileNameOnly, location=excelLocation)
        
        # newFileLocation=filePath +"\\temp_" + fileNameOnly

        try:
            os.makedirs(filePath +"\\Temp")
        except FileExistsError:
            # directory already exists
            pass

        # newFileLocation=filePath +"\\temp_" + fileNameOnly




        newFileLocation=filePath +"\\Temp\\temp_" + fileNameOnly



        newFileLocation0=filePath +"\\" + fileNameOnly

        Dictionary={'fname':fname, 'filePath':filePath, 'fileNameOnly':fileNameOnly ,'newFileLocation':newFileLocation,'newFileLocation0':newFileLocation0, 'FilesInDatabaseLocation':FilesInDatabaseLocation }





        DataToCheck = 'newFileLocation'   

        checkLocationOk = False  

        try:
            newFileLocation=getTableData.GetDataFromDatabase(DataToCheck)      

            checkLocationOk = True

        except:
            pass

        # except KeyError:
        #     print('all ok, there is no pdf')
        
        # except ValueError:
        #     print('all ok, there is no pdf')



        if checkLocationOk:

            # newFileLocationImg =  '\\'.join(newFileLocation0.split('\\')[-1]) + fileNameOnly


            #  newFileLocationImg = '\\'.join(newFileLocation.split('\\')[:-1])+'\\'


            newFileLocationImg =  filePath +"\\Temp\\" + fileNameOnly

            Dictionary={'fname':newFileLocation, 'filePath':filePath, 'fileNameOnly':fileNameOnly ,'newFileLocation':newFileLocation,'newFileLocation0':newFileLocation0, 'FilesInDatabaseLocation':FilesInDatabaseLocation, 'fileLocation': newFileLocation,  'newFileLocationImg': newFileLocationImg }

        
        if InFileLocation:
            print("there is the same file inside")

            print("SameFileInside")
            
            ##### change the window to one saying that file already exists and asking the user what to do
            ##### if the user answers favorable the function below will ran:
            ##### ReturnFromSameFileInside(fname=fname, filePath=filePath, fileNameOnly=fileNameOnly)
            # 
            #### message is bellow
            #### "Filename already exists in the database. Click OK to make a new rule for this file. Press CANCEL to quit this process. If this file is new, it needs to be renamed to continue without error. "
            #### else the user will be guided to inde.html 

            # print(fname)
            # print(filePath)
            # print(filePath)
            # print("FileAlreadyExist")


            # fname=ValueToBytes(str(fname))
            # filePath=ValueToBytes(str(filePath))
            # filePath=ValueToBytes(str(filePath))
            

            print(fname)
            print(filePath)
            print(fileNameOnly)
            print("FileAlreadyExist")

            FileExists='FileAlreadyExist'

            # Dictionary={'fname':fname, 'filePath':filePath, 'fileNameOnly':fileNameOnly ,'newFileLocation':newFileLocation,'newFileLocation0':newFileLocation0, 'FilesInDatabaseLocation':FilesInDatabaseLocation }

            Dictionary['FileExists']=FileExists

            getTableData.MultipleDictionaryWriteDataDatabase(DictionaryAdd=Dictionary)

            # getTableData.MultipleDictionaryWriteDataDatabase()


            


            # Dictionary={'fname':fname, 'filePath':filePath, 'fileNameOnly':fileNameOnly ,'FileExists':'FileAlreadyExist' }

            # Dictionary={'fname':fname, 'filePath':filePath, 'fileNameOnly':fileNameOnly ,'FileExists':'FileAlreadyExist','newFileLocation':newFileLocation,'newFileLocation0':newFileLocation0, 'FilesInDatabaseLocation':FilesInDatabaseLocation }

            # createSqliteTableFromList.SetValues(Dictionary=Dictionary)

            # NameLocationDictionary={'newFileLocation':newFileLocation}

            # createSqliteTableFromList.SetValues(TableName=SqlNameFileNameLocation, Dictionary=NameLocationDictionary)

            # NameLocationDictionary2={'newFileLocation0':newFileLocation0, 'FilesInDatabaseLocation':FilesInDatabaseLocation}

            print("done 1")

            print("FileAlreadyExist")

        else:

            # print(fname)
            # print(filePath)
            # print(fileNameOnly)
            # print("FileDoesNOTExist")


            # fname=ValueToBytes(str(fname))
            # filePath=ValueToBytes(str(filePath))
            # filePath=ValueToBytes(str(filePath))


            print(fname)
            print(filePath)
            print(fileNameOnly)
            print("FileDoesNOTExist")

            # Dictionary={'fname':fname, 'filePath':filePath, 'fileNameOnly':fileNameOnly ,'FileExists':'FileDoesNOTExist' }

            # Dictionary={'fname':fname, 'filePath':filePath, 'fileNameOnly':fileNameOnly ,'FileExists':'FileDoesNOTExist','newFileLocation':newFileLocation,'newFileLocation0':newFileLocation0, 'FilesInDatabaseLocation':FilesInDatabaseLocation }

            Dictionary['FileExists']='FileDoesNOTExist'

            # createSqliteTableFromList.SetValues(Dictionary=Dictionary)


            print(Dictionary)

            print('Dictionary to write above')


            getTableData.MultipleDictionaryWriteDataDatabase(DictionaryAdd=Dictionary)


            print(Dictionary)

            print("done 1")

            print("FileDoesNOTExist")
            
            # ReturnFromSameFileInside(fname=fname, filePath=filePath, fileNameOnly=fileNameOnly)
##### Above blocked for now


            
            # rsp=self.fileAlreadyExits()
            
            #if the user answers favorably her goes here

            # if rsp==1:
                
            #     newFileLocation0=filePath +"\\" + fileNameOnly
            #     print(newFileLocation0)
            
            #     print("newFileLocation not coppied")
            
            #     newFileLocation=filePath +"\\temp_" + fileNameOnly
            #     print(newFileLocation)
                
            #     print("newFileLocation")
            #     copiedDoc=False
            #     rsp=1
            #     while copiedDoc==False and rsp==1:
            #         try:
            #             shutil.copy2(fname, newFileLocation)
            #             copiedDoc=True
            #         except PermissionError:

            #             ####  the program window will change with the message below asking the user for assisstance after the save the program goes to a different window
            #             #### "There is a program dependent document that is currently opened and altered. Save or close this document and click OK to continue or click CANCEL to cancel the operation."
                        
            #             # rsp=self.InicioSalveDocumento()
                    
            # else:
            #     fname=''
            
        # else:

            # print("add file to this folder")
            
            # newFileLocation0=filePath +"\\" + fileNameOnly
            # print(newFileLocation0)
            
            # print("newFileLocation")
            
            # shutil.copy2(fname, newFileLocation0)
            
            # newFileLocation=filePath +"\\temp_" + fileNameOnly
            # print(newFileLocation)
            
            # print("newFileLocation")
            # copiedDoc=False
            # rsp=1
            # while copiedDoc==False and rsp==1:
            #     try:
            #         shutil.copy2(fname, newFileLocation)
            #         copiedDoc=True
            #     except PermissionError:

            #         ####  the program window will change with the message below asking the user for assisstance after the save the program goes to a different window
            #         #### "There is a program dependent document that is currently opened and altered. Save or close this document and click OK to continue or click CANCEL to cancel the operation."
            #         # rsp=self.InicioSalveDocumento()
            # pass
            
        # if rsp==1:
        #     if fname=='':
        #         print("cancel button clicked")
            
        #     else:
                # datafillName, FilesInDatabaseExists, rsp2=CheckJobNameRedo(SqlDatase=SqlDatase, FilesInDatabaseLocation=FilesInDatabaseLocation, columnsFileinDatabase=columnsFileinDatabase)
                # try:
                #     if IgonoreClicked: 
                #         rsp2=1
                # except:
                #     pass
                
                # if rsp2==1:
                    
                #     #### This is to rewrite the files name
                #     rsp=0

# def AddToDatabase2(FilesInDatabaseLocation,columnsFileinDatabase,datafillName):


#     datafillName, FilesInDatabaseExists, rsp2=CheckJobNameRedo(SqlDatase=True, FilesInDatabaseLocation=FilesInDatabaseLocation, columnsFileinDatabase=columnsFileinDatabase,datafillName=datafillName)

#     print(datafillName)
#     print(FilesInDatabaseExists)
#     print(rsp2)

# def AddToDatabase3(FilesInDatabaseLocation,columnsFileinDatabase,newFileLocation, newFileLocation0,datafillName, FilesInDatabaseExists):
                        
#                         print("before openWorkbook")
                        
#                         wb = openWorkbook(newFileLocation)
                        
#                         print("after openWorkbook")
                    
#                         if wb!=None:
                        
#                             NumList=0
#                             rsp=1
                            
#                             while NumList==0 and rsp==1:



#                                 #### create copy and paste window
#                                 # rsp=self.CopyPasteWindow()
                                
#                                 NumList, listOfValueNames, rsp =checkListValues(excelFileLocation=newFileLocation, workbook=wb, rsp=rsp)
                                
#                                 print(NumList)
                                
#                             if rsp==1:
                                
#                                 print("list has more then one value")
                                
#                                 clickedAddFile(FilesInDatabaseLocation=FilesInDatabaseLocation,columnsFileinDatabase=columnsFileinDatabase,listOfValueNames=listOfValueNames, newFileSavedLocation=newFileLocation0, UseExcel=False, SqlDatase=True, datafillName=datafillName,FilesInDatabaseExists=FilesInDatabaseExists)
                                 
                   



# def ReturnFromSameFileInside(fname,filePath,fileNameOnly):

#     newFileLocation0=filePath +"\\" + fileNameOnly
#     print(newFileLocation0)

#     print("newFileLocation not coppied")

#     newFileLocation=filePath +"\\temp_" + fileNameOnly
#     print(newFileLocation)
    
#     print("newFileLocation")
#     copiedDoc=False
#     rsp=1
#     ####################### while copiedDoc==False and rsp==1: keep blocked

    
#     #### blocked from below this
#     try:
#         shutil.copy2(fname, newFileLocation)
#         copiedDoc=True
#         # print(copiedDocTrue)
#     except PermissionError:
#         copiedDoc=False
#         ####  the program window will change with the message below asking the user for assisstance after the save the program goes to a different window
#         #### "There is a program dependent document that is currently opened and altered. Save or close this document and click OK to continue or click CANCEL to cancel the operation."
#         # print(copiedDocFalse)
#     print(copiedDoc)
#     print(newFileLocation0)
#         # rsp=self.InicioSalveDocumento()

# def clickedAddFile(FilesInDatabaseLocation,columnsFileinDatabase,listOfValueNames, newFileSavedLocation, SqlDatase, datafillName, FilesInDatabaseExists, UseExcel=True):
#         Skip=False

#         UseExcel=False
        
#         updateNamesFile='updateNamesFile.xlsx'
#         #### add below object to above anterior function
#         # FilesInDatabaseLocation=self.FilesInDatabaseLocation
        
#         if SqlDatase==True:
#             updateNamesFile=updateNamesFile.split('.')[0]
#             FilesInDatabaseLocation=FilesInDatabaseLocation.split('.')[0]
        
#         #### add below object to above anterior function
#         # columnsFileinDatabase=self.columnsFileinDatabase
          
#         ExistsNan=True
#         rsp=1
        
#         if UseExcel==True:
#             UpdateValues=pandas.DataFrame(columns=listOfValueNames)
#             Skip= OpenDeleteRecreateSheet(filename=updateNamesFile, frame=UpdateValues,columnList=listOfValueNames, SqlDatase=SqlDatase)
#             if Skip==False:
#                 frameStyleByColor(path=updateNamesFile, columnsList=listOfValueNames, color='blue')
#                 os.startfile(updateNamesFile)
#         if UseExcel==False:
#             Skip=False
#             sizeFrame=len(listOfValueNames)
#             frame=['']*sizeFrame
            
#         while rsp==1 and ExistsNan==True and Skip==False:
#             print(rsp)
#             print("rsp after while loop")
#             print(ExistsNan)
#             print("ExistisNan after while loop")
#             print(Skip)
#             print("Skip after while loop")
                            
#             if UseExcel==False:
#                 #### create a window with a row for every excel cel filled
#                 # rsp, frame=addInfoTable(frame=frame, columnNames=listOfValueNames)
#                 # ExistsNan=Inframe(frame)
#                 pass

#         print(rsp)
#         print("rsp after while loop end")
#         print(ExistsNan)
#         print("ExistisNan after while loop end")
#         print(Skip)
#         print("Skip after while loop end")

                        
#         if rsp==QtWidgets.QDialog.Accepted:
#             print("Ok now it starts updating data")
            
#             SheetName="KEY_" + datafillName.split('.')[0] + '.xlsx'    

#             if SqlDatase==True:
#                 SheetName=SheetName.split('.')[0]
            
#             print(SheetName)
                            
#             if UseExcel==False:
                
#                 print(listOfValueNames)
#                 print("the above is the list of columns")
                
#                 storedValues=pandas.DataFrame(columns=listOfValueNames)
                
#                 print(frame)
#                 print('frame before for loop')
#                 for i in range(len(listOfValueNames)):
#                     storedValues[listOfValueNames[i]]=[frame[i]]
                
#                 print(storedValues)
                
#                 print("this is the endframe just created")
#                 Skip= OpenDeleteRecreateSheet(filename=SheetName, frame=storedValues,columnList=listOfValueNames, SqlDatase=SqlDatase)
            
#             if Skip==False:
                
#                 InputData=[datafillName,SheetName,newFileSavedLocation]
                
                
                
                
#                 if SqlDatase==False:
#                     FilesInDatabaseExists=False
#                     try:
#                         FilesInDatabase=pandas.read_excel(FilesInDatabaseLocation)
#                         FilesInDatabaseExists=True
#                     except FileNotFoundError:
#                         print('database DOES NOT exist')
#                         FilesInDatabaseExists=False

                
#                 if SqlDatase==True:
#                     FilesInDatabase , FilesInDatabaseExists = self.readSqlDatabase(table_name=FilesInDatabaseLocation,columns=columnsFileinDatabase)
                    
#                 if FilesInDatabaseExists==False:
#                     FilesInDatabase=pandas.DataFrame(columns=[])
#                     for i in range(len(columnsFileinDatabase)):
#                         #print(FilesInDatabase[columnsFileinDatabase[i]])
#                         FilesInDatabase[columnsFileinDatabase[i]]= pandas.Series(InputData[i])
                
#                 if FilesInDatabaseExists==True:
#                     #### add below object to above anterior function
#                     if self.IgonoreClicked:
#                         FilesInDatabase=FilesInDatabase[~(FilesInDatabase[columnsFileinDatabase[0]]==datafillName)]
#                         self.IgonoreClicked=False
                    
                    
#                     print("database exists")
#                     TempFilesInDatabase=pandas.DataFrame(columns=[])
#                     for i in range(len(columnsFileinDatabase)):
#                         #print(TempFilesInDatabase[columnsFileinDatabase[i]])
#                         TempFilesInDatabase[columnsFileinDatabase[i]]= pandas.Series(InputData[i])
                        
#                     print(TempFilesInDatabase)
#                     FilesInDatabase=pandas.concat([FilesInDatabase,TempFilesInDatabase])
                    
#                     FilesInDatabase["UPPER"]=FilesInDatabase[columnsFileinDatabase[0]].str.upper()
    
#                     pandas.DataFrame.sort_values(FilesInDatabase, by=["UPPER", columnsFileinDatabase[0],columnsFileinDatabase[1],columnsFileinDatabase[2]], inplace=True)
#                     #FilesInDatabase=FilesInDatabase[columnsFileinDatabase]
                    

#                     print(FilesInDatabase)
                    
                
                
#                 Skip= OpenDeleteRecreateSheet(filename=FilesInDatabaseLocation, frame=FilesInDatabase,columnList=columnsFileinDatabase, SqlDatase=SqlDatase)
                
#                 if Skip==False:
                    
#                     uploadDatabase(SqlDatase=SqlDatase)
                    
#                     ##### Create an operation concluded window
#                     # self.OperaConcluidaWindow()



                 


# def OpenDeleteRecreateSheet(filename,frame,columnList, SqlDatase=True, noColumnList=False):
    
#         Skip=False
#         if SqlDatase==False:
#                     Skip=preOpenDeleteRecreateSheet(filename=filename,frame=frame,columnList=columnList, noColumnList=noColumnList)
                    
#         if SqlDatase==True:
#             writeToSqlite(frame=frame, table_name=filename)
#             Skip=False
            
#         return Skip
    
        
# def preOpenDeleteRecreateSheet(filename,frame,columnList, noColumnList):
    
#     ### Open delete sheet so it can be saved later below 2
#     Skip=False
#     rsp=1
    
#     writer = pandas.ExcelWriter(filename)
#     print('check 111111')
#     try:   
#         wb=openpyxl.load_workbook(filename)
#         print('check 222222')
#         sheetloaded=True
#     except:
#         sheetloaded=False
#         ProblemSaving=False
#         pass
    
#     if sheetloaded==True:    
#         print('check 222333')
#         del wb['Sheet1']
#         print('check 333333')
        
#         try:
#             writer.save()
#             ProblemSaving=False
#         except:
#             ProblemSaving=True
            
#     if ProblemSaving==True:
#         #xl = Dispatch('Excel.Application')
#         Skip=False
        
#         SkipWhileLoop=False
#         secondException=False
#         while SkipWhileLoop==False and Skip==False:
#             print("start loop SkipWhileLoop==False")
#             try:
#                 xl = Dispatch('Excel.Application')
#                 wb = xl.Workbooks(filename)
#                 SkipWhileLoop=True
#                 Skip=False
#             except Exception as e:
#                 print(e)
#                 f=str(e)
#                 print(type(f))
#                 print(f)
#                 g=''
#                 try: 
#                     g=e.args[1]
#                     if g== 'Exception occurred.':
#                         secondException=True

#                 except Exception as d:
#                     print(d)
#                     print("exeption of exception")
#                     pass
                
#                 if  f=="Excel.Application.Workbooks":
#                     rsp=self.InicioSalveDocumento()

#                 if rsp==QtWidgets.QDialog.Accepted:
#                     Skip=False
#                     SkipWhileLoop=False
#                     if secondException:
#                         print("secondException=True runned")
#                         SkipWhileLoop=True
#                     pass
                
#                 if rsp==0:
#                     Skip=True
#                     SkipWhileLoop=False

#         if Skip==False:
#             if secondException==False:
#                 writer.save()
#                 wb.Close(True)
# ##### Open delete sheet so it can be saved later above 2
    
#     if Skip==False:
        
#         writer = pandas.ExcelWriter(filename)
        
#         print(frame)
#         print('frame before column filtering')
        
#         #### noColumnList=False added so columnlistfilter can be ignored
#         if noColumnList==False:
#             frame=frame[columnList]
        
#         print(frame)
#         print("frame with unamed")

#         frame.drop(frame.columns[frame.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
#         print("step 1111111" )
#         #frame.to_excel(writer,'Sheet1', index=False)
#         frame.to_excel(writer, index=False)
#         print("step 22222222" )
#         try:
            
#             writer.save()
#             print("step 333333333" )
#         except PermissionError:
#             xl = Dispatch('Excel.Application')
#             print("step 44444444444" )
#             wb = xl.Workbooks(filename)
#             print("step 55555555" )
#             # do some stuff
#             wb.Close(True) # save the workbook
#             print("step 66666666" )
#             writer.save()
#             print("step 777777777" )
    
#         print(Skip)
#         print("skip")
    
#     return Skip


# def writeToSqlite(frame,table_name,DatabaseName):
#         conn = sqlite3.connect(DatabaseName)
#         print(frame)
#         frame.to_sql(table_name, conn, if_exists="replace")

# def uploadDatabase(SqlDatase,FilesInDatabaseLocation,columnsFileinDatabase):
#         # FilesInDatabaseLocation=self.FilesInDatabaseLocation
#         # columnsFileinDatabase=self.columnsFileinDatabase
        
#         if SqlDatase==True:
#             FilesInDatabaseLocation=FilesInDatabaseLocation.split('.')[0]
        
#         FileExists=False
        
#         if SqlDatase==False:
#             try:
#                 FilesInDatabase=pandas.read_excel(FilesInDatabaseLocation)
#                 FileExists=True
                
#             except FileNotFoundError:
#                 FileExists=False
#                 #self.ui0.tableWidget.clearContents()
#     # =============================================================================
#     #             self.ui0.tableWidget.setRowCount(0)
#     #             self.ui0.tableWidget.setRowCount(7)
#     #             
#     #             header=self.ui0.tableWidget.horizontalHeader()
#     #             header.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
#     #             header.setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)
#     #             header.setSectionResizeMode(2, QtWidgets.QHeaderView.Fixed)
#     #             self.ui0.tableWidget.horizontalHeader().setDefaultSectionSize(132)
#     # =============================================================================
                
#             pass
        
#         if SqlDatase==True:
#             FilesInDatabase , FileExists = self.readSqlDatabase(table_name=FilesInDatabaseLocation,columns=columnsFileinDatabase)
            
        
#         if FileExists==False:
#             self.ui0.tableWidget.setRowCount(0)
#             self.ui0.tableWidget.setRowCount(7)
            
#             header=self.ui0.tableWidget.horizontalHeader()
#             header.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
#             header.setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)
#             header.setSectionResizeMode(2, QtWidgets.QHeaderView.Fixed)
#             self.ui0.tableWidget.horizontalHeader().setDefaultSectionSize(132)
        
#         if FileExists==True:
# # =============================================================================
# #             FilesInDatabase["UPPER"]=FilesInDatabase[columnsFileinDatabase[0]].str.upper()
# #             
# #             pandas.DataFrame.sort_values(FilesInDatabase, by=["UPPER", columnsFileinDatabase[0],columnsFileinDatabase[1],columnsFileinDatabase[2]], inplace=True)
# #             FilesInDatabase=FilesInDatabase[columnsFileinDatabase]
# # =============================================================================
            
            
#             FilesInDatabase=FilesInDatabase[columnsFileinDatabase]
            
#             NumbRowsPandas=len(FilesInDatabase.index)
#             print(len(FilesInDatabase.index))
#             print("len(FilesInDatabase.index)")
            
#             if NumbRowsPandas ==0:
#                 #self.ui0.tableWidget.clearContents()
#                 # self.ui0.tableWidget.setRowCount(0)
#                 # self.ui0.tableWidget.setRowCount(7)
                
#                 # header=self.ui0.tableWidget.horizontalHeader()
#                 # header.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
#                 # header.setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)
#                 # header.setSectionResizeMode(2, QtWidgets.QHeaderView.Fixed)
#                 # self.ui0.tableWidget.horizontalHeader().setDefaultSectionSize(132)
#                 pass

#             else:
#                 print(FilesInDatabase)
                
#                 # #self.ui.tableWidget.setRowCount(0)
#                 # self.ui0.tableWidget.setRowCount(0)
#                 # #self.ui.tableWidget.setRowCount(0)
                
#                 # for rowNumber, rowData in enumerate(FilesInDatabase.values):
#                 #     self.ui0.tableWidget.insertRow(rowNumber)
#                 #     for columnNumber , data in enumerate(rowData):
#                 #         #self.ui.tableWidget.insertColumn(columnNumber)
#                 #         self.ui0.tableWidget.setItem(rowNumber, columnNumber, QtWidgets.QTableWidgetItem(str(data)))
                
#                 # header=self.ui0.tableWidget.horizontalHeader()
#                 # header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
#                 # header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
#                 # header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
                
#         pass

# def funcStartswithTemp(filename):
    
#         checkstring=filename.split("/")[-1]
    
#         StartswithTemp=checkstring.startswith('temp_')
    
#         return StartswithTemp

#in function
def CheckIfInFileLocation(fileToCheck, internalLocation='Documents', location='AutoFormFillerFiles'):
        

        home = os.path.expanduser('~')
             
        print(home, flush=True)
         
        filePath = os.path.join(home, internalLocation ,location)

        
        if not os.path.exists(filePath):
            os.makedirs(filePath)

        
        files = [f for f in listdir(filePath) if isfile(join(filePath, f))]
         
        # files = [f.split("\\")[-1] for f in glob.glob(filePath + "/*", recursive=True)]
        
        print(files, flush=True)
        print('files', flush=True)

        print(fileToCheck, flush=True)
        print('fileToCheck', flush=True)


        ##### files printed above shows ? values which may cause error
        
        
        
        if isList(item=fileToCheck):
            if len(fileToCheck)==1:
                if fileToCheck[0] in files:
                    InFileLocation=True
                    SenteceOpenFiles=str(fileToCheck)
                else:
                    InFileLocation=False
                    SenteceOpenFiles=''
                    
            #if multipleFiles==True:
            if isList(item=fileToCheck):    
                if len(fileToCheck)>1:
                    InFileLocation0=[]
                    ListOfOpenFiles=[]
                    for single in fileToCheck:
                        if single in files:
                            
                            value=True
                            InFileLocation0.append(value)
                            ListOfOpenFiles.append(single)
                    print(InFileLocation0)
                    InFileLocation=True in InFileLocation0
                    SenteceOpenFiles0=ListToSentence.ListToSentence(ListOfOpenFiles)
                    SenteceOpenFiles=str(SenteceOpenFiles0)
                    if InFileLocation==False:
                        SenteceOpenFiles=''
                        
        if isList(item=fileToCheck)==False:
            if fileToCheck in files:
                    InFileLocation=True
                    SenteceOpenFiles=str(fileToCheck)
            else:
                InFileLocation=False
                SenteceOpenFiles=''

        print(InFileLocation, flush=True)
                
        return InFileLocation, SenteceOpenFiles

# in function
def isList(item):
        IsthisList=type(item)==type([])
        return IsthisList  


# def CheckJobNameRedo(SqlDatase, FilesInDatabaseLocation, columnsFileinDatabase,datafillName):
#             Redowhile=True
#             rsp=1
#             SqlDatase=True
#         # datafillName=''
        
#         # print("Job name Window Started Now")
#         # while (Redowhile==True or datafillName =='')  and rsp==1:
#             #### Create a window asking for the job name
#             ##### "Name the new data fill job bellow:"

#             # rsp, datafillName=self.NewJobNameWindow()
            
#             datafillName=datafillName.split()
#             datafillName=" ".join(datafillName)
            
#             # if SqlDatase==False:

#             #     FilesInDatabaseExists=False
#             #     try:
#             #         FilesInDatabase=pandas.read_excel(FilesInDatabaseLocation)
#             #         FilesInDatabaseExists=True
#             #     except FileNotFoundError:
#             #         print('database DOES NOT exist... continue')
#             #         FilesInDatabaseExists=False
                    
#             if SqlDatase==True:
#                 FilesInDatabase , FilesInDatabaseExists = readSqlDatabase(table_name=FilesInDatabaseLocation,columns=columnsFileinDatabase)
                    
#             if FilesInDatabaseExists==True:
                
#                 if datafillName in list(FilesInDatabase[columnsFileinDatabase[0]]):
#                     Redowhile=True
#                     if rsp==1:

#                         #### create window with the text:
#                         #### label="Data fill job name already exists in the database. Click OK and change the job name used to a job name not registered, click CANCEL to cancel the process, or click Rewrite to rewrite the job name."
#                         # rsp=self.DRewriteDatafillJobName(filenameUsed=datafillName)
#                         pass
#                 else:
#                    Redowhile=False 
            
#             if FilesInDatabaseExists==False:
#                 Redowhile=False
                
#             return datafillName, FilesInDatabaseExists, rsp


# def readSqlDatabase(DatabaseName,table_name,columns=None):
#         conn = create_engine('sqlite:///'+ DatabaseName)
#         try:
#             df2=pandas.read_sql_table(table_name, conn, columns=columns)
#             #print(df2)
#             TableFound=True
#         except ValueError:
#             df2=None
#             TableFound=False
#         return df2,TableFound



# def checkListValues(excelFileLocation, workbook, rsp):
        
#     wb = workbook
    
#     print(os.getcwd())
    
#     # documentSaved=False
    
#     # while documentSaved==False and rsp==1:
        
#     try:
        
#         ws = wb.Sheets(1)
#         documentSaved=True
#     except:
#         ##### Change the bellow to show button alert when the excception ran
#         ##### the alert should say:
#         ##### "Um documento usado pelo programa se encontra em estado aberto e alterado. Salve ou feche o documento e aperte OK para continuar ou aperte CANCEL para cancelar a operação."
        
#         ##### clicking Ok will rerun this function
        
#         # rsp=addInformationANDSave()
#         print("exception runned")
#     if documentSaved:
#         checkListValues2(rsp=rsp)

# def checkListValues2(rsp):
#     if rsp==1:    
#         allData = ws.UsedRange
        
#         excel = win32.gencache.EnsureDispatch('Excel.Application') 
        
#         excel.Visible = True
        
#         # Get number of rows used on active sheet
#         ind = allData.Rows.Count
#         print ('Number of rows used in sheet : ', ind)
        
#         #Get number of columns used on active sheet
#         col = allData.Columns.Count
#         print ('Number of columns used in sheet : ', col)
        
#         print(col)
        
#         print(ind)
        
#         listOfValues=[]
#         listOfValueNames=[]
        
#         for i in range(1,ind+1):
            
#             for c in range(1,col+1):
                
#                 value = ws.Cells(i,c).Value
                
#                 if value == "XYXYXYXYX":
#                     listOfValueNames.append("["+ str(i) +","+ str(c)+"]")
#                     listOfValues.append([i,c])

#         NumList= len(listOfValues)
#         return NumList, listOfValueNames, rsp
    
#     if rsp==0:
#         NumList=0
#         listOfValueNames= []
        
#         return NumList, listOfValueNames, rsp


# def frameStyleByColor(path, columnsList, color):
        
#         if color=='blue':
#             frameStyle(path=path, columnsList=columnsList)
#             pass
        
#         if color=='green':
#             frameStyle(path=path, columnsList=columnsList, BackgroundRGBr=0 , BackgroundRGBg= 195, BackgroundRGBb=0)
#             pass
        
#         if color=='red':
#             frameStyle(path=path, columnsList=columnsList, BackgroundRGBr=237 , BackgroundRGBg= 0, BackgroundRGBb=0)
#             pass
        
#         if color=='yellow':
#             frameStyle(path=path, columnsList=columnsList, BackgroundRGBr=255 , BackgroundRGBg= 255, BackgroundRGBb=0, LetterRGBr=0, LetterRGBg=0, LetterRGBb=0)
#             pass
        
    
    
# def frameStyle(path,columnsList,BackgroundRGBr=0,BackgroundRGBg=0,BackgroundRGBb=206,LetterRGBr=255,LetterRGBg=255,LetterRGBb=255):

#     DictionaryofWidths= {x: 1.3*(int(len(x))+13) for x in columnsList}

#     frame2 = StyleFrame.read_excel(path= path, sheet_name='Sheet1')
#     print(frame2)
#     print('ok 1111')
    
#     print(columnsList)
    
#     print('columnsList used in frameStyle')
        
#     ew = StyleFrame.ExcelWriter(path)
    
#     print('ok 2222')
        
#     HeaderStyle= Styler(bg_color=self.DecHex(BackgroundRGBr)+self.DecHex(BackgroundRGBg)+self.DecHex(BackgroundRGBb), bold=True, font_color= self.DecHex(LetterRGBr)+self.DecHex(LetterRGBg)+self.DecHex(LetterRGBb), border_type='medium', horizontal_alignment='center', vertical_alignment='center', shrink_to_fit=False)
        
#     print('ok 3333')
    
#     frame2.apply_headers_style(HeaderStyle, style_index_header=True)
        
#     print('ok 4444')
#     StyleFrame.set_column_width_dict(frame2, DictionaryofWidths)
    
#     StyleFrame.to_excel(frame2, excel_writer = ew, sheet_name='Sheet1')

#     print('ok 5555')
    
#     ew.save()
    
    
# def DecHex(n):
#     '''
#     :para n: int
#     :return: str
#     >>> DecHex(10)
#     'A'
#     >>> DecHex(15)
#     'F'
#     >>> DecHex(32)
#     '20'
#     >>> DecHex(255)
#     'FF'
#     >>> DecHex(65535)
#     'FFFF'
#     '''

#     x16 = '0 1 2 3 4 5 6 7 8 9 a b c d e f'.upper().split()
#     result = []
#     try:
#         n = int(n)
#         if n == 0:
#             return '00'
#         if 17 > n:
#             result.append('0' + x16[(n % 16)])
#             n = n // 16
#         result.reverse()
#         while n > 0:
#             result.append(x16[(n % 16)])
#             n = n // 16
#         result.reverse()
#     except ValueError as e:
#         return ('Erro: %s' %e)
#     except:
#         raise
#     else:
#         return ''.join(result)




# def addInfoTable(frame, columnNames):
#     DInfoTable = QtWidgets.QDialog()
#     self.ui4 = Ui_DInfoTable()
#     self.ui4.setupUi(DInfoTable)
#     DInfoTable.show()
    
    
#     self.ui4.tableWidget.setColumnCount(0)
#     numColumn=len(columnNames)
#     self.ui4.tableWidget.setColumnCount(numColumn)
    
    
#     print(columnNames)
#     print("columnNames in for loop")
    
#     self.ui4.tableWidget.setHorizontalHeaderLabels(columnNames)
#     for i in range(len(columnNames)):
#         self.ui4.tableWidget.setItem(0, i, QTableWidgetItem(frame[i]))
    
    
#     rsp=DInfoTable.exec_()
    
#     if rsp==QtWidgets.QDialog.Accepted:
#         frame=[]
#         for i in range(len(columnNames)):
#             print(self.ui4.tableWidget.item(0,i).text())
#             CellValue=self.ui4.tableWidget.item(0,i).text()
            
#             CellValue=CellValue.split()
#             CellValue=" ".join(CellValue)
            
#             frame.append(CellValue)
            
#         print(frame)
        
#         return rsp, frame
#     else:
#         return rsp, frame
    
#     pass


# def Inframe(frame):
#         if '' in frame:
#             ExistsNan=True
#         else:
#             ExistsNan=False
#         return ExistsNan



# def ValueToBytes(ListofValues):

#     ListofChars=[ord(x) for x in list(ListofValues)]

#     return ListofChars





# a="C:/Users/IgorDC/Documents/AutoFormFillerFiles/New folder/2016-07-28_OS_Modelo_OS do Cliente - Serviço L3VPN_Concentrador_Informações Cliente_DF_Brasília_Sede_An d1.xlsx"

# stringOfChars = sys.argv[1]






# CurrentWorkingPath0 = sys.argv[1]


# CurrentWorkingPath0 = FilePathFromPython.FilePathFromPython()





# CurrentWorkingPath = CurrentWorkingPath0 + '\\'


# GetDataFromDatabase(CurrentWorkingPath, dataName,








dataName = 'fileLocation'

# stringOfChars=getTableData.GetDataFromDatabase(dataName)

stringOfChars=getTableData.GetDataFromDatabase(dataName)



AddToDatabase(stringOfChars)



# dataName = 'testLocationError'     ##### test remove when done

# try:
#     stringOfChars=getTableData.GetDataFromDatabase(dataName)       ##### test remove when done

# except KeyError:
#     print('all ok but now it stoped')

