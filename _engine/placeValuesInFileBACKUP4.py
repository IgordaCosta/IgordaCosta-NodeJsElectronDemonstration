import pandas
import os
import shutil
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import datetime 




import getTableData
import readSqlDatabase
import getAddressesFromColumn
import openWorkbook
import ChangeStartupDirectoryT
import getItemFromSameLineDb
import SingleSeriesValueToString
import TestIfTableValueExists
import StringListIntoList
import getUniqueAddFileEnd
import GetAllFontNamesFromFolderFunction
import GetFontFilePaths
import generateTxtFile
import getUniqueAddFileEndWithFIlename
import ReplaceInDoubleList
import PrintTexListSerial









def placeValuesInFile():

    ListToPrint = []
    ######## first run checkIfDocumentSaved()
    Folder='AutoFormFillerKey'
    ChangeStartupDirectoryT.ChangeStartupDirectory(Folder)

    home = os.path.expanduser('~')

    ValueToCheck='storedValues'
    
    ItEsists=TestIfTableValueExists.TestIfTableValueExists(ValueToCheck=ValueToCheck)

    dataName='datafillName'

    datafillName=getTableData.GetDataFromDatabase(dataName=dataName)

    dataNameList=['datafillName','rw','dataframe', 'FolderSaveLocation', 'columnList']

    OutputDictionary=getTableData.GetMultipleDataFromDatabase(dataNameList=dataNameList)

    dataNameList1 = ['Job Name','File KEY', 'FontName', 'FontSize', 'ExtensionType']

    TableName1 = 'FontAndItsSize'

    dataName2 = 'File Saved Location'

    TableName2 = 'FilesInDatabase'

    OutputDictionaryTableName1=getTableData.GetTableDataFromTable(TableName=TableName1)

    FileSavedLocation=getTableData.GetDataFromDatabase(dataName=dataName2,TableName=TableName2)

    TableData = OutputDictionaryTableName1[0]

    TableColumns = OutputDictionaryTableName1[1]

    dfTable1 = pandas.DataFrame(TableData,columns=TableColumns)

    valueToCheck = 'File KEY'

    FileKey= (dfTable1[valueToCheck][dfTable1['Job Name']==datafillName]).values[0]

    valueToCheck = 'ExtensionType'

    ExtensionType= (dfTable1[valueToCheck][dfTable1['Job Name']==datafillName]).values[0]

    if ExtensionType == 'image':

        valueToCheck = 'Job Name'

        JobName= (dfTable1[valueToCheck][dfTable1['Job Name']==datafillName]).values[0]

        valueToCheck = 'FontName'

        FontName= (dfTable1[valueToCheck][dfTable1['Job Name']==datafillName]).values[0]

        valueToCheck = 'FontSize'

        FontSize= (dfTable1[valueToCheck][dfTable1['Job Name']==datafillName]).values[0]


        TableName3 = FileKey

        OutputTableName3 = getTableData.GetTableData(TableName=TableName3)

        spaceReplaceData = '$%3&*&'

        OutputTableName3Keys0 = str(list(OutputTableName3.keys())).replace('"',"'").replace("]', '[", "', '[").split("', '[")
        OutputTableName3Values = str(list(OutputTableName3.values())).replace('[','').replace(']','').replace('"','').replace("'",'').replace(", ",',').replace(" ,",',').replace(spaceReplaceData, ' ').split(',')

        OutputTableName3Keys = [d.replace('[','').replace(']','').replace('"','').replace("'", '').replace(' ','').split(',') for d in OutputTableName3Keys0 ]    

        RealListOfColumnnames = OutputDictionary['columnList'].replace('[','').replace(']','').replace('"','').replace("'",'').replace(", ",',').replace(" ,",',').replace(spaceReplaceData, ' ').split(',') #turns text to list of strings

    datafillName = OutputDictionary['datafillName']

    LocationAsked = OutputDictionary['FolderSaveLocation']

    rw = int(OutputDictionary['rw'])

    dataframe1 = OutputDictionary['dataframe']

    stringCheked = str(dataframe1)

    IsDoubleList = "], [" in stringCheked

    StringList=dataframe1

    dataframe0=StringListIntoList.StringListIntoList(StringList=StringList,DoubleListCutAmount=3,DoublesSeparator1="'], ['", DoublesSeparator2=", ",DoubleList=True)

    commaReplace = '#3B&a$'

    DoubleList = dataframe0

    Item = commaReplace

    Subtitution = ', '

    dataframe = ReplaceInDoubleList.ReplaceInDoubleList(DoubleList=DoubleList, Item=Item, Subtitution=Subtitution)

    BaseFileLocation0=getItemFromSameLineDb.getDatafillName()

    BaseFileLocation2=SingleSeriesValueToString.SingleSeriesValueToString(BaseFileLocation0)

    BaseFileLocation3=BaseFileLocation2.split(".")

    uniqueValue = getUniqueAddFileEnd.getUniqueAddFileEnd()

    BaseFileLocation=BaseFileLocation3[0] + '__' + uniqueValue + "_temp."+BaseFileLocation3[-1]

    if ExtensionType == 'image':

        noError=False
        try:
            shutil.copy(BaseFileLocation2, BaseFileLocation)
            noError = True
        except:
            pass

        if noError == False:

            BaseFileLocation = getUniqueAddFileEndWithFIlename.getUniqueAddFileEndWithFIlename(filename=BaseFileLocation)
            try:
                shutil.copy(BaseFileLocation2, BaseFileLocation)
                noError = True
            except:
                
                ListToPrint.append('SheetIsOpenAndHasChanges')

                PrintTexListSerial.PrintTexListSerial(ListToPrint = ListToPrint)


        if LocationAsked == '':

            location='AutoFormFillerOutputFiles'

            home = os.path.expanduser('~')       
            filePath = os.path.join(home, 'Documents',location)

        else:
            
            filePath = LocationAsked[:-1]

        if noError:

            numberOfRows=len(dataframe)

            if rw<numberOfRows:

                if not os.path.exists(filePath):
                    os.makedirs(filePath)

                FinalSaveLocation0 = dataframe[rw][0]

                FinalSaveLocation=filePath +"\\" + FinalSaveLocation0 
            
                OriginalImageLocation0 = BaseFileLocation

                systemFonts = GetAllFontNamesFromFolderFunction.GetAllFontNamesFromFolder()
                        
                systemFontsList=systemFonts.split('|')

                newFont = FontName

                indexOfItemInListOfFonts=systemFontsList.index(newFont)

                fontFilePaths=GetFontFilePaths.GetFontFilePaths()

                fontSelectedPath= fontFilePaths[indexOfItemInListOfFonts]

                img = Image.open(OriginalImageLocation0)
                draw = ImageDraw.Draw(img)

                FontSize1 = int(FontSize)

                font = ImageFont.truetype(fontSelectedPath, FontSize1)

                for j in range(len(RealListOfColumnnames)  -1 ):

                    i = j+1

                    TextToPut = dataframe[rw][i]
                    textWidth, textHeight = draw.textsize(TextToPut, font)

                    ListInvOutputTableName3 = OutputTableName3Keys[i]

                    draw.text((int(ListInvOutputTableName3[1]), int(ListInvOutputTableName3[0]) - textHeight ),TextToPut,(0,0,0),font=font)

                FileSaved= False
                try:
                    img.save(FinalSaveLocation)
                    FileSaved = True

                except:
                    pass

                if FileSaved== False:
                    try:
                        FinalSaveLocation = getUniqueAddFileEndWithFIlename.getUniqueAddFileEndWithFIlename(filename=FinalSaveLocation)

                        img.save(FinalSaveLocation)
                        FileSaved = True

                    except:
                        ListToPrint.append('DocNOTsaved')
                        PrintTexListSerial.PrintTexListSerial(ListToPrint = ListToPrint)

                if FileSaved:

                    rw=rw+1

                    os.remove(BaseFileLocation)

                    AllDone = True
                    try:                      
                        FSaVedLocation=dataframe[rw][0]
                        AllDone = False

                    except:
                        FSaVedLocation="Done"

                    if rw == 1:

                        currentDT = datetime.datetime.now()

                        timeNow = str(currentDT).split('.')[0].replace(':', '-').replace(' ', '_')

                        IdentifierName0 = datafillName +'-' + timeNow

                        spaceReplaceDataUserImput = '$%78&*&'

                        IdentifierName = '_'.join(IdentifierName0.split(spaceReplaceDataUserImput))
                        
                        TextToWrite = str(dataframe) + ', '+ str([RealListOfColumnnames])

                        TextToWriteQR = str(dataframe0) + ', '+ str([RealListOfColumnnames])

                        SaveLocationTxt = filePath +"\\" + IdentifierName +  '_Txt' + '.txt'

                        SaveLocationLitxt =  filePath +"\\" + IdentifierName +  '_TxLi' + '.txt'

                        TextToWrite2 = str(TextToWrite).replace(']], [', ']], \n [').replace('], [', '], \n [')

                        generateTxtFile.generateTxtFile(TextToWrite=TextToWrite2,SaveLocation=SaveLocationTxt)

                        generateTxtFile.generateTxtFile(TextToWrite=TextToWriteQR,SaveLocation=SaveLocationLitxt, changeExtension = True)
                    
                    FFinalSaveLocation2=(FSaVedLocation.split("\\")[-1])
                    
                    FFinalSaveLocation1=(FFinalSaveLocation2.split("/")[-1])

                    IdenfierName = (FFinalSaveLocation1.split('.')[0])

                    FFinalSaveLocation0 = IdenfierName + ".jpg"
                    data=rw

                    dataName='rw'

                    getTableData.WriteDataDatabase(data,dataName)

                    percentageDone=int((rw/numberOfRows)*100)

                    ListToPrint.append(percentageDone)

                    #the percent done at the moment

                    ListToPrint.append(numberOfRows)

                    # number of rows above

                    ListToPrint.append(rw+1)

                    # step in completion above

                    if AllDone:
                        ListToPrint.append(FSaVedLocation)

                    else:
                        ListToPrint.append(FFinalSaveLocation0)

                    # final save locatiion of current saved item

                    ListToPrint.append("ItemSaved")


                    # number of prints to go back is 5

                    PrintTexListSerial.PrintTexListSerial(ListToPrint = ListToPrint)
     
            if rw==numberOfRows:
               
                path=os.path.realpath(filePath)
                os.startfile(path)

                ListToPrint.append("AllDONE")

                PrintTexListSerial.PrintTexListSerial(ListToPrint = ListToPrint)

                # number of prints to go back is 1


    if ExtensionType == 'excel':

        wb,excel,noError = openWorkbook.openWorkbook(BaseFileLocation2)

        try:
            wb.Close(True)
        except:
            pass


        try:
            shutil.copy(BaseFileLocation2, BaseFileLocation)
        except:
            noError=False
            print('SheetIsOpenAndHasChanges')


        if noError:

        
            wb,excel,noError = openWorkbook.openWorkbook(BaseFileLocation)


        #    it must run twice with noError==True
        if noError:

        # if ExtensionType == 'excel':
            ws = wb.Sheets(1)


            excel.Visible = False

            excel.ScreenUpdating = False
            excel.DisplayAlerts = False
            excel.EnableEvents = False

            ### ws in the old template excel sheet being written to and
            ### dataframe is where the program gets all the new data
        

            storedValues=dataframe


            # print(storedValues)

            # print('storedValues above')




            databaseUsed0 = readSqlDatabase.readSqlDatabase(table_name="KEY_"+datafillName)
            databaseUsed=databaseUsed0[0]

            # print(databaseUsed)

            # print('databaseUsed above')


            itemAddress=databaseUsed.columns.values[1:]

            # print(itemAddress)

            # print('itemAddress above')





            if LocationAsked == '':

                location='AutoFormFillerOutputFiles'

                home = os.path.expanduser('~')       
                filePath = os.path.join(home, 'Documents',location)

            else:
                
                filePath = LocationAsked[:-1]


                
            rowList, columnList=getAddressesFromColumn.getAddressesFromColumn(itemAddress=itemAddress)

            

            

            # print(storedValues)

            # print('storedValues above')

            # print(storedValues[0])

            # print('storedValues[0] above')

            # storedValues=storedValues[0]





            numberOfRows=len(storedValues)

            # print(numberOfRows)

            # print('numberOfRows above')

            if rw<numberOfRows:

                for cl in range(len(itemAddress)):

                    
                    # print(cl+1)
                    # print("cl above")

                    # print(storedValues[rw][cl+1])

                    # print(str(storedValues[rw][cl+1]).upper()=="NAN")

                    i=rowList[cl]
                    c=columnList[cl]


                    if str(storedValues[rw][cl+1]).upper()!="NAN":


                        print("ok")
                        ws.Cells(i,c).Value=storedValues[rw][cl+1]
                    else:


                        print("Not Nan ok")
                        ws.Cells(i,c).Value=''
                

                # The current file name is bellow

                SaVedLocation=storedValues[rw][0]
                print(SaVedLocation)
                print((SaVedLocation.split('.')[0])+".xlsx")
                
                FinalSaveLocation2=(SaVedLocation.split("\\")[-1])
                
                print(FinalSaveLocation2)
                
                
                FinalSaveLocation1=(FinalSaveLocation2.split("/")[-1])
                
                print(FinalSaveLocation1)
                
                FinalSaveLocation0=(FinalSaveLocation1.split('.')[0])+".xlsx"
                
                print(FinalSaveLocation0)

                # The current file is above



                # The next file name to come is below
                try:
                    
                    FSaVedLocation=storedValues[rw+1][0]

                except:
                    FSaVedLocation="Done"


                print(FSaVedLocation)
                print((FSaVedLocation.split('.')[0])+".xlsx")
                
                FFinalSaveLocation2=(FSaVedLocation.split("\\")[-1])
                
                print(FFinalSaveLocation2)
                
                
                FFinalSaveLocation1=(FFinalSaveLocation2.split("/")[-1])
                
                print(FFinalSaveLocation1)

                # uniqueValue = getUniqueAddFileEnd.getUniqueAddFileEnd()
                
                FFinalSaveLocation0=(FFinalSaveLocation1.split('.')[0]) + ".xlsx"
                
                print(FFinalSaveLocation0)


                # The next file name to come is above










                
                
                if not os.path.exists(filePath):
                    os.makedirs(filePath)
                

                

                FinalSaveLocation=filePath +"\\" + FinalSaveLocation0 
                
                
                print(FinalSaveLocation)
                print("FinalSaveLocation")
                
                

                ########   run this again suppling the rw number as the input for rw must be done in a separate file

                try:


                    # raise Exception('block this exeption after checking for error') # block this after error check




                    wb.SaveAs(FinalSaveLocation)
                    # FileSaved=True
                    
                    
                    
                    
                    rw=rw+1
                    print("rw"+str(rw))


                    wb.Close(True)

                    excel.ScreenUpdating = True
                    excel.DisplayAlerts = True
                    excel.EnableEvents = True


                    #delete temp file below

                    # import os
                    os.remove(BaseFileLocation)

                    print("BaseFileLocation temp File Removed!")


                    data=rw

                    dataName='rw'

                    getTableData.WriteDataDatabase(data,dataName)


                    percentageDone=int((rw/numberOfRows)*100)

                    print(percentageDone)

                    #the percent done at the moment


                    print(numberOfRows)

                    # number of rows above

                    

                    print(rw)

                    # step in completion above


                    print(FFinalSaveLocation0)

                    # final save locatiion of current saved item

                    print("ItemSaved")

                    # number of prints to go back is 5




                    


            # =============================================================================
                # except Exception as e:
                except:

                
                    try:
                        wb.Close(True)
                    except:
                        pass

                    excel.ScreenUpdating = True
                    excel.DisplayAlerts = True
                    excel.EnableEvents = True

                    print("rw"+str(rw))
                    print("DocNOTsaved")
                    ###### run window to close required excel document the start this program with the current rw as input
                    
                    # number of prints to go back is 1

            if rw==numberOfRows:
                
        # =============================================================================
                try:
                    wb.Close(True)
                except:
                    pass
                
                path=os.path.realpath(filePath)
                os.startfile(path)

                print("AllDONE")

                # number of prints to go back is 1










placeValuesInFile()





# data=0                        # block this after test

# dataName='rw'                 # block this after test

# getTableData.WriteDataDatabase(data,dataName)             # block this after test



