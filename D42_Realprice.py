# 載入所需要的套件
import pandas as pd
import numpy as np

import datetime
from datetime import timedelta

# 1-1_利用Pandas中的pd.read_csv()分別讀取A_lvr_land_A.csv、B_lvr_land_A.csv、E_lvr_land_A.csv、F_lvr_land_A.csv
dataA = pd.read_csv('A_lvr_land_A.csv', low_memory=False)
dataB = pd.read_csv('B_lvr_land_A.csv', low_memory=False)
dataE = pd.read_csv('E_lvr_land_A.csv', low_memory=False)
dataF = pd.read_csv('F_lvr_land_A.csv', low_memory=False)
# 1-2_刪除csv中第二列英文翻譯，The villages and towns urban district,transaction sign,land sector position building sector house number plate,land shifting total area square meter,....
dataA=dataA.drop([0])
dataB=dataB.drop([0])
dataE=dataE.drop([0])
dataF=dataF.drop([0])
# 1-3_生成city欄位其中以地區分類台北市Taipei(A_lvr_land_A.csv)、新北市New_Taipei(F_lvr_land_A.csv)、台中市Taichung(B_lvr_land_A.csv)、高雄市Kaohsiung(E_lvr_land_A.csv)
dataA["city"]="Taipei"
dataB["city"]="Taichung"
dataE["city"]="Kaohsiung"
dataF["city"]="New_Taipei"
# 1-4_將以上四份資料運用pd.concat()串接
Data=pd.concat([dataA,dataB,dataE,dataF], ignore_index=True)


# 2_條件設定: 因為我是想買來住的房子，所以幫忙刪除住宿用途以外的資料，並且限制 1. 交易年月日，限制在109年 2. 建物現況格局-房，1~5間 3. 建物現況格局-廳，1~2廳
# 以下columns_mapping、analysis_columns、columns_type提供給資料科學家配合使用 1. 利用.rename()並配合以下columns_mapping，將原中文欄位名稱改為英文方便之後分析 2. 取出主要用途(main_use)為'住家用'以及都市土地使用分區(use_zoning)為'住'的資料並針對以下欄位analysis_columns做分析並去除na值 (提示:先取完之後再.dropna()) 3. 觀察欄位資料型態，並利用.astype()搭配以下提供的columns_type做欄位型態轉換 4. 做資料切片將
# 新增欄位交易年月日(tx_dt_year)，從交易年月日(tx_dt)萃取出年份
# 1.交易年月日(tx_dt_year)，限制在109年
# 2.建物現況格局-房(room_number)，限制在1到5間
# 3.建物現況格局-廳(hall_number)，限制在1到2廳
# 4.最後運用.reset_index()重新定義索引

columns_mapping = {
    '鄉鎮市區':'towns',
'交易標的':'transaction_sign',
'土地區段位置建物區段門牌':'house_number',
'土地移轉總面積平方公尺':'land_area_square_meter', 
'都市土地使用分區':'use_zoning', 
'非都市土地使用分區':'land_use_district',
'非都市土地使用編定':'land_use',
'交易年月日':'tx_dt', 
'交易筆棟數':'transaction_pen_number', 
'移轉層次':'shifting_level', 
'總樓層數':'total_floor_number', 
'建物型態':'building_state', 
'主要用途':'main_use', 
'主要建材':'main_materials',
'建築完成年月':'complete_date', 
'建物移轉總面積平方公尺':'building_area_square_meter', 
'建物現況格局-房':'room_number', 
'建物現況格局-廳':'hall_number', 
'建物現況格局-衛':'health_number', 
'建物現況格局-隔間':'compartmented_number', 
'有無管理組織':'manages', 
'總價元':'total_price', 
'單價元平方公尺':'unit_price', 
'車位類別':'berth_category', 
'車位移轉總面積(平方公尺)':'berth_area_square_meter',
'車位總價元':'berth_price', 
'備註':'note', 
'編號':'serial_number', 
'主建物面積':'main_building_area', 
'附屬建物面積':'auxiliary_building_area', 
'陽台面積':'balcony_area', 
'電梯':'elevator'
                  }
analysis_columns = ['city','towns','main_use','use_zoning','total_price','building_area_square_meter',
                                     'main_building_area',
                                     'tx_dt','unit_price','room_number','hall_number','health_number']
columns_type = {'total_price': 'int','unit_price':'float','building_area_square_meter':'float',
                                      'main_building_area': 'float',
                                      'room_number': 'int','hall_number': 'int','health_number': 'int'}

# 2-1_利用.rename()並配合以下columns_mapping，將原中文欄位名稱改為英文方便之後分析
Data=Data.rename(mapper=columns_mapping,axis=1)
# 2-2_取出主要用途(main_use)為'住家用'以及都市土地使用分區(use_zoning)為'住'的資料並針對以下欄位analysis_columns做分析並去除na值 (提示:先取完之後再.dropna())
mask1=Data["use_zoning"]=="住"
mask2=Data["main_use"]=="住家用"
Data1=Data[(mask1 & mask2)]
Data1=Data1.dropna(subset=analysis_columns)
# 2-3_觀察欄位資料型態，並利用.astype()搭配以下提供的columns_type做欄位型態轉換
Data1=Data1.astype(columns_type)
# print(Data1.info())
# 2-4_做資料切片將新增欄位交易年月日(tx_dt_year)，從交易年月日(tx_dt)萃取出年份
# 2-4-1_交易年月日(tx_dt_year)，限制在109年
# 2-4-2_建物現況格局-房(room_number)，限制在1到5間
# 2-4-3_建物現況格局-廳(hall_number)，限制在1到2廳
# 2-4-4_最後運用.reset_index()重新定義索引
Data1["tx_dt_year"]=Data1["tx_dt"].apply(lambda x: x[0:3:])
mask3=Data1["tx_dt_year"]=="109"
mask4=(Data1["room_number"]>=1) & (Data1["room_number"]<=5)
mask5=(Data1["hall_number"]>=1) & (Data1["hall_number"]<=2)
Data2= Data1[(mask3) & (mask4) & (mask5)]
Data2=Data2.reset_index()


