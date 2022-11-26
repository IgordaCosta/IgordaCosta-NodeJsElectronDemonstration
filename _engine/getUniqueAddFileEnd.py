import time

def getUniqueAddFileEnd():

    timeOut = int(time.time() *10000000)
    returnText0 =  str(hex(timeOut))[2:]

    returnText = returnText0[5:] + returnText0[:5] 

    return returnText


# print(getUniqueAddFileEnd())