from PIL import Image


def jpgToPdf(ImageName,Folderlocation ='', PdfSaveName='', ReturnLocation = False):

    image1 = Image.open(Folderlocation + ImageName)
    im1 = image1.convert('RGB')

    if PdfSaveName == '':

        PdfSaveName = '.'.join(ImageName.split('.')[:-1]) + '.pdf'

    SaveLocation = Folderlocation + PdfSaveName
    
    im1.save(SaveLocation)

    if ReturnLocation:
        
        return SaveLocation




# ImageTypesSupported = ['.jpg' ,'.jpeg' ,'.jpe' ,'.jfif' ,'.bmp' ,'.dib' ,'.gif' ,'.png' ,'.tiff']




# ImageName = 'comprovanteResistencia2.jpg'

# PdfSaveName = 'comprovanteResistencia2.pdf'


# Folderlocation= r'C:\Users\Tigereye\Desktop\images' + '\\'




# ImageName = 'Untitled' + '.' + 'jpg'

# ImageName = 'Untitled' + '.' + 'jpeg'

# ImageName = 'Untitled' + '.' + 'jpe'

# ImageName = 'Untitled' + '.' + 'jfif'

# ImageName = 'Untitled' + '.' + 'bmp'

# ImageName = 'Untitled' + '.' + 'dib'

# ImageName = 'Untitled' + '.' + 'gif'

# ImageName = 'Untitled' + '.' + 'png'

# ImageName = 'Untitled' + '.' + 'tiff'





# PdfSaveName = 'image.pdf'

# jpgToPdf(Folderlocation, ImageName,PdfSaveName)

# print('Done')