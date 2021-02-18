from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np


# Case_01_"projection" 參數為“ortho"時，所得圖位地球儀截面
plt.figure(figsize=(8, 8))
m = Basemap(projection='ortho', 
            resolution=None, 
            lat_0=50, 
            lon_0=-100)
m.bluemarble(scale=0.5);
plt.title("Full Disk Orthographic Projection")
plt.show()


# Case_02_"projection" 參數為“lcc"時
fig = plt.figure(figsize=(8, 8))
m = Basemap(projection='lcc', resolution=None,
            lat_1=45.,lat_2=55,lat_0=50,lon_0=-107,
            width=1.2E7, height=0.9E7)
m.bluemarble(scale=0.5);
plt.title("Lambert Conformal Projection")
plt.show()


# Case_03_"projection" 參數為“mill"時
fig = plt.figure(figsize=(12,8))
m = Basemap(projection='mill',llcrnrlat=-90,urcrnrlat=90,\
            llcrnrlon=-180,urcrnrlon=180,resolution='f')
m.drawcoastlines()
m.drawcountries(linewidth=2)
#這會畫出國家，並使用線寬為2 的線條生成分界線。
m.drawstates(color="b")
#這會用藍色線條畫出州。
m.drawcounties(color="darkred")
#這會畫出城市
plt.title('Basemap Tutorial')
plt.show()

# 參考資料
# Basemap Matplotlib Toolkit(https://matplotlib.org/basemap/)

# 操作步驟(Basemap)
# 01_導入開發套件
# 02_新建地圖
# 03_畫圖
# 04_顯示结果
# 05_存储结果