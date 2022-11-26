from fontTools import ttLib

FONT_SPECIFIER_NAME_ID = 4
FONT_SPECIFIER_FAMILY_ID = 1
def GetFontName( fontToUse ):
    font = ttLib.TTFont(fontToUse)
    """Get the short name from the font's names table"""
    name = ""
    family = ""
    for record in font['name'].names:
        if b'\x00' in record.string:
            name_str = record.string.decode('utf-16-be')
        else:
            try:   
                name_str = record.string.decode('utf-8')
            except:
                name_str = record.string.decode('latin-1')

        if record.nameID == FONT_SPECIFIER_NAME_ID and not name:
            name = name_str
        elif record.nameID == FONT_SPECIFIER_FAMILY_ID and not family: 
            family = name_str
        if name and family: break
    # return name, family
    return name

# tt = 'C:\\Windows\\Fonts\\NotoSansArabic-Bold.ttf'
# # print("Name: %s  Family: %s" % shortName(tt))

# fontName= GetFontName(tt)

# print(fontName)