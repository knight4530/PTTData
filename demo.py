


from PTTData import Load as PTT
import datetime

date = str( datetime.datetime.now().date() - datetime.timedelta(30) )

PTT_data_list = PTT.LoadDataList()
print(PTT_data_list[:5])

data = PTT.LoadData(table = 'job',date = date,select = 'title',article_type = '台北')
print(data[:5])

data = PTT.LoadData(table = 'AdvEduUK',date = date,select = 'article',article_type = '徵求')
print(data[:5])


