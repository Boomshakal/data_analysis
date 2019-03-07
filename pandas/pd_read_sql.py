import pandas as pd
import pymssql

sql='select * from mm_item'
con=pymssql.connect(host='192.168.0.126',user='sa',password='2018@Ikahe',database='X1_CORE_PROD',charset="utf8")

data_sql=pd.read_sql(sql,con)

print(type(data_sql),data_sql)