# library
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import math
import statistics


# Case_01_大樂透的頭獎，你必須從49個挑選出 6 個號碼，且這六個號碼與頭獎的六個號碼一致，頭獎的機率是屬於哪一種分配？
print("超幾何分配(Hypergeometric Distribution)")
# 超幾何分配(Hypergeometric Distribution)描述了,由有限個物件中抽出n個物件，成功抽出指定種類的物件的個數（不歸還（without replacement))若隨機變量X 服從參數，則記為  H(n,K,N)，
# 𝑁 : 共有幾個物件, 𝑁 =0,1,…
# 𝐾 : 𝑁 個物件中，有 𝐾 個是你關心的物件類型個數, 𝐾 =0,1,2,…, 𝑁
# 𝑛 : K個物件，要抽出 𝑛 個物件, 𝑛 =0,1,…, 𝑁


# Case_02_運用範例的 python 程式碼，計算大樂透的中頭獎機率？
# 1.定義超幾何分配的基本資訊
N=49
K=6
n=6
r = n
# 超幾何分配的累積機率 (cumulative density function)，pmf 的累加
cumsum_probs = stats.hypergeom.pmf(r, N,K,n)
print("大樂透的中頭獎機率=",cumsum_probs)


# Case_03_你覺得電腦簽注的中獎機率，和人腦簽注相比，哪一個機率高？
print("電腦簽注的中獎機率，和人腦簽注相同")

# 參考資料
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.nbinom.html#scipy.stats.nbinom (負二項分配)
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.hypergeom.html(超幾何分配)