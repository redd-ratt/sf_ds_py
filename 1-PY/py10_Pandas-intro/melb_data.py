import pandas as pd
melb_data = pd.read_csv('data/melb_data.csv', sep=',')
melb_data['Car'] = melb_data['Car'].astype('int64')
melb_data['Bedroom'] = melb_data['Bedroom'].astype('int64')
melb_data['Bathroom'] = melb_data['Bathroom'].astype('int64')
melb_data['Propertycount'] = melb_data['Propertycount'].astype('int64')
melb_data['YearBuilt'] = melb_data['YearBuilt'].astype('int64')

#Условия можно комбинировать, используя операторы & (логическое И) и | (логическое ИЛИ). 
# Условия при этом заключаются в скобки.
melb_data[(melb_data['Rooms'] == 3) & (melb_data['Price'] < 300000)].shape[0]

melb_df = melb_data.copy()
melb_df = melb_df.drop(['index', 'Coordinates'], axis=1)
total_rooms = melb_df['Rooms'] + melb_df['Bedroom'] + melb_df['Bathroom']
melb_df['MeanRoomsSquare'] = melb_df['BuildingArea'] / total_rooms

diff_area = melb_df['BuildingArea'] - melb_df['Landsize']
sum_area = melb_df['BuildingArea'] + melb_df['Landsize']
melb_df['AreaRatio'] = diff_area/sum_area

melb_df['Date'] = pd.to_datetime(melb_df['Date'], dayfirst=True)
melb_df['MonthSale'] = melb_df['Date'].dt.month
delta_days = melb_df['Date'] - pd.to_datetime('2016-01-01') 
melb_df['AgeBuilding'] = melb_df['Date'].dt.year - melb_df['YearBuilt']
melb_df = melb_df.drop('YearBuilt', axis=1)
melb_df['WeekdaySale'] = melb_df['Date'].dt.dayofweek

weekend_count = melb_df[(melb_df['WeekdaySale']==5)| (melb_df['WeekdaySale']==6)]['WeekdaySale'].count()



def get_weekend(weekday):
    if weekday in (5, 6):
        return 1
    else:
        return 0
    
melb_df['Weekend']=melb_df['WeekdaySale'].apply(get_weekend)


melb_df[melb_df['Weekend']==1]['Price'].mean()


#
SellerG49 = melb_df['SellerG'].value_counts().nlargest(49).index
print(SellerG49)

melb_df['SellerG'] = melb_df['SellerG'].apply(lambda x: x if x in SellerG49 else 'other')

display(melb_df[melb_df['SellerG']=='Nelson']['Price'].min())
display(melb_df[melb_df['SellerG']=='other']['Price'].min())

#Давайте определим число уникальных категорий в каждом столбце нашей таблицы melb_df. 
# Для этого создадим вспомогательную таблицу unique_counts:
unique_list = []
# пробегаемся по именам столбцов в таблице
for col in melb_df.columns:
    # создаём кортеж (имя столбца, число уникальных значений)
    item = (col, melb_df[col].nunique(),melb_df[col].dtypes) 
    # добавляем кортеж в список
    unique_list.append(item) 
# создаём вспомогательную таблицу и сортируем её
unique_counts = pd.DataFrame(
    unique_list,
    columns=['Column_Name', 'Num_Unique', 'Type']
).sort_values(by='Num_Unique',  ignore_index=True)
# выводим её на экран
display(unique_counts)

cols_to_exclude = ['Date', 'Rooms', 'Bedroom', 'Bathroom', 'Car'] # список столбцов, которые мы не берём во внимание
max_unique_count = 150 # задаём максимальное число уникальных категорий
for col in melb_df.columns: # цикл по именам столбцов
    if melb_df[col].nunique() < max_unique_count and col not in cols_to_exclude: # проверяем условие
        melb_df[col] = melb_df[col].astype('category') 


Suburb119 = melb_df['Suburb'].value_counts().nlargest(119).index
melb_df['Suburb'] = melb_df['Suburb'].apply(lambda x: x if x in Suburb119 else 'other')
melb_df['Suburb'] = melb_df['Suburb'].astype('category') 
display(melb_df.info())
