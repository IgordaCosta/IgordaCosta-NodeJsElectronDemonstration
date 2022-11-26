


def RemoveExtraSlashes(TextToRemoveSlashes):

    

    # print(str(TextToRemoveSlashes).split('\\'))
    # print(len(str(TextToRemoveSlashes).split('\\')))
    if len(str(TextToRemoveSlashes).split('\\')) == 1:
        # print('slashes not removed for no \\')
        return TextToRemoveSlashes
        

    TypeTuppleUsed = False
    if type(TextToRemoveSlashes) == type(()):
        TextToRemoveSlashes00 = TextToRemoveSlashes
        TextToRemoveSlashes = list(TextToRemoveSlashes00)
        TypeTuppleUsed = True

    # if type(TextToRemoveSlashes) == type(int(7)):
    #     return TextToRemoveSlashes

    TextToRemoveSlashes1 = str(TextToRemoveSlashes).replace('/','\\')


    TextToRemoveChars2 = '\\'.join([i for i in TextToRemoveSlashes1.split('\\') if i !=''])

    if TypeTuppleUsed:
        TextToRemoveChars200 = TextToRemoveChars2
        TextToRemoveChars2 = tuple(TextToRemoveChars200)

    return TextToRemoveChars2




def RemoveExtraSlashesList(ListToRemoveSlashes):
    
    ListOfItemNoSlashes = []

    for item in range(len(ListToRemoveSlashes)):
        item2 = RemoveExtraSlashes(item)
        ListOfItemNoSlashes.append(item2)

    return ListOfItemNoSlashes



# type(int(7))
# TextToRemoveSlashes = 'C/////Users\\\\\\\\Tigereye\\\\\\\\Desktop\\\\\\\\Apps\\\\\\\\CSSAutoFormFiller2\\\\\\\\CSSAutoFormFiller\\\\\\\\_clientImageFiles'

# print(RemoveExtraSlashes(TextToRemoveSlashes))

# TextToRemoveSlashes = ''


# print(str(TextToRemoveSlashes).split('\\'))


# print(len(str(TextToRemoveSlashes).split('\\')))






# textToCheck = str(TextToRemoveSlashes).replace('/','\\')

# itemA = [x for x in textToCheck.split('\\') if x !='']
# print(itemA)

# print('\\'.join(itemA))



