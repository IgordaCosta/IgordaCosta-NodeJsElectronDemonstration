import RunExcelMacro



def RunMergeCellsMacro(Location,excelFile,bottomLeft,topLeft,topRight):

    
    MacroName="Macro1"

    Macro=\
    '''Sub Macro1()

    '
    ' Macro1 Macro
    '

    '
        Range("%s:%s").Select
        Range("%s").Activate
        With Selection
            .HorizontalAlignment = xlCenter
            .VerticalAlignment = xlBottom
            .WrapText = False
            .Orientation = 0
            .AddIndent = False
            .IndentLevel = 0
            .ShrinkToFit = False
            .ReadingOrder = xlContext
            .MergeCells = False
        .Merge
        End With
    End Sub
    '''%(bottomLeft,topLeft,topRight)




    RunExcelMacro.RunExcelMacro(Location=Location,excelFile=excelFile,MacroName=MacroName,Macro=Macro)

    print("Done Merging Cells")