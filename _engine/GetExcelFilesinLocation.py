import glob
import os

from importedDataPyinternalLocation import *



def GetExcelFilesinLocation(location, IncludeFolder=False):
        home = os.path.expanduser('~') 
        
        SelectedFolder = os.path.join(home, internalLocation,location)
        
        # print(SelectedFolder)
        
        # print("files in folder with ~$")
        
        if IncludeFolder==False:
            filesInFolder = [f.split("\\")[-1] for f in glob.glob(SelectedFolder + "/[!~$]*.xl*", recursive=True)]
            
            # print(filesInFolder)
            # print("files in folder withOUT ~$")
        if IncludeFolder==True:
            filesInFolder=glob.glob(SelectedFolder+"\\*.xl*")
        
        return filesInFolder