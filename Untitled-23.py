# -*- coding: utf-8 -*-
import numpy as np
from scipy.optimize import leastsq
import pylab as pl


def func(x, p):
    """
    数据拟合所用的函数: A*sin(2*pi*k*x + theta)+a
    """
    A, k, theta,a = p
    return A*np.sin(2*np.pi*k*x+theta)+a

def residuals(p, y, x):
    """
    实验数据x, y和拟合函数之间的差，p为拟合需要找到的系数
    """
    return y - func(x, p)

x = np.array([0,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48])
y=np.array([48.5,52.6,27.0,-13.8,-38.0,-29.5,-4.9,25.2,48.6,53.2,26.7,-16.1,-39.4,-29.9,-3.5,25.2,48.5])   
x0=np.linspace(0,48*np.pi/180,100)
# y0=np.linspace(-55,55,100)
p0 = [40,2, 0,2] # 第一次猜测的函数拟合参数

# 调用leastsq进行数据拟合
# residuals为计算误差的函数
# p0为拟合参数的初始值
# args为需要拟合的实验数据
plsq = leastsq(residuals, p0, args=(y, x*np.pi/180))

print("拟合参数",plsq[0]) # 实验数据拟合后的参数
pl.rcParams['font.family'] = ['SimHei']
pl.rcParams['font.sans-serif'] = ['SimHei'] # -serif字体）
pl.rcParams['axes.unicode_minus'] = False   # 步骤二步骤一（替换sans（解决坐标轴负数的负号显示问题）
pl.plot((x/360)*2*np.pi, y, label=u"真实数据")
pl.plot(x0, func(x0, plsq[0]), label=u"拟合数据")
pl.legend()

pl.xlabel('转动角度/弧度')
pl.ylabel('输出电压/mV')

pl.show()




