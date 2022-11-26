import win32com.client as win32
import pandas
import os

import getTableData
import dropSqlTable
import createSqliteTableFromList
import CloseEspecificWorkbook
import CheckLocationDataExcel
import PrintTexListSerial












def getLocationsExcel():
    ListToPrint = []

    dataName='newFileLocation'

    xlfile=getTableData.GetDataFromDatabase(dataName=dataName)

    # xlapp = win32.gencache.EnsureDispatch('Excel.Application') 
                
    # xlapp.Visible = True
    # xlapp.DisplayAlerts = False
    
    # wb = xlapp.Workbooks.Open(xlfile)

    # ws = wb.Sheets(1)

    # pdExcelFile= pandas.read_excel(xlfile, header=None)

    # pdExcelShape=pdExcelFile.shape

    # allData = ws.UsedRange
            
    # excel = win32.gencache.EnsureDispatch('Excel.Application') 
    
    # excel.Visible = True
    
    # Get number of rows used on active sheet
    #ind = allData.Rows.Count

    # ind = pdExcelShape[0]

    # ind=ind+1

    # print ('Number of rows used in sheet : ', ind)
    
    #Get number of columns used on active sheet
    #col = allData.Columns.Count

    # col = pdExcelShape[1]

    # print ('Number of columns used in sheet : ', col)
    
    # print(col)
    
    # print(ind)
    
    
    # listOfValueNames=[]

    # listOfRows=[]

    # listOfColumns=[]

    # listOfValues=[]

    itemToCheck = "XYXYXYXYX"

    listOfColumns, listOfRows = CheckLocationDataExcel.CheckLocationDataExcel(FileLocation=xlfile,itemToCheck=itemToCheck)
    
    # for i in range(1,ind+1):
        
    #     for c in range(1,col+1):
            
    #         value = ws.Cells(i,c).Value
            
    #         if value == "XYXYXYXYX":

    #             # listOfValueNames.append("["+ str(i) +","+ str(c)+"]")

    #             listOfRows.append(i)

    #             listOfColumns.append(c)

    #             # listOfValues.append([i,c])





    




    getTableData.WriteDataDatabase(data=listOfRows,dataName='listOfRows')

    getTableData.WriteDataDatabase(data=listOfColumns,dataName='listOfColumns')



    


    NumList= len(listOfRows)

    ##### check the value in NumList if its empty send signal to
    # ask the user to try again

    if NumList == 0:
        # print('ListEmpty')
        ListToPrint.append('ListEmpty')

    else:

        getTableData.WriteDataDatabase(data=NumList,dataName='NumList')

        # print(xlfile)

        CloseEspecificWorkbook.CloseEspecificWorkbook(fileName=xlfile)


        os.remove(xlfile)
        # print("File Removed!")

        ListToPrint.append('')


    PrintTexListSerial.PrintTexListSerial(ListToPrint = ListToPrint)    
        









        # print("NumList")
        # print('listOfRows')
        # print('listOfColumns')

        # print(NumList)
        # print(listOfRows)
        # print(listOfColumns)

        

        
        # return NumList, listOfValueNames, rsp

        # data1=NumList
        # dataName1='NumList'

        # data2=listOfRows
        # dataName2='listOfRows'
        
        # data3=listOfColumns
        # dataName3='listOfColumns'


        ### continue to clickedAddFile the Write3DataDatabase may not be needed



        # Write3DataDatabase(data1=data1,data2=data2,data3=data3,dataName1=dataName1,dataName2=dataName2,dataName3=dataName3)

        # clickedAddFile.clickedAddFile(listOfValueNames=listOfValueNames)
        

        # print(listOfValueNames)

        # print(NumList)
        

        # print(listOfColumns)

        # print(listOfRows)
















getLocationsExcel()

# print('')