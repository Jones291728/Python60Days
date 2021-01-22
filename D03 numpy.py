import numpy as np
from numpy.lib.function_base import _calculate_shapes
v0=20
v1=20000
print("談話聲(unit:dB) :",20*(np.log10(v1/v0)))

calculate_30=20*(np.power(10,(30/20)))
calculate_50=20*(np.power(10,(50/20)))
print("30分貝的聲壓(30_V1) :",(calculate_30))
print("50分貝的聲壓(50_V1) :",(calculate_50))
print("30分貝的聲壓是50分貝(ratio) :",(calculate_30/calculate_50))