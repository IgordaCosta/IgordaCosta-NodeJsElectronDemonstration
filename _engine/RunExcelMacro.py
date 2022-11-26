import os, sys
import win32com.client

import RemoveMacroFromSheet




def RunExcelMacro(Location,excelFile,MacroName,Macro):
    
    macroAdded=False
    path=Location

    pathToExcelFile = path + excelFile
    
    myMacroName = MacroName

    macroInString=Macro    

    macro=macroInString

    # open up an instance of Excel
    excel = win32com.client.Dispatch("Excel.Application")

    # do the operation without opening Excel visually

    excel.Visible = False

    # open the excel workbook from file
    workbook = excel.Workbooks.Open(Filename=pathToExcelFile)

    #check if the excel program has the right configuration
    try:
        excelModule = workbook.VBProject.VBComponents.Add(1)
        macroAdded=True
    except:
        print("must change options in excel!")
        ##### provide here window with the steps

    if macroAdded:

        excelModule.CodeModule.AddFromString(macro)

        # run the macro
        excel.Application.Run(myMacroName)

        #removeMacroFiles
        RemoveMacroFromSheet.RemoveMacroFromSheet(excelApp=excel,excelWorkbook=workbook)

        # save the workbook and close
        excel.Workbooks(1).Close(SaveChanges=1)
        excel.Application.Quit()

        # garbage collection
        del excel
    
    print("Done Macro Run")



# Location="C:\\Users\\IgorDC\\Desktop\\"

# excelFile="MacroTest.xlsx"

# MacroName="Macro1"






# Macro=\
# '''
# Sub Macro1()

# '
# ' Macro1 Macro
# '
# '
#     ActiveWindow.View = xlPageLayoutView
#     Application.PrintCommunication = False
#     With ActiveSheet.PageSetup
#         .PrintTitleRows = ""
#         .PrintTitleColumns = ""
#         .LeftHeader = ""
#         .CenterHeader = "" & Chr(10) & ""
#         .RightHeader = ""
#         .LeftFooter = ""
#         .CenterFooter = ""
#         .RightFooter = ""
#         .LeftMargin = Application.InchesToPoints(0)
#         .RightMargin = Application.InchesToPoints(0)
#         .TopMargin = Application.InchesToPoints(0)
#         .BottomMargin = Application.InchesToPoints(0)
#         .HeaderMargin = Application.InchesToPoints(0)
#         .FooterMargin = Application.InchesToPoints(0)
#         .PrintHeadings = False
#         .PrintGridlines = False
#         .PrintComments = xlPrintNoComments
#         .PrintQuality = 600
#         .CenterHorizontally = True
#         .CenterVertically = False
#         .Orientation = xlPortrait
#         .Draft = False
#         .PaperSize = xlPaperLetter
#         .FirstPageNumber = xlAutomatic
#         .Order = xlDownThenOver
#         .BlackAndWhite = False
#         .Zoom = 93
#         .PrintErrors = xlPrintErrorsDisplayed
#         .OddAndEvenPagesHeaderFooter = False
#         .DifferentFirstPageHeaderFooter = False
#         .ScaleWithDocHeaderFooter = True
#         .AlignMarginsHeaderFooter = True
#         .EvenPage.LeftHeader.Text = ""
#         .EvenPage.CenterHeader.Text = ""
#         .EvenPage.RightHeader.Text = ""
#         .EvenPage.LeftFooter.Text = ""
#         .EvenPage.CenterFooter.Text = ""
#         .EvenPage.RightFooter.Text = ""
#         .FirstPage.LeftHeader.Text = ""
#         .FirstPage.CenterHeader.Text = ""
#         .FirstPage.RightHeader.Text = ""
#         .FirstPage.LeftFooter.Text = ""
#         .FirstPage.CenterFooter.Text = ""
#         .FirstPage.RightFooter.Text = ""
#     End With
#     Application.PrintCommunication = True
#     Columns("A:K").Select
#     Selection.Rows.AutoFit
#     Selection.RowHeight = 3.5
#     Rows("1:1").Select
#     ActiveWindow.SmallScroll Down:=165
#     Rows("1:235").Select
#     Selection.ColumnWidth = 0.33
#     Range("CL11").Select
#     ActiveWindow.SmallScroll Down:=-123
#     ActiveWindow.DisplayWhitespace = False
#     Range("A1").Activate
# End Sub
# '''






# RunExcelMacro(Location,excelFile,MacroName,Macro)