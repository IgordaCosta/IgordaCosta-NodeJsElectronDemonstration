import os
import pandas




def LoadToMultipleFilesDetails(self, datafillName, FilesInDatabaseLocation, columnsFileinDatabase):
        
    filename="OneFileToMultipleFiles.xlsx"
    
    location=filename
    
    home = os.path.expanduser('~')       
    filePath = os.path.join(home, 'Documents',location)
    
    filesInFolder1 = GetExcelFilesinLocation(location="AutoFormFillerFiles")
    
    
    filesInFolder2 = GetExcelFilesinLocation(location="AutoFormFillerOutputFiles")
    
    listTocheck=[filename]+filesInFolder1+filesInFolder2
    print(listTocheck)
    

    location='AutoFormFillerOutputFiles'
    
    home = os.path.expanduser('~')       
    filePath = os.path.join(home, 'Documents',location)
    
    databaseUsed0 = readSqlDatabase(table_name="KEY_"+datafillName)
    databaseUsed=databaseUsed0[0]
    # ###################################      Imput Data      ########################################
    
    FilesInDatabaseLocation='FilesInDatabase'
    columnsFileinDatabase=['Job Name', 'File KEY', 'File Saved Location']

    # ###################################      Imput Data      ########################################


    OriginalFileNameTable0 = readSqlDatabase(table_name=FilesInDatabaseLocation)
    print(OriginalFileNameTable0)
    OriginalFileNameTable=OriginalFileNameTable0[0]
    print(OriginalFileNameTable)
    print("OriginalFileNameTable")
    OriginalFileNameTable=OriginalFileNameTable[OriginalFileNameTable[columnsFileinDatabase[0]]==datafillName]
    OriFileName0=OriginalFileNameTable[columnsFileinDatabase[2]]
    print(OriFileName0)
    OriFileName=OriFileName0.values[0]
    print(OriFileName)


    print("OriFileName after")

    databaseUsed0 = readSqlDatabase(table_name="KEY_"+datafillName)
    databaseUsed=databaseUsed0[0]
    itemAddress=databaseUsed.columns.values[1:]

    print(itemAddress)
    print("item address above")
    
    itemDescription=databaseUsed.values[0][1:]
    print(itemDescription)
    print("item Description above")
    itemDescription=["Save Name"]+list(itemDescription)
    FrameUsed=pandas.DataFrame(columns=itemDescription)

   


    Skip= OpenDeleteRecreateSheet(filename=filename, frame=FrameUsed,columnList=itemDescription, SqlDatase=False)

    if Skip==False:

        frameStyleByColor(path=filename, columnsList=itemDescription, color='blue')

        # os.startfile(filename)



##########################################    First Part Ends Above     ###############################################





        # #############################    Change Screen     ###################################

        # rsp=self.AddInfoEXCEL()

        # #############################    Change Screen     ###################################


    #######################################################################################################
    ########################      This is the next section of the program       ###########################

    ###################################       open file section       #####################################

            # os.startfile(filename)


            #user clicks OK when done entering the data in the excel table



            storedValues=pandas.read_excel(filename)

            storedValues0 = getLocationValues(dataframe=storedValues, column="Save Name")

            # rsp, storedValues = FileExistInDatabaseFunction(dataframe=storedValues0,column="Save Name",filename=filename, listTocheck=listTocheck)      

            FileExistInDatabaseFunction(dataframe=storedValues0,column="Save Name",filename=filename, listTocheck=listTocheck)      
            
            print(storedValues)
            print("storedValues after")
        
                
        if rsp==1:
            


            #######################################################################################################
            ########################      This is the next section of the program       ###########################




            # wb = openWorkbook(OriFileName)
            # wb.Close(True)
            # wb = openWorkbook(OriFileName)

            placeValuesInFile(storedValues=storedValues)

    pass


