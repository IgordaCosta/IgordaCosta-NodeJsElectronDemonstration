import StringToOrdList




def encodeBase64Db(stringToEncode):
    
    encodedString = StringToOrdList. StringToOrdList(stringToEncode)

    # stringToEncodeByte = bytes(stringToEncode, 'utf-8')

    # # print(stringToEncodeByte)

    # encoded = base64.b64encode(stringToEncodeByte)

    # encodedString = str(encoded).replace("b'", '').replace("'", '')

    # print(encoded)

    # print(encodedString)

    return encodedString




    

def decodeBase64Db(stringToDecode):

    OrdLisUsed = str(stringToDecode).replace('[','').replace(']','').replace(', ','*&&%#@').replace(',','*&&%#@').split('*&&%#@')

    Decodeddata = StringToOrdList.OrdListToStringChr(OrdLisUsed)



    # stringToDecodeByte = bytes(stringToDecode, 'utf-8')

    # # print(stringToDecodeByte)
    
    # data = base64.b64decode(stringToDecodeByte)

    # Decodeddata = data.decode('utf-8')

    return Decodeddata

    



# stringToEncode = 'coração de Título ìndio'

# stringToDecode = encodeBase64Db(stringToEncode)


# print(stringToDecode)


# stringToDecode = [99, 111, 114, 97, 231, 227, 111, 32, 100, 101, 32, 84, 237, 116, 117, 108, 111, 32, 236, 110, 100, 105, 111]


# print(decodeBase64Db(stringToDecode))