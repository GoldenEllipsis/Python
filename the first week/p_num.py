'''
判断是否为回文数
算法：输入一个字符串，计算字符串长度，
取前半部字符串，反转字符串后再取前半部字符串
取到的两个字符串比较
'''
num = input("请输入一个整数:")

m = int(len(num)/2)

str1 = num[0:m]
num = num[::-1]
str2 = num[0:m]

if str1 == str2:
    print("是回文数")
else:
    print("不是回文数")
