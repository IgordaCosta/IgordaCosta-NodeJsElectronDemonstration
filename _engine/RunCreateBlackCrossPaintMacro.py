import pathlib

import RunExcelMacro



def RunCreateBlackCrossPaintMacro(excelFile,Location):
    MacroName="Macro1"

    Macro=\
    '''
    Sub Macro1()

    '
    ' Macro1 Macro
    '

    '
        ActiveWindow.SmallScroll Down:=150
        Range("CL1:CU219").Select
        With Selection.Interior
            .PatternColorIndex = xlAutomatic
            .ThemeColor = xlThemeColorLight1
            .TintAndShade = 0
            .PatternTintAndShade = 0
        End With
        ActiveWindow.SmallScroll Down:=45
        Range("A113:GF122").Select
        With Selection.Interior
            .PatternColorIndex = xlAutomatic
            .ThemeColor = xlThemeColorLight1
            .TintAndShade = 0
            .PatternTintAndShade = 0
        End With
        ActiveWindow.SmallScroll Down:=-69
        Range("A1").Activate
    End Sub
    '''

    RunExcelMacro.RunExcelMacro(Location=Location,excelFile=excelFile,MacroName=MacroName,Macro=Macro)

    print("Black cross created in excelsheet!")





#Location="C:\\Users\\IgorDC\\Desktop\\"


homedir = pathlib.Path.home()

Location = str(homedir) + '\\Desktop\\'


excelFile="MacroTest2.xlsx"


RunCreateBlackCrossPaintMacro(excelFile,Location)