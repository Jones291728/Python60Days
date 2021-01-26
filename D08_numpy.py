import numpy as np
name = ['小明','小華','小菁','小美','小張','John','Mark','Tom']
sex = ['boy','boy','girl','girl','boy','boy','boy','boy']
weight = [67.5,75.3,50.1,45.5,80.8,90.4,78.4,70.7]
rank = [8,1,5,4,7,6,2,3]
myopia = [True,True,False,False,True,True,False,False]
data=np.zeros(8,dtype={"names":("name","sex","weight","rank","myopia"),
                        "formats":("U10","U5","f8","i4","bool")})
data["name"]=name
data["sex"]=sex
data["weight"]=weight
data["rank"]=rank
data["myopia"]=myopia

print("印出Structured Array:\n",data)
print("八位體重平均:",np.average(weight))
boyweight=data[data["sex"] == "boy"]["weight"]
print("男生體重平均:",np.average(boyweight))
girlweight=data[data["sex"] == "girl"]["weight"]
print("女生體重平均:",np.average(girlweight))
