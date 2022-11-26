from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
import os

from pdf2image import convert_from_path
import PyPDF2
import base93Characterconversion






def pdfToJpg(FolderLocation,PdfFileName,FolderSaveLocation='',OutputFilename=''):

    if OutputFilename=='':

        OutputFilename=PdfFileName

    if FolderSaveLocation=='':
        
        FolderSaveLocation=FolderLocation
    

    if len(OutputFilename.split(".")) >1:

        remove=OutputFilename.split(".")[-1]
        OutputFilename=OutputFilename.strip("."+remove)

   
    PdfFileNameFinal=FolderLocation+PdfFileName

    
    NOError  = True
    try:
        images = convert_from_path(PdfFileNameFinal)
    except Exception as e:
        compareSizes = [int(x) for x in str(e).replace('(','').replace(')','').split(' ') if x.isnumeric()]
        print(compareSizes)
        NOError =False

    if NOError == False:
        percentageToComare = round((compareSizes[1]/compareSizes[0]) * 0.6, 2)

        NumOfPages = PyPDF2.PdfFileReader(PdfFileNameFinal).getNumPages()

        TextTOAdd = base93Characterconversion.base93Characterconversion()

        PdfFileNameFinal2 = '.'.join(PdfFileNameFinal.split('.')[:-1]) + TextTOAdd + '.pdf'


        for i in range(NumOfPages):
            pdf = PyPDF2.PdfFileReader(PdfFileNameFinal)
            page0 = pdf.getPage(i)
            page0.scaleBy(percentageToComare)  # float representing scale factor - this happens in-place
            writer = PyPDF2.PdfFileWriter()  # create a writer to save the updated results
            writer.addPage(page0)
            with open(PdfFileNameFinal2, "wb+") as f:
                writer.write(f)
        
        images = convert_from_path(PdfFileNameFinal2)

    filenames=[]
    i=0
    for page in images:
        i=i+1
        if len(images) >1:
            newFileName=OutputFilename+"_"+str(i)+'.jpg'
        else:
            newFileName=OutputFilename+'.jpg'

        pagefilename=FolderSaveLocation +newFileName

        page.save(pagefilename, 'JPEG')
        
        filenames.append(newFileName)
        
    
    try:
        os.remove(PdfFileNameFinal2)
    except:
        pass

    if i==1:
        return newFileName
    else:
        return filenames



    

    




# FolderLocation= r'C:\Users\Tigereye\Desktop' + '\\'

# PdfFileName="adosMultaFacesIsabela.pdf"

# OutputFilename='adosMultaFacesIsabela'




# pdfToJpg(FolderLocation=FolderLocation,PdfFileName=PdfFileName,OutputFilename=OutputFilename)