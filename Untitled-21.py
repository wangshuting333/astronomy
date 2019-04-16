import matplotlib
from pandas import read_csv
from matplotlib import pyplot as plt

# 导入数据 
df = read_csv('three55.csv')

# 提取数据
number=list(df['考号'])
name=list(df['姓名'])
date=list(df.iloc[:,5:21])
score=[]
for i in range(41):
    b=list(df.iloc[i,5:21])
    score.append(b)

# 为了便于图中显示中文
font={'family':'SimHei'}
matplotlib.rc('font',**font)

# 输出折线图
for j in range(41):
    list1=date
    list2=score[j]
    plt.plot(range(len(list1)),list2,'-')
    # 编辑横、纵坐标
    plt.xticks(range(len(list1)),list1)
    plt.ylim(0,100)
    # 设置折线图标题
    plt.title(number[j])
    # 设置图片名字并保存图片
    plt.savefig(name[j])
    plt.show()
