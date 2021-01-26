import numpy as np
#1.運用array1計算反矩陣，乘上原矩陣，並觀察是否為單位矩陣?
array1=np.array([[10,8],[3,5]])
array2=np.linalg.inv(array1)
print("反矩陣:\n",array2)
print("觀察單位矩陣結果:\n",np.dot(array1,array2))
#2.運用array1計算特徵值、特徵向量?
w,v=np.linalg.eig(array1)
print("特徵值(eigenvalue)、特徵向量(eigenvector):\n",w,v)
#3.運用array1計算SVD
u,s,vh=np.linalg.svd(array1)
print("SVD計算結果:\n",u,s,vh)
