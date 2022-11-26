import time
import string
import random

def dec2Anybase(num,baseList): 
    
    base=len(baseList)
    base_numList = []    
    newdiv = num
    
    while newdiv>base:
        dig = int(newdiv%base)

        newdiv = newdiv/base
        base_num = base_numList.append(baseList[dig])

    base_num = base_numList.append(baseList[int(newdiv)])
    base_numList = base_numList[::-1]  
    
    base_numString= ''.join(base_numList)
        
    return base_numString




def endingFileDiferentiator(Multiple = 1.789, makeRandom=False):
    num=int(time.time()*1000)*Multiple 

    separator = '_' # this is the string used to append this ending so to remove it for name rerification
    stringChosen = string.ascii_letters + '!#$%&()*+,-:;<=>?@[]^{|}~'

    baseList= list(stringChosen)
    
    if makeRandom:
        random.shuffle(baseList)

    FileDiferentiator = dec2Anybase(num,baseList)
    
    
    return FileDiferentiator