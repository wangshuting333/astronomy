func=0
contactor={}
while(func!=4):
    print('''
    <<手机通讯录>>
    1.	新增联系人
    2.	删除联系人
    3.	显示联系人
    4.	退出
    ''')
    func=int(input())
    if func == 1:
        name=input("联系人姓名：")
        number=input("手机号码：")
        contactor[name]=number
        print("已储存该联系人！")
    if func == 2:
        name_=input("所需删除联系人姓名：")
        if name_ in contactor:
            del contactor[name_]
            print("已删除该联系人！")
        else:
            print("该联系人不存在！")
    if func == 3:
        name__=input("所需显示联系人姓名：")
        if name__ in contactor:
            print(name__,contactor[name__])
        else:
            print("该联系人不存在！")
    if func == 4:
        print("已退出！")
        break
