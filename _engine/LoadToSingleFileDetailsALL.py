import os
import pandas
# from StyleFrame import StyleFrame, Styler
from styleframe import StyleFrame, Styler

import GetExcelFilesinLocation
import ListToSentence
import getLocationValues
import readSqlDatabase
import getAddressesFromColumn
import openWorkbook
import ChangeStartupDirectoryT
from importedDataPyexcelLocation import *


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
    print(frame2)
    print('ok 1111')
    
    print(columnsList)
    
    print('columnsList used in frameStyle')
        
    ew = StyleFrame.ExcelWriter(path)
    
    print('ok 2222')
        
    HeaderStyle= Styler(bg_color=DecHex(BackgroundRGBr)+DecHex(BackgroundRGBg)+DecHex(BackgroundRGBb), bold=True, font_color= DecHex(LetterRGBr)+DecHex(LetterRGBg)+DecHex(LetterRGBb), border_type='medium', horizontal_alignment='center', vertical_alignment='center', shrink_to_fit=False)
        
    print('ok 3333')
    
    frame2.apply_headers_style(HeaderStyle, style_index_header=True)
        
    print('ok 4444')
    StyleFrame.set_column_width_dict(frame2, DictionaryofWidths)
    
    StyleFrame.to_excel(frame2, excel_writer = ew, sheet_name='Sheet1')

    print('ok 5555')
    
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


def valueInList(firstList,listTocheck, InListFlag=True, KeepOriginal=True):
    
    print(listTocheck)
    print("listTocheck before before")
        
    firstList1=getLocationValues.getLocationValues(dataframe=firstList)
    
    listTocheck1=getLocationValues.getLocationValues(dataframe=listTocheck)
    
    print(firstList1)
    
    print("firstList1 in valueInList1 before")
    
    print(listTocheck1)
    
    print("listTocheck1 in valueInList before")
    
    
    ListofInlist=[]
    ExistInside=False
    for value in range(len(listTocheck1)):
        if InListFlag==True:
            Inlist=listTocheck1[value] in firstList1
        if InListFlag==False:    
            Inlist=listTocheck1[value] not in firstList1
        if Inlist:
            ExistInside=True
            if KeepOriginal==True:
                ListofInlist.append(listTocheck[value])
            if KeepOriginal==False:
                ListofInlist.append(listTocheck1[value])
                
    print(ListofInlist)
    return ExistInside, ListofInlist 


