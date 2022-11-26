import os

import ExcelToPdf

def MultipleExcelToMultiplePdfs(Folderlocation,desiredFileType):

    Excelmerge =[]
    for filename in os.listdir(Folderlocation):
        if filename.endswith(".xlsx"):
            if (filename.split("_")[0]==desiredFileType):
                Excelmerge.append(filename)

    print(Excelmerge)

    Excelmerge.sort()

    print(Excelmerge)


    for filename in Excelmerge:
        excelFolderSavePath=Folderlocation
        pdfFolderSavePath=Folderlocation

        filename=filename.split(".")[0]

        pdfFileName= filename +'.pdf'
        excelFileName= filename +'.xlsx'
        
        ExcelToPdf.ExcelToPdf(excelFileName,pdfFileName,excelFolderSavePath,pdfFolderSavePath)

    print("Done All Excel to Pdfs")





# desiredFileType="testFile"



# MultipleExcelToMultiplePdfs(Folderlocation=Folderlocation,desiredFileType=desiredFileType)



