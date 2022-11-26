import os







def cleanUpFolderFiles(Folderlocation,nameOfNewFile,desiredFileType):
    print("Started File Cleanup")
    pdf2merge =[]
    for filename in os.listdir(Folderlocation):
        if filename.endswith(".pdf"):
            if (filename.split("_")[0]==desiredFileType):
                pdf2merge.append(filename)

    print(pdf2merge)

    pdf2merge.sort()

    print(pdf2merge)

    
    for filename in pdf2merge:
        
        os.remove(Folderlocation+filename)
    
    print("Finished File Cleanup")







# nameOfNewFile="NewFileJoined"
# desiredFileType="testFile"




# cleanUpFolderFiles(Folderlocation=Folderlocation,nameOfNewFile=nameOfNewFile,desiredFileType=desiredFileType)