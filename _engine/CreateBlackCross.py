from PIL import Image, ImageDraw
import pathlib




imageH=980
ImageW=758

#Location="C:\\Users\\IgorDC\\Desktop\\"

homedir = pathlib.Path.home()

Location = str(homedir) + '\\Desktop\\'

ImageName="BlackCross.jpg"


def CreateBlackCross(ImageW,imageH,Location,ImageName):
    im = Image.new('RGB', (ImageW, imageH), (255, 255, 255))
    draw = ImageDraw.Draw(im)


    draw.rectangle(((ImageW/2)-20, imageH,(ImageW/2)+20 , 0), fill=(0, 0, 0), outline=None)

    draw.rectangle((0, (imageH/2)+20,ImageW , (imageH/2)-20), fill=(0, 0, 0), outline=None)

    im.save(Location+ImageName, quality=100)

    print("image Created")


CreateBlackCross(ImageW,imageH,Location,ImageName)