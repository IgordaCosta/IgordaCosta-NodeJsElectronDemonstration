import checkIfDoubleList



def IfSingleListMakeDoubleList(List):

    if isinstance(List, list):

        isListDoubleList=checkIfDoubleList.checkIfDoubleList(List)
        
        if isListDoubleList:
            DoubleList=List
        else:
            DoubleList=[]
            DoubleList.append(List)

        return DoubleList

    else:
        # print("this is not a list")

        return ''




# List='[[11, 21, 31, 41]]'


# NewList=IfSingleListMakeDoubleList(List)

# print(NewList)
