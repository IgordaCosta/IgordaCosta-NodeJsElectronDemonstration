import pandas

import writeToSqlite






data = {'index': ['0'],
         '[95, 770]': ['a$%3&*&space21'],
          '[1423, 615]': ['b$%3&*&space22']}
 
# Create the pandas DataFrame
frame = pandas.DataFrame(data=data)

print(frame)


# 'test$%78&*&b$%78&*&space2'

# $


table_name0 = 'test%78&*&b%78&*&space2'

table_name = 'KEY_' +table_name0


writeToSqlite.writeToSqlite(frame=frame,table_name=table_name)