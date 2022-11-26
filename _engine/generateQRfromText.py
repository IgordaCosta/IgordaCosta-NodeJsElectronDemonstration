import qrcode
# from PIL import Image

# import getTableData


def generateQRfromText(TextToAdd, checkContinueValue, SaveLocation):


    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )


    # checkContinueValue= 'laksdf1456'        # this data is the check code for the next option

    # TextToAdd = 'Test1023'

    AllTextToAdd = str(checkContinueValue) +'_' + str(TextToAdd).replace("'", "").replace('"','')

    
    # print(AllTextToAdd)

    # print('AllTextToAdd above')


    # AllTextToAdd = 'ghkfasdygdi345363_[[bbbaaa1.jpg, aaa1], [bbbnnn1.jpg, nnn1], [bbbmmm1.jpg, mmm1], [bbblll1.jpg, lll1], [bbbrrr1.jpg, rrr1]], [[SaveName, topright]]'    #block after testing   ##### this worked

    AllTextToAdd = 'ghkfasdygdi345363_[[bbbaaa1.jpg, aaa1]], [[SaveName, topright]]'    #block after testing
    
    
    qr.add_data(str(AllTextToAdd))
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    

    img.save(SaveLocation)


    return 'Done'









# TextToAdd = 'this is a third text done now'
# checkContinueValue = 'laksdf1456'



# print(generateQRfromText(TextToAdd, checkContinueValue, SaveLocation))
