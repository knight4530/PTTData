


from PTTData import Load as PTT

print(' get all ptt table name ' )
PTT_data_list = PTT.LoadDataList()
print(PTT_data_list[:5])

print('load data')
data = PTT.LoadData(table = 'job',date = '2018-12-10',select = 'title')
print(data[:5])

