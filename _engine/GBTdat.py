import yfinance

import json

import base93Characterconversion




def WriteFl(fileName):
    data = yfinance.download(tickers='BTC-USD', period = '1d', interval = '5m',progress=False)

    OtherNumer0 = ''
    for i in range(len(data)):
        OtherNumer0 = OtherNumer0 + str(list(data.iloc[i][:-1])).replace('[','').replace(']','').replace(' ','').replace('.','').replace(',', '')
        

    # OtherNumer =str(dataString[57:159])

    print(OtherNumer0)

    # print(len(OtherNumer0))

    TimeBased = False

    # for itenRange in OtherNumer0:

    #     dataString = base93Characterconversion.base93Characterconversion(TimeBased=TimeBased, OtherNumer=OtherNumer)

    # print(dataString)

    # print(len(dataString))

# def WriteFl(fileName):

#     data = yfinance.download(tickers='BTC-USD', period = '2h', interval = '90m',progress=False)

#     dataString = ''
#     for i in range(len(data)):
#         dataString = dataString + str(list(data.iloc[i][:-1])).replace('[','').replace(']','').replace(' ','').replace('.','').replace(',', '')
        

#     print(len(dataString))

    # file1 = open(fileName,"w")

    # file1.write(dataString)

    # file1.close() 






 
    # Data to be written
    
    

def GetFlInf(fileName):

    file1 = open(fileName,"r+") 
  
    dataString = file1.read()

    dataString = ''
    with open(fileName) as FileObj:
        pass
       
        for lines in FileObj:
            # print(lines)
            dataString = ''.join(lines)
    
    print(dataString)

    print(len(dataString))

    checkLocation = dataString[15:37]

    print(checkLocation)

    A = dataString[215]

    B = int(A) + 3

    print(A)

    print(B)

    OtherNumer = dataString[int(checkLocation):int(checkLocation) + 58]

    TimeBased = False

    # OtherNumer = SnGten

    TableDataValueSS2 = base93Characterconversion.base93Characterconversion(TimeBased=TimeBased, OtherNumer=OtherNumer)

    checkLocation = dataString[5897:5901]

    SnGten = dataString[int(checkLocation):int(checkLocation) + 25]

    TimeBased = False

    OtherNumer = SnGten

    TableDataValueSS3 = str(base93Characterconversion.base93Characterconversion(TimeBased=TimeBased, OtherNumer=OtherNumer)) + '.db'


    return TableDataValueSS3, TableDataValueSS2

        


import os


fileName = os.getcwd() + '\\' + "adfasdgaf.rvx"


WriteFl(fileName)

# print(GetFlInf(fileName))