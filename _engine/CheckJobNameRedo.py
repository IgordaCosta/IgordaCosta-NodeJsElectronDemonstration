# import sys
import re

import readSqlDatabase
import getTableData
import createSqliteTableFromList
# import dropSqlTable
import PrintTexListSerial

def CheckJobNameRedo(datafillName):

    FilesInDatabaseLocation='FilesInDatabase'
    columnsFileinDatabase=['Job Name', 'File KEY', 'File Saved Location']

    datafillName0=datafillName.split()
    datafillName1=" ".join(datafillName0)
    
    ListToPrint = []

    
    # ''.join([i for i in contentjoined if i in aminoacids])

    datafillName2 = re.sub("[^A-Za-z0-9\s]","",datafillName1)


    if datafillName2 == '':
        # print(True)

        ListToPrint.append(True)


    else:

        spaceReplaceDataUserImput = '$%78&*&'

        # print(' '.join(checkstring.split(ImportLibrary)))

        # datafillName = datafillName2.replace(' ',spaceReplaceDataUserImput)

        # datafillName =' '.join(datafillName.split(spaceReplaceDataUserImput))

        datafillName = spaceReplaceDataUserImput.join(datafillName.split(' '))

        
        

        FilesInDatabase , FilesInDatabaseExists = readSqlDatabase.readSqlDatabase(table_name=FilesInDatabaseLocation,columns=columnsFileinDatabase)

        # print('FilesInDatabaseExists:',FilesInDatabaseExists)

        if FilesInDatabaseExists==True:
            
            if datafillName in list(FilesInDatabase[columnsFileinDatabase[0]]):
                
                # print(True)

                ListToPrint.append(True)
            else:
                Dictionary=getTableData.GetTableData()
                Dictionary["datafillName"]=datafillName

                try:
                    del Dictionary['id']
                except:
                    pass

                # dropSqlTable.DropTable()

                createSqliteTableFromList.SetValues(Dictionary=Dictionary)

                # print(False)

                ListToPrint.append(False)

        if FilesInDatabaseExists==False:

            Dictionary=getTableData.GetTableData()
            Dictionary["datafillName"]=datafillName

            try:
                del Dictionary['id']
            except:
                pass

            # dropSqlTable.DropTable()

            createSqliteTableFromList.SetValues(Dictionary=Dictionary)

            # print(False)

            ListToPrint.append(False)


    PrintTexListSerial.PrintTexListSerial(ListToPrint=ListToPrint)

                


    
    
dataName='datafillName'


# datafillName = sys.argv[1]

datafillName=getTableData.GetDataFromDatabase(dataName=dataName)




CheckJobNameRedo(datafillName=datafillName)