import pandas as pd
import pymssql
import matplotlib.pyplot as plt

from  pyecharts import  Map

sql='SELECT [local],COUNT([local]) count FROM mm_customer_service GROUP BY [local]'
con=pymssql.connect(host='*****',user='sa',password='*******',database='***',charset="utf8")

data_sql=pd.read_sql(sql,con)
x=data_sql['local'].values.tolist()
y=data_sql['count'].values.tolist()
#print(x,y)
map = Map("分布省份", width=1200, height=600,background_color='#404a59')
map.add(
   '',
   x,
   y,
   maptype='china',
   is_visualmap=True,
   symbol_size=10,
   visual_text_color='#fff'
)

map.render('全国个点.html')