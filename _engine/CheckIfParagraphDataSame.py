# this is to get the original text data information

##### this is all the steps to get the page general settings

from docx import Document

from bs4 import BeautifulSoup

import pprint




def GetDocNameandLocationfromPath(Path):
    
    
    DocumentName =str(Path.split('\\')[-1:][0])

    Location = '\\'.join(Path.split('\\')[:-1])
    
    return Location, DocumentName



def getParagraphData(Location, DocumentName):

    LocOriginalDocument = Location + DocumentName

    document = Document(LocOriginalDocument)

    item = document.element.xml

    soup = BeautifulSoup(item)


    responseFind = soup.find('w:sectpr')

    sectData = str(responseFind)

    responseFind2 = soup.find('w:body').findChildren('w:p', recursive=False)

    PprParagraphList= []
    WrParagraphList= []
    for i in responseFind2:

        ppr = i.find_all('w:ppr')    
        PprParagraphList.append(ppr)

        Wr = i.find_all('w:r')    
        if Wr == []:
            pass

        else:   
            WrParagraphList.append(Wr)


    return WrParagraphList, PprParagraphList, sectData



def CompareSectData(sectData, sectData2):
    if sectData == sectData2:
        return 'sectDataIsSame'
    else:
        return 'sectDataNOTsame'
    

    
def ComparePprParagraphList(PprParagraphList, PprParagraphList2):
    if PprParagraphList == PprParagraphList2:
        return 'PprParagraphListIsSame'
    else:
        return 'PprParagraphListNOTsame'
    
    
    
def getwtValueList(WrParagraphList):
    
    wtValueListText = ''
    wtValueList = []
    for Paragraph in WrParagraphList:

        for item in Paragraph:

            wtValue = item.find('w:t')

            if wtValue == None:
                wtValue = ''
            else:
                pass

            wtValueList.append(wtValue.text)
            wtValueListText = wtValueListText + wtValue.text
    
    ValueInText = False
    if 'Ÿ' in wtValueListText:
        ValueInText = True

    wtValueListText = wtValueListText.replace(" Ÿ", "")
    wtValueListText = wtValueListText.replace("Ÿ", "")

    
    return wtValueList , wtValueListText, ValueInText




def TextSameCheck(wtValueListText, wtValueListText2):
    
    if wtValueListText == wtValueListText2:
        return 'TextIsSame'
    else:
        return 'TextNOTsame'
        
        
        
        
def OrderCorrectlyWtValues(wtValueList, wtValueList2):

    if str(wtValueList) == str(wtValueList2):
        checkValue = '2'
        valueForFunction = wtValueList
        valueForFunctionLess = wtValueList2

    else:
        checkValue='-1'
        if len(wtValueList)> len(wtValueList2):
            checkValue = '0'
            valueForFunction = wtValueList
            valueForFunctionLess = wtValueList2
            
        else:
            checkValue = '1'
            valueForFunction = wtValueList2
            valueForFunctionLess = wtValueList
            

    return checkValue, valueForFunction , valueForFunctionLess



def getStartSentecePartList(valueForFunctionLess, valueForFunction):

    StartSentecePartList = []
    StartSentecePart = -1
    NumberOfSentecePartsList = []
    
    for i in range(len(valueForFunctionLess)):
        item = valueForFunctionLess[i]

        startLetterLocation = -1    
        for l in range(len(item)):
            letter = item[l]

            breakHappend = False
            for x in range(StartSentecePart, len(valueForFunction)):

                if breakHappend:
                    break

                senteceTocheck = valueForFunction[x]            

                for z in range(startLetterLocation , len(senteceTocheck)):

                    if breakHappend:
                        break                    

                    startLetterLocation  = startLetterLocation  + 1

                    leterToCheck = senteceTocheck[z]

                    if z == len(senteceTocheck) -1 :
                        startLetterLocation = -1
                        StartSentecePart = StartSentecePart + 1

                    if leterToCheck == letter:                   
                        NumberOfSentecePartsList.append(StartSentecePart)                
                        breakHappend = True
                        break


        StartSentecePartList.append(StartSentecePart - 1)     

        
    return StartSentecePartList





def getRangeChangeList(StartSentecePartList):
    
    RangeList = []
    for i in range(len(StartSentecePartList)):

        HigherRange = StartSentecePartList[i] 

        if i == 0:
            LowerRange = 0
        else:
            LowerRange = StartSentecePartList[i-1] +1

        RangeItem = [LowerRange, HigherRange]

        RangeList.append(RangeItem)


    return RangeList






######## this is for checking if the words even though having a controlled additin were not altered by things like 
######## if its bold or italic or underlined, etc.


