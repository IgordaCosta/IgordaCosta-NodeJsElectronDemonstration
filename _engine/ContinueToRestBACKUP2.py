import os
import time
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import datetime

import CopyFileToNewLocation
import getUniqueAddFileEndWithFIlename
import PrintTexListSerial
import GetAllFontNamesFromFolderFunction
import GetFontFilePaths
import getTableData
import generateTxtFile
import CopyFileToNewLocation


def ContinueToRest(BaseFileLocation2,BaseFileLocation,dataframe,OutputDictionary,RealListOfColumnnames, ListToPrint, LocationAsked, FontName, FontSize, dataframe0, datafillName, OutputTableName3Keys, noError, rw, TimeNameFull):

    
    if noError == False:
       
        noError, RetunValue = CopyFileToNewLocation.CopyFileToNewLocation(getFileLocation=BaseFileLocation2, CopyToLocaion=BaseFileLocation, TimeNameFull=TimeNameFull)

        if noError == False:
            ListToPrint.append('SheetIsOpenAndHasChanges')

            PrintTexListSerial.PrintTexListSerial(ListToPrint = ListToPrint)


    if LocationAsked == '':

        location='AutoFormFillerOutputFiles'

        home = os.path.expanduser('~')       
        filePath = os.path.join(home, 'Documents',location)

    else:
        
        filePath = LocationAsked[:-1]

    if noError:
       
        numberOfRows=len(dataframe)

        # print(numberOfRows)
        # print('numberOfRows above')

        halfnumberOfRows = int(numberOfRows/2)
        InitLoopRowTime = 0
       
        if rw == 0: 
            numberOfRowsToCheck = 1
            initValue = rw

            print('rw == 0')
       
            # add time here and at the end or run for first item run time
            # the aproximate total time will then be calculated from the 
            #time gotten from the javascript function minus 
            # the time here plus
            # the time from here to the end function time multiplied by the numberOfRows

            InitLoopRowTime = int(time.time()*1000)

            JsInitTimeInMliSeconds = int(OutputDictionary['JsInitTimeInMliSeconds'])

            ElaspeTimeTillStartOfFunctin= InitLoopRowTime - JsInitTimeInMliSeconds
            
        elif rw <=  halfnumberOfRows:

            HalfPassed = OutputDictionary['HalfPassed']

            # print(HalfPassed)

            if str(HalfPassed) == 'False':
                print('half passed is false')
                
                numberOfRowsToCheck = halfnumberOfRows
                # initValue = 1
                initValue = rw
                # initRw = 'Mid'
                # here there is no run time but there is one at the end
                # to get the aproximate half eld time
                #the half time gotten at the end of the function will be used to 
                # updtate the total time remaining for completion
                # this diference in time will be added to the current time
                # thus updating the remaining time accurately
            elif str(HalfPassed) == 'True':
                print('half passed is True')
                numberOfRowsToCheck = numberOfRows
                # initValue = halfnumberOfRows

                initValue = rw
                # initRw = 'Ending'
                # here it has no time taken

                # print('half is here')
                # print(rw)
                # print('rw')

            else:
                # print('ERRROR')
                pass

        else:
            numberOfRowsToCheck = numberOfRows
            # initValue = halfnumberOfRows

            initValue = rw
            # initRw = 'Ending'
            # here it has no time taken

            # print('half is here')
            # print(rw)
            # print('rw')

        for filleToAdd in range(initValue,numberOfRowsToCheck):
        # this seems to be the place to start the for loop

            # if rw<numberOfRows:
            
            if rw<numberOfRowsToCheck:

                if not os.path.exists(filePath):
                    os.makedirs(filePath)

                FinalSaveLocation0 = dataframe[rw][0]

                FinalSaveLocation=filePath +"\\" + FinalSaveLocation0 
            

                OriginalImageLocation0 = TimeNameFull

                systemFonts = GetAllFontNamesFromFolderFunction.GetAllFontNamesFromFolder()
                        
                systemFontsList=systemFonts.split('|')

                newFont = FontName

                indexOfItemInListOfFonts=systemFontsList.index(newFont)

                fontFilePaths=GetFontFilePaths.GetFontFilePaths()

                fontSelectedPath= fontFilePaths[indexOfItemInListOfFonts]


                # print(OriginalImageLocation0)
                # print('OriginalImageLocation0 Before')
            

                NOtSaved = True    
                while NOtSaved:    
                    # print(NOtSaved)
                    # print(OriginalImageLocation0)
                    # print('OriginalImageLocation0')
                    try:
                        img = Image.open(OriginalImageLocation0)
                        NOtSaved = False
                    except FileNotFoundError:

                        getFileLocation = BaseFileLocation2
                        CopyToLocaion = BaseFileLocation
                        
                        CopyFileToNewLocation.CopyFileToNewLocation(getFileLocation, CopyToLocaion, TimeNameFull)


                draw = ImageDraw.Draw(img)

                FontSize1 = int(FontSize)

                font = ImageFont.truetype(fontSelectedPath, FontSize1)

                for j in range(len(RealListOfColumnnames)  -1 ):

                    i = j+1

                    TextToPut = dataframe[rw][i]
                    textWidth, textHeight = draw.textsize(TextToPut, font)

                    ListInvOutputTableName3 = OutputTableName3Keys[i]

                    draw.text((int(ListInvOutputTableName3[1]), int(ListInvOutputTableName3[0]) - textHeight ),TextToPut,(0,0,0),font=font)

                FileSaved= False
                try:
                    img.save(FinalSaveLocation)
                    FileSaved = True

                except:
                    pass

                if FileSaved== False:
                    try:
                        FinalSaveLocation = getUniqueAddFileEndWithFIlename.getUniqueAddFileEndWithFIlename(filename=FinalSaveLocation)

                        img.save(FinalSaveLocation)
                        FileSaved = True

                    except:
                        ListToPrint.append('DocNOTsaved')
                        PrintTexListSerial.PrintTexListSerial(ListToPrint = ListToPrint)
                        break

                if FileSaved:

                    rw=rw+1

                    os.remove(OriginalImageLocation0)

                    if rw == 1:

                        currentDT = datetime.datetime.now()

                        timeNow = str(currentDT).split('.')[0].replace(':', '-').replace(' ', '_')

                        IdentifierName0 = datafillName +'-' + timeNow

                        spaceReplaceDataUserImput = '$%78&*&'

                        IdentifierName = '_'.join(IdentifierName0.split(spaceReplaceDataUserImput))
                        
                        TextToWrite = str(dataframe) + ', '+ str([RealListOfColumnnames])

                        TextToWriteQR = str(dataframe0) + ', '+ str([RealListOfColumnnames])

                        SaveLocationTxt = filePath +"\\" + IdentifierName +  '_Txt' + '.txt'

                        SaveLocationLitxt =  filePath +"\\" + IdentifierName +  '_TxLi' + '.txt'

                        TextToWrite2 = str(TextToWrite).replace(']], [', ']], \n [').replace('], [', '], \n [')

                        generateTxtFile.generateTxtFile(TextToWrite=TextToWrite2,SaveLocation=SaveLocationTxt)

                        generateTxtFile.generateTxtFile(TextToWrite=TextToWriteQR,SaveLocation=SaveLocationLitxt, changeExtension = True)
                    

                
        if rw == 1: 
            numberOfRowsToCheck = 1
            initValue = 0
            #initRw = 'Init'
            InitLoopOutRowTime = int(time.time()*1000)

            ElaspeTimeTillLoopEnd = InitLoopOutRowTime - InitLoopRowTime 

            AproxTimeTillAllLoopComplete = ElaspeTimeTillLoopEnd * numberOfRows

            AproxTotalTimeComplete = ElaspeTimeTillStartOfFunctin + AproxTimeTillAllLoopComplete

            NewEndTimeOfCompletion = JsInitTimeInMliSeconds+ AproxTotalTimeComplete

            # print(rw)
            print('rw above 1')


            HalfPassed = 'False'

            dataList= [rw, HalfPassed]

            dataNameList=['rw' , 'HalfPassed']


            getTableData.MultipleListWriteDataDatabase(dataList,dataNameList)

            #this will be calculated constantly on the javascript end  with a similar formula





            ListToPrint.append(NewEndTimeOfCompletion) # this is for the timer part of the code

            ListToPrint.append(JsInitTimeInMliSeconds) # this is used to get the percentage


            ListToPrint.append(AproxTotalTimeComplete) # this is used to get the percentage


            ListToPrint.append("ItemSaved")

            
            PrintTexListSerial.PrintTexListSerial(ListToPrint = ListToPrint)



            
        elif rw ==  halfnumberOfRows:
            if str(HalfPassed) == 'False':
                numberOfRowsToCheck = halfnumberOfRows
                initValue = 1
                #initRw = 'Mid'

                StepComplteTtime = int(time.time()*1000)

                JsInitTimeInMliSeconds = int(OutputDictionary['JsInitTimeInMliSeconds'])

                AproxTotalTimeComplete0 = StepComplteTtime - JsInitTimeInMliSeconds 

                AproxTotalTimeComplete = (AproxTotalTimeComplete0/rw) * rw

                NewEndTimeOfCompletion = JsInitTimeInMliSeconds + AproxTotalTimeComplete





                ListToPrint.append(NewEndTimeOfCompletion) # this is for the timer part of the code

                ListToPrint.append(JsInitTimeInMliSeconds) # this is used to get the percentage


                ListToPrint.append(AproxTotalTimeComplete) # this is used to get the percentage


                ListToPrint.append("ItemSaved")

                # print(rw)

                # print('rw above half')


                # number of prints to go back is 5

                PrintTexListSerial.PrintTexListSerial(ListToPrint = ListToPrint)



                # fix the expecte time here to calculate the whole time divided by 
                #the amount of itens ran times the total items to run


                # percentDone = int(HalfCompleteTime/NewEndTimeOfCompleion) * 100
                #this will be calculated constantly on the javascript end  with a similar formula

        else:

            #initRw = 'Ending'
            pass

        if rw ==  halfnumberOfRows:

            # print(HalfPassed)

            # print('HalfPassed at half')

            if str(HalfPassed) == 'False':
                

                # data= rw

                # dataName='rw'

                HalfPassed = 'True'

                dataList= [rw, HalfPassed]

                dataNameList=['rw' , 'HalfPassed']


                getTableData.MultipleListWriteDataDatabase(dataList,dataNameList)

                # # final save locatiion of current saved item

                ListToPrint.append(NewEndTimeOfCompletion) # this is for the timer part of the code

                ListToPrint.append(JsInitTimeInMliSeconds) # this is used to get the percentage


                ListToPrint.append(AproxTotalTimeComplete) # this is used to get the percentage


                ListToPrint.append("ItemSaved")

                # print(rw)

                # print('rw above half')


                # number of prints to go back is 5

                PrintTexListSerial.PrintTexListSerial(ListToPrint = ListToPrint)


        if rw==numberOfRows:

            # print(rw)
            # print('last rw')
        
            path=os.path.realpath(filePath)
            os.startfile(path)

            ListToPrint.append("AllDONE")

            PrintTexListSerial.PrintTexListSerial(ListToPrint = ListToPrint)

            # number of prints to go back is 1










