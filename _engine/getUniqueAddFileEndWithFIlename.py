import getUniqueAddFileEnd


def getUniqueAddFileEndWithFIlename(filename):

    filenameOnly= '.'.join(filename.split('.')[:-1])

    extension = '.' + filename.split('.')[-1]

    uniqueName = getUniqueAddFileEnd.getUniqueAddFileEnd()

    WholeNewFilename = filenameOnly + '_' +  uniqueName + extension

    return WholeNewFilename




# filename = r'C:\Users\Tigereye\Desktop\images' + '\\' + 'imageName.jpg'


# print(getUniqueAddFileEndWithFIlename(filename))
