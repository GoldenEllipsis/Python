'''
BMI   Body Mass Index
国内标准 国际标准
体重kg，身高m
'''
weight = input("请输入体重：\n")
high = input("请输入身高：\n")
BMI = eval(weight)/pow(eval(high),2)
if BMI < 18.5:
    print("国际标准：偏瘦")
    print("国内标准：偏瘦")
elif BMI < 25:
    print("国际标准：正常")
    if BMI < 24:
        print("国内标准：正常")
    else:
        print("国内标准：偏胖")
elif BMI < 30:
    print("国际标准：偏胖")
    if BMI < 28:
        print("国内标准：偏胖")
    else:
        print("国内标准：肥胖")
else:
    print("国际标准：肥胖")
    print("国内标准：肥胖")
