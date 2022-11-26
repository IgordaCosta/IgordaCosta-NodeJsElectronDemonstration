import time
import string
import random

def myfunction():
  return glRand






def base93Characterconversion(TimeBased=True, OtherNumer='',OnlyUpper=False):

    # print(OtherNumer)

    if OnlyUpper == False:
        choices = str(string.ascii_letters)+str(string.digits)
    else:
        choices = str(string.ascii_uppercase)

    NumberOfChoice = len(choices)

    if TimeBased:
        number = int(time.time()*1000)
    else:
        try:
            # print('ok int before')
            x = int(int(OtherNumer)/NumberOfChoice)
            # int(OtherNumer/2)
            # print('ok int')
            
        except:
            OtherNumer = ''

        if OtherNumer == '':
            number = int(time.time()*1000)
        
        else:
            number = int(OtherNumer)


    ListOfConversion = []
    while True:
        
        remainder = int(number%NumberOfChoice)

        number = int(number/NumberOfChoice)
        ListOfConversion.append(choices[remainder])
            
        if int(number) == 0:
            break

    FinalString0 = str(ListOfConversion).replace('[','').replace(']','').replace("'",'').replace(' ','').replace(",",'')

    if OnlyUpper:
        FinalString = FinalString0[::-1]

    else:
        FinalString = FinalString0

    
    global glRand
    glRandLen = int(len(str(number)))
    if glRandLen>3:
        glRand = int(str(list(number[-3])))/10
    else:
        glRand = 0.7


    strVar = list(FinalString)
    random.shuffle(strVar,myfunction)
    FinalString2 =''.join(strVar)
    return FinalString2






# print(str(string.ascii_uppercase)+str(string.digits))

# print(len((str(string.ascii_uppercase)+str(string.digits))))