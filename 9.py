a = int(input("qingshuzhengshu"))
if a % 2 ==0:
    if a % 3 ==0:
        print(a)
    else:
        print("此数能被2整除，不能被三整除。")
else:
    print("不能被二整除")
