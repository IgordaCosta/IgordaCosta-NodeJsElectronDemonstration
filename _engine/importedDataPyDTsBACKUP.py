
import FilePathFromPython
import GBTdat
from importedFNUDataPyDTs import *




try:
    TableDataValueSS3, TableDataValueSS2 = GBTdat.GetFlInf(fileName=fileNameUsed)

    Dasv = TableDataValueSS3
    pqw= ';' +  TableDataValueSS2
    dataBasePath = FilePathFromPython.FilePathFromPython()  + '\\' + Dasv


except FileNotFoundError:
    pass


# print(dataBasePath)


    