def GetExcelFilesinLocation(location, IncludeFolder=False):
        home = os.path.expanduser('~') 
        
        SelectedFolder = os.path.join(home, 'Documents',location)
        
        print(SelectedFolder)
        
        print("files in folder with ~$")
        
        if IncludeFolder==False:
            filesInFolder = [f.split("\\")[-1] for f in glob.glob(SelectedFolder + "/[!~$]*.xl*", recursive=True)]
            
            print(filesInFolder)
            print("files in folder withOUT ~$")
        if IncludeFolder==True:
            filesInFolder=glob.glob(SelectedFolder+"\\*.xl*")
        
        return filesInFolder


def readSqlDatabase(table_name,columns=None):
        DatabaseName="AutoFormFiller.db"
        conn = create_engine('sqlite:///'+DatabaseName)
        try:
            df2=pandas.read_sql_table(table_name, conn, columns=columns)
            #print(df2)
            TableFound=True
        except ValueError:
            df2=None
            TableFound=False
        return df2,TableFound


def OpenDeleteRecreateSheet(filename,frame,columnList, SqlDatase=True, noColumnList=False):
    
        Skip=False
        if SqlDatase==False:
                    Skip = preOpenDeleteRecreateSheet(filename=filename,frame=frame,columnList=columnList, noColumnList=noColumnList)
                    
                    
        return Skip



