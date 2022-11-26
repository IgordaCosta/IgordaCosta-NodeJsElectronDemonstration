import pandas

from importedDataPyAutoFormFiller_OutputFiles import *
import getTableData
import getLocationValues
import FileExistInDatabaseFunction
import GetExcelFilesinLocation
import changeDirectory
# import PrintTexListSerial

from importedDataPyexcelLocation import *


def LMFAddInfoExcel():

 

        filename=getTableData.GetDataFromDatabase(dataName='filename')




        

        filesInFolder1=GetExcelFilesinLocation.GetExcelFilesinLocation(location=excelLocation)

        filesInFolder2=GetExcelFilesinLocation.GetExcelFilesinLocation(location=AutoFormFiller_OutputFiles)



        listTocheck=[filename]+filesInFolder1+filesInFolder2


        changeDirectory.ChangeTokey()

        storedValues=pandas.read_excel(filename)



        # commaReplace = '$%#3Ba$*&'


        # storedValues = storedValues1.replace(', ',commaReplace, regex=True)





        storedValues0=getLocationValues.getLocationValues(dataframe=storedValues, column="Save Name")
        
        FileExistInDatabaseFunction.FileExistInDatabaseFunction(dataframe=storedValues0,column="Save Name",filename=filename, listTocheck=listTocheck)        
        


        # print(storedValues)
        # print("storedValues after")


        data = 0

        dataName = 'rw'

        getTableData.WriteDataDatabase(data=data,dataName=dataName)
    
            
   





LMFAddInfoExcel()