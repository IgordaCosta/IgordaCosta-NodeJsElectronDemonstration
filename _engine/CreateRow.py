import pandas



def CreateDataframeWithOneRow(columns,row):

    frame = pandas.DataFrame(columns=columns)

    # print(row)

    # print('row check above')

    frame.loc[len(frame)] = row

    # print(frame)

    return frame



def AddRowToExistingDataframe(frame,row):

    frame.loc[len(frame)] = row

    # print(frame)

    return frame






