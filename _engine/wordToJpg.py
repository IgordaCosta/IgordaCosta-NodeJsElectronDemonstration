import os

import pdfToJpg
import wordToPdf





def wordToJpg(WordFileName,FolderLocation,OutputFilename):

    
    remove=WordFileName.split(".")[-1]
    PdfFileName=WordFileName.strip("."+remove)

    PdfFileName=PdfFileName+".pdf"

    print(PdfFileName)

    UnecessaryPdfFile=wordToPdf.wordToPdf(WordFileName=WordFileName,PdfFileName=PdfFileName,FolderLocation=FolderLocation)


    pdfToJpg.pdfToJpg(FolderLocation=FolderLocation,PdfFileName=PdfFileName,OutputFilename=OutputFilename)

    os.remove(UnecessaryPdfFile)

    print("All Done")



# WordFileName="Wedding-Photography-Contract.docx"

# FolderLocation='C:\\Users\\IgorDC\\Desktop\\'

# OutputFilename='WordTojpgFile.jpg'

# wordToJpg(WordFileName=WordFileName,FolderLocation=FolderLocation,OutputFilename=OutputFilename)