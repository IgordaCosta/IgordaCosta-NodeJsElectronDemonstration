import os
import pathlib
# from os.path import join


def GetFontFilePaths():
    #mypath='C:\\Windows\\Fonts\\'

    homedir = pathlib.Path.home()

    homeanchor = homedir.anchor

    mypath = homeanchor + 'Windows\\Fonts\\'

    allPathsList = []

    for folder, subs, files in os.walk(mypath):
        for filename in files:
            if (filename.split(".")[-1]=="ttf"):
                allPathsList.append(os.path.abspath(os.path.join(folder, filename)))

    return allPathsList


# print(GetFontFilePaths())



