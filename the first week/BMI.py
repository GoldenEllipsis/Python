'''
BMI   Body Mass Index
国内标准
	体重kg，身高m
国际标准：BMi 24改成25，28改成30
'''
weight = input("请输入体重：\n")
high = input("请输入身高：\n")
BMI = eval(weight)/pow(eval(high),2)
if BMI<18.5:
	print("偏瘦")
elif BMI>=18.5 and BMI<24:
	print("正常")
elif BMI>=24 and BMI<28: 
	print("偏胖")
elif BMI>=28:            
	print("肥胖")
