import sqlite3 

import changeDirectory
import GetKeyfileNameType
import RegularExpressionTextOrList
import GetWriteDBTableSecured

 
  
def create_table(Database,ColumnsList,TableName,TypeList=[]): 
    conn = sqlite3.connect(Database) 
    c = conn.cursor() 

    TableOptions = ['FontAndItsSize','FilesInDatabase','qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq','KEY_']


    TableNameUsed = ''
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


    if TypeList==[]:
        string=" ( id integer PRIMARY KEY,"
               
        for i in range(len(ColumnsList)):
        
            txt = ColumnsList[i]
            ColumnToAdd = RegularExpressionTextOrList.RegularExpressionTextOrList(txt)

            string=string + ColumnToAdd +" TEXT, "
            # print(string)
        string = string[:-2]
        string=string+")"

        # print(string)

        c.execute('CREATE TABLE IF NOT EXISTS '+ TableNameUsed + string) 
 
    else:
        string=" ( id integer PRIMARY KEY,"

        for i in range(len(ColumnsList)):
            # print(i)
            
            txt = ColumnsList[i]
            ColumnToAdd = RegularExpressionTextOrList.RegularExpressionTextOrList(txt)

            txt2 = TypeList[i]
            TypeListToAdd = RegularExpressionTextOrList.RegularExpressionTextOrList(txt2)

            string = string + ColumnToAdd +" "+ TypeListToAdd +", "

   
        string = string[:-2]
        string=string+")"

        # print('CREATE TABLE IF NOT EXISTS '+ TableNameUsed + string)

        c.execute('CREATE TABLE IF NOT EXISTS '+ TableNameUsed + string) 

        # print(ColumnsList)

        # print('executed program above')


        

  
def data_entry(Database,TableName,ColumnsList,ValuesList): 
    conn = sqlite3.connect(Database) 
    c = conn.cursor() 

    ColumnsList=list(ColumnsList)

    ValuesList=list(ValuesList)

    ColumnString=" ( "
    ValueLocationString = " ( "
    ValueLst = []
    for i in range(len(ColumnsList)):
    
        txt = ColumnsList[i]
        ColumnToAdd = RegularExpressionTextOrList.RegularExpressionTextOrList(txt)

        ValueLst.append(str(ValuesList[i]))

        ColumnString=ColumnString + ColumnToAdd +", "

        ValueLocationString=ValueLocationString+ ' ?' +", "

        # print(ColumnString)
        # print(ValueLocationString)

    ColumnString = ColumnString[:-2]
    ColumnString = ColumnString+")"

    ValueLocationString = ValueLocationString[:-2]
    ValueLocationString = ValueLocationString+")"


    TableOptions = ['FontAndItsSize','FilesInDatabase','qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq','KEY_']

    TableNameUsed = ''
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

    # print("INSERT INTO "+ TableNameUsed + " " + ColumnString + ' VALUES '+ ValueLocationString  , ValueLst)

    c.execute("INSERT INTO "+ TableNameUsed + " " + ColumnString + ' VALUES '+ ValueLocationString  , ValueLst) 
    
    conn.commit() 
  

def CreateTableAndInsertValues(Database,TableName,TypeList ,ColumnsList=[],ValuesList=[],Dictionary={}):

    changeDirectory.ChangeTokey()

    conn = sqlite3.connect(Database) 
    c = conn.cursor() 

    if Dictionary!={}:

        ColumnsList, ValuesList = zip(*Dictionary.items())

    create_table(Database=Database,ColumnsList=ColumnsList, TableName=TableName,TypeList=TypeList)
    data_entry(Database=Database,TableName=TableName,ColumnsList=ColumnsList, ValuesList=ValuesList)
    # print("Done database write")
    c.close() 
    conn.close() 


# Adapt this with the Write table itens for dictionary and List as inputs
def SetValues(TableName="qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq",ColumnsList=[],ValuesList=[],Dictionary={}):

    if TableName == 'qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq':

        if Dictionary!={}:

            InputDictionary = Dictionary
             
            GetWriteDBTableSecured.WriteTableSecuredDictionary(InputDictionary = InputDictionary)
             

        elif ColumnsList!=[]:

            ItemNameList= ColumnsList
            colValueList = ValuesList
            
            GetWriteDBTableSecured.WriteTableSecuredList(ItemNameList=ItemNameList,colValueList=colValueList)
        else:
            pass

    else:

        if Dictionary!={}:

            ColumnsList, ValuesList = zip(*Dictionary.items())


        elif ColumnsList!=[]:
            TypeList=[]
            TableName=TableName
            Database="AutoFormFiller.db"

            for i in range(len(ColumnsList)):
                TypeList.append("text")

            CreateTableAndInsertValues(Database=Database,TableName=TableName,ColumnsList=ColumnsList,ValuesList=ValuesList,TypeList=TypeList)

        else:
            pass



# Dictionary={'col1': 'val1', 'col2': 'val2', 'col3': 'val3', 'col4': 'val4', 'col5': 'val5'}

# ColumnsList=["col1","col2","col3","col4","col5"]
# ValuesList=["val1","val2","val3","val4","val5"]

# SetValues(ColumnsList=ColumnsList,ValuesList=ValuesList)


# # SetValues(Dictionary=Dictionary)