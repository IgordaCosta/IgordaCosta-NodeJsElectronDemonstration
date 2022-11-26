# import pprint
# import re
import time

# from distutils.util import change_root
import string

# print(b'a'/5)


# 33 - 126
#      93

# print(chr(100))

# ListUsed = []
# for i in range(93):
#     ListUsed.append(chr(i+33))

# pprint.pprint(ListUsed)


def base93Characterconversion(TimeBased=True, OtherNumer=''):

    choices = str(string.ascii_letters)+str(string.digits)

    NumberOfChoice = len(choices)

    if TimeBased:
        number = int(time.time()*1000)
    else:
        try:
            int(OtherNumer/2)
        except:
            OtherNumer = ''

        if OtherNumer == '':
            number = int(time.time()*1000)
        
        else:
            number = OtherNumer

    # number1 = number



    # print(number)

    # print(int(0.3))

    ListOfConversion = []
    while True:
        remainder = int(number%NumberOfChoice)

        number = int(number/NumberOfChoice)
        ListOfConversion.append(choices[remainder])
        
        if int(number) == 0:
            break

    FinalString = str(ListOfConversion).replace('[','').replace(']','').replace("'",'').replace(' ','').replace(",",'')

    return FinalString
    # print(FinalString)

    # print(len(FinalString))

    # print(len(str(number1)))


# print(base93Characterconversion(TimeBased=True, OtherNumer=''))