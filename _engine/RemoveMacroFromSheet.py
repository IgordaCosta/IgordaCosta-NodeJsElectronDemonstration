import win32com.client



def RemoveMacroFromSheet(Filename='',Location='',excelApp='',excelWorkbook='',IfAlreadyOpen=True,closeExcel=False):
    # OPEN EXCEL APP AND WORKBOOK
    if IfAlreadyOpen:
        xlApp=excelApp
        xlwb=excelWorkbook
    else:
        xlApp = win32com.client.Dispatch("Excel.Application")
        xlwb = xlApp.Workbooks.Open(Location+Filename)

    # ITERATE THROUGH EACH VB COMPONENT (CLASS MODULE, STANDARD MODULE, USER FORMS)
    try:    
        for i in xlwb.VBProject.VBComponents:        
            xlmodule = xlwb.VBProject.VBComponents(i.Name)
            if xlmodule.Type in [1, 2, 3]:            
                xlwb.VBProject.VBComponents.Remove(xlmodule)

    except Exception as e:
        print(e)

    if closeExcel:   
        # CLOSE AND SAVE AND UNINITIALIZE APP
        xlwb.Close(True)
        xlApp.Quit

        xlApp = None