def FolderHasProribitedFileNames():
        
        filename="OneFileToMultipleFiles.xlsx"
        
        location="AutoFormFillerKey"
        
        home = os.path.expanduser('~')    
        
        filePath = os.path.join(home, 'Documents',location)
        
        filename2=filePath+"\\"+filename
        
                
        print(home)
        
        location = os.path.join(home, 'Desktop')
        
        SelectedFolder=''
        
        ExistInside=True
        rsp=1
        IgonoreClicked=False
        while ExistInside==True and rsp==1:
            SelectedFolder = QFileDialog.getExistingDirectory(str("Select the folder where the files are located"),location, QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
            
            print(SelectedFolder)
                   
             
            SelectedFolderFiles=GetExcelFilesinLocation.GetExcelFilesinLocation(location=SelectedFolder, IncludeFolder=True)
            
            print(SelectedFolderFiles)
            
            
            # filesInFolder1=GetExcelFilesinLocation.GetExcelFilesinLocation(location="AutoFormFillerFiles", IncludeFolder=True)
            filesInFolder1=GetExcelFilesinLocation.GetExcelFilesinLocation(location=excelLocation, IncludeFolder=True)
            
            
            listTocheck=[filename2]+filesInFolder1
            
            print(listTocheck)
            print("listTocheck before check")
            
            
            print(SelectedFolderFiles)
            print("SelectedFolderFiles before check")
            
        
            ExistInside, ListofInlist=valueInList(firstList=SelectedFolderFiles,listTocheck=listTocheck, InListFlag=True, KeepOriginal=False)
            
            print(ExistInside)
            print(ListofInlist)
            
            print("ListofInlist after check")
            
            ListofInlist2=ListToSentence.ListToSentence(ListUsed=ListofInlist)
            
            print(ListofInlist2)
            if ExistInside==True:
                print("ok its inside")
                rsp=DProriFileNamesInFolderUsed(filenameUsed=ListofInlist2)
                print(rsp)
        
        if IgonoreClicked==True:
            rsp=1
            ExistInside, SelectedFolderFiles=valueInList(firstList=listTocheck,listTocheck=SelectedFolderFiles, InListFlag=False, KeepOriginal=True)
            print(SelectedFolderFiles)
            print("SelectedFolderFiles after igore button clicked")
            
       
        return SelectedFolderFiles, rsp


def LoadToSingleFileDetails():

        # datafillName=getTableData.GetDataFromDatabase(dataName='datafillName')

        # FilesInDatabaseLocation='FilesInDatabase'
        # columnsFileinDatabase=['Job Name', 'File KEY', 'File Saved Location']
            
        # SelectedFolderFiles, rsp= FolderHasProribitedFileNames()
        
        # print(SelectedFolderFiles)
        
        # if len(SelectedFolderFiles)!=0 and rsp==1:
        #     print("folder chosen and it has data")
            
        #     FileFolder='AutoFormFillerSingleFileOutput'
        #     filename=''
            
        #     InFileLocation=True
        #     rsp=1
        #     IgonoreClicked=False
        #     while InFileLocation==True and rsp==1:
        #         rsp, filename=NameFileToSaveAs()
        #         if rsp==1:
        #             if filename !='':
        #                 updateNamesFile=filename.split('.')[0]
        #                 FinalFilename=updateNamesFile+".xlsx"
        #                 InFileLocation, SenteceOpenFiles=CheckIfInFileLocation(fileToCheck=FinalFilename, location=FileFolder)
                    
        #             else:
        #                 InFileLocation=True
                    
        #             if InFileLocation==True:
        #                 rsp=DSingleFileNameUsed(filenameUsed=FinalFilename)
        #     if IgonoreClicked:
        #         rsp=1
        #         InFileLocation=False
            
            
        #     if rsp==1:
   
        #         print(InFileLocation, "<<<InFileLocation value")
        #         if InFileLocation==False:
        #             home = os.path.expanduser('~')
                    
        #             filePath = os.path.join(home, 'Documents',FileFolder)
                     
        #             if not os.path.exists(filePath):
        #                 os.makedirs(filePath)
                    
        #             updateNamesFile=filename.split('.')[0]
        #             FinalFilename=updateNamesFile+".xlsx"
                    
        #             print("FinalFilename location name")
        #             print("filename used in the end")
                    
                    # filesInFolder=SelectedFolderFiles
                    # print(filesInFolder)
                    
                    # numberOfFilesinFolder=len(filesInFolder)
                    # print(numberOfFilesinFolder)
                    
                    # databaseUsed0=readSqlDatabase.readSqlDatabase(table_name="KEY_"+datafillName)
                    # databaseUsed=databaseUsed0[0]
                    
                    # print(databaseUsed)
                    
                    # print("databaseUsed")
                    
                    # itemAddress=databaseUsed.columns.values[1:]
                    # print(itemAddress)
                    
                    # itemDescription=databaseUsed.values[0][1:]
                    # print(itemDescription)
                    
                    # rowList, columnList=getAddressesFromColumn.getAddressesFromColumn(itemAddress=itemAddress)
                    
                    # numberOfRows=numberOfFilesinFolder
                    # print(numberOfRows)
                    
                    # ListUsed=[]
                    # for rw in range(numberOfRows):
                    #     print("open file in row to extract data")
                    #     ListUsed.append([])
                        
                    #     xlfile=filesInFolder[rw]
                        
                    #     wb = openWorkbook.openWorkbook(xlfile)
                    #     ws = wb.Sheets(1)
                        
                    #     if wb!=None:
                        
                    #         for cl in range(1,len(itemAddress)+1):
                
                    #             i=rowList[cl-1]
                    #             c=columnList[cl-1]
                                
                    #             ValueSaved=ws.Cells(i,c).Value
                                
                    #             ListUsed[rw].append(ValueSaved)
                            
                    #         wb.Close(True)
                   
                    print(ListUsed)
                    print("ListUsed values at the end")
                    
                    
                    df = pandas.DataFrame(ListUsed, columns =itemDescription)
                    df["Save Name"]=filesInFolder
                    
                    
                    itemDescription=["Save Name"]+list(itemDescription)
                    
                    df=df[itemDescription]
                    
                    print(df)
                    print("dataframe final")
                    

                    # ChangeStartupDirectory(Folder=FileFolder)
                    ChangeStartupDirectoryT.ChangeStartupDirectory(Folder=FileFolder)
                    FileSaved=False 
                    rsp=1
                    
                    while FileSaved==False and rsp==1:
                        print(rsp)
                        print("rsp")
                        writer = pandas.ExcelWriter(FinalFilename)
                    
                        df.to_excel(writer,'Sheet1', index=False)
                        
                        try:
                            writer.save()
                            FileSaved=True
                        except:
                            print("close excel file and try again")
                            rsp=DCloseDocToContinue(DocumentNameUsed=FinalFilename)
                            print(rsp)
                            print("rsp")
                            
                    print(FileSaved)
                    print("end of loop FileSaved")
                    

                    if rsp==1:
                        frameStyleByColor(path=FinalFilename, columnsList=itemDescription, color='blue')
                        os.startfile(FinalFilename)
                        
                        path=os.path.realpath(filePath)
                        os.startfile(path)
                        OperaConcluidaWindow()
                    
                    ChangeStartupDirectoryT.ChangeStartupDirectory(Folder='AutoFormFillerKey')






LoadToSingleFileDetails()
                    
 
    