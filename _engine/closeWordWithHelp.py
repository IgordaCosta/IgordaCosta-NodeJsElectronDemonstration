import win32com.client as win32

import PrintTexListSerial



# newFileLocation="C:\\Users\\IgorDC\\Desktop\\barra De Progresso Igor 2.docx"

# doc = docx.Document(newFileLocation) 
# print(doc)


# fileName="C:\\Users\\IgorDC\\Desktop\\barra De Progresso Igor 2.docx"

#### Add this close function method to the excel and if possible the pdf and image documents 

def closeWord(fileName):

    ListToPrint = []
    word = win32.gencache.EnsureDispatch('Word.Application')

    try:
        returnValue=word.Documents.Open(fileName).Close(True)
        # print("AllOK")

        ListToPrint.append('AllOK')
    except:
        # print('SheetIsOpenAndHasChanges')
        ListToPrint.append('SheetIsOpenAndHasChanges')
    
    # PrintTexListSerial.PrintTexListSerial(ListToPrint = ListToPrint)

    
    # print(returnValue)




def OpenWord(fileName):

    ListToPrint = []
    # word = win32.gencache.EnsureDispatch('Word.Application')

    word = win32.Dispatch('Word.Application')
    
    word.Visible = True
            
    word.ScreenUpdating = True
    word.DisplayAlerts = True
    #word.EnableEvents = True
    # word.WindowState = win32.constants.xlMaximized  # this works for me 
    
    word.WindowState = win32.constants.wdWindowStateMaximize


    try:
        returnValue=word.Documents.Open(fileName)
        word.Visible = True
            
        word.ScreenUpdating = True
        word.DisplayAlerts = True
        #word.EnableEvents = True

        #word.WindowState = win32.constants.xlMaximized  # this works for me 

        word.WindowState = win32.constants.wdWindowStateMaximize

        ListToPrint.append('AllOK')
    except:
        # print('SheetIsOpenAndHasChanges')
        ListToPrint.append('SheetIsOpenAndHasChanges')

    
    PrintTexListSerial.PrintTexListSerial(ListToPrint = ListToPrint)


