def RemoveExtension(StringUsed):
    lenExtension = len(StringUsed.split('.')[-1])+1

    OutputString = StringUsed[:-lenExtension]
    
    return OutputString