#1.將下列清單(list1)，轉成維度為(5X6)的array，順序按列填充。(hint:order="F")
mport numpy as np
array1 = np.array(range(30))
data=np.reshape(array1,(5,6),order="F")
print(data)
#2.呈上題的array，找出被6除餘1的數的索引
import numpy as np
array1 = np.array(range(30))
data=np.reshape(array1,(5,6),order="F")
index=np.where(data % 6==1)
print(index)
