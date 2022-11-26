import CopyFileToNewLocation
import ContinueToRest




def CopyFileAnContinue(BaseFileLocation2,BaseFileLocation,dataframe,OutputDictionary,RealListOfColumnnames,  ListToPrint, LocationAsked, FontName, FontSize, dataframe0, datafillName, OutputTableName3Keys, noError, rw, TimeNameFull):
                      
    
    # noError = 'False'
    # noErrorDefault = 'False'
    # while noError == noErrorDefault:
    #     # ok= CopyFileToNewLocation.CopyFileToNewLocation(getFileLocation=BaseFileLocation2, CopyToLocaion=BaseFileLocation)
    #     # noError = str(ok)
    #     if noError == 'True':
    #         # noError = 'True'
    #         print(type(noError))
    #     else:
    #         ok= CopyFileToNewLocation.CopyFileToNewLocation(getFileLocation=BaseFileLocation2, CopyToLocaion=BaseFileLocation)
    #         noError = str(ok)
    #         # print(noError)
    #     print(noError)

    #     print('True' == 'True')

    #     print("'True' == 'True'")
    # if noError == 'True' :
    #         ContinueToRest.ContinueToRest (BaseFileLocation2,BaseFileLocation,dataframe,OutputDictionary,RealListOfColumnnames, ListToPrint, LocationAsked, FontName, FontSize, dataframe0, datafillName, OutputTableName3Keys, noError, rw)


    noError = False
    # noErrorDefault = 'False'
    while noError == False:
        # ok= CopyFileToNewLocation.CopyFileToNewLocation(getFileLocation=BaseFileLocation2, CopyToLocaion=BaseFileLocation)
        # noError = str(ok)
        if noError == True:
            # noError = 'True'
            print(type(noError))
        else:
            noError, RetunValue = CopyFileToNewLocation.CopyFileToNewLocation(getFileLocation=BaseFileLocation2, CopyToLocaion=BaseFileLocation, TimeNameFull=TimeNameFull)
            # noError = ok
            # print(noError)
        print(noError)

        # print('True' == 'True')

        # print("'True' == 'True'")
    if noError == True :
            ContinueToRest.ContinueToRest (BaseFileLocation2,BaseFileLocation,dataframe,OutputDictionary,RealListOfColumnnames, ListToPrint, LocationAsked, FontName, FontSize, dataframe0, datafillName, OutputTableName3Keys, noError, rw, TimeNameFull)
