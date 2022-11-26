from docx import Document

from bs4 import BeautifulSoup





#def getWrParagraphList(Location, DocumentName):
def getWrParagraphList(DocLocation):

    #LocOriginalDocument = Location + DocumentName

    LocOriginalDocument = DocLocation

    document = Document(LocOriginalDocument)

    item = document.element.xml

    soup = BeautifulSoup(item)

    responseFind2 = soup.find('w:body').findChildren('w:p', recursive=False)


    WrParagraphList= []
    for i in responseFind2:

        Wr = i.find_all('w:r')    
        if Wr == []:
            pass

        else:   
            WrParagraphList.append(Wr)


    return WrParagraphList


def checkIfValueInText(WrParagraphList):
    
    wtValueListText = ''
    wtValueList = []
    for Paragraph in WrParagraphList:

        for item in Paragraph:

            wtValue = item.find('w:t')

            if wtValue == None:
                wtValue = ''
            else:
                pass

            wtValueListText = wtValueListText + wtValue.text
    
    ValueInText = False
    if 'Ÿ' in wtValueListText:
        ValueInText = True

    
    return ValueInText