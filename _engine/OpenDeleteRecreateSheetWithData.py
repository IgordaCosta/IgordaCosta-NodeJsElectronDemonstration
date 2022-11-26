import pandas
import openpyxl
# import os
from win32com.client import Dispatch
# import win32com.client as win32
# from StyleFrame import StyleFrame, Styler

from styleframe import StyleFrame, Styler



# import getTableData
# import StringListIntoList
import openWorkbook


def OpenDeleteRecreateSheet(columnList, dataList, filename):

    # dataNameList=['filename','columnList']

    # OutputDictionary=getTableData.GetMultipleDataFromDatabase(dataNameList=dataNameList)

    # filename = OutputDictionary['filename']
    # columnList = OutputDictionary['columnList']

    # columnList=StringListIntoList.StringListIntoList(StringList=columnList)

    

    frame=pandas.DataFrame(dataList, columns=columnList)
    
    writer = pandas.ExcelWriter(filename)
    # print('check 111111')
    try:   
        wb=openpyxl.load_workbook(filename)
        # print('check 222222')
        sheetloaded=True
    except:
        sheetloaded=False
        ProblemSaving=False
        pass
    
    if sheetloaded==True:    
        # print('check 222333')
        del wb['Sheet1']
        # print('check 333333')
        
        try:
            writer.save()
            ProblemSaving=False
        except:
            ProblemSaving=True

    if ProblemSaving:
        ProblemSavingTrue(filename,frame,columnList)

    else:
        # print("Done this part, go to next")
        SavedOK(filename,frame,columnList)
                
        

def ProblemSavingTrue(filename,frame,columnList):
    SavedFile=False
    try:
        xl = Dispatch('Excel.Application')
        wb = xl.Workbooks(filename)
        writer.save()
        wb.Close(True)
        SavedFile=True
        # print("saved file successuly")
    except Exception as e:
        # print(e)
        pass

    # print(SavedFile)

    if SavedFile:
        # print("continue to the next part")
        SavedOK(filename,frame,columnList)
    
    else:
        # print("did NOT save")
        # brings to window saying that the file is open and altered and asks the user to close it
        # save "filename,frame,columnList" values
        #afterwards it sends the user to the OpenDeleteRecreateSheet function again
        pass

    
                    
def SavedOK(filename,frame,columnList):
       
    writer = pandas.ExcelWriter(filename)
    
    # print(frame)
    # print('frame before column filtering')
    
    #### noColumnList=False added so columnlistfilter can be ignored
    
    frame=frame[columnList]
    
    # print(frame)
    # print("frame with unamed")

    frame.drop(frame.columns[frame.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
    # print("step 1111111" )
    #frame.to_excel(writer,'Sheet1', index=False)
    frame.to_excel(writer, index=False)
    # print("step 22222222" )
    try:
        
        writer.save()
        # print("step 333333333" )
    except PermissionError:
        xl = Dispatch('Excel.Application')
        # print("step 44444444444" )
        wb = xl.Workbooks(filename)
        # print("step 55555555" )
        # do some stuff
        wb.Close(True) # save the workbook
        # print("step 66666666" )
        writer.save()
        # print("step 777777777" )


    frameStyleByColor(path=filename, columnsList=columnList, color='blue')

    # os.startfile(filename)

    openWorkbook.openWorkbook(xlfile=filename, Invisable=False)

    # print("continue to next section print new screen")

    # print("Saved OK")

    
        
    


def frameStyleByColor(path, columnsList, color):
        
        if color=='blue':
            frameStyle(path=path, columnsList=columnsList)
            pass
        
        if color=='green':
            frameStyle(path=path, columnsList=columnsList, BackgroundRGBr=0 , BackgroundRGBg= 195, BackgroundRGBb=0)
            pass
        
        if color=='red':
            frameStyle(path=path, columnsList=columnsList, BackgroundRGBr=237 , BackgroundRGBg= 0, BackgroundRGBb=0)
            pass
        
        if color=='yellow':
            frameStyle(path=path, columnsList=columnsList, BackgroundRGBr=255 , BackgroundRGBg= 255, BackgroundRGBb=0, LetterRGBr=0, LetterRGBg=0, LetterRGBb=0)
            pass
        
    
    
def frameStyle(path,columnsList,BackgroundRGBr=0,BackgroundRGBg=0,BackgroundRGBb=206,LetterRGBr=255,LetterRGBg=255,LetterRGBb=255):

    DictionaryofWidths= {x: 1.3*(int(len(x))+13) for x in columnsList}

    frame2 = StyleFrame.read_excel(path= path, sheet_name='Sheet1')

    # print(frame2)
    # print('ok 1111')
    
    # print(columnsList)
    
    # print('columnsList used in frameStyle')
        
    ew = StyleFrame.ExcelWriter(path)

        
    # print('ok 2222')
        
    HeaderStyle= Styler(bg_color = DecHex(BackgroundRGBr)+ DecHex(BackgroundRGBg)+ DecHex(BackgroundRGBb), bold=True, font_color= DecHex(LetterRGBr)+ DecHex(LetterRGBg)+ DecHex(LetterRGBb), border_type='medium', horizontal_alignment='center', vertical_alignment='center', shrink_to_fit=False)
        
    # print('ok 3333')
    
    frame2.apply_headers_style(HeaderStyle, style_index_header=True)
        
    # print('ok 4444')
    StyleFrame.set_column_width_dict(frame2, DictionaryofWidths)

    
    StyleFrame.to_excel(frame2, excel_writer = ew, sheet_name='Sheet1')


    # print('ok 5555')
    
    ew.save()
    
    
def DecHex(n):
    '''
    :para n: int
    :return: str
    >>> DecHex(10)
    'A'
    >>> DecHex(15)
    'F'
    >>> DecHex(32)
    '20'
    >>> DecHex(255)
    'FF'
    >>> DecHex(65535)
    'FFFF'
    '''

    x16 = '0 1 2 3 4 5 6 7 8 9 a b c d e f'.upper().split()
    result = []
    try:
        n = int(n)
        if n == 0:
            return '00'
        if 17 > n:
            result.append('0' + x16[(n % 16)])
            n = n // 16
        result.reverse()
        while n > 0:
            result.append(x16[(n % 16)])
            n = n // 16
        result.reverse()
    except ValueError as e:
        return ('Erro: %s' %e)
    except:
        raise
    else:
        return ''.join(result)