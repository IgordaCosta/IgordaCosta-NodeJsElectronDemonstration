import GetAllFontNamesFromFolderFunction
import PrintTexListSerial


ListToPrint = []

OutputGotten = GetAllFontNamesFromFolderFunction.GetAllFontNamesFromFolder()


# print(OutputGotten)



ListToPrint.append(OutputGotten)


PrintTexListSerial.PrintTexListSerial(ListToPrint=ListToPrint)





# import os

# import GetFontName


# def GetAllFontNamesFromFolder():
#     allFontNames = []

#     mypath='C:\\Windows\\Fonts\\'

#     for folder, subs, files in os.walk(mypath):
#         for filename in files:
#             if (filename.split(".")[-1]=="ttf"):
#                 fontToUse=os.path.abspath(os.path.join(folder, filename))

#                 # print(fontToUse)

#                 FontNameOnly=GetFontName.GetFontName(fontToUse=fontToUse)

#                 allFontNames.append(FontNameOnly)


#     # print(allFontNames)

#     s="|"

#     allFontNamesString0=s.join(allFontNames)


#     allFontNamesString=allFontNamesString0.replace(' ','+')

#     print(allFontNamesString)

#     # return allFontNamesString



# GetAllFontNamesFromFolder()










# # Arial|Helvetica+Neue|Courier+New|Times+New+Roman|Comic+Sans+MS|Verdana|Impact'

