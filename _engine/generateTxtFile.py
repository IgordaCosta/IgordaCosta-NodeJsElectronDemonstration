import ChangeFileExtension


def generateTxtFile(TextToWrite,SaveLocation, changeExtension = False):

    

    # TextToWrite = 'this is my third test for this txt file'


    with open(SaveLocation, 'w') as f:
        f.write(str(TextToWrite))

    if changeExtension:
        fileName = SaveLocation
        NewFileExtension = '.txli'
        ChangeFileExtension.ChangeFileExtension(fileName, NewFileExtension)


    return 'Done'




# TextToWrite = 'this is my 5th test for this txt file'


# print(generateTxtFile(TextToWrite,SaveLocation))