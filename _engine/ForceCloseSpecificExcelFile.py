import os

def ForceCloseSpecificExcelFile(fileName, Program="Excel"):

    try:
        os.system('cmd /c "taskkill /F /FI "WindowTitle eq '+fileName+' - '+Program+'" /T"')

    except Exception:
        print("Excel file "+fileName+" was not found")




# fileName="orange2.xlsx"

# ForceCloseSpecificExcelFile(fileName=fileName)