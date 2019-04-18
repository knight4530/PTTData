
import pymysql
import pandas as pd
import numpy as np

HOST = '103.29.68.107'
USER = 'guest'
PASSWORD = '123'
DATABASE = 'PTTData'

def LoadDataList():
    def execute_sql2(sql):
        conn = ( pymysql.connect(host = HOST,
                         port = 3306,
                         user = USER,
                         password = PASSWORD,
                         database = DATABASE,  
                         charset="utf8") )  
                                 
        cursor = conn.cursor()    
        try:   
            cursor.execute(sql)
            data = cursor.fetchall()
            conn.close()
            return data
        except:
            conn.close()
            return ''    
    tem = execute_sql2('show tables')
    value = np.concatenate(tem, axis=0)
    return value

def LoadData(table, select, date, article_type = ''):
    def execute_sql2(sql):
        
        conn = ( pymysql.connect(host = HOST,
                         port = 3306,
                         user = USER,
                         password = PASSWORD,
                         database = DATABASE,  
                         charset="utf8") )  
                                 
        cursor = conn.cursor()    
        try:   
            cursor.execute(sql)
            data = cursor.fetchall()
            conn.close()
            return data
        except:
            conn.close()
            return ''
    def load(table ,date, select, article_type):
        if isinstance(select,list):
            select2 = "`,`".join(select)
            
        sql = "select `{}` from {} WHERE `date` >= '{}'".format(select2,table,date)
        if article_type != '': sql = "{} AND `article_type` = '{}' ".format(sql,article_type)
        tem = execute_sql2(sql)
        data = pd.DataFrame(list(tem))
        if len(data) > 0:
            data.columns = select
        return data
    
    #-----------------------------------------------
    if isinstance(select,str) or isinstance(select,list):
        data = load(table ,date, select, article_type)
        return data