def preOpenDeleteRecreateSheet(filename,frame,columnList, noColumnList):
        
        ### Open delete sheet so it can be saved later below 2
        Skip=False
        rsp=1
        
        writer = pandas.ExcelWriter(filename)
        print('check 111111')
        try:   
            wb=openpyxl.load_workbook(filename)
            print('check 222222')
            sheetloaded=True
        except:
            sheetloaded=False
            ProblemSaving=False
            pass
        
        if sheetloaded==True:    
            print('check 222333')
            del wb['Sheet1']
            print('check 333333')
            
            try:
                writer.save()
                ProblemSaving=False
            except:
                ProblemSaving=True
                
        if ProblemSaving==True:
            #xl = Dispatch('Excel.Application')
            Skip=False
            
            SkipWhileLoop=False
            secondException=False
            while SkipWhileLoop==False and Skip==False:
                print("start loop SkipWhileLoop==False")
                try:
                    xl = Dispatch('Excel.Application')
                    wb = xl.Workbooks(filename)
                    SkipWhileLoop=True
                    Skip=False
                except Exception as e:
                    print(e)
                    f=str(e)
                    print(type(f))
                    print(f)
                    g=''
                    try: 
                        g=e.args[1]
                        if g== 'Exception occurred.':
                            secondException=True
    
                    except Exception as d:
                        print(d)
                        print("exeption of exception")
                        pass
                    
                    if  f=="Excel.Application.Workbooks":

                        # #####################     Change Screens     ####################################

                        rsp=self.InicioSalveDocumento()

                        # #####################     Change Screens     ####################################
    
                    if rsp==QtWidgets.QDialog.Accepted:
                        Skip=False
                        SkipWhileLoop=False
                        if secondException:
                            print("secondException=True runned")
                            SkipWhileLoop=True
                        pass
                    
                    if rsp==0:
                        Skip=True
                        SkipWhileLoop=False
    
            if Skip==False:
                if secondException==False:
                    writer.save()
                    wb.Close(True)
    ##### Open delete sheet so it can be saved later above 2
        
        if Skip==False:
            
            writer = pandas.ExcelWriter(filename)
            
            print(frame)
            print('frame before column filtering')
            
            #### noColumnList=False added so columnlistfilter can be ignored
            if noColumnList==False:
                frame=frame[columnList]
            
            print(frame)
            print("frame with unamed")
    
            frame.drop(frame.columns[frame.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
            print("step 1111111" )
            #frame.to_excel(writer,'Sheet1', index=False)
            frame.to_excel(writer, index=False)
            print("step 22222222" )
            try:
              
                writer.save()
                print("step 333333333" )
            except PermissionError:
                xl = Dispatch('Excel.Application')
                print("step 44444444444" )
                wb = xl.Workbooks(filename)
                print("step 55555555" )
                # do some stuff
                wb.Close(True) # save the workbook
                print("step 66666666" )
                writer.save()
                print("step 777777777" )
        
            print(Skip)
            print("skip")
        
        return Skip



def frameStyleByColor(path, columnsList, color):
        
        if color=='blue':
            frameStyle(path=path, columnsList=columnsList)
            pass
        
        if color=='green':
            frameStyle(path=path, columnsList=columnsList, BackgroundRGBr=0 , BackgroundRGBg= 195, BackgroundRGBb=0)
            pass
        
        if color=='red':
            frameStyle(path=path, columnsList=columnsList, BackgroundRGBr=237 , BackgroundRGBg= 0, BackgroundRGBb=0)
            pass
        
        if color=='yellow':
            frameStyle(path=path, columnsList=columnsList, BackgroundRGBr=255 , BackgroundRGBg= 255, BackgroundRGBb=0, LetterRGBr=0, LetterRGBg=0, LetterRGBb=0)
            pass
        
    
    
def frameStyle(path,columnsList,BackgroundRGBr=0,BackgroundRGBg=0,BackgroundRGBb=206,LetterRGBr=255,LetterRGBg=255,LetterRGBb=255):

    DictionaryofWidths= {x: 1.3*(int(len(x))+13) for x in columnsList}

    frame2 = StyleFrame.read_excel(path= path, sheet_name='Sheet1')
    print(frame2)
    print('ok 1111')
    
    print(columnsList)
    
    print('columnsList used in frameStyle')
        
    ew = StyleFrame.ExcelWriter(path)
    
    print('ok 2222')
        
    HeaderStyle= Styler(bg_color = DecHex(BackgroundRGBr)+ DecHex(BackgroundRGBg)+ DecHex(BackgroundRGBb), bold=True, font_color= DecHex(LetterRGBr)+ DecHex(LetterRGBg)+ DecHex(LetterRGBb), border_type='medium', horizontal_alignment='center', vertical_alignment='center', shrink_to_fit=False)
        
    print('ok 3333')
    
    frame2.apply_headers_style(HeaderStyle, style_index_header=True)
        
    print('ok 4444')
    StyleFrame.set_column_width_dict(frame2, DictionaryofWidths)
    
    StyleFrame.to_excel(frame2, excel_writer = ew, sheet_name='Sheet1')

    print('ok 5555')
    
    ew.save()
    
    
def DecHex(n):
    '''
    :para n: int
    :return: str
    >>> DecHex(10)
    'A'
    >>> DecHex(15)
    'F'
    >>> DecHex(32)
    '20'
    >>> DecHex(255)
    'FF'
    >>> DecHex(65535)
    'FFFF'
    '''

    x16 = '0 1 2 3 4 5 6 7 8 9 a b c d e f'.upper().split()
    result = []
    try:
        n = int(n)
        if n == 0:
            return '00'
        if 17 > n:
            result.append('0' + x16[(n % 16)])
            n = n // 16
        result.reverse()
        while n > 0:
            result.append(x16[(n % 16)])
            n = n // 16
        result.reverse()
    except ValueError as e:
        return ('Erro: %s' %e)
    except:
        raise
    else:
        return ''.join(result)





def getLocationValues(dataframe, column=None):
        Skip=False
        IsItAList= isList(item=dataframe)
    
        if IsItAList:
            PandaslistT = pandas.Series(dataframe)
            print(PandaslistT)
            print("PandaslistT")
            
            Pandaslist=PandaslistT.str.split('\\',expand=True).iloc[:,-1]
            print(Pandaslist)
            print("Pandaslist")
        else:
            try:
                Pandaslist=dataframe[column].str.split('\\',expand=True).iloc[:,-1]
            except IndexError:
                dataframe=pandas.DataFrame(columns=[])
                Skip=True
        
        if Skip==False:
            print(Pandaslist)
            Pandaslist0=Pandaslist.str.split('/',expand=True).iloc[:,-1]
            Pandaslist1=Pandaslist0.str.split('.',expand=True)[0]
            print(Pandaslist)
            Pandaslist2=Pandaslist1+".xlsx"
            print(Pandaslist2)
            
            if IsItAList:
                #dataframe to list
                dataframe=Pandaslist2.tolist() 
            else:
                dataframe[column]=Pandaslist2
                
        return dataframe




def isList(item):
        IsthisList=type(item)==type([])
        return IsthisList  


def FileExistInDatabaseFunction(dataframe,column,filename,listTocheck):
             
    dataframe=pandas.read_excel(filename)
    
    dataframe= getLocationValues(dataframe=dataframe, column="Save Name")
    
    ExistsNan=CheckAllFilled(dataframe, anyNan=False)
    if ExistsNan:
        print("ExistsNan")

        ##### in the screen asking the user to insert data into the table a red alert is shown on 
        ##### the screen saying that there are required values missing 
        ##### telling the user to fill them


    try:
        
        ExistInside, ListofInlist0 = valueInFrame(dataframe=dataframe,column=column, listTocheck=listTocheck)
        SkipExistInside=False
    except KeyError:
        pass
    
    if SkipExistInside==False:

        ListofInlist= ListToSentence(ListofInlist0)
        if ExistInside==True:
            print('ExistInside')
            
            ###### here a message is shown saying that the user must change the names of the files for 
            ###### they are already taken by other required files

    if SkipExistInside:
        ListofInlist= ListToSentence(ListofInlist0)
        if ExistInside:
            print('ExistInsideExistsNan')

            ###### here both messages are shown

    if (ExistsNan==False) and (ExistInside==False):
        print("AllOKToContinue")

            ##### in this case the program will continue to the next part


       


def CheckAllFilled(storedValues, anyNan=True):        
        
        if storedValues.empty==False:
            if anyNan==True:
                ExistsNan=(pandas.isnull(storedValues.values)).any()
            if anyNan==False:
                
                print(storedValues.iloc[:,[0]])
                print("storedValues.iloc[:,[0]]")
                print(pandas.isnull(storedValues.iloc[:,[0]]).values.any())
                print("pandas.isnull(storedValues.iloc[:,[0]]).values.any()")
                print(storedValues.iloc[:,[0]])
                
                print(len(storedValues.columns.values))
                print("len(storedValues.columns.values)")
                print("len(storedValues.column.values)")
                colnum=len(storedValues.columns.values)
                
                
                
                if ~(pandas.isnull(storedValues.iloc[:,[0]]).values.any()):
                    lisOfNan=[]
                    for i in range(1, colnum):
                        valueInList=~(pandas.isnull(storedValues.iloc[:,[i]]).values.all())
                        print(valueInList)
                        lisOfNan.append(valueInList)
                    print(lisOfNan)
                    if True in lisOfNan:
                        print("True in ListNan")
                        ExistsNan=False
                    else:
                        ExistsNan=True
                    
                else:
                   ExistsNan=True 
                                    

        if storedValues.empty ==True:
            
            ExistsNan=True

        print(ExistsNan)   
        return ExistsNan





def valueInFrame(dataframe,column, listTocheck):
        print(dataframe[column])
        ListofInlist=[]
        ExistInside=False
        for value in listTocheck:
            print(value)
            print(dataframe[column])
            Inlist=value in list(dataframe[column])
            if Inlist:
                ExistInside=True
                ListofInlist.append(value)
        print(ListofInlist)
        return ExistInside, ListofInlist



def ListToSentence(ListUsed):
        listb=str(ListUsed)
        listc=listb[1:-1]
        return listc


def openWorkbook(xlfile):
        rsp=1
        noerror=False
        xlwb = None    
        while rsp==1 and noerror==False:
            try:
                
                xlapp = win32.gencache.EnsureDispatch('Excel.Application')
                
# =============================================================================
#                 xlapp.ScreenUpdating = False
#                 xlapp.DisplayAlerts = False
#                 xlapp.EnableEvents = False
# =============================================================================
                xlapp.DisplayAlerts = False
                print("no eror -1")
                xlapp.Visible = True
                print("no eror 0")
                noerror=True
                rsp=1
                print("no eror")
            except TypeError:
                print('sheet is open and has changes')

                # #############################       Changed Screen        ################################

                rsp = self.InicioSalveDocumento()


                # #############################       Changed Screen        ################################


                #noerror=False
        
        if rsp==1:
            
            if noerror==True:
        
                    try:
                        print("no eror 1")
                        xlapp = win32.gencache.EnsureDispatch('Excel.Application')
# =============================================================================
#                         xlapp.ScreenUpdating = False
#                         xlapp.DisplayAlerts = False
#                         xlapp.EnableEvents = False
# =============================================================================
                        
                        xlapp.DisplayAlerts = False
                        xlapp.Visible = True
                        print("no eror 2")
                        xlwb = xlapp.Workbooks.Open(xlfile)
                        #xlapp.Visible = True
                        print("no eror 3")
                        #xlapp.DisplayAlerts = False
                    except Exception as e:
                        print("no eror exception")
                        print(e)
                        xlapp.DisplayAlerts = False
                        map(lambda book: book.Close(False), xlapp.Workbooks)
                        xlapp.Quit()
                        
                        xlapp = win32.gencache.EnsureDispatch('Excel.Application') 
# =============================================================================
#                         xlapp.ScreenUpdating = False
#                         xlapp.DisplayAlerts = False
#                         xlapp.EnableEvents = False
# =============================================================================
                        
                        
                        xlapp.Visible = True
                        xlapp.DisplayAlerts = False
                        
                        xlwb = xlapp.Workbooks.Open(xlfile)
                        #xlapp.Visible = True
                        
                        
# =============================================================================
#         xlapp.ScreenUpdating = True
#         xlapp.DisplayAlerts = True
#         xlapp.EnableEvents = True        
# =============================================================================
        return(xlwb)


# def checkIfDocumentSaved():

#     dataName='datafillName'

#     datafillName = getTableData.GetDataFromDatabase(dataName=dataName)


# # ###################################      Imput Data      ########################################

#     FilesInDatabaseLocation='FilesInDatabase'
#     columnsFileinDatabase=['Job Name', 'File KEY', 'File Saved Location']

#     # ###################################      Imput Data      ########################################
    

#     OriginalFileNameTable0 = readSqlDatabase(table_name=FilesInDatabaseLocation)
#     print(OriginalFileNameTable0)
#     OriginalFileNameTable=OriginalFileNameTable0[0]
#     print(OriginalFileNameTable)
#     print("OriginalFileNameTable")
#     OriginalFileNameTable=OriginalFileNameTable[OriginalFileNameTable[columnsFileinDatabase[0]]==datafillName]
#     OriFileName0=OriginalFileNameTable[columnsFileinDatabase[2]]
#     print(OriFileName0)
#     OriFileName=OriFileName0.values[0]
#     print(OriFileName)


#     wb = openWorkbook(OriFileName)
#     wb.Close(True)
#     wb = openWorkbook(OriFileName)
    
#     print(os.getcwd())
    
#     # documentSaved=False
#     # rsp=1
    
#     try:
        
#         ws = wb.Sheets(1)
#         # documentSaved=True
#         print("documentSaved")
#     except:

#         # ##################################       Changed Screen       #############################

        

#         # ##################################       Changed Screen       #############################

#         print("DocumentNOTSaved")

        

#     # if documentSaved:
#     #     placeValuesInFile()


    


# def placeValuesInFile(rw=0):

#     ######## first run checkIfDocumentSaved()


#     dataNameList=['filename','datafillName']

#     OutputDictionary=getTableData.GetMultipleDataFromDatabase(dataNameList=dataNameList)

#     filename = OutputDictionary['filename']
#     datafillName = OutputDictionary['datafillName']


#     dataframe=pandas.read_excel(filename)
        
#     storedValues=getLocationValues(dataframe=dataframe, column="Save Name")


#     databaseUsed0 = readSqlDatabase(table_name="KEY_"+datafillName)
#     databaseUsed=databaseUsed0[0]
#     itemAddress=databaseUsed.columns.values[1:]

#     location='AutoFormFillerOutputFiles'

#     home = os.path.expanduser('~')       
#     filePath = os.path.join(home, 'Documents',location)

        
#     allData = ws.UsedRange
    
#     excel = win32.gencache.EnsureDispatch('Excel.Application') 
    
#     excel.Visible = True
    
#     # Get number of rows used on active sheet
#     ind = allData.Rows.Count
#     print ('Number of rows used in sheet : ', ind)
    
#     #Get number of columns used on active sheet
#     col = allData.Columns.Count
#     print ('Number of columns used in sheet : ', col)
    
#     print(col)
    
#     print(ind)
    
    
#     rowList, columnList=getAddressesFromColumn(itemAddress=itemAddress)
    
    
#     numberOfRows=len(storedValues.index)
#     print(numberOfRows)
    
                    
#     # for rw in range(numberOfRows):
#     for cl in range(1,len(itemAddress)+1):
#         print(storedValues.values[rw][cl])
#         #print(type(storedValues.values[rw][cl]))
#         print(str(storedValues.values[rw][cl]).upper()=="NAN")
#         i=rowList[cl-1]
#         c=columnList[cl-1]
#         if str(storedValues.values[rw][cl]).upper()!="NAN":
#             print("ok")
#             ws.Cells(i,c).Value=storedValues.values[rw][cl]
#         else:
#             print("Not Nan ok")
#             ws.Cells(i,c).Value=''
    
#     SaVedLocation=storedValues.values[rw][0]
#     print(SaVedLocation)
#     print((SaVedLocation.split('.')[0])+".xlsx")
    
#     FinalSaveLocation2=(SaVedLocation.split("\\")[-1])
    
#     print(FinalSaveLocation2)
    
    
#     FinalSaveLocation1=(FinalSaveLocation2.split("/")[-1])
    
#     print(FinalSaveLocation1)
    
#     FinalSaveLocation0=(FinalSaveLocation1.split('.')[0])+".xlsx"
    
#     print(FinalSaveLocation0)
    
    
#     if not os.path.exists(filePath):
#         os.makedirs(filePath)
    
#     FinalSaveLocation=filePath +"\\" + FinalSaveLocation0
    
    
#     print(FinalSaveLocation)
#     print("FinalSaveLocation")
    
    

#     ########   run this again suppling the rw number as the input for rw must be done in a separate file

#     FileSaved=False 
#     rsp=1
#     # while FileSaved==False and rsp==1:
#     try:
#         wb.SaveAs(FinalSaveLocation)
#         FileSaved=True
#         rw=rw+1
#         print("rw"+str(rw))
# # =============================================================================
#     except Exception as e:
#         print("rw"+str(rw))
#         print("DocNOTsaved")
#         ###### run window to close required excel document the start this program with the current rw as input
            
    

#     if rw==numberOfRows:
        
# # =============================================================================
#         wb.Close(True)
        
#         path=os.path.realpath(filePath)
#         os.startfile(path)

#         print("AllDONE")

#         # #########################      Changed to DONE Screen       ###############################

#         # self.OperaConcluidaWindow()

#         # #########################      Changed to DONE Screen       ###############################





def getAddressesFromColumn(itemAddress):
        
    rowList=[]
    columnList=[]
    for values in range(len(itemAddress)):
        temp = re.findall(r'\d+', itemAddress[values]) 
        i,c = list(map(int, temp)) 
        rowList.append(i)
        columnList.append(c)
        print(i)
        print(c)
    print(columnList)
    print("columnList")
    print(rowList)
    print("rowList")
    
    return rowList, columnList







