import os

import getTableData

import CheckIfParagraphDataSame

def checkIfThereAreOtherChanges():

    dictValue=getTableData.GetTableData()

    newFileLocation=dictValue['newFileLocation']

    fileLocation=dictValue['fileLocation']

    Location, DocumentName = CheckIfParagraphDataSame.GetDocNameandLocationfromPath(Path = newFileLocation)

    Location2, DocumentName2 = CheckIfParagraphDataSame.GetDocNameandLocationfromPath(Path = fileLocation)


    isSameValues = CheckIfParagraphDataSame.CheckIfParagraphDataSame(Location, DocumentName, DocumentName2, Location2)


    data = isSameValues

    dataName = 'isSameValues'

    getTableData.WriteDataDatabase(data,dataName)





checkIfThereAreOtherChanges()






    
  

