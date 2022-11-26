import pandas


def CheckAllFilled(storedValues, anyNan=True):        
        
        if storedValues.empty==False:
            if anyNan==True:
                ExistsNan=(pandas.isnull(storedValues.values)).any()
            if anyNan==False:

                # print(storedValues.iloc[:,[0]])
                # print("storedValues.iloc[:,[0]]")
                # print(pandas.isnull(storedValues.iloc[:,[0]]).values.any())
                # print("pandas.isnull(storedValues.iloc[:,[0]]).values.any()")
                # print(storedValues.iloc[:,[0]])
                
                # print(len(storedValues.columns.values))
                # print("len(storedValues.columns.values)")
                # print("len(storedValues.column.values)")
                colnum=len(storedValues.columns.values)

                rownum= len(storedValues)
                              
                                
                lisOfNan=[] 
                for i in range(colnum):
                    for r in range(rownum):
                        valueInList=(pandas.isnull(storedValues.iloc[[r],[i]]).values.all())
                        # print(valueInList)
                        lisOfNan.append(valueInList)

                    # print(lisOfNan)
                    if True in lisOfNan:
                        # print("True in ListNan")
                        ExistsNan=True
                    else:
                        ExistsNan=False
                    
                               
        if storedValues.empty:
            
            ExistsNan=True

        # print(ExistsNan)   
        return ExistsNan