def CheckforItalicBoldAlteration(RangeList, WrParagraphList):
       
    rprItemList = []
    for x in range(len(WrParagraphList)):
        checkedItem = WrParagraphList[x]

        for t in range(len(checkedItem)):
            checkedItemPart = checkedItem[t]
            rprItem = checkedItemPart.find('w:rpr')
            rprItemList.append(rprItem)
        

    NotTheSame = False
    for i in range(len(RangeList)):

        if NotTheSame:
            break

        rangeListItem = RangeList[i]

        for i in range(rangeListItem[0], rangeListItem[1] + 1 ):
            if rangeListItem[0] == i:
                compareItem = rprItemList[i]
                
            else:
                if str(compareItem) == str(rprItemList[i]):
                    pass
                
                else:
                    NotTheSame = True
                    break

    if NotTheSame:
        return 'NOTtheSame'

    else:
        return 'SameValues'
    
    
    


def CheckIfParagraphDataSame(Location, DocumentName, DocumentName2, Location2 = ''):
    
    if Location2 == '':
        Location2 = Location

    isSameValues = 'NOTtheSame'  
        
    WrParagraphList, PprParagraphList, sectData = getParagraphData(Location, DocumentName)

    Location = Location2
    DocumentName = DocumentName2 

    WrParagraphList2, PprParagraphList2, sectData2 = getParagraphData(Location, DocumentName)

    IsSectDataSame = CompareSectData(sectData, sectData2)

    ContinueOK = False
    if IsSectDataSame == 'sectDataIsSame':
        ContinueOK = True
    elif IsSectDataSame == 'sectDataNOTsame':
        pass
    else:
        print('IsSectDataSame is not a valid value, IsSectDataSame is: ' + IsSectDataSame)

    if ContinueOK:
        ContinueOK = False

        IsPprParagraphListSame = ComparePprParagraphList(PprParagraphList, PprParagraphList2)

        if IsPprParagraphListSame == 'PprParagraphListIsSame':
            ContinueOK = True
        elif IsPprParagraphListSame == 'PprParagraphListNOTsame':
            pass
        else:
            print('IsPprParagraphListSame is not a valid value, IsPprParagraphListSame is: ' + IsPprParagraphListSame)


        if ContinueOK:
            ContinueOK = False
            
            wtValueList , wtValueListText, ValueInText = getwtValueList(WrParagraphList)
            wtValueList2 , wtValueListText2, ValueInText2 = getwtValueList(WrParagraphList2)
            
            if ValueInText == ValueInText2:
                if ValueInText == False:
                    isSameValues = 'ValueNOTAdded'
                    
                else:
                    isSameValues = 'ERRORoriginalDocumentHasLetterCode'

            else:
                ContinueOK = True
                
            
            if ContinueOK:
                ContinueOK = False
                
                if ValueInText:
                    pass
                else:
                    
                    CwtValueList  = wtValueList2                     
                    CwtValueListText = wtValueListText2                    
                    CValueInText = ValueInText2
                    
                    
                    CwtValueList2 = wtValueList                 
                    CwtValueListText2 = wtValueListText                    
                    CValueInText2 = ValueInText
                    
                    
                    wtValueList2  = CwtValueList2                    
                    wtValueListText2 = CwtValueListText2                  
                    ValueInText2 = CValueInText2
                    
                    
                    wtValueList = CwtValueList                    
                    wtValueListText = CwtValueListText                   
                    ValueInText = CValueInText
                    
                                                            
                    CWrParagraphList = WrParagraphList2
                    
                    CWrParagraphList2 = WrParagraphList                                  
                    
                    
                    WrParagraphList = CWrParagraphList 
                    
                    WrParagraphList2 = CWrParagraphList2
                    
                                                                                                                                                   
                isTextSame = TextSameCheck(wtValueListText, wtValueListText2)

                if isTextSame == 'TextIsSame':
                    ContinueOK = True
                elif isTextSame == 'TextNOTsame':
                    pass
                else:
                    print('isTextSame is not a valid value, isTextSame is: ' + isTextSame)


                if ContinueOK:
    #                 ContinueOK = False

                    checkValue, valueForFunction , valueForFunctionLess = OrderCorrectlyWtValues(wtValueList, wtValueList2)

                    StartSentecePartList = getStartSentecePartList(valueForFunctionLess, valueForFunction)

                    RangeList = getRangeChangeList(StartSentecePartList)

                    isSameValues = CheckforItalicBoldAlteration(RangeList, WrParagraphList)
            
            
            
            
            
    
    return isSameValues
        
            
        
    
    
    
    
