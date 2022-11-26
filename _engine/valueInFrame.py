

def valueInFrame(dataframe,column, listTocheck):
        # print(dataframe[column])
        ListofInlist=[]
        ExistInside=False
        for value in listTocheck:
            # print(value)
            # print(dataframe[column])
            Inlist=value in list(dataframe[column])
            if Inlist:
                ExistInside=True
                ListofInlist.append(value)
        # print(ListofInlist)
        return ExistInside, ListofInlist