import os, PyPDF2
from PIL import Image
from datetime import datetime
import subprocess

import getTableData
import ResizeImagesInBulk







def JoinImagesIntoPdf(Folderlocation):

    Folderlocation0 = Folderlocation

    Folderlocation = Folderlocation0 + '\\'


    now = datetime.now()

    now2 = str(now).replace('.','__').replace(' ','--').replace(":",'-')

    nameOfNewFile = 'ImageMergeOn_' + now2

    ImageNameList0 = []
    PdfNameList = []

    ImageEndingList = ['jpg' ,'jpeg' ,'jpe' ,'jfif' ,'bmp' ,'dib' ,'gif' ,'png' ,'tiff']

    for filename in os.listdir(Folderlocation):
            # if filename.endswith(".pdf"):
        if str(filename).split('.')[-1] in ImageEndingList:

            ImageNameList0.append(filename)
            PdfNameList.append(filename.replace('.','_'))


    # print(ImageNameList0)

    # print('ImageNameList0')

    # print(PdfNameList)

    # print('PdfNameList')


    ImagesNameList = ImageNameList0
    
    
    ImageNameListOutput = ResizeImagesInBulk.ResizeImagesInBulk(Folderlocation = Folderlocation, ImagesNameList = ImagesNameList)

    

    for i in range(len(ImageNameListOutput)):

        image1 = Image.open(Folderlocation + ImageNameListOutput[i])
        im1 = image1.convert('RGB')
        im1.save(Folderlocation + PdfNameList[i] + '.pdf')
            
        
  
    pdfWriter = PyPDF2.PdfFileWriter()

    OpenFiles = []

    for filename in PdfNameList:
        try:
            pdfFileObj = open(Folderlocation+filename + '.pdf',"rb")
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
            
            for pageNumber in range(pdfReader.numPages):
                pageObj = pdfReader.getPage(pageNumber)
                pdfWriter.addPage(pageObj)

            OpenFiles.append(pdfFileObj)
            # print(filename+"was appended")

        except FileNotFoundError:
            pass


    pdfOutput = open(Folderlocation+nameOfNewFile+'.pdf','wb')

    pdfWriter.write(pdfOutput)

    pdfOutput.close()

    for i in range(len(PdfNameList)):
        try:
            OpenFiles[i].close()
            os.remove(Folderlocation+PdfNameList[i] + '.pdf')
        
        except:
            pass
        
    # print("Done Join Pdfs")



    #delete temporary image files
    for i in range(len(ImageNameListOutput)):
        
        os.remove(Folderlocation + ImageNameListOutput[i])



        
    dataList = [nameOfNewFile, Folderlocation]

    dataNameList = ['nameOfNewFile', 'FolderSaveLocation']


    getTableData.MultipleListWriteDataDatabase(dataList=dataList, dataNameList=dataNameList)


    subprocess.Popen(r'explorer /open, ' + Folderlocation)

    



# Folderlocation=r'C:\Users\Tigereye\Desktop\images' + '\\'








DataToGet = 'FolderSaveLocation'   # unblock this when done testting
    
FolderSaveLocation=getTableData.GetDataFromDatabase(DataToGet)      # unblock this when done testing






JoinImagesIntoPdf(Folderlocation=FolderSaveLocation)

