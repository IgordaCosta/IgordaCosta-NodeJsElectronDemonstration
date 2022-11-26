# import os, PyPDF2
from datetime import datetime
import subprocess

import JoinPdfs
import getTableData


now = datetime.now()

# print("now =", now)


now2 = str(now).replace('.','__').replace(' ','--').replace(":",'-')

# print(now2)


nameOfNewFile = 'MergeOn_' + now2

# print(nameOfNewFile)



dataName = 'FolderSaveLocation'

FolderSaveLocation = getTableData.GetDataFromDatabase(dataName = dataName)



JoinPdfs.JoinPdfs(Folderlocation=FolderSaveLocation,nameOfNewFile=nameOfNewFile,desiredFileType='')

data2 = nameOfNewFile

dataName2 = 'nameOfNewFile'

getTableData.WriteDataDatabase(data=data2, dataName=dataName2)



subprocess.Popen(r'explorer /open, ' + FolderSaveLocation)












# # def JoinPdfs(Folderlocation,nameOfNewFile,desiredFileType):

# #     pdf2merge =[]
# #     for filename in os.listdir(Folderlocation):
# #         if filename.endswith(".pdf"):
# #             if (filename.split("_")[0]==desiredFileType):
# #                 pdf2merge.append(filename)

# #     print(pdf2merge)

# #     pdf2merge.sort()

# #     print(pdf2merge)

# #     pdfWriter = PyPDF2.PdfFileWriter()

# #     for filename in pdf2merge:

# #         pdfFileObj = open(Folderlocation+filename,"rb")
# #         pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        
# #         for pageNumber in range(pdfReader.numPages):
# #             pageObj = pdfReader.getPage(pageNumber)
# #             pdfWriter.addPage(pageObj)
            
        
# #         print(filename+"was appended")

                
# #     pdfOutput = open(Folderlocation+nameOfNewFile+'.pdf','wb')

# #     pdfWriter.write(pdfOutput)

# #     pdfOutput.close()

# #     print("Done Join Pdfs")








# # # nameOfNewFile="NewFileJoined"
# # # desiredFileType="testFile"



# # # JoinPdfs(Folderlocation=Folderlocation,nameOfNewFile=nameOfNewFile,desiredFileType=desiredFileType)



