



def SingleSeriesValueToString(SeriesValueToBeString):


    SeriesValueToBeString.reset_index(drop=True, inplace=True)


    resultStringValue=SeriesValueToBeString.get(key=0)

    return resultStringValue