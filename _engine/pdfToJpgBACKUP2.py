import pypdfium2 as pdfium
from multiprocessing import Process




# print(imgFileName)




# def pdfToJpg2Function(FolderLocation,PdfFileName,FolderSaveLocation='',OutputFilename=''):
#     print('here')
#     if __name__ == '__main__':
#         print('here2')
#         pdfToJpg(FolderLocation,PdfFileName,FolderSaveLocation=FolderSaveLocation,OutputFilename=OutputFilename)

def pdfToJpg(FolderLocation,PdfFileName,FolderSaveLocation='',OutputFilename=''):



    print('ok')

    if OutputFilename=='':

        OutputFilename=PdfFileName

    if FolderSaveLocation=='':
        
        FolderSaveLocation=FolderLocation
    

    if len(OutputFilename.split(".")) >1:

        remove=OutputFilename.split(".")[-1]
        OutputFilename=OutputFilename.strip("."+remove)



    pathToPdfFile = FolderLocation + PdfFileName

    pdf = pdfium.PdfDocument(pathToPdfFile)
    n_pages = len(pdf)  # get the number of pages in the document


    page_indices = [i for i in range(n_pages)]  # all pages
    renderer = pdf.render_to(
        pdfium.BitmapConv.pil_image,
        page_indices = page_indices,
        scale = 200/72,  # 300dpi resolution
    )

    print('ok2')
    # if __name__ == '__main__':
    print('in function')


    makeJpgCall(page_indices,renderer, n_pages, OutputFilename,FolderSaveLocation)

    
    # filenames = []
    # for i, image in zip(page_indices, renderer):
    #     if n_pages >1:
    #         newFileName=OutputFilename+"_"+str(i)+'.jpg'

    #     else:
    #         newFileName=OutputFilename+'.jpg'
        
    #     pagefilename=FolderSaveLocation + newFileName

    #     print(filenames)
        
    #     image.save(pagefilename)

    #     filenames.append(newFileName)

    # if n_pages==1:
    #     print(newFileName)
    #     return newFileName

    # else:
    #     print(filenames)
    #     return filenames




def makeJpgCall(page_indices,renderer, n_pages, OutputFilename,FolderSaveLocation):

    if __name__ == '__main__':

        
        process = Process(target = makeJpg, kwargs={"page_indices":page_indices,
         "renderer":renderer,
         "n_pages":n_pages,
         "OutputFilename":OutputFilename,
         "FolderSaveLocation":FolderSaveLocation


        
        })
        # start the new process
        process.start()
        # wait for the new process to finish
        process.join()

        print('Done')



        
   




def makeJpg(page_indices, renderer, n_pages, OutputFilename, FolderSaveLocation ):
    filenames = []
    for i, image in zip(page_indices, renderer):
        if n_pages >1:
            newFileName=OutputFilename+"_"+str(i)+'.jpg'

        else:
            newFileName=OutputFilename+'.jpg'
        
        pagefilename=FolderSaveLocation + newFileName

        print(filenames)
        
        image.save(pagefilename)

        filenames.append(newFileName)

    # if n_pages==1:
    #     print(newFileName)
    #     return newFileName

    # else:
    #     print(filenames)
    #     return filenames


FolderLocation = r'C:\Users\Tigereye\Desktop\New folder\New folder' + '\\'

PdfFileName = 'PASSOS PARA ATIVA????O DO SEU OFFICE 2019 (2) (2) (1) (4) (1) (1) (1) (1) (4) (1) (1)_aRy4vDN.pdf'


# PdfFileName = 'Document 9.pdf'

pdfToJpg(FolderLocation,PdfFileName,FolderSaveLocation='',OutputFilename='')