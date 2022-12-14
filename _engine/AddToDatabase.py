import os
from os import listdir
from os.path import isfile, join

from importedDataPyimageFolderLocation import *
from importedDataPyinternalLocation import *
from importedDataPyexcelLocation import *
from importedDataPyFilesInDatabaseLocation import *
from importedDataPyupdateNamesFile import *
from importedDataPyinternalLocation import *
import changeDirectory
import getTableData
import ListToSentence
import pdfToJpg
import PrintTexListSerial
import base93Characterconversion



def AddToDatabase(updateNamesFile, FilesInDatabaseLocation, fname=""):

    ListToPrint = []

    changeDirectory.ChangeTokey()
    
    SqlDatase=True
    updateNamesFile0 = updateNamesFile

    FilesInDatabaseLocation0  = FilesInDatabaseLocation
        
    if SqlDatase==True:
        updateNamesFile=updateNamesFile0.split('.')[0]
        FilesInDatabaseLocation=FilesInDatabaseLocation0.split('.')[0]

    
    home = os.path.expanduser('~')
    
    filePath = os.path.join(home, internalLocation ,excelLocation)
    
    if fname !='':
    
        ExtensionUsed = getTableData.GetTableData()['ExtensionType']

        if ExtensionUsed == 'pdf':

            import PyPDF2
            file = open(fname, 'rb')
            readpdf = PyPDF2.PdfFileReader(file)
            totalpages = readpdf.numPages
            if totalpages == 1:

                FolderLocation = '\\'.join(fname.split('\\')[:-1]) + '\\'
                PdfFileName = fname.split('\\')[-1]

                # print(FolderLocation)

                # print(PdfFileName)

                filenameOutputUsed = pdfToJpg.pdfToJpg(FolderLocation= FolderLocation,PdfFileName=PdfFileName)

                print(filenameOutputUsed)

                #already added the '\\' above
                NewFileFocus = FolderLocation + filenameOutputUsed

                PDFfile ='true'

                dataNameList = ['ExtensionType','fileLocation']
                dataList = ['image', NewFileFocus]

                getTableData.MultipleListWriteDataDatabase(dataList=dataList,dataNameList=dataNameList)

                fname = NewFileFocus
        else:
             PDFfile ='false'
        
        fname=fname.replace("\\","/")
        
        fileNameOnly=fname.split("/")[-1]
        
        InFileLocation, SenteceOpenFiles=CheckIfInFileLocation(fileToCheck=fileNameOnly, location=excelLocation)
        
        TempFolderLocation = filePath +"\\Temp"

        try:
            os.makedirs(TempFolderLocation)
        except FileExistsError:
            # directory already exists
            LocationToDeleteFIles = TempFolderLocation

            PDFfile = getTableData.GetTableData()['PDFfile']
            if PDFfile =='true':
                pass
            else:  
                pass
     

        FileEnding = base93Characterconversion.base93Characterconversion()

        newFileLocation= TempFolderLocation + "\\temp_" + '.'.join(str(fileNameOnly).split('.')[:-1]) + '_' + FileEnding + '.'+ str(fileNameOnly).split('.')[-1]

        newFileLocation0=filePath +"\\" + fileNameOnly

        Dictionary={'fname':fname, 'filePath':filePath, 'fileNameOnly':fileNameOnly ,'newFileLocation':newFileLocation,'newFileLocation0':newFileLocation0, 'FilesInDatabaseLocation':FilesInDatabaseLocation, 'imageFolderLocation':imageFolderLocation, 'PDFfile': PDFfile }

        DataToCheck = 'newFileLocation'   

        checkLocationOk = False  

        try:
            newFileLocation=getTableData.GetDataFromDatabase(DataToCheck)      

            checkLocationOk = True

        except:
            pass


        if checkLocationOk:

            newFileLocationImg =  TempFolderLocation +"\\" + fileNameOnly

            Dictionary={'fname':newFileLocation, 'filePath':filePath, 'fileNameOnly':fileNameOnly ,'newFileLocation':newFileLocation,'newFileLocation0':newFileLocation0, 'FilesInDatabaseLocation':FilesInDatabaseLocation, 'fileLocation': newFileLocation,  'newFileLocationImg': newFileLocationImg }

        if InFileLocation:
            FileExists='FileAlreadyExist'

            Dictionary['FileExists']=FileExists

            getTableData.MultipleDictionaryWriteDataDatabase(DictionaryAdd=Dictionary)

            ListToPrint.append('FileAlreadyExist')

        else:
            Dictionary['FileExists']='FileDoesNOTExist'
            
            getTableData.MultipleDictionaryWriteDataDatabase(DictionaryAdd=Dictionary)

            ListToPrint.append('FileDoesNOTExist')
       
        PrintTexListSerial.PrintTexListSerial(ListToPrint=ListToPrint)


#in function
def CheckIfInFileLocation(fileToCheck, internalLocation=internalLocation, location='AutoFormFillerFiles'):

        home = os.path.expanduser('~')
             
        filePath = os.path.join(home, internalLocation ,location)

        try:
            os.makedirs(filePath)
        except:
            pass
        
        files = [f for f in listdir(filePath) if isfile(join(filePath, f))]
        
        if isList(item=fileToCheck):
            if len(fileToCheck)==1:
                if fileToCheck[0] in files:
                    InFileLocation=True
                    SenteceOpenFiles=str(fileToCheck)
                else:
                    InFileLocation=False
                    SenteceOpenFiles=''
                    
            if isList(item=fileToCheck):    
                if len(fileToCheck)>1:
                    InFileLocation0=[]
                    ListOfOpenFiles=[]
                    for single in fileToCheck:
                        if single in files:
                            
                            value=True
                            InFileLocation0.append(value)
                            ListOfOpenFiles.append(single)
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

        return InFileLocation, SenteceOpenFiles

# in function
def isList(item):
        IsthisList=type(item)==type([])
        return IsthisList  





dataName = 'fileLocation'

stringOfChars=getTableData.GetDataFromDatabase(dataName)

AddToDatabase(updateNamesFile=updateNamesFile, fname = stringOfChars, FilesInDatabaseLocation=FilesInDatabaseLocation)
