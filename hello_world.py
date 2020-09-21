# a="ahelog"
# t=("a","4","3")
# q=["a","4","l"]
# s={"name":"花花","sex":"女"}
# print("a"in t)
# #如果有100元吃包子，1000元买车子，有30000元买房子，没有洗洗睡吧
# money = 40000
# if(money < 100):
#     print("洗洗睡")
# elif(money < 1000):
#     print("买包子")
# elif(money < 30000):
#     print("买车子")
# else:
#     print("买房子")
#
# for i in [4,5,6,7,8]:
#     print(i)
#     print("写十遍")
# for i in range(5):
#     print("写十遍")
#     for i in range(5):
#     print("写十遍")
#
# print(list(range(1,10)))
# print(list(range(1,10,2)))
# print(list(range(10,1,-1)))
# print(list(range(10,0,-1)))
# print(tuple(range(1,10,2)))
# print(list(range(1,10)))
# print(list(range(1,10,2)))
# print(list(range(10,1,-1)))
# print(list(range(10,0,-1)))
# print(tuple(range(1,10,2)))

# i = 1
# while (i<10):
#     print(i)
#     i+=1
# i = 1
# while (i<10):
#     print(i)
#     i+=4
# for i in range (5, 20):
#     if i in [6,7,8,9]:
#         continue
#     print(i
def div (a,b):
    if b ==0:
       print("被除数不能为0")
    else:
        print (a/b)
# div (80,20)
# div (5,2)
# def cc(a,b):
#     w=a+b
#     return w
# print(cc(1,5))
# def select_data(sql):
# #     res = "查询结果"
# #     return res
# result = select_data("")
# # print (result)
# def s(a,b=10):
#    return a+b
# print (s(1))
# def s(a,b=10):
#     return a+b
# print (s(5))
# def ar(*a):
#     print(a)
# ar(1,2,3,4,5)
# def ar(*a,**b):
#     print(a)
#     print(b)
# ar(1,2,3,4,5,a=10,b=20,c=30)

# a = "ddf"
# print(id(a))
# i = input("请输入一个数据")
# print(i)
# i = input("hello")
# print(i)

# print(type(a))
# print(type("sdf"))
#
# c = 10
# def aa():
#     global c
#     c = 20
# a="1234567890"
# b="456"
# print(a[0])第一个
# print(a[2:6])
# print(a[-2:])
# print(a[-4:])
# a = "  dfhdjfdh  "
#
# print (a.lstrip())
# a = "xx,dd，cc,xx"
# # print(a.split(','))
# a = a.replace("，",",")
# print(a.split(',')
#     九九乘法表
# for i in range(1,10):
#     for j in range (1,i+1):
#         print ("{} x {} ={}".format(j,i,i*j),end='\t')
#     print()
# a = 30
# b = 5
# if b == 0:
#     print("被除数不能为0")
# else:
#   print(a/b)
#
import random
def phone():
    hao_duan_list = ["131","130","135","181","182","183","188","187","171"]
    hao_duan = random.choices(hao_duan_list)
    i= random.choices("0123456789",k=8)
    ba_wei = "".join(i)
    return hao_duan + ba_wei
print(phone())

