import RunExcelMacro


def RunImportImageMacro(excelLocation,excelFile,imageLocation,imageFilename):


    ImageWholeLocation=imageLocation+imageFilename

    MacroName="Macro1"

    Macro=\
    '''
    Sub Macro1()

    '
    ' Macro1 Macro
    '
    '
        ActiveSheet.PageSetup.CenterHeaderPicture.Filename = _
           "%s"
        Application.PrintCommunication = False
        With ActiveSheet.PageSetup
            .LeftHeader = ""
            .CenterHeader = "" & Chr(10) & "&G"
            .RightHeader = ""
            .LeftFooter = ""
            .CenterFooter = ""
            .RightFooter = ""
            .LeftMargin = Application.InchesToPoints(0.7)
            .RightMargin = Application.InchesToPoints(0.7)
            .TopMargin = Application.InchesToPoints(0.75)
            .BottomMargin = Application.InchesToPoints(0.75)
            .HeaderMargin = Application.InchesToPoints(0.3)
            .FooterMargin = Application.InchesToPoints(0.3)
            .Zoom = 100
            .PrintErrors = xlPrintErrorsDisplayed
            .OddAndEvenPagesHeaderFooter = False
            .DifferentFirstPageHeaderFooter = False
            .ScaleWithDocHeaderFooter = True
            .AlignMarginsHeaderFooter = True
            .EvenPage.LeftHeader.Text = ""
            .EvenPage.CenterHeader.Text = ""
            .EvenPage.RightHeader.Text = ""
            .EvenPage.LeftFooter.Text = ""
            .EvenPage.CenterFooter.Text = ""
            .EvenPage.RightFooter.Text = ""
            .FirstPage.LeftHeader.Text = ""
            .FirstPage.CenterHeader.Text = ""
            .FirstPage.RightHeader.Text = ""
            .FirstPage.LeftFooter.Text = ""
            .FirstPage.CenterFooter.Text = ""
            .FirstPage.RightFooter.Text = ""
        End With
        Application.PrintCommunication = True
        Range("E7").Select
        ActiveCell.FormulaR1C1 = "a"
        Range("E8").Select
        Application.PrintCommunication = False
        With ActiveSheet.PageSetup
            .PrintTitleRows = ""
            .PrintTitleColumns = ""
        End With
        Application.PrintCommunication = True
        ActiveSheet.PageSetup.PrintArea = ""
        Application.PrintCommunication = False
        With ActiveSheet.PageSetup
            .LeftHeader = ""
            .CenterHeader = "" & Chr(10) & "&G"
            .RightHeader = ""
            .LeftFooter = ""
            .CenterFooter = ""
            .RightFooter = ""
            .LeftMargin = Application.InchesToPoints(0)
            .RightMargin = Application.InchesToPoints(0)
            .TopMargin = Application.InchesToPoints(0.75)
            .BottomMargin = Application.InchesToPoints(0)
            .HeaderMargin = Application.InchesToPoints(0.3)
            .FooterMargin = Application.InchesToPoints(0)
            .PrintHeadings = False
            .PrintGridlines = False
            .PrintComments = xlPrintNoComments
            .PrintQuality = 600
            .CenterHorizontally = True
            .CenterVertically = False
            .Orientation = xlPortrait
            .Draft = False
            .PaperSize = xlPaperLetter
            .FirstPageNumber = xlAutomatic
            .Order = xlDownThenOver
            .BlackAndWhite = False
            .Zoom = 100
            .PrintErrors = xlPrintErrorsDisplayed
            .OddAndEvenPagesHeaderFooter = False
            .DifferentFirstPageHeaderFooter = False
            .ScaleWithDocHeaderFooter = True
            .AlignMarginsHeaderFooter = True
            .EvenPage.LeftHeader.Text = ""
            .EvenPage.CenterHeader.Text = ""
            .EvenPage.RightHeader.Text = ""
            .EvenPage.LeftFooter.Text = ""
            .EvenPage.CenterFooter.Text = ""
            .EvenPage.RightFooter.Text = ""
            .FirstPage.LeftHeader.Text = ""
            .FirstPage.CenterHeader.Text = ""
            .FirstPage.RightHeader.Text = ""
            .FirstPage.LeftFooter.Text = ""
            .FirstPage.CenterFooter.Text = ""
            .FirstPage.RightFooter.Text = ""
        End With
        ActiveWindow.View = xlPageLayoutView
        Range("A1").Activate
        ActiveWindow.DisplayWhitespace = True
        Application.PrintCommunication = True
    End Sub
    '''%(ImageWholeLocation)

    RunExcelMacro.RunExcelMacro(Location=excelLocation,excelFile=excelFile,MacroName=MacroName,Macro=Macro)

    print("Done importing Image")





# excelLocation="C:\\Users\\IgorDC\\Desktop\\"

# excelFile="MacroTest.xlsx"

# imageFilename="blackTest.png"

# imageLocation=excelLocation

# RunImportImageMacro(excelLocation,excelFile,imageLocation,imageFilename)