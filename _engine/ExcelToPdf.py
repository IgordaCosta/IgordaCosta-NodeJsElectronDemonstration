
from win32com import client
# import win32api
# import pathlib



### pip install pypiwin32 if module not found
def ExcelToPdf(excelFileName,pdfFileName,excelFolderSavePath,pdfFolderSavePath):

    try:
        xl = client.gencache.EnsureDispatch('Excel.Application')
    except AttributeError:
        # Corner case dependencies.
        import os
        import re
        import sys
        import shutil
        # Remove cache and try again.
        MODULE_LIST = [m.__name__ for m in sys.modules.values()]
        for module in MODULE_LIST:
            if re.match(r'win32com\.gen_py\..+', module):
                del sys.modules[module]
        shutil.rmtree(os.path.join(os.environ.get('LOCALAPPDATA'), 'Temp', 'gen_py'))
        # from win32com import client
        # xl = client.gencache.EnsureDispatch('Excel.Application')

  
    excel_file = excelFileName
    pdf_file = pdfFileName
    excel_path = (excelFolderSavePath + excel_file)
    pdf_path = (pdfFolderSavePath+ pdf_file)
    excel = client.dynamic.Dispatch("Excel.Application")
    excel.Visible = 0

    # print(excel_path)

    wb = excel.Workbooks.Open(excel_path)


    # ws = wb.Worksheets[0]
    try:
        wb.SaveAs(pdf_path, FileFormat=57)
    except Exception as e:
        # print("Failed to convert")
        # print(str(e))
        pass
    finally:
        wb.Close()
        excel.Quit()
        # print("DONE single Excel to Pdf")

    return pdf_path


# excelFileName='testFile.xlsx'

# pdfFileName='testFile.pdf'






# ExcelToPdf(excelFileName=excelFileName,pdfFileName=pdfFileName,excelFolderSavePath=excelFolderSavePath,pdfFolderSavePath=pdfFolderSavePath)