
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
    def load(table ,date, select, article_type = ''):
        if isinstance(select,list):
            select2 = "`,`".join(select)
        else:
            select = [select]
            select2 = "','".join(select)
            
        if isinstance(article_type,list):
            article_type2 = "','".join(article_type)
        else:
            article_type = [article_type]
            article_type2 = "','".join(article_type)
        #article_type2 = article_type
        #select2 = select
        
        sql = "select `{}` from `{}` WHERE `date` >= '{}'".format(select2,table,date)
        if article_type2 != '': 
            sql = "{} AND `article_type` IN ('{}') ".format(sql,article_type2)
        tem = execute_sql2(sql)
        data = pd.DataFrame(list(tem))
        if len(data) > 0:
            data.columns = select
        return data

    #-----------------------------------------------
    if isinstance(select,str) or isinstance(select,list):
        data = load(table ,date, select, article_type)
        return data

