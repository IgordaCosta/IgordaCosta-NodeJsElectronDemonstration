import RegularExpressionTextOrList


# KeyFilename = 'KEY_"tg;&%--lp'



def GetKeyfileNameType(KeyFilename):

    KeyFileChek = KeyFilename[:4]

    KeyFileChange = KeyFilename[4:]

    txt = KeyFileChange

    if KeyFileChek == 'KEY_':
        OutputKey0 = RegularExpressionTextOrList.RegularExpressionTextOrList(txt=txt)
        
        OutputKey = KeyFileChek + OutputKey0
        return OutputKey

    else:
        return ''



    
# print(GetKeyfileNameType(KeyFilename))