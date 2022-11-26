import pandas



# products_list = [
# ['laptop1',13001,'car1','bike1','tv1']
# ]

# df = pandas.DataFrame (products_list, columns = ['product_name', 'price', 'bikeUsed', 'carUsed','tvUsed'])


def PadasDbToSringInput(dataframe):

    df = dataframe
    Output = str(df.values.tolist()) + ', '+ str(df.columns.tolist())

    return Output


def SringDataframeToDaframe(StringDataframe):
    Output = StringDataframe

    Data, columnNames = Output.split("]], [")
    #Database string data turned into list
    Rows = Data[2:].replace("'",'').split('], [')

    DataList = []
    for row in Rows:
        SplitRow = row.split(", ")
        DataList.append(SplitRow)

    # Takes the string Column list and Makes into a Real list
    ColumnNamesList = columnNames.replace("'",'').replace("]",'').split(", ")

    #creates a dataframe from datalist and columnNameList
    df2 = pandas.DataFrame (DataList, columns = ColumnNamesList)

    return df2

