'''
BMI   Body Mass Index
国内标准 国际标准
体重kg，身高m
'''
weight = input("请输入体重：\n")
high = input("请输入身高：\n")
BMI = eval(weight)/pow(eval(high),2)
if BMI < 18.5:
    print("国际标准：偏瘦\n")
    print("国内标准：偏瘦\n")
elif BMI < 25:
    print("国际标准：正常\n")
    if BMI < 24:
        print("国内标准：正常\n")
    else:
        print("国内标准：偏胖\n")
elif BMI < 30:
    print("国际标准：偏胖\n")
    if BMI < 28:
        print("国内标准：偏胖\n")
    else:
        print("国内标准：肥胖\n")
else:
    print("国际标准：肥胖\n")
    print("国内标准：肥胖\n")
