height=eval(input("shengao"))
weight=eval(input("tizhong"))
bmi=weight/pow(height,2)
if bmi < 18.5:
    d = ("偏瘦")
elif bmi >= 18.5 and bmi < 25:
    d = ("正常")
elif bmi >=25 and bmi < 30:
    d = ("偏胖")
else:
    d = ("肥胖")
print("BMI数值为：{}".format(d))
