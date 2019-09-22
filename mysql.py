import pymysql
import time
import pandas as pd

pd.set_option('display.max_columns',1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth',1000)

def timer(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        x = func(*args,**kwargs)
        end_time = time.time()
        print('查询时间:',end_time-start_time)
        return x
    return wrapper


db = pymysql.connect(host='localhost',

                     user='root',
                     password='123456',
                     port=3306
                     )

cursor = db.cursor()
cursor.execute('SELECT VERSION()')
version = cursor.fetchone()
print('version:',version[0])
print(type(version))
sql_cx_select = 'select count(*) from CX.cx_hb_fin  where source_time = %s '
sql_pashazera_select = 'select rank,name from bili.bili_rank_user_info order by rank'

@timer
def qeuryfromt(sql,*args):

    try:
        cursor.execute(sql, args)
        print('count:', cursor.rowcount)
        result = cursor.fetchall()
        return result

    except:
        print('error')

data = qeuryfromt(sql_pashazera_select)


df = pd.read_sql(sql_pashazera_select,con=db)
print(df)





