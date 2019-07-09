#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import random
def findmax(self,p):
    max=self[0]
    for i in range(1,p):
        if self[i]>max:
            max=self[i]
    return max
arraylenth=1000
x=range(0,arraylenth)#x坐标
y=[0]*arraylenth#y坐标
for k in range(1,10000):
    z=[]#比较值序列

    for i in range(1,arraylenth):
        z.append(random.randint(1,65535))
    #生成随机数
    acturemax=findmax(z,arraylenth-1)
    for i in range(1,arraylenth-2):
        p=findmax(z,i)
        for j in range(i+1,arraylenth-1):
            if z[j]>p:
                if z[j]==acturemax:
                    y[i]+=1
                break
print('求解了10000次，找到了最优解近似值为%f'% (findmax(y,arraylenth)/1000))
plt.plot(x,y)
plt.show()



