import os




def ChangeFileExtension(fileName, NewFileExtension):

    # print(fileName)

    pre, ext = os.path.splitext(fileName)
    # print (pre)
    try:
        os.rename(fileName, pre + NewFileExtension)
        # print('Done')
    except:
        pass


# oldfExt= '.txt'

# NewFileExtension = '.txli '





# ChangeFileExtension(fileName, NewFileExtension)