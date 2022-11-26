




def StringToOrdList(stringUsed):

    stringUsed1 = str(stringUsed)

    stringUsedList = []
    for i in stringUsed1:
        # print(ord(i))
        stringUsedList.append(ord(i))
        

    return stringUsedList









def OrdListToStringChr(OrdLisUsed):


    if type(OrdLisUsed) == type([]):
        pass

    else:
        OrdLisUsedstr = OrdLisUsed
        OrdLisUsed = str(OrdLisUsedstr).replace('[','').replace(']','').replace(', ','*&&%#@').replace(',','*&&%#@').split('*&&%#@')


    stringChr = ''
    for i in OrdLisUsed:
        # print(ord(i))
        if i =='':
            pass
        elif i == ' ':
            pass
        else: 
            try:
                ChrItem = chr(int(i))
            except:
                ChrItem = i
                
            stringChr= stringChr + ChrItem

    return stringChr






# OrdLisUsed = [231, 231, 231, 84, 101, 115, 116]


# stringUsed = 'çççTest'


# print(StringToOrdList(stringUsed))

# print(OrdListToStringChr(OrdLisUsed))