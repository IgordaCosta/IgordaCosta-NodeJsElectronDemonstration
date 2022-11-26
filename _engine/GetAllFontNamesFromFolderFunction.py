import os
import pathlib

import GetFontName


def GetAllFontNamesFromFolder():
    allFontNames = []

    #mypath='C:\\Windows\\Fonts\\'          # This is the font location for Windows 7, 10, and 11 so this path does not change

    homedir = pathlib.Path.home()

    homeanchor = homedir.anchor

    mypath = homeanchor + 'Windows\\Fonts\\'

    for folder, subs, files in os.walk(mypath):
        for filename in files:
            if (filename.split(".")[-1]=="ttf"):
                fontToUse=os.path.abspath(os.path.join(folder, filename))

                # print(fontToUse)

                FontNameOnly=GetFontName.GetFontName(fontToUse=fontToUse)

                allFontNames.append(FontNameOnly)


    # print(allFontNames)

    s="|"

    allFontNamesString0=s.join(allFontNames)


    allFontNamesString=allFontNamesString0.replace(' ','+')

    # print(allFontNamesString)

    return allFontNamesString



# GetAllFontNamesFromFolder()










# Arial|Helvetica+Neue|Courier+New|Times+New+Roman|Comic+Sans+MS|Verdana|Impact'

