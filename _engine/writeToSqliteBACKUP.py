import sqlite3

from h11 import Data

import GetKeyfileNameType
import PandasDfIntoSecureDb
import GetWriteDBTableSecured
import changeDirectory

def writeToSqlite(frame,table_name):

    #frame here is a pandas dataframe

    DatabaseName="AutoFormFiller.db"

    TableName = table_name

    TableNameUsed = ''

    TableOptions = ['FontAndItsSize','FilesInDatabase','qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq','KEY_']

    if TableName == 'FontAndItsSize':
        TableNameUsed = TableOptions[0]

    elif TableName == 'FilesInDatabase':
        TableNameUsed = TableOptions[1]

    elif TableName == 'qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq':
        TableNameUsed = TableOptions[2]

    elif TableName[:4] == 'KEY_':
 
        KeyFilename = TableName
        TableNameUsed = GetKeyfileNameType.GetKeyfileNameType(KeyFilename)

    else:
        pass

    if TableNameUsed == 'qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq':

        dataframe = frame

        StringFrame= PandasDfIntoSecureDb.PadasDbToSringInput(dataframe=dataframe)

        ItemName = 'PdFrame'
        
        ItenValue = StringFrame

        GetWriteDBTableSecured.WriteTableSecuredIten(ItemName=ItemName,ItenValue=ItenValue)



    else:

        changeDirectory.ChangeTokey()

        conn = sqlite3.connect(DatabaseName)
        # print(frame)
        frame.to_sql(TableNameUsed, conn, if_exists="replace")