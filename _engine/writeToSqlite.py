import sqlite3
import time
from datetime import date, datetime

from h11 import Data

import GetKeyfileNameType
import PandasDfIntoSecureDb
import GetWriteDBTableSecured
import changeDirectory
import base93Characterconversion
import keepOnly10OfTypeFilesInFolder



def writeToSqlite(frame,table_name, DatabaseName, DatabaseNameBACKUP):

    #frame here is a pandas dataframe

    # DatabaseName="AutoFormFiller.db"

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
        
        ItemValue = StringFrame

        GetWriteDBTableSecured.WriteTableSecuredIten(ItemName=ItemName,ItemValue=ItemValue)

    else:
        WriteTableLocaion(frame = frame, databaseName=DatabaseName, tableNameUsed=TableNameUsed, DatabaseNameBACKUP= DatabaseNameBACKUP)

        # DatabaseNameBackup = GetDatePartName(DatabaseNameInput= DatabaseName)

        # WriteTableLocaion(frame = frame, databaseName= DatabaseNameBackup, tableNameUsed=TableNameUsed)






def WriteTableLocaion(frame, databaseName, tableNameUsed, DatabaseNameBACKUP):
    changeDirectory.ChangeTokey()

    conn = sqlite3.connect(databaseName)

    frame.to_sql(tableNameUsed, conn, if_exists="replace")

    FolderToChange= 'UserDatabaseBackups'

    BackupFolderLocation0 = changeDirectory.ChangeStartupDirectory(Folder=FolderToChange)

    BackupFolderLocation = BackupFolderLocation0 + '\\'

    # DatabaseNameBACKUP =  GetDatePartName(DatabaseNameInput= databaseName)

    conn = sqlite3.connect(DatabaseNameBACKUP)

    frame.to_sql(tableNameUsed, conn, if_exists="replace")

    Location = BackupFolderLocation

    extension = 'db'

    keepOnly10OfTypeFilesInFolder.DeleteTheFirstOfTenTypeFiles(Location, extension)



def GetDatePartName(DatabaseNameInput):
    dateNow = datetime.fromtimestamp(time.time())

    [dategotten0, timegotten0] = str(dateNow).split(' ')

    dategotten =dategotten0.replace('-','')

    timegotten1 = timegotten0.replace(':','').replace('.','')

    timegotten = base93Characterconversion.base93Characterconversion(TimeBased=False, OtherNumer=timegotten1, OnlyUpper=True)

    
    DateName = str(dategotten)+'_' +  str(timegotten)

    DatabaseNameInputName = DatabaseNameInput.split('.')[0]

    DatabaseNameInputExtension = '.' + DatabaseNameInput.split('.')[-1]

    DatabaseNameOutput = str(DatabaseNameInputName)+ '_'+ DateName + DatabaseNameInputExtension

    return DatabaseNameOutput




# DatabaseNameInput = 'AutoFormFiller.db'
# print(   GetDatePartName(DatabaseNameInput) )