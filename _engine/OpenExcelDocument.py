# import win32com.client as win32
import os

import getTableData
# import createSqliteTableFromList
# import dropSqlTable



from importedDataPyexcelLocation import *
from importedDataPyinternalLocation import *
import PrintTexListSerial
import openWorkbook
import CloseEspecificWorkbook

def OpenExcelDocument():
    # wb = openWorkbook(newFileLocation)

    Dictionary=getTableData.GetTableData()
    # print(Dictionary)

    fileNameOnly=Dictionary['fileNameOnly']
    
    exceptionRunned =False
    try:
        newFileLocation=Dictionary['newFileLocation']
    except:
        exceptionRunned = True
    
    if exceptionRunned:
        home = os.path.expanduser('~')
        
        filePath = os.path.join(home, internalLocation ,excelLocation)
        
        try:
            os.makedirs(filePath +"\\Temp")
        except FileExistsError:
            # directory already exists
            pass

        newFileLocation=filePath +"\\Temp\\temp_" + fileNameOnly
        Dictionary['newFileLocation']=newFileLocation

    # print(newFileLocation)

    # print('newFileLocation above')
    

    # openWorkbook(newFileLocation)

    CloseEspecificWorkbook.CloseEspecificWorkbook(fileName=newFileLocation)

    wb,excel,noError = openWorkbook.openWorkbook(xlfile=newFileLocation, Invisable=False)


    ListToPrint = []
    if noError:
        ListToPrint.append('AllOk')

    else:
        ListToPrint.append('ERROR')

    PrintTexListSerial.PrintTexListSerial(ListToPrint = ListToPrint)




    # # if wb!=None:
    # #     print("continue")

    # #     # rsp=self.CopyPasteWindow()
    # # else:
    # #     print("DONOTcontinue")




# def openWorkbook(xlfile):
#         # rsp=1
#         # noerror=False
#         # xlwb = None    
#         # while rsp==1 and noerror==False:
#         print(xlfile)
#         print('xlfile above')
#         try:
            
#             # xlapp = win32.gencache.EnsureDispatch('Excel.Application')
            
#             # xlapp.DisplayAlerts = False
#             # # print("no eror -1")
#             # # xlapp.Visible = True

#             # xlapp.Visible = False
#             # # print("no eror 0")
#             # # noerror=True
#             # # rsp=1
#             # print("AllOk")


#             xlapp = win32.gencache.EnsureDispatch('Excel.Application')
#             xlapp.Visible = True
#             xlapp.WindowState = win32.constants.xlMaximized #added to maximaze excel sheet after opening it
#             wb = xlapp.Workbooks.Open(xlfile, False, False, None)


#             #### add wb to databse of values




#             # Dictionary=getTableData.GetTableData()
#             # Dictionary["wb"]=wb

#             # del Dictionary['id']

#             # dropSqlTable.DropTable()

#             # createSqliteTableFromList.SetValues(Dictionary=Dictionary)



#             print("AllOk")
#         except TypeError:
#             print('sheet is open and has changes')
#             # rsp = self.InicioSalveDocumento()

#             print("ERROR")

#     ##### get this print statament to continue with the rest of the program bellow

        
# #         if rsp==1:
            
# #             if noerror==True:
        
# #                     try:
# #                         print("no eror 1")
# #                         xlapp = win32.gencache.EnsureDispatch('Excel.Application')
# # # =============================================================================
# # #                         xlapp.ScreenUpdating = False
# # #                         xlapp.DisplayAlerts = False
# # #                         xlapp.EnableEvents = False
# # # =============================================================================
                        
# #                         xlapp.DisplayAlerts = False
# #                         xlapp.Visible = True
# #                         print("no eror 2")
# #                         xlwb = xlapp.Workbooks.Open(xlfile)
# #                         #xlapp.Visible = True
# #                         print("no eror 3")
# #                         #xlapp.DisplayAlerts = False
# #                     except Exception as e:
# #                         print("no eror exception")
# #                         print(e)
# #                         xlapp.DisplayAlerts = False
# #                         map(lambda book: book.Close(False), xlapp.Workbooks)
# #                         xlapp.Quit()
                        
# #                         xlapp = win32.gencache.EnsureDispatch('Excel.Application') 
# # # =============================================================================
# # #                         xlapp.ScreenUpdating = False
# # #                         xlapp.DisplayAlerts = False
# # #                         xlapp.EnableEvents = False
# # # =============================================================================
                        
                        
# #                         xlapp.Visible = True
# #                         xlapp.DisplayAlerts = False
                        
# #                         xlwb = xlapp.Workbooks.Open(xlfile)
# #                         #xlapp.Visible = True
                        
                        
# # # =============================================================================
# # #         xlapp.ScreenUpdating = True
# # #         xlapp.DisplayAlerts = True
# # #         xlapp.EnableEvents = True        
# # # =============================================================================
# #         return(xlwb)








# ##### make one or multiple tables in database dased on what the user needs

# #### make one with this information that is needed for this area

# # newFileLocation

# # # home = os.path.expanduser('~')





# # # newFileLocation=filePath +"\\temp_" + fileNameOnly




# OpenExcelDocument(newFileLocation)

OpenExcelDocument()
            