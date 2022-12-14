import pypdfium2 as pdfium
from multiprocessing.pool import ThreadPool





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

    PdfImgLoop(renderer, OutputFilename, FolderSaveLocation, n_pages)
    # filenames = []
    # # for i, image in zip(page_indices, renderer):
    # i = 0
    # for image in renderer:
    #     print(image)
    #     i = i + 1
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



def PdfImgloopFunction(renderer, OutputFilename, FolderSaveLocation):
    filenames = []
    # for i, image in zip(page_indices, renderer):
    i = 0
    for image in renderer:
        print(image)
        i = i + 1

        newFileName=OutputFilename+"_"+str(i)+'.jpg'
        
        pagefilename=FolderSaveLocation + newFileName

        print(filenames)
        
        image.save(pagefilename)

        filenames.append(newFileName)

    
    return filenames



def task(renderer, OutputFilename, FolderSaveLocation, n_pages):

    item = 0
    filenames = []
    ImageList = []
    pagefilenameList = []
    for image in renderer:
        item = item + 1
        # print(item)
        # print('item')
        # print(image)
        # print('image')
        

        # print(image)
        newFileName=OutputFilename+"_"+str(item)+'.jpg'
            
        pagefilename=FolderSaveLocation + newFileName

        # print(pagefilename)
    
        # image.save(pagefilename)

        pagefilenameList.append(pagefilename)

        ImageList.append(image)

    # print(ImageList)
    # print(pagefilenameList)

    return ImageList, pagefilenameList


def PdfImgLoop(renderer, OutputFilename, FolderSaveLocation, n_pages):

    # create and configure the thread pool
    with ThreadPool() as pool:
        # issue tasks to the thread pool
        # item = -1
        filenames = []
        # for _ in range(n_pages):
        #     item = item + 1
        #     # print(list(renderer)[0])
        ImageList, pagefilenameList = pool.apply_async(task,args=(renderer, OutputFilename, FolderSaveLocation, n_pages)).get()
        # filenames.append(newFileName)

        # print(ImageList)
        # print(pagefilenameList)


        # close the thread pool
        pool.close()
        # wait for all tasks to complete
        pool.join()

        # print(filenames)
    print('DONE')
    print(ImageList)
    print(pagefilenameList)

    # p1 = Process(target = PdfImgloopFunction, kwargs={
        
    #     "renderer":renderer,
    #     "OutputFilename":OutputFilename,
    #     "FolderSaveLocation":FolderSaveLocation

        
        
    #     })
    
    # p1.start()
   
    # p1.join()
   


FolderLocation = r'C:\Users\Tigereye\Desktop\New folder\New folder' + '\\'

PdfFileName = 'PASSOS PARA ATIVAÇÃO DO SEU OFFICE 2019 (2) (2) (1) (4) (1) (1) (1) (1) (4) (1) (1)_aRy4vDN.pdf'


# PdfFileName = 'Document 9.pdf'

pdfToJpg(FolderLocation,PdfFileName,FolderSaveLocation='',OutputFilename='')