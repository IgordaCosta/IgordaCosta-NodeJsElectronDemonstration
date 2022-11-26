
import re


# txt = "The, rain,                in 7777777,Spain///[]<<<<<<<<<<>>>>>>>>>çççççççç============&&&&&&&&,|||||||"


# txt = "The, rain,                in 7777777,Spain///[]<<<<<<<<<<>>>>>>>>>çççççççç============&&&&&&&&,|||||||]"

def RegularExpressionTextOrList(txt,TextInput = True, ForDatabase = False):

    if TextInput:
        if ForDatabase:
            x = re.sub("[^A-Z^a-z\d^/]", "", txt)     # For database Input
                                                    #  this only has suport for american characters   ## this is for text support (2)

        else:
            x = re.sub("[^A-Z^a-z\d]", "", txt)       # for UserText Input 
                                                    # this only has suport for american characters   ## this is for text support (2)
    else:
        if txt[0] == '[':                             # this if for checking lists
            if txt[-1] == ']':
                x = txt      
            else:
                x = ''                         # this does not change the list data if it´s a list
        else:
            x = ''

    return x





# print(RegularExpressionList(txt,TextInput = True, ForDatabase = True))