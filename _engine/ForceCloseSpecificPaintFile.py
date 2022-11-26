import os

def ForceCloseSpecificPaintFile(fileName, Program="Paint"):

    try:
        os.system('cmd /c "taskkill /F /FI "WindowTitle eq '+fileName+' - '+Program+'" /T"')

    except Exception:
        print("Paint file "+fileName+" was not found")




# fileName="ExcelBlackCrossPaintCheck.jpg"

# ForceCloseSpecificPaintFile(fileName)