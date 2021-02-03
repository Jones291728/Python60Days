import matplotlib.pyplot as plt
import numpy as np 
#1.畫出 cos 圖檔，並儲存
x=np.arange(-2*np.pi,2*np.pi,0.1) 
y = np.cos(x)
plt.plot(x,y,color='green') 
plt.title('cos-s') 
plt.legend(['cos']) 
plt.savefig("Trigon_cos.png",dpi=300,format="png")

#2.給定散點圖顏色(Scatter Plots)
n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
color=np.arctan2(X,Y)
plt.scatter(X,Y,c=color,s=50,marker="s",alpha=0.5)
plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)
plt.title("Scatter Polts")
plt.show()

#參考資料numpy.arctan2