# 3_建立自定義特徵加入分析
# 以台灣來說大家都是以坪為單位計算使用面積，應該是不會問說你家有幾平方公尺吧?，但是偏偏資料中沒有以坪為單位計算，所以接下來請各位幫忙產生新的欄位以坪為單位計算面積，轉換公式我也幫你找好了，在下面的定義。
# 定義 : 1平方公尺相當於0.3025坪
# 建立新特徵 
# 3-1_建物移轉總面積坪(building_area_square_feet) : 建物移轉總面積平方公尺*0.3025 
# 3-2_主建物面積坪(main_building_area_square_feet) : 主建物面積*0.3025 
# 3-3_單價元坪(unit_price_square_feet) : 單價元平方公尺/0.3025
Data2["building_area_square_feet"]=Data2["building_area_square_meter"]*0.3025
Data2["main_building_area_square_feet"]=Data2["main_building_area"]*0.3025
Data2["unit_price_square_feet"]=Data2["unit_price"]/0.3025
# print(Data2.describe())
# 可以利用.describe()做一下資料觀察，是否有奇怪的資料? 如果有請將資料移除，並說明為什麼移除此資料?
mask6=(Data2["main_building_area"]!= 0) & (Data2["unit_price"]!= 0)
Data3=Data2[(mask6)]
print("可能因為有些欄位數值為0卻並非nan，所以dropna的時候沒有被排出掉\n",Data3.describe())


# 4_找出台北市時價登入總價高度相關的變數.阿宏我是台北人他想找出影響台北市總價、單價元坪的因子
# 4-1_資料切片切出city欄位為台北市的資料，並找出時價登入總價(total_price)高度相關的變數
# 4-2_資料切片切出city欄位為台北市的資料，找出單價元坪(unit_price_square_feet)高度相關的變數
mask7=Data3["city"]=="Taipei"
loc_taipei=Data3[mask7]
corr_taipei=loc_taipei.corr()
corr_with_total_price=corr_taipei["total_price"].sort_values(ascending=False)
corr_with_unit_price_square_feet=corr_taipei["unit_price_square_feet"].sort_values(ascending=False)
# print("total_price= {0}".format(corr_with_total_price.index[1]))
# print("unit_price_square_feet = {0}".format(corr_with_unit_price_square_feet.index[0]))


# 5_資料視覺化並解釋
# 我想要以視覺化的方式來看房價資料，並且請各位資料科學家解釋圖表給阿宏我知道 
# 5-1_以城市(city)為x軸，以單價元坪(unit_price_square_feet)為y軸畫出boxplot，並找出單價元坪(unit_price_square_feet)中位數最高的地區
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
fig,axs=plt.subplots(1,1,figsize=(10,5))
ax2=sns.boxplot(data=Data3,x="city",y="unit_price_square_feet",ax=axs)
plt.show()
groupby_city=Data3.groupby("city")
get_median=groupby_city.median()
max_value=get_median["unit_price_square_feet"].max()
max_city=get_median["unit_price_square_feet"][get_median["unit_price_square_feet"]==max_value].index[0]
print("unit_price_square_feet 中位數最高的是 {0},數值為 {1}".format(max_city,max_value))

# 5-2_進一步對台北市的資料做圖，以建物現況格局-房(room_number)為x軸，以總價元(total_price)為y軸畫出boxplot，並找出總價元(total_price)中位數最高的房間數。hint:資料切片找出city欄位為台北市的資料，再進一步畫圖 
fig,axs=plt.subplots(1,1,figsize=(10,5))
taipei_data=Data3[Data3["city"]=="Taipei"]
sns.boxplot(data=taipei_data,x="room_number",y="total_price")
plt.show()
groupby_room_number=taipei_data.groupby("room_number").median()
max_value=groupby_room_number["total_price"].max()
index=(groupby_room_number[groupby_room_number["total_price"]==max_value]).index[0]
print("total_price中位數最高的對應房間數為 {0}".format(index))

# 5-3_對台北市的資料做圖，先將地區(twons)做編碼在進行，再以地區(twon)為x軸，以單價元坪(unit_price_square_feet)為y軸畫出boxplot，並找出單價元坪(unit_price_square_feet)中位數最高的地區。hint:運用LabelEncoder()對地區(twons)做編碼，運用.inverse_transform()反查編碼的地區
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
taipei_data=Data3[Data3["city"]=="Taipei"]
le.fit(taipei_data["towns"])
taipei_data.loc[:,["towns"]]=le.transform(taipei_data["towns"])
fig2,axs2=plt.subplots(1,1,figsize=(10,5))
sns.boxplot(data=taipei_data,x="towns",y="unit_price_square_feet",ax=axs2)
plt.show()
groupby_towns=taipei_data.groupby("towns").median()
max_value=groupby_towns["unit_price_square_feet"].max()
index=(groupby_towns[groupby_towns["unit_price_square_feet"]==max_value]).index[0]
index2=le.inverse_transform([index])
print("unit_price_square_feet 中位數最高的對應地區為 {0}".format(index2))