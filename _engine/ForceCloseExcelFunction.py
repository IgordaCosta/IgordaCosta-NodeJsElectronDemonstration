import os

def ForceCloseExcel():

    try:
        os.system('TASKKILL /F /IM EXCEL.EXE')

    except Exception:
        # print("Excel not found")
        pass