import pandas
import os

import getTableData
import getLocationValues
import CheckAllFilled
import valueInFrame
import ListToSentence
# import CloseWorkbook
import CloseEspecificWorkbook
import PrintTexListSerial


def FileExistInDatabaseFunction(dataframe,column,filename,listTocheck):

        ListToPrint = []

        ExistInside=True

        ExistsNan=True

        SkipExistInside=True
 
           
        dataframe=pandas.read_excel(filename)
        
        dataframe=getLocationValues.getLocationValues(dataframe=dataframe, column="Save Name")



        columnlist0 = getTableData.GetTableData()['columnList']

        columnlist = columnlist0.replace("'",'').replace('[','').replace(']','').replace('"','').split(', ')



        ExistsNan=CheckAllFilled.CheckAllFilled(dataframe, anyNan=False)

        if ExistsNan:
         
            # print("go back to old window")
            # print("ExistsNanTrue")

            ListToPrint.append('ExistsNanTrue')

        else:

            try:
                
                ExistInside, ListofInlist0 = valueInFrame.valueInFrame(dataframe=dataframe,column=column, listTocheck=listTocheck)
                SkipExistInside=False
            except KeyError:
                # print("go back to old window")
                # print("ExistsNanTrue")

                ListToPrint.append('ExistsNanTrue')


                pass
            
            if SkipExistInside==False:

                if ExistInside:
                    ListofInlist=ListToSentence.ListToSentence(ListofInlist0)


                    data=ListofInlist
                    dataName='ListofInlist'

                    getTableData.WriteDataDatabase(data,dataName)

                    # print(ListofInlist)
                    # print("PriorityFileNamesUsed")

                    ListToPrint.append('PriorityFileNamesUsed')

                else:


                    #continue from here 


                  

                    commaReplace = '#3B&a$'


                    dataframe1 = dataframe.replace(', ',commaReplace, regex=True)

      





                    # dataframe0=dataframe.values.tolist()

                    dataframe00=dataframe1.values.tolist()

                    # print(dataframe00)

                    # print('dataframe00 List is above')



                    sizeColumn = len(columnlist)

                    # print(sizeColumn)

                    dataframe0 = []
                    for item in dataframe00:
                        item2 = item[:sizeColumn]
                        dataframe0.append(item2)



                    data=dataframe0
                    dataName="dataframe"


                    getTableData.WriteDataDatabase(data,dataName)

                    # print(filename)

                    # print("this is the filename being closed and printed above")


                    CloseEspecificWorkbook.CloseEspecificWorkbook(fileName=filename)


                    # CloseWorkbook.CloseWorkbook()

                    try:              
                        os.remove(filename)
                    except:
                        pass
                    # print("File Removed!")

                    # print(dataframe0)

                    # print("dataframe0 clean above")
                    # print("ContinueToNextPart")

                    ListToPrint.append('ContinueToNextPart')




        

        PrintTexListSerial.PrintTexListSerial(ListToPrint=ListToPrint)
            
               