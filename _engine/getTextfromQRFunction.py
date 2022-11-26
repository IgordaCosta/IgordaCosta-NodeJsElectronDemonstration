import cv2 as cv



def getTextfromQR(SaveLocation,checkContinueValue):
    

    # checkContinueValue= 'laksdf1456'  

    

    print(SaveLocation)
    print('SaveLocation inside function')
    
    im = cv.imread(SaveLocation)


    det = cv.QRCodeDetector()
    
    NoError = False
    
    errorCode = ''

    try:
        retval, points, straight_qrcode = det.detectAndDecode(im)

        NoError = True
    except Exception as e:
        print('=============================================')
        # print('_________' + str(e) + '__________')
        print('=============================================')

        errorCode = str(e).strip() 

        print('_________' + errorCode + '_________')

        print('=============================================')


    if NoError:
        print(retval)
        print('retval above')


        # print(retval.split('_')[0])

        checkvalue = retval.split('_')[0]

        Passed = 'NotPassed'

        print(checkvalue)
        print('checkvalue above')

        if checkvalue == checkContinueValue:
            Passed = 'CheckPassed'
            TextResult = retval.split('_')[1]

        else:
            TextResult = ''


        # print(TextResult)

        return [TextResult, Passed]

    else:

        TextResult = ''
        
        if str(errorCode) == r"OpenCV(4.5.4) D:\a\opencv-python\opencv-python\opencv\modules\objdetect\src\qrcode.cpp:29: error: (-215:Assertion failed) !img.empty() in function 'cv::checkQRInputImage'":
        
            Passed = 'fileNotQR'

        else:
            Passed = 'OtherError'


        return [TextResult, Passed]




# checkContinueValue= 'laksdf1456'               




# print(getTextfromQR(SaveLocation,checkContinueValue))

