import pandas
import numpy








def CheckLocationDataExcel(FileLocation,itemToCheck):

    pdExcelFile=pandas.read_excel(FileLocation,header=None)

    listOfRows=[]

    listOfColumns=[]

    for i in range(len(pdExcelFile.columns)):
        location=numpy.where(pdExcelFile[i] == itemToCheck)
        TudoOK=False
        try:
            result=location[0][0]
            TudoOK=True
        except:
            pass

        if TudoOK:
            for x in location[0]:
                listOfRows.append(x+1)
                listOfColumns.append(i+1)

            
    return listOfColumns, listOfRows








        
# itemToCheck = 'XYXYXYXYX'


# FileLocation= r'C:\Users\IgorDC\Desktop\Hard_testExcel.xlsx'


# # FileLocation= r'C:\Users\IgorDC\Desktop\testExcel.xlsx'





# listOfColumns, listOfRows = CheckLocationDataExcel(FileLocation,itemToCheck)


# print('columnList: ',listOfColumns)

# print('RowList: ',listOfRows)
