import CopyFileToNewLocation
import ContinueToRest




def CopyFileAnContinue(BaseFileLocation2,BaseFileLocation,dataframe,OutputDictionary,RealListOfColumnnames,  ListToPrint, LocationAsked, FontName, FontSize, dataframe0, datafillName, OutputTableName3Keys, noError, rw, TimeNameFull):
         

    noError = False

    while noError == False:
        if noError == True:
            # print(type(noError))
            pass
        else:
            noError, RetunValue = CopyFileToNewLocation.CopyFileToNewLocation(getFileLocation=BaseFileLocation2, CopyToLocaion=BaseFileLocation, TimeNameFull=TimeNameFull)
        print(noError)
    if noError == True :
            ContinueToRest.ContinueToRest (BaseFileLocation2,BaseFileLocation,dataframe,OutputDictionary,RealListOfColumnnames, ListToPrint, LocationAsked, FontName, FontSize, dataframe0, datafillName, OutputTableName3Keys, noError, rw, TimeNameFull)
