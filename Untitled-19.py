# 创建文件
f=open('test.txt','w')
# 生成50个随机数
import random
list_a=[]
for i in range(50):
        list_a.append(int(random.random()*100))
# 将50个随机数按从小到大排序
for n in range(50):
        for m in range(n+1,50):
                if list_a[n]>list_a[m]:
                        list_a[n],list_a[m]=list_a[m],list_a[n]
# 将列表写入txt文件内
for j in range(50):
        number=list_a[j]
        f.write(str(number)+"\n")
f.close()
# 将txt文件内的数据读取出来
list_b=[]
with open('test.txt','r')as f:
        for line in f:
                list_b.append(list(map(int,line.split(','))))
        print(list_b)
list_c=[]
for x in range(0,50):
        list_c.append(list_b[x][0])
print(list_c)
# 将50个数据反向排序
for n in range(50):
        for m in range(n+1,50):
                if list_c[n]<list_c[m]:
                        list_c[n],list_c[m]=list_c[m],list_c[n]
print(list_c)
# 换行
with open('test.txt','a')as f:
        f.write('\n')
        f.close()
# 将反序数据写入txt文件
with open('test.txt','a')as f:
        for j in range(50):
                number_=list_c[j]
                f.write(str(number_)+"\n")
f.close()