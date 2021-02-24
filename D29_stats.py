import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# Case_01_計算標準常態分配，小於1的機率有多大
loc=0
scale=1
probs=stats.norm.cdf(1,loc,scale)
print("標準常態分佈，x<1的機率為：=",probs)


# Case_02_計算標準常態分配，大於1，小於 -1 的機率有多大?
loc=0
scale=1
probs01=stats.norm.cdf(1,loc,scale)
probs02=stats.norm.cdf(-1,loc,scale)
print("標準常態分佈，x>1 & x <-1的機率為：",1-(probs01-probs02))


# Case_03_X~N(2,4),x 服從常態分配，平均數為2,變異數為 4，計算 X小於 6 的機率有多大?
# 一般常態轉成標準常態分配
SD=4**0.5
z=((6-2)/SD)
loc=0
scale=1
probs=stats.norm.cdf(z,loc,scale)
print("標準常態分佈，x<6的機率為：=",probs)


# 參考資料
# 常態分佈(高斯分佈)_normal distribution(Gaussian distribution)以Z~N(0,1)表示,是以0為期望值,1為標準差之
# http://www.cust.edu.tw/mathmet/stat/z-dist.pdf(常態分配表)
