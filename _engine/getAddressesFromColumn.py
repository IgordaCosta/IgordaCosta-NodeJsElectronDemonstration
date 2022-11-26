import re



def getAddressesFromColumn(itemAddress):
        
    rowList=[]
    columnList=[]
    for values in range(len(itemAddress)):
        temp = re.findall(r'\d+', itemAddress[values]) 
        i,c = list(map(int, temp)) 
        rowList.append(i)
        columnList.append(c)
    #     print(i)
    #     print(c)
    # print(columnList)
    # print("columnList")
    # print(rowList)
    # print("rowList")
    
    return rowList, columnList