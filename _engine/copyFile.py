import os
import shutil
from os import path

def copyFile(Location,filename):
    
    src=Location + filename
	
    remove=filename.split(".")[-1]
    filenamestrip=filename.strip("."+remove)

    filename0=filenamestrip + "Backup"

    filename2=filename0+ "." + remove
    
    dst=Location+filename2

    print(dst)
    print('dst')

    print(src)
    print('src')

    shutil.copy(src, dst)
	
	
    shutil.copystat(src,dst)

    print("Done")

    return filename0




# filename="testPicTOExcelNeedsImprovement.xlsx"

# Location="C:\\Users\\IgorDC\\Desktop\\"



# dst=copyFile(Location=Location,filename=filename)

# print(dst)