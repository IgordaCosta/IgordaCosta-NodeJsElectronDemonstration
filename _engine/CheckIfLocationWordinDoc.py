import checkIfValueInText
import getTableData





DataGotten = getTableData.GetTableData()

DocLocation = DataGotten['newFileLocation']

WrParagraphList = checkIfValueInText.getWrParagraphList(DocLocation = DocLocation)

ValueInText = checkIfValueInText.checkIfValueInText(WrParagraphList=WrParagraphList)

if ValueInText:
    ValueInTextResult = 'ValueIsInText'

else: 
    ValueInTextResult = 'ValueNOTinText'

data = ValueInTextResult

dataName = 'ValueInText'

getTableData.WriteDataDatabase(data=data,dataName=dataName)