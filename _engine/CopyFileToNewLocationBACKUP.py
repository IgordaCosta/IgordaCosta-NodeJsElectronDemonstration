import shutil
import os
# import time

# import base93Characterconversion

def CopyFileToNewLocation(getFileLocation, CopyToLocaion, TimeNameFull):


    # BaseFileLocation2 = r'C:\\Users\Tigereye\Documents\AutoFormFillerFiles\adosMultaFacesIsabela.jpg'
    # BaseFileLocation = r'C:\\Users\Tigereye\Documents\AutoFormFillerFiles\adosMultaFacesIsabela__57fd1a2863b28d_temp.jpg'



    BaseFileLocation2 =getFileLocation
    BaseFileLocation = CopyToLocaion


    
    # print(BaseFileLocation)

    # print('BaseFileLocation')

    
    # print(BaseFileLocation2)

    # print('BaseFileLocation2')



    currentDirectory = BaseFileLocation.split(':')[0]+ ':/'

    # print(currentDirectory)

    # print('currentDirectory')

    os.chdir(currentDirectory)


    # LocationPath11 = BaseFileLocation.replace('/','\\').split('\\')



    # LocationPath1 = '\\'.join(LocationPath11[:-1]) + '\\'

    # FileName1 = LocationPath11[-1]



    

    # LocationPath22 = BaseFileLocation2.replace('/','\\').split('\\')

    

    # LocationPath2 = '\\'.join(LocationPath22[:-1]) + '\\'

    # FileName2 = LocationPath2[-1]



    # BaseFileLocation2 =getFileLocation.replace("\\",'\\\\')
    # BaseFileLocation = CopyToLocaion.replace("\\",'\\\\')



    # print(getFileLocation)

    # print('getFileLocation')

    # print(CopyToLocaion)

    # print('CopyToLocaion')

    # print( r'C:\\Users\Tigereye\Documents\AutoFormFillerFiles\adosMultaFacesIsabela.jpg' == getFileLocation)

    # print( r'C:\\Users\Tigereye\Documents\AutoFormFillerFiles\adosMultaFacesIsabela.jpg == getFileLocation')

    # print(r'C:\\Users\Tigereye\Documents\AutoFormFillerFiles\adosMultaFacesIsabela.jpg')
    # print('should be getFileLocation')

    # print(r'C:\\Users\Tigereye\Documents\AutoFormFillerFiles\adosMultaFacesIsabela__57fd1a2863b28d_temp.jpg')
    # print('should be CopyToLocaion')

    # noError=False
    # try:
    #     # shutil.copy(BaseFileLocation2, BaseFileLocation)
    #     shutil.copyfile(BaseFileLocation2, BaseFileLocation)
    #     noError = True
    # except:
    #     pass

    # os.chdir(path=LocationPath1)

    # TempBaseFileLocation = str('/'.join(BaseFileLocation.split('/')[:-1])) + '/'+ str(BaseFileLocation.split('__')[-1])

    # print(TempBaseFileLocation)

    # TimeName = str(int(time.time()*1000))

    # TimeName = base93Characterconversion.base93Characterconversion()

    # BaseLocationUsed = str('\\'.join(BaseFileLocation.split('\\')[:-1]))

    # print(BaseLocationUsed)

    # print('BaseLocationUsed')

    # ExtensionUsed = str(BaseFileLocation.split('.')[-1])

    # NameFile = str(str(BaseFileLocation.split('\\')[-1]).split('_')[0])

    # print(ExtensionUsed)

    # print('ExtensionUsed')

    # print('TempBaseFileLocation')
    # TimeNameFull =BaseLocationUsed + '\\' + NameFile  + '_' +  str(TimeName)+ '_temp' + '.'+ ExtensionUsed
    

    # print(TimeNameFull)

    # print('TimeNameFull')
    noError= False
    # RetunValue= shutil.copy(BaseFileLocation2, TempBaseFileLocation)

    NOTCopy = True
    while NOTCopy:
    
        RetunValue= shutil.copy(BaseFileLocation2, TimeNameFull)

        print('fileNotCopied')

        # # os.system("'"+'cmd /k ' + '"'+ 'copy '+ BaseFileLocation2 + ' '+ BaseFileLocation +'"'+"'" )

        # os.system('cmd /c "copy {} {}"'.format(BaseFileLocation2, BaseFileLocation))

        # os.system('cmd /c "copy {} {}"'.format(BaseFileLocation2, r'C:\Users\Tigereye\Documents\AutoFormFillerFiles\aadfasdfasdf'))
        # #  "Shepherd {} is {} years old.".format(shepherd, age)
        # time.sleep(5)

        if os.path.exists(str(TimeNameFull)):
            print(TimeNameFull)
            NOTCopy =False
            print('file just copied')
            noError = True

       

    # os.rename(TempBaseFileLocation, BaseFileLocation)

    # RetunValue= shutil.copyfile(BaseFileLocation2, FileName1)


    # FileName1
    # # os.
    
    # print('RetunValue')

    # print(RetunValue)
    
    # if RetunValue =="":
    #     pass
    # else:
    #     noError = True

    return noError, RetunValue

# BaseFileLocation2 = r'C:\\Users\Tigereye\Documents\AutoFormFillerFiles\adosMultaFacesIsabela.jpg'
# BaseFileLocation = r'C:\\Users\Tigereye\Documents\AutoFormFillerFiles\adosMultaFacesIsabela__57fd1a2863b28d_temp.jpg'


# getFileLocation = BaseFileLocation2
# CopyToLocaion = BaseFileLocation

# print(CopyFileToNewLocation(getFileLocation, CopyToLocaion))