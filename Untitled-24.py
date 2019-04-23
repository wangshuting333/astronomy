# -*- coding: utf-8 -*-
import numpy as np
from scipy.optimize import curve_fit
import pylab as pl

def func(x,A,theta,D):
    """
    数据拟合所用的函数: A*sin(np.pi*x/6 + theta)
    """
    return A*np.sin(np.pi*x/6+theta)+D

x=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
y_max= np.array([17, 19, 21, 28, 33, 38, 37, 37, 31, 23, 19, 18])
y_min=np.array([-62, -59, -56, -46, -32, -18, -9, -13, -25, -46, -52, -58])

pl.rcParams['font.family'] = ['SimHei']
pl.rcParams['font.sans-serif'] = ['SimHei'] # 步骤一（替换sans-serif字体）
pl.rcParams['axes.unicode_minus'] = False   # 步骤二（解决坐标轴负数的负号显示问题）

# 非线性最小二乘法拟合
x1=np.linspace(0,12,40)

popt1,pcov1=curve_fit(func, x, y_max)
a1=popt1[0]
b1=popt1[1]
c1=popt1[2]
pl.plot(x, y_max,label=u"最高温度真实数据")
pl.plot(x1,func(x1,a1,b1,c1),label=u"最高温度拟合数据",)
print(popt1, pcov1)

popt2,pcov2=curve_fit(func, x, y_min)
a2=popt2[0]
b2=popt2[1]
c2=popt2[2]
pl.plot(x, y_min,label=u"最低温度真实数据")
pl.plot(x1,func(x1,a2,b2,c2),label=u"最低温度拟合数据")
print(popt2, pcov2)

pl.legend()
pl.xlabel('月份')
pl.ylabel('温度')

pl.show()






