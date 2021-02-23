# library
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import math
import statistics

# 機率 0.5
p = 0.5  
# 重複實驗100次
n = 100
# 可以出現的範圍為 0,1,2,...,5-->101種可能出現的結果  
r = np.arange(0,101) 
probs = stats.binom.pmf(r, n, p)
plt.bar(r, probs)
plt.ylabel('P(X=x)')
plt.xlabel('x')
plt.title('binomial(n=100,p=0.5)')
plt.show()