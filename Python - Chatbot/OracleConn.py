import cx_Oracle
import os
dsn_tns = cx_Oracle.makedsn('10.192.12.67', '1521', service_name='MABEPRD1') # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
conn = cx_Oracle.connect(user=r'HRSDBA', password='Syshrs#bdoss87', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'

c = conn.cursor()

c.execute("DROP USER TestUser")

Query = open("CreateScript", "r",encoding="utf-8").readlines()
Query = map(lambda s: s.strip(), Query)

for row in Query:
    print(row)
    c.execute(row)

c.execute('GRANT ISOC_SEL TO TestUser')


#c.execute(Query)

#for row in c:
#    print (row) # this only shows the first two columns. To add an additional column you'll need to add , '-', row[2], etc.
#conn.close()

