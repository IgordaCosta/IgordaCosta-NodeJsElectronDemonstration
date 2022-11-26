import readSqlDatabase



datafillName = 'test$%78&*&b$%78&*&space2'



# table_name = "KEY_"+datafillName

# table_name = 'KEY_itemspaced1'


table_name0 = 'test%78&*&b%78&*&space2'

table_name = 'KEY_' +table_name0


dataframegotten, dataframeRetieved = readSqlDatabase.readSqlDatabase(table_name=table_name)


print(dataframegotten)


# print(type(dataframegotten))


# print(len(dataframegotten))

# print(dataframegotten['[85, 720]'])


# print(dataframegotten['[1623, 815]'])

# print(dataframegotten['index'])