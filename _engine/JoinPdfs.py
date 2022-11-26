import os, PyPDF2










def JoinPdfs(Folderlocation,nameOfNewFile,desiredFileType):

    pdf2merge =[]

    # FileList = os.listdir(Folderlocation)
    # print(FileList)

    Folderlocation0 = Folderlocation

    Folderlocation = Folderlocation0 + '\\'

    for filename in os.listdir(Folderlocation):
        if filename.endswith(".pdf"):
            if desiredFileType == '':
                if filename.split('_')[0] == 'MergeOn':
                    pass
                else:
                    pdf2merge.append(filename)
            elif (filename.split("_")[0]==desiredFileType):
                pdf2merge.append(filename)
            else:
                pass

    # print(pdf2merge)

    pdf2merge.sort()

    # print(pdf2merge)

    pdfWriter = PyPDF2.PdfFileWriter()

    for filename in pdf2merge:

        pdfFileObj = open(Folderlocation+filename,"rb")
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        
        for pageNumber in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNumber)
            pdfWriter.addPage(pageObj)
            
        
        # print(filename+"was appended")

                
    pdfOutput = open(Folderlocation+nameOfNewFile+'.pdf','wb')

    pdfWriter.write(pdfOutput)

    pdfOutput.close()

    # print("Done Join Pdfs")








# nameOfNewFile="NewFileJoined"
# desiredFileType="testFile"



# JoinPdfs(Folderlocation=Folderlocation,nameOfNewFile=nameOfNewFile,desiredFileType=desiredFileType)



