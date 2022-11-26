import getTableData
import PutListDataIntoImage


def getFinalLocationItens():

    DataGotten = getTableData.GetTableData()

    # print(DataGotten)


    lastTempLocationPointX = DataGotten['lastTempLocationPointX']

    lastTempLocationPointY = DataGotten['lastTempLocationPointY']

    FoundData = False
    try: 
        finalLocationsX = DataGotten['finalLocationsX']

        FoundData = True

    except KeyError:
        pass





    if FoundData:

    
        finalLocationsY = DataGotten['finalLocationsY']

        #['['1314']', '98']",

        ListA = str(finalLocationsX).replace('[','').replace(" ",'').replace(']','').replace("'",'').split(',')

        ListB = str(finalLocationsY).replace('[','').replace(" ",'').replace(']','').replace("'",'').split(',')

        DataA = lastTempLocationPointX

        DataB = lastTempLocationPointY



    else:


        finalLocationsX=[]

        finalLocationsY=[]


        ListA = finalLocationsX

        ListB = finalLocationsY

        DataA = lastTempLocationPointX

        DataB = lastTempLocationPointY



    AddTwoDataToListsSave(ListA,ListB,DataA,DataB)

   





def AddTwoDataToListsSave(ListA, ListB, DataA, DataB):

  
  try:

    finalLocationsX = ListA.split(',')

    finalLocationsY = ListB.split(',')

  except:

    # print("it is just an empty list")

    # print('ListA :', ListA)

    # print('ListB :', ListB)

    finalLocationsX = ListA

    finalLocationsY = ListB

  


  lastTempLocationPointX = DataA

  lastTempLocationPointY = DataB


  
  finalLocationsX.append(lastTempLocationPointX)

  finalLocationsY.append(lastTempLocationPointY)


  dataList = [finalLocationsX, finalLocationsY]

  dataNameList = ['finalLocationsX', 'finalLocationsY']


  getTableData.MultipleListWriteDataDatabase(dataList=dataList,dataNameList=dataNameList)


  PutListDataIntoImage.PutListDataIntoImage(finalLocationsX, finalLocationsY)


 





getFinalLocationItens()

