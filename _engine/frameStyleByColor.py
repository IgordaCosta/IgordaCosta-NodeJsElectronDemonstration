# from StyleFrame import StyleFrame, Styler
from styleframe import StyleFrame, Styler



def frameStyleByColor(path, columnsList, color):
        
    if color=='blue':
        frameStyle(path=path, columnsList=columnsList)
        pass
    
    if color=='green':
        frameStyle(path=path, columnsList=columnsList, BackgroundRGBr=0 , BackgroundRGBg= 195, BackgroundRGBb=0)
        pass
    
    if color=='red':
        frameStyle(path=path, columnsList=columnsList, BackgroundRGBr=237 , BackgroundRGBg= 0, BackgroundRGBb=0)
        pass
    
    if color=='yellow':
        frameStyle(path=path, columnsList=columnsList, BackgroundRGBr=255 , BackgroundRGBg= 255, BackgroundRGBb=0, LetterRGBr=0, LetterRGBg=0, LetterRGBb=0)
        pass
        
    
    
def frameStyle(path,columnsList,BackgroundRGBr=0,BackgroundRGBg=0,BackgroundRGBb=206,LetterRGBr=255,LetterRGBg=255,LetterRGBb=255):

    DictionaryofWidths= {x: 1.3*(int(len(x))+13) for x in columnsList}

    frame2 = StyleFrame.read_excel(path= path, sheet_name='Sheet1')
    print(frame2)
    print('ok 1111')
    
    print(columnsList)
    
    print('columnsList used in frameStyle')
        
    ew = StyleFrame.ExcelWriter(path)
    
    print('ok 2222')
        
    HeaderStyle= Styler(bg_color=DecHex(BackgroundRGBr)+DecHex(BackgroundRGBg)+DecHex(BackgroundRGBb), bold=True, font_color= DecHex(LetterRGBr)+DecHex(LetterRGBg)+DecHex(LetterRGBb), border_type='medium', horizontal_alignment='center', vertical_alignment='center', shrink_to_fit=False)
        
    print('ok 3333')
    
    frame2.apply_headers_style(HeaderStyle, style_index_header=True)
        
    print('ok 4444')
    StyleFrame.set_column_width_dict(frame2, DictionaryofWidths)
    
    StyleFrame.to_excel(frame2, excel_writer = ew, sheet_name='Sheet1')

    print('ok 5555')
    
    ew.save()
    
    
def DecHex(n):
    '''
    :para n: int
    :return: str
    >>> DecHex(10)
    'A'
    >>> DecHex(15)
    'F'
    >>> DecHex(32)
    '20'
    >>> DecHex(255)
    'FF'
    >>> DecHex(65535)
    'FFFF'
    '''

    x16 = '0 1 2 3 4 5 6 7 8 9 a b c d e f'.upper().split()
    result = []
    try:
        n = int(n)
        if n == 0:
            return '00'
        if 17 > n:
            result.append('0' + x16[(n % 16)])
            n = n // 16
        result.reverse()
        while n > 0:
            result.append(x16[(n % 16)])
            n = n // 16
        result.reverse()
    except ValueError as e:
        return ('Erro: %s' %e)
    except:
        raise
    else:
        return ''.join(result)