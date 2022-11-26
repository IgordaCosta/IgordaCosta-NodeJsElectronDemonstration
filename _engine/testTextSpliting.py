import base93Characterconversion

# TextToChange = r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2\CSSAutoFormFiller\_clientImageFiles\adosMul_taF_aces_Isabela.jpg'
TextToChange = r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller2\CSSAutoFormFiller\_clientImageFiles\adosMultaFacesIsabela.jpg'
# TextToChange = r'_clientImageFiles\ados_Mu_lt_aFacesIsabela.jpg'
FileEnding = base93Characterconversion.base93Characterconversion()


OriginalFileName = 'adosMultaFacdesIsabela.jpg'
def ReplaceEndingFunction(TextToChange, FileEnding, OriginalFileName):

        
    checkUsed = part1 = '\\'.join(TextToChange.replace('/', '\\').split('\\')[:-1])

    print(part1)

    # print(TextToChange.replace('/', '\\').split('\\')[0])

    

    part21 = (TextToChange.replace('/', '\\').split('\\')[-1])
    
    print(part21)

    

    part2 = ''
    if part21 == OriginalFileName:
        part23 = part21
    else:
        part23 = '_'.join(part21.split("_")[:-1])
        print(part23)
        print('print(part23)')

    try:
        part2 =  part23.split('.')[:-1][0]
        
    except:
        part2 = part23

    print(part2)

    # # print(part21.split("_"))

    # # if len(part21.split("_"))>1:
    # #     part2 = '_'.join(part21.split("_")[:-1])
    # # else:
    # #     part2 = part21

    part3 = '.' + TextToChange.split('.')[-1]

    print(part3)


    

    partfull= part1 + '\\' + part2 +  '_' + FileEnding  + part3

    return partfull



print(ReplaceEndingFunction(TextToChange, FileEnding, OriginalFileName))