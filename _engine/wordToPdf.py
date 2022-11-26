from docx2pdf import convert





def wordToPdf(WordFileName,PdfFileName,FolderLocation):

    folder=FolderLocation

    inputFileNameFinal=folder+WordFileName
    outputFileNameFinal=folder+PdfFileName

    convert(inputFileNameFinal, outputFileNameFinal)

    # print("done conversion")

    return outputFileNameFinal




# FolderLocation="C:\\Users\\IgorDC\\Downloads\\"

# WordFileName="Wedding-Photography-Contract.docx"
# PdfFileName="WeddingContract.pdf"



# wordToPdf(WordFileName,PdfFileName,FolderLocation)




    