import os
import sys
from os import listdir
from os.path import isfile, join
# from typing import List

import changeDirectory
import getTableData
import ListToSentence
import pdfToJpg
import PrintTexListSerial



def AddToDatabase(fname=""):

    ListToPrint = []

    changeDirectory.ChangeTokey()

    # print(fname, flush=True)
    # print('fname', flush=True)
    
    SqlDatase=True
    
    updateNamesFile='updateNamesFile.xlsx'
    
    FilesInDatabaseLocation='FilesInDatabase.xlsx'
    
    if SqlDatase==True:
        updateNamesFile=updateNamesFile.split('.')[0]
        FilesInDatabaseLocation=FilesInDatabaseLocation.split('.')[0]
    
        
    internalLocation='Documents'
    excelLocation='AutoFormFillerFiles'
    
    # print("ok add file clicked")
    
    home = os.path.expanduser('~')
    
    # print(home)
    
    filePath = os.path.join(home, internalLocation ,excelLocation)
        
    # print("done up to before qfiledialog")
    
    if fname !='':
        
        # print(fname, flush=True)
        
        # print("fname", flush=True)

        ExtensionUsed = getTableData.GetTableData()['ExtensionType']

        if ExtensionUsed == 'pdf':

            import PyPDF2
            file = open(fname, 'rb')
            readpdf = PyPDF2.PdfFileReader(file)
            totalpages = readpdf.numPages
            # print(totalpages)
            if totalpages == 1:

                FolderLocation = '\\'.join(fname.split('\\')[:-1]) + '\\'
                PdfFileName = fname.split('\\')[-1]

                # print(FolderLocation)

                # print(PdfFileName)

                filenameOutputUsed = pdfToJpg.pdfToJpg(FolderLocation= FolderLocation,PdfFileName=PdfFileName)

                # print(filenameOutputUsed)

                NewFileFocus = FolderLocation + filenameOutputUsed

                # print(NewFileFocus)


                dataNameList = ['ExtensionType','fileLocation']
                dataList = ['image', NewFileFocus ]


                getTableData.MultipleListWriteDataDatabase(dataList=dataList,dataNameList=dataNameList)


                fname = NewFileFocus








        
        
        fname=fname.replace("\\","/")
        
        fileNameOnly=fname.split("/")[-1]
        
        # print(fileNameOnly, flush=True)
        # print('fileNameOnly', flush=True)
        
        InFileLocation, SenteceOpenFiles=CheckIfInFileLocation(fileToCheck=fileNameOnly, location=excelLocation)
        
        try:
            os.makedirs(filePath +"\\Temp")
        except FileExistsError:
            # directory already exists
            pass

        
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


        if checkLocationOk:

            newFileLocationImg =  filePath +"\\Temp\\" + fileNameOnly

            Dictionary={'fname':newFileLocation, 'filePath':filePath, 'fileNameOnly':fileNameOnly ,'newFileLocation':newFileLocation,'newFileLocation0':newFileLocation0, 'FilesInDatabaseLocation':FilesInDatabaseLocation, 'fileLocation': newFileLocation,  'newFileLocationImg': newFileLocationImg }

        
        if InFileLocation:
            # print("there is the same file inside")

            # print("SameFileInside")

            # print(fname)
            # print(filePath)
            # print(fileNameOnly)
            # print("FileAlreadyExist")

            FileExists='FileAlreadyExist'

            Dictionary['FileExists']=FileExists

            getTableData.MultipleDictionaryWriteDataDatabase(DictionaryAdd=Dictionary)

            # print("done 1")

            # print("FileAlreadyExist")

            ListToPrint.append('FileAlreadyExist')

        else:

            # print(fname)
            # print(filePath)
            # print(fileNameOnly)
            # print("FileDoesNOTExist")

            Dictionary['FileExists']='FileDoesNOTExist'
            # print(Dictionary)

            # print('Dictionary to write above')

            getTableData.MultipleDictionaryWriteDataDatabase(DictionaryAdd=Dictionary)


            # print(Dictionary)

            # print("done 1")

            # print("FileDoesNOTExist")

            ListToPrint.append('FileDoesNOTExist')


        
        PrintTexListSerial.PrintTexListSerial(ListToPrint=ListToPrint)


        




#in function
def CheckIfInFileLocation(fileToCheck, internalLocation='Documents', location='AutoFormFillerFiles'):
        

        home = os.path.expanduser('~')
             
        # print(home, flush=True)
         
        filePath = os.path.join(home, internalLocation ,location)

        
        # if not os.path.exists(filePath):
        try:
            os.makedirs(filePath)
        except:
            pass

        
        files = [f for f in listdir(filePath) if isfile(join(filePath, f))]
         
                
        # print(files, flush=True)
        # print('files', flush=True)

        # print(fileToCheck, flush=True)
        # print('fileToCheck', flush=True)


        ##### files printed above shows ? values which may cause error
        
        
        
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
                    # print(InFileLocation0)
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

        # print(InFileLocation, flush=True)
                
        return InFileLocation, SenteceOpenFiles

# in function
def isList(item):
        IsthisList=type(item)==type([])
        return IsthisList  





dataName = 'fileLocation'


stringOfChars=getTableData.GetDataFromDatabase(dataName)



AddToDatabase(stringOfChars)



# dataName = 'testLocationError'     ##### test remove when done

# try:
#     stringOfChars=getTableData.GetDataFromDatabase(dataName)       ##### test remove when done

# except KeyError:
#     print('all ok but now it stoped')

