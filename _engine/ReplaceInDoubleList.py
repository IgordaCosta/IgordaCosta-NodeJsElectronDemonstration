



def ReplaceInDoubleList(DoubleList, Item, Subtitution):
  
    NewList = []
    for words in DoubleList:
        listItem = [w.replace(Item, Subtitution) for w in words]
        NewList.append(listItem)



    return NewList



# DoubleList = [['1a','2a','3a', '4a','5a'],['1ab','2ab','3ab', '4ab','5ab'], ['1ac','2ac','3ac', '4ac','5ac'], ['1ad','2ad','3ad', '4ad','5ad']]


# Item = 'a'

# Subtitution = 'ttttt'

# print(ReplaceInDoubleList(DoubleList, Item, Subtitution))