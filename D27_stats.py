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
r = 50
probs = stats.binom.pmf(r, n, p)
print(probs)
