from sqlite3.dbapi2 import Error
# import sys
import shutil
# import docx

import os

import changeDirectory
# import createSqliteTableFromList
# import dropSqlTable
import getTableData
import CloseEspecificWorkbook
import ForceCloseSpecificPaintFile
import closeWordWithHelp
import PrintTexListSerial





def GetLastNumTextFromText(TextToGet, WholeTextWithText):


    TextLenGetFROMLENMinus = len(WholeTextWithText) - len(TextToGet)

    EndText = WholeTextWithText[TextLenGetFROMLENMinus:]

    return EndText


# def ReturnFromSameFileInside(fname,filePath,fileNameOnly):
def ReturnFromSameFileInside():

    changeDirectory.ChangeTokey()

    curentWorkingDirectory = os.getcwd()
    # print(curentWorkingDirectory)
    # print("New curentWorkingDirectory")

    dictValue=getTableData.GetTableData()

    ListToPrint = []


    # print("bellow is the data")

    # print(dictValue)

    # print("==============================================")

    

    fname=dictValue['fname']

    filePath=dictValue['filePath']

    fileNameOnly=dictValue['fileNameOnly']

    ExtensionType = dictValue['ExtensionType']

    newFileLocation0 = dictValue['newFileLocation0']

    newFileLocation = dictValue['newFileLocation']

    # print(fname)
    # print(filePath)
    # print(fileNameOnly)
    




    # newFileLocation0=filePath +"\\" + fileNameOnly
    # print(newFileLocation0)

    # print("newFileLocation not coppied")

    # newFileLocation=filePath +"\\temp_" + fileNameOnly

   


    # print(newFileLocation)
    
    # print("newFileLocation")
    copiedDoc=False
    rsp=1
    ####################### while copiedDoc==False and rsp==1: keep blocked

    
    #### blocked from below this
    if ExtensionType=='excel':
        CloseEspecificWorkbook.CloseEspecificWorkbook(fileName=newFileLocation)

    if ExtensionType=='image':
        ForceCloseSpecificPaintFile.ForceCloseSpecificPaintFile(fileName=newFileLocation, Program="Paint")

    if ExtensionType=='word':
        # raise ValueError('Come to ReturnFromSameFileInside.py file and add a close function in case the word file is open ')
        Donefunc= closeWordWithHelp.closeWord(fileName=newFileLocation)
        if Donefunc == 'SheetIsOpenAndHasChanges':
            ForceCloseSpecificPaintFile.ForceCloseSpecificPaintFile(fileName=newFileLocation, Program="Word")


    if ExtensionType=='pdf':
        ForceCloseSpecificPaintFile.ForceCloseSpecificPaintFile(fileName=newFileLocation, Program="Adobe Acrobat Reader DC")

    try:
        # shutil.copy2(fname, newFileLocation)
        shutil.copy(fname, newFileLocation)

        copiedDoc=True



        # dropSqlTable.DropTable()



        # print(copiedDocTrue)
    except PermissionError:
        copiedDoc=False
        ####  the program window will change with the message below asking the user for assisstance after the save the program goes to a different window
        #### "There is a program dependent document that is currently opened and altered. Save or close this document and click OK to continue or click CANCEL to cancel the operation."
        # print(copiedDocFalse)

    except Exception as WholeTextWithText0:

        WholeTextWithText = str(WholeTextWithText0)
        TextToGet = 'are the same file'

        OutputCheck = GetLastNumTextFromText(TextToGet, WholeTextWithText)

        if OutputCheck == TextToGet:
            copiedDoc=True
            
        else:
            raise Error

        # print(str(e) == 'INFO: No tasks running with the specified criteria.')

        # print('Ok is true above')

    
    # print('copiedDoc')
   

    # print(copiedDoc)
    # print(newFileLocation0)

    ListToPrint.append(copiedDoc)


    PrintTexListSerial.PrintTexListSerial(ListToPrint=ListToPrint)





    



# fname = sys.argv[1]
# filePath = sys.argv[2]
# fileNameOnly = sys.argv[3]

# print('fname',fname)
# print('filePath',filePath)
# print('fileNameOnly',fileNameOnly)




# ReturnFromSameFileInside(fname,filePath,fileNameOnly)


ReturnFromSameFileInside()