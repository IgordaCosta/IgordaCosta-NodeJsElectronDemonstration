import base93Characterconversion



def CreateTempSaveLoationName(BaseFileLocation):
    
    BaseLocationUsed = str('\\'.join(BaseFileLocation.split('\\')[:-1]))

    NameFile = str(str(BaseFileLocation.split('\\')[-1]).split('_')[0])

    TimeName = base93Characterconversion.base93Characterconversion()

    ExtensionUsed = str(BaseFileLocation.split('.')[-1])


    TimeNameFull =BaseLocationUsed + '\\' + NameFile  + '_' +  str(TimeName)+ '_temp' + '.'+ ExtensionUsed

    # TimeNameFull =BaseLocationUsed + '\\' + str(TimeName)+ '.'+ ExtensionUsed

    print(TimeNameFull)


    print('TimeNameFull')



    return TimeNameFull