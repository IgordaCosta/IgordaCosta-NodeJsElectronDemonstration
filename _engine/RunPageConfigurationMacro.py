import RunExcelMacro



def RunPageConfigurationMacro(excelFile,Location):

    MacroName="Macro1"

    Macro=\
    '''
    Sub Macro1()

    '
    ' Macro1 Macro
    '
    '
        ActiveWindow.View = xlPageLayoutView
        Application.PrintCommunication = False
        With ActiveSheet.PageSetup
            .PrintTitleRows = ""
            .PrintTitleColumns = ""
            .LeftHeader = ""
            .CenterHeader = "" & Chr(10) & ""
            .RightHeader = ""
            .LeftFooter = ""
            .CenterFooter = ""
            .RightFooter = ""
            .LeftMargin = Application.InchesToPoints(0)
            .RightMargin = Application.InchesToPoints(0)
            .TopMargin = Application.InchesToPoints(0.7)
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
            .Zoom = 93
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
        Columns("A:K").Select
        Selection.Rows.AutoFit
        Selection.RowHeight = 3.5
        Rows("1:1").Select
        ActiveWindow.SmallScroll Down:=165
        Rows("1:235").Select
        Selection.ColumnWidth = 0.33
        Range("CL11").Select
        ActiveWindow.SmallScroll Down:=-123
        ActiveWindow.DisplayWhitespace = False
        Range("A1").Activate
        ActiveWindow.DisplayWhitespace = True
    End Sub
    '''


    RunExcelMacro.RunExcelMacro(Location=Location,excelFile=excelFile,MacroName=MacroName,Macro=Macro)

    print("Excel´s file page is configured properly")







# Location="C:\\Users\\IgorDC\\Desktop\\"

# excelFile="MacroTest.xlsx"


# RunPageConfigurationMacro(Location=Location,excelFile=excelFile)