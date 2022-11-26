import pandas

import getTableData
import isList

def getLocationValues(dataframe, column=None):


    ExtensionType = getTableData.GetDataFromDatabase(dataName='ExtensionType',TableName='FontAndItsSize')

    # print(ExtensionType)

    # print('ExtensionType above')


    Skip=False
    IsItAList= isList.isList(item=dataframe)

    if IsItAList:
        PandaslistT = pandas.Series(dataframe)
        # print(PandaslistT)
        # print("PandaslistT")
        
        Pandaslist=PandaslistT.str.split('\\',expand=True).iloc[:,-1]
        # print(Pandaslist)
        # print("Pandaslist")
    else:
        try:
            Pandaslist=dataframe[column].str.split('\\',expand=True).iloc[:,-1]
        except IndexError:
            dataframe=pandas.DataFrame(columns=[])
            Skip=True
    
    if Skip==False:
        # print(Pandaslist)
        Pandaslist0=Pandaslist.str.split('/',expand=True).iloc[:,-1]
        Pandaslist1=Pandaslist0.str.split('.',expand=True)[0]
        # print(Pandaslist)

        if ExtensionType =='excel':

            Pandaslist2=Pandaslist1+".xlsx"

        if ExtensionType == 'image':

            Pandaslist2=Pandaslist1+".jpg"



        # print(Pandaslist2)
        
        if IsItAList:
            #dataframe to list
            dataframe=Pandaslist2.tolist() 
        else:
            dataframe[column]=Pandaslist2
            
    return dataframe







# dataframe= ''


# getLocationValues(dataframe, column=None)