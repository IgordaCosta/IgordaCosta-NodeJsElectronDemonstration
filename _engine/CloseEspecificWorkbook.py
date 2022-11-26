# from win32com.client import Dispatch

import win32com.client as win32

import ForceCloseExcelFunction


def CloseEspecificWorkbook(fileName):

    
    
        
    noError=False
    try:
        
        excel = win32.Dispatch('Excel.Application')
        
       
        excel.DisplayAlerts = False

        excel.Visible = False

        
        excel.ScreenUpdating = False
        excel.DisplayAlerts = False
        excel.EnableEvents = False

        noError=True

    except:
        noError=False
        # print('SheetIsOpenAndHasChanges')

        ForceCloseExcelFunction.ForceCloseExcel()
        



    
    if noError:

        try:

            
            excel = win32.Dispatch('Excel.Application')
                    
            # excel.Visible = False

            # excel.ScreenUpdating = False
            # excel.DisplayAlerts = False
            # excel.EnableEvents = False

            # print("no eror 2")
            wb = excel.Workbooks.Open(fileName)

            # excel.Visible = False
          
            # excel.ScreenUpdating = False
            # excel.DisplayAlerts = False
            # excel.EnableEvents = False

            wb.Close(True)

            # excel.ScreenUpdating = True
            # excel.DisplayAlerts = True
            # excel.EnableEvents = True

            # print("AllOK")

            # print("no eror 3")

        except Exception as e:
            # print("no eror exception")
            # print(e)
            
            # print("no eror 4")
            map(lambda book: book.Close(False), excel.Workbooks)
            excel.Quit()
            

            # print("AllOK")
            # print("no eror 5")
                       
                        
        # return(wb,excel,noError)





