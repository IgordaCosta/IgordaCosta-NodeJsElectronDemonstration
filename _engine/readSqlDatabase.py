from sqlalchemy import create_engine
import pandas

import GetKeyfileNameType
import GetWriteDBTableSecured
import PandasDfIntoSecureDb
import changeDirectory



#this does not apply to the secured database
def readSqlDatabase(table_name,columns=None):

    pandas.set_option("display.max_colwidth", None)


    TableName = table_name

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

        ItemName = 'PdFrame'

        TableFound = False
        df2 = None
        try:
            StringFrame = GetWriteDBTableSecured.GetTableSingleItensSecuredData(ItemName=ItemName)
            TableFound = True
            
        except:
            pass

        if TableFound:
            StringDataframe = StringFrame

            df2 = PandasDfIntoSecureDb.SringDataframeToDaframe(StringDataframe=StringDataframe)


        return df2,TableFound


    else:

        changeDirectory.ChangeTokey()


        DatabaseName="AutoFormFiller.db"
        conn = create_engine('sqlite:///'+ DatabaseName)
        try:
            df2=pandas.read_sql_table(TableNameUsed, conn, columns=columns)


            # df['range'] = df['range'].str.replace(',','-')

            TableFound=True
        except ValueError:
            df2=None
            TableFound=False

        try:
            spaceReplaceDataUserImput = '$%78&*&'
            df2['Job Name'] = df2['Job Name'].str.replace(spaceReplaceDataUserImput,' ')

        except:
            pass


        return df2,TableFound




