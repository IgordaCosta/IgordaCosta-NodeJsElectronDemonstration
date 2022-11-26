from PIL import Image





def CheckIfPixelColorIsBlack(Location,imageName):

    im = Image.open(Location+imageName) # Can be many different formats.
    pix = im.load()
    print(im.size)

    (x,y)=im.size


    print('x',x)

    print('y',y)

    halfY=int(y/2)

    print('halfY',halfY)

    print(pix[0,halfY])



    (a, b, c)=pix[0,halfY]



    print(a)

    print(b)

    print(c)

    

    if a<100 and b<100 and c<100:
        print("this pushes to black")
        IfBlack=True



    else:
        print("this pushes to white")
        IfBlack=False

    return IfBlack





# imageName='blackTest.png'

# Location="C:\\Users\\IgorDC\\Desktop\\"


# IfBlack=CheckIfPixelColorIsBlack(Location,imageName)

#   # Get the width and hight of the image for iterating over

# print("IfBlack= ",IfBlack)



# # print(pix[x,y])  # Get the RGBA Value of the a pixel of an image
# # pix[x,y] = value  # Set the RGBA Value of the image (tuple)
# # im.save('alive_parrot.png')