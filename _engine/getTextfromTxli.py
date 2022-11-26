# from cv2 import checkChessboard
# import pandas
import datetime

import getTextfromLiTxFunction

import getTableData
import OpenDeleteRecreateSheetWithData




def getTextfromQR():

    dataName= 'fileLocation'

    SaveLocation = getTableData.GetDataFromDatabase(dataName=dataName)

    # print(SaveLocation)

    # print('\\'.join(SaveLocation.split('\\')[:-1]))

    LocationOnly = '\\'.join(SaveLocation.split('\\')[:-1]) +'\\'

    # print(LocationOnly)

    fileNameGotten = SaveLocation.split('\\')[-1]

    # print(fileNameGotten.split('-')[0])

    fileJobName = fileNameGotten.split('-')[0]
    
    # print(fileJobName)

    # print('fileJobName')




    # checkContinueValue = 'ghkfasdygdi345363'    

    # OutputText = getTextfromQRFunction.getTextfromQR(SaveLocation=SaveLocation,checkContinueValue=checkContinueValue)

    OutputText = getTextfromLiTxFunction.getTextfromLiTxFunction(SaveLocation=SaveLocation)

    # print(OutputText)


    # print(OutputText[0])


    # print(OutputText[1])

    # ResultFunction =''

    # if OutputText[1] == 'CheckPassed':


        # print(OutputText[0].replace('[[','').replace("]]",'').replace("'",'').split('], ['))

        # print(OutputText[0].replace("'",'').split(']], [['))


    Item = '#3B&a$'

    Subtitution = ', '


    



    database = OutputText[0].replace("'",'').split(']], [[')

    database = OutputText.replace("'",'').split(']], [[')


    


    # print(database[0].replace('[[','').split('], ['))

    # print(database[1].replace("]]",'').split(', '))

    # columnNames = database[1].replace("]]",'').split(', ')

    columnNames0 = database[1].replace("]]",'').split(', ')


    

    columnNames = [w2.replace(Item, Subtitution) for w2 in columnNames0]



    # print(columnNames)

    # print(columnNames[1])


    # ItemsData = OutputText[0].replace('[[','').replace("]]",'').replace("'",'').split('], [')


    ItemsData =  database[0].replace('[[','').split('], [')

    # print(ItemsData)

    # print(ItemsData[1])


    ItensList = []
    for i in range(len(ItemsData)):
        # print(i)
        ItemsData2 =ItemsData[i].split(', ')


        listItem = [w.replace(Item, Subtitution) for w in ItemsData2]


        # ItensList.append(ItemsData2)

        ItensList.append(listItem)


    # print(ItensList)

    # print(ItensList[0][1])



    # df = pandas.DataFrame(ItensList, columns=columnNames)





    currentDT = datetime.datetime.now()

    timeNow = str(currentDT).split('.')[0].replace(':', '-')




    filename = LocationOnly+ fileJobName + '-'+ "LiTxData"+'-' + timeNow + ".xlsx"


    OpenDeleteRecreateSheetWithData.OpenDeleteRecreateSheet(columnList=columnNames, dataList=ItensList, filename = filename)
    
    # print('Done')

    ResultFunction =  'Done'


    # elif 'NotPassed':
    #     #  print('Error')
    #      ResultFunction = 'Error'

    # elif 'fileNotQR':
    #     #  print('Error')
    #     ResultFunction = 'Error'

    # elif 'OtherError':
    #     #  print('Error')
    #     ResultFunction = 'Error'


    # else:
    #     # print('other text not suported at output')
    #     ResultFunction = 'Error'

    data = ResultFunction

    dataName1 = 'ResultFunction'

    getTableData.WriteDataDatabase(data = data, dataName=dataName1)

        





getTextfromQR()

