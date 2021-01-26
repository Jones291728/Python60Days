import numpy as np
#1.將下兩列array存成npz檔
array1 = np.array(range(30))
array2 = np.array([2,3,5])
np.savez("merge2_array.npz",array1=array1,array2=array2)
file01=np.load("merge2_array.npz")
print("將兩列array存成npz檔",file01.files)
print("=================================================")
multi_array=np.load("multi_array.npz")
array3,array4,array5=multi_array["array1"],multi_array["array2"],multi_array["array3"]
array6=np.genfromtxt("names.txt",dtype=None,encoding="utf-8")
array7=np.load("one_array.npy")
array8=np.genfromtxt("test.csv", delimiter=",")
array9=np.genfromtxt("test.gz", delimiter=",")
array10=np.load("test.npy")
array11=np.genfromtxt("test.out", delimiter=",")

def trans(s):
    if s == b'Yes':
        return 1
    else:
        return 0
def conversion(x):
    return float(x.strip(b"%"))/100
array12=np.genfromtxt("transform.txt", delimiter=',', converters={2:trans, 3:conversion})
np.savez("merge12_array.npz",array1=array1,array2=array2,array3=array3,array4=array4,array5=array5,array6=array6,array7=array7,array8=array8,array9=array9,array10=array10,array11=array11,array12=array12)
file02=np.load("merge12_array.npz")
print("讀取剛剛的 npz 檔，加入下列 array 一起存成新的 npz 檔",file02.files)