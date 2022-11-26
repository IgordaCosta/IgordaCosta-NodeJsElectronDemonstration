import pathlib
    

def FilePathFromPython():

    PyPath = pathlib.Path(__file__).parent.resolve()
    CurrentWorkingPath = '\\'.join(str(PyPath).split('\\')[:-1])


    return CurrentWorkingPath

    


