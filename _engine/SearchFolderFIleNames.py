import os
import re


def sentenceCase(stringToChange):
    if stringToChange != '':
        SentenceString = re.sub('([A-Z])', r' \1', stringToChange)
        return SentenceString[:1].upper() + SentenceString[1:].lower()
    return ''





def SearchFolderFIleNames(TextToCheck, pathToCheck, CamelCaseIntoSentence =False):
    FilesInPath = os.listdir(path=pathToCheck)

    ListOfFileFoldersWithText = []
    for items in FilesInPath:
        if CamelCaseIntoSentence:
            itemnsList = sentenceCase(items).replace('_', ' ').replace('-', ' ').replace('.', ' ').replace('(', ' ').replace(')', ' ').replace('[', ' ').replace(']', ' ').split(' ')
       
        else:
            itemnsList = items.replace('_', ' ').replace('-', ' ').replace('.', ' ').replace('(', ' ').replace(')', ' ').replace('[', ' ').replace(']', ' ').split(' ')

        itemnsList2 = [x for x in itemnsList if x != '']

        itemnsList3 = [x.lower() for x in itemnsList2]

        TextToCheck2 = TextToCheck.lower()
        if TextToCheck2 in itemnsList3:
            ListOfFileFoldersWithText.append(items)


    return ListOfFileFoldersWithText



TextToCheck = 'get'

CamelCaseIntoSentence =True

FileToCheck = 'py'




if FileToCheck == 'js':
    FileToCheckID = 0

elif FileToCheck ==  'py':
    FileToCheckID = 1

else:
    pass

pathToCheck = ''
if FileToCheckID == 0:
    pathToCheck =r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2\CSSAutoFormFiller\js' + '\\'

elif FileToCheckID == 1:
    pathToCheck =r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2\CSSAutoFormFiller\_engine' + '\\'

else:
    pass


import pprint
pprint.pprint(SearchFolderFIleNames(TextToCheck, pathToCheck, CamelCaseIntoSentence =CamelCaseIntoSentence))