import pathlib

from importedDataPyFAutoForm_FillerFiles import *
from importedDataPyinternalLocation import *
import JoinPdfs
import MultipleExcelToMultiplePdfs







homedir = pathlib.Path.home()


Folderlocation = str(homedir) + '\\' + internalLocation+'\\' + AutoForm_FillerFiles +'\\'

# print(Folderlocation)







nameOfNewFile="NewFileJoined"
desiredFileType="testFile"


MultipleExcelToMultiplePdfs.MultipleExcelToMultiplePdfs(Folderlocation=Folderlocation,desiredFileType=desiredFileType)


JoinPdfs.JoinPdfs(Folderlocation=Folderlocation,nameOfNewFile=nameOfNewFile,desiredFileType=desiredFileType)







