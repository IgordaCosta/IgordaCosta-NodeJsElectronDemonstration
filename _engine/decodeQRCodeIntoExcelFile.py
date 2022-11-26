import cv2 as cv
import pathlib




homedir = pathlib.Path.home()

location = str(homedir) + '\\Documents\\AutoFormFillerOutputFiles\\' 

#filename = 'img3-2021-12-30 19-42-16_QR.png'

Wholefilename = location + filename


im = cv.imread(Wholefilename)
det = cv.QRCodeDetector()


retval, points, straight_qrcode = det.detectAndDecode(im)


print(retval)

print('Done')