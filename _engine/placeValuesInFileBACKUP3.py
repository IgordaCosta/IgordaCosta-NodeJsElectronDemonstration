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

    #print("in placeValuesInFile function")

    Folder='AutoFormFillerKey'

    ChangeStartupDirectoryT.ChangeStartupDirectory(Folder)

    
    # rw=0


    home = os.path.expanduser('~')

    ValueToCheck='storedValues'
    
    ItEsists=TestIfTableValueExists.TestIfTableValueExists(ValueToCheck=ValueToCheck)

    #print(ItEsists)

    #print("ItEsists above")

    dataName='datafillName'

    datafillName=getTableData.GetDataFromDatabase(dataName=dataName)


    # dataNameList=['filename','datafillName','rw','dataframe', 'FolderSaveLocation']

    dataNameList=['datafillName','rw','dataframe', 'FolderSaveLocation', 'columnList']

    OutputDictionary=getTableData.GetMultipleDataFromDatabase(dataNameList=dataNameList)



    dataNameList1 = ['Job Name','File KEY', 'FontName', 'FontSize', 'ExtensionType']

    TableName1 = 'FontAndItsSize'



    dataName2 = 'File Saved Location'

    TableName2 = 'FilesInDatabase'






    


    OutputDictionaryTableName1=getTableData.GetTableDataFromTable(TableName=TableName1)



    FileSavedLocation=getTableData.GetDataFromDatabase(dataName=dataName2,TableName=TableName2)

    #print('OutputDictionaryTableName1 below_________________________________________---')

    #print(OutputDictionaryTableName1)

    #print('OutputDictionaryTableName1 above_____________________________________')



    TableData = OutputDictionaryTableName1[0]

    TableColumns = OutputDictionaryTableName1[1]

    # print(TableData)


    dfTable1 = pandas.DataFrame(TableData,columns=TableColumns)

    #print(dfTable1)

    valueToCheck = 'File KEY'

    FileKey= (dfTable1[valueToCheck][dfTable1['Job Name']==datafillName]).values[0]

    #print(FileKey)



    valueToCheck = 'ExtensionType'

    ExtensionType= (dfTable1[valueToCheck][dfTable1['Job Name']==datafillName]).values[0]

    # getTableData.GetDataFromDatabase(dataName=dataNameList2,TableName=TableName2)




    #print(ExtensionType)

    #print("ExtensionType above")






    

    if ExtensionType == 'image':

        valueToCheck = 'Job Name'

        JobName= (dfTable1[valueToCheck][dfTable1['Job Name']==datafillName]).values[0]




        valueToCheck = 'FontName'

        FontName= (dfTable1[valueToCheck][dfTable1['Job Name']==datafillName]).values[0]


        valueToCheck = 'FontSize'

        FontSize= (dfTable1[valueToCheck][dfTable1['Job Name']==datafillName]).values[0]



        #print(JobName)

        #print('JOBNAME ABOVE')


        #print(FontName)

        #print('FontName above')


        #print(FontSize)

        #print('FontSize above')



        # dataNameList3

        TableName3 = FileKey

        #print(TableName3)

        # OutputDictionaryTableName3=getTableData.GetTableData(TableName=TableName3)

        OutputTableName3 = getTableData.GetTableData(TableName=TableName3)

        #print(OutputTableName3)

        #print('OutputTableName3 above')

        #print(OutputTableName3.keys())

        #print(OutputTableName3.values())


        spaceReplaceData = '$%3&*&'


        OutputTableName3Keys0 = str(list(OutputTableName3.keys())).replace('"',"'").replace("]', '[", "', '[").split("', '[")
        OutputTableName3Values = str(list(OutputTableName3.values())).replace('[','').replace(']','').replace('"','').replace("'",'').replace(", ",',').replace(" ,",',').replace(spaceReplaceData, ' ').split(',')


        OutputTableName3Keys = [d.replace('[','').replace(']','').replace('"','').replace("'", '').replace(' ','').split(',') for d in OutputTableName3Keys0 ]    

        #print(OutputTableName3Keys)

        #print('OutputTableName3Keys')

        #print(OutputTableName3Values)

        #print('OutputTableName3Values')



        # es = dict(zip(test_keys, test_values))

        #InvOutputTableName3 = dict(zip(OutputTableName3Values, OutputTableName3Keys))

        # spaceReplaceData = '$%3&*&'


        # print(OutputTableName3['[124, 1329]'])

        # print('OutputTableName3 above2')


        # # InvOutputTableName3 = {v: k for k, v in OutputTableName3.items()}

        # # InvOutputTableName3 = {v: k.replace('[','').replace(']','').replace(" ",'').replace("'",'').split(',') for k, v in OutputTableName3.items()}

        # # InvOutputTableName3 = {v: k.replace('[','').replace(']','').replace(" ",'').replace("'",'').split(',') for k, v in OutputTableName3.items()}

        # InvOutputTableName3 = {v: k.replace('[','').replace(']','').replace('"','').replace("'",'').replace(", ",',').replace(" ,",',').split(',') for k, v in OutputTableName3.items()}

        # print(InvOutputTableName3)

        #print('InvOutputTableName3 above')


        #print(TableColumns)

        #print(type(TableColumns))


        # print(InvOutputTableName3)




        #print(OutputDictionary['dataframe'])

        

        #print('OutputDictionary.dataframe above')

        #print(OutputDictionary['columnList'])

        #print(type(OutputDictionary['columnList']))



        # print(OutputDictionary['columnList'].strip('[').strip(']').replace(' ','').replace("'",'').split(','))


        # RealListOfColumnnames = OutputDictionary['columnList'].strip('[').strip(']').replace(' ','').replace("'","").split(',') #turns text to list of strings

        RealListOfColumnnames = OutputDictionary['columnList'].replace('[','').replace(']','').replace('"','').replace("'",'').replace(", ",',').replace(" ,",',').replace(spaceReplaceData, ' ').split(',') #turns text to list of strings

        # print(RealListOfColumnnames)

        # print(RealListOfColumnnames[-1])






        #print(InvOutputTableName3)

        # print(InvOutputTableName3[RealListOfColumnnames[1]])

        
        # ListInvOutputTableName3 = InvOutputTableName3[RealListOfColumnnames[1]].strip('[').strip(']').replace(' ','').split(',')    # this list starts at 1 and goes to amount of items

        # print(ListInvOutputTableName3)

        # print(ListInvOutputTableName3[0]) 

        # print(ListInvOutputTableName3[1]) 

    
    
    








    # filename = OutputDictionary['filename']
    datafillName = OutputDictionary['datafillName']

    LocationAsked = OutputDictionary['FolderSaveLocation']

    rw = int(OutputDictionary['rw'])

    dataframe1 = OutputDictionary['dataframe']


    stringCheked = str(dataframe1)


    IsDoubleList = "], [" in stringCheked





    # commaReplace = '#3B&a$'

    # dataframe = dataframe0.replace(commaReplace, ', ', regex=True)
    




    


    StringList=dataframe1


    dataframe0=StringListIntoList.StringListIntoList(StringList=StringList,DoubleListCutAmount=3,DoublesSeparator1="'], ['", DoublesSeparator2=", ",DoubleList=True)

    # print(dataframe0)

    # print('dataframe0 altered above')

    # print(type(dataframe0))

    # print('dataframe0 altered type above')


    commaReplace = '#3B&a$'


    DoubleList = dataframe0

    Item = commaReplace

    Subtitution = ', '



    dataframe = ReplaceInDoubleList.ReplaceInDoubleList(DoubleList=DoubleList, Item=Item, Subtitution=Subtitution)


    # print(dataframe)

    # print('dataframe above')


    BaseFileLocation0=getItemFromSameLineDb.getDatafillName()


    BaseFileLocation2=SingleSeriesValueToString.SingleSeriesValueToString(BaseFileLocation0)

   
    # print(BaseFileLocation2)

    # print("new BaseFileLocation2")

    BaseFileLocation3=BaseFileLocation2.split(".")

    uniqueValue = getUniqueAddFileEnd.getUniqueAddFileEnd()

    BaseFileLocation=BaseFileLocation3[0] + '__' + uniqueValue + "_temp."+BaseFileLocation3[-1]

    # print(BaseFileLocation)

    # print('BaseFileLocation with _temp extension')

    # shutil.copy(BaseFileLocation2, BaseFileLocation)






    if ExtensionType == 'image':

        noError=False
        try:
            shutil.copy(BaseFileLocation2, BaseFileLocation)
            noError = True
        except:

            # print('SheetIsOpenAndHasChanges')
            pass




        if noError == False:

            BaseFileLocation = getUniqueAddFileEndWithFIlename.getUniqueAddFileEndWithFIlename(filename=BaseFileLocation)
            try:
                shutil.copy(BaseFileLocation2, BaseFileLocation)
                noError = True
            except:
                
                # print('SheetIsOpenAndHasChanges')
                ListToPrint.append('SheetIsOpenAndHasChanges')

                PrintTexListSerial.PrintTexListSerial(ListToPrint = ListToPrint)



        if LocationAsked == '':

            location='AutoFormFillerOutputFiles'

            home = os.path.expanduser('~')       
            filePath = os.path.join(home, 'Documents',location)

        else:
            
            filePath = LocationAsked[:-1]
            # print(filePath)
            # print('filePath used')
            #the error seems to be here above


        if noError:


            numberOfRows=len(dataframe)


            # print(numberOfRows)

            # print('numberOfRows above')

            if rw<numberOfRows:

                # if LocationAsked == '':

                #     location='AutoFormFillerOutputFiles'

                #     home = os.path.expanduser('~')       
                #     filePath = os.path.join(home, 'Documents',location)

                # else:
                    
                #     filePath = LocationAsked[:-1]



                if not os.path.exists(filePath):
                    os.makedirs(filePath)



                # print(dataframe)

                # print(len(dataframe))

                # print(rw)


                # print(dataframe[rw])

                # print(dataframe[rw][0])        # the save location name for the item rw

                # print(dataframe[rw][1])        # the first item name to add

                # print(rw)                       # the number used to count goes into function also the row to be added

                # print(len(dataframe[rw]))

                # print('len(print(dataframe[rw]))')

                # print(OutputTableName3[0])


                FinalSaveLocation0 = dataframe[rw][0]

                        

                # # dataList1 = [BaseFileLocation, filePath,]

                # # dataNameList1['BaseFileLocation', 'filePath', ]
                
                # # getTableData.MultipleListWriteDataDatabase(dataList=dataList1, dataNameList=dataNameList1)

                FinalSaveLocation=filePath +"\\" + FinalSaveLocation0 

            
                OriginalImageLocation0 = BaseFileLocation


                systemFonts = GetAllFontNamesFromFolderFunction.GetAllFontNamesFromFolder()

                        
                systemFontsList=systemFonts.split('|')


                newFont = FontName

                indexOfItemInListOfFonts=systemFontsList.index(newFont)

                # print(indexOfItemInListOfFonts)

                fontFilePaths=GetFontFilePaths.GetFontFilePaths()


                fontSelectedPath= fontFilePaths[indexOfItemInListOfFonts]



                img = Image.open(OriginalImageLocation0)
                draw = ImageDraw.Draw(img)


                FontSize1 = int(FontSize)

                font = ImageFont.truetype(fontSelectedPath, FontSize1)


                # print(InvOutputTableName3)        

                # print('InvOutputTableName3 above')

                # print(RealListOfColumnnames)

                # print('RealListOfColumnnames')


                for j in range(len(RealListOfColumnnames)  -1 ):

                    i = j+1

                    TextToPut = dataframe[rw][i]
                    textWidth, textHeight = draw.textsize(TextToPut, font)

                    # print(i)

                    # print(RealListOfColumnnames)    #this is ok

                    # print(RealListOfColumnnames[1])

                    # print(InvOutputTableName3)    # this is not ok

                    # print(FileKey)

                    # print(RealListOfColumnnames)

                    # print(InvOutputTableName3)

                    # print(RealListOfColumnnames[i])

                    # print(dataframe[rw][0])


                    # print(dataframe[rw][i])

                    

                    

                    

                    #ListInvOutputTableName3 = InvOutputTableName3[RealListOfColumnnames[i]]    # this list starts at 1 and goes to amount of items


                    ListInvOutputTableName3 = OutputTableName3Keys[i]


                    draw.text((int(ListInvOutputTableName3[1]), int(ListInvOutputTableName3[0]) - textHeight ),TextToPut,(0,0,0),font=font)

                FileSaved= False
                try:
                    img.save(FinalSaveLocation)
                    FileSaved = True

                except:
                    # print("rw"+str(rw))
                    # print("DocNOTsaved")
                    # ListToPrint.append('DocNOTsaved')
                    pass




                if FileSaved== False:
                    try:
                        FinalSaveLocation = getUniqueAddFileEndWithFIlename.getUniqueAddFileEndWithFIlename(filename=FinalSaveLocation)

                        img.save(FinalSaveLocation)
                        FileSaved = True

                    except:
                        # print("rw"+str(rw))
                        # print("DocNOTsaved")
                        ListToPrint.append('DocNOTsaved')
                        PrintTexListSerial.PrintTexListSerial(ListToPrint = ListToPrint)








                if FileSaved:

                    rw=rw+1
                    # print("rw"+str(rw))


                
                    #delete temp file below

                    # import os
                    os.remove(BaseFileLocation)

                    # print("BaseFileLocation temp File Removed!")



                    # The next file name to come is below
                    AllDone = True
                    try:
                        
                        FSaVedLocation=dataframe[rw][0]
                        AllDone = False

                    except:
                        FSaVedLocation="Done"



                    if rw == 1:


                        currentDT = datetime.datetime.now()
                        # print (str(currentDT))



                        # print(str(currentDT).split('.')[0])

                        timeNow = str(currentDT).split('.')[0].replace(':', '-').replace(' ', '_')


                        IdentifierName0 = datafillName +'-' + timeNow


                        spaceReplaceDataUserImput = '$%78&*&'



                        IdentifierName = '_'.join(IdentifierName0.split(spaceReplaceDataUserImput))



                        
                        TextToWrite = str(dataframe) + ', '+ str([RealListOfColumnnames])

                        # if IsDoubleList:
                        TextToWriteQR = str(dataframe0) + ', '+ str([RealListOfColumnnames])
                        # else:
                        #     TextToWriteQR = str(dataframe1) + ', '+ str([RealListOfColumnnames])


                        # print(TextToWrite)

                        # print('QR TextToWrite above')


                        # print(type(TextToWrite))

                        # print('type QR TextToWrite above')

                        # checkContinueValue = 'ghkfasdygdi345363'

                        SaveLocationTxt = filePath +"\\" + IdentifierName +  '_Txt' + '.txt'

                        # SaveLocationQR =  filePath +"\\" + IdentifierName +  '_QR' + '.png'

                        SaveLocationLitxt =  filePath +"\\" + IdentifierName +  '_TxLi' + '.txt'


                    

                        TextToWrite2 = str(TextToWrite).replace(']], [', ']], \n [').replace('], [', '], \n [')


                        generateTxtFile.generateTxtFile(TextToWrite=TextToWrite2,SaveLocation=SaveLocationTxt)

                        ## generateQRfromText.generateQRfromText(TextToAdd=TextToWrite,checkContinueValue=checkContinueValue,SaveLocation=SaveLocationQR)

                        #generateQRfromText.generateQRfromText(TextToAdd=TextToWriteQR,checkContinueValue=checkContinueValue,SaveLocation=SaveLocationQR)

                        generateTxtFile.generateTxtFile(TextToWrite=TextToWriteQR,SaveLocation=SaveLocationLitxt, changeExtension = True)

                        




                    


                    # print(FSaVedLocation)
                    # print((FSaVedLocation.split('.')[0])+".jpg")
                    
                    FFinalSaveLocation2=(FSaVedLocation.split("\\")[-1])
                    
                    # print(FFinalSaveLocation2)
                    
                    
                    FFinalSaveLocation1=(FFinalSaveLocation2.split("/")[-1])
                    
                    # print(FFinalSaveLocation1)

                    # uniqueValue = getUniqueAddFileEnd.getUniqueAddFileEnd()

                    IdenfierName = (FFinalSaveLocation1.split('.')[0])
                    
                    # FFinalSaveLocation0=(FFinalSaveLocation1.split('.')[0]) + ".jpg"

                    FFinalSaveLocation0 = IdenfierName + ".jpg"


                    
                    
                    # print(FFinalSaveLocation0)


                    # The next file name to come is above



                    data=rw

                    dataName='rw'

                    getTableData.WriteDataDatabase(data,dataName)


                    percentageDone=int((rw/numberOfRows)*100)

                    # print(percentageDone)

                    ListToPrint.append(percentageDone)

                    #the percent done at the moment


                    # print(numberOfRows)

                    ListToPrint.append(numberOfRows)

                    # number of rows above

                    # print(rw+1)

                    ListToPrint.append(rw+1)

                    # step in completion above

                    if AllDone:
                        # print(FSaVedLocation)
                        ListToPrint.append(FSaVedLocation)

                    else:
                    #     print(FFinalSaveLocation0)
                        ListToPrint.append(FFinalSaveLocation0)

                    # final save locatiion of current saved item

                    # print("ItemSaved")
                    ListToPrint.append("ItemSaved")


                    # number of prints to go back is 5

                    PrintTexListSerial.PrintTexListSerial(ListToPrint = ListToPrint)

        

            if rw==numberOfRows:
                

                path=os.path.realpath(filePath)
                os.startfile(path)


                # add txt and qr code add file function here


                # TextToWrite = dataframe

                # checkContinueValue = 'ghkfasdygdi345363'

                # SaveLocationTxt = filePath +"\\" + IdenfierName +  '_Txt' + '.txt'

                # SaveLocationQR =  filePath +"\\" + IdenfierName +  '_QR' + '.png'


                # generateTxtFile.generateTxtFile(TextToWrite=TextToWrite,SaveLocation=SaveLocationTxt)

                # generateQRfromText.generateQRfromText(TextToAdd=TextToWrite,checkContinueValue=checkContinueValue,SaveLocation=SaveLocationQR)







                # print("AllDONE")

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



