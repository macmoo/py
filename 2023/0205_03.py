print("------------------------------------------");
# str_a = input("입력>")
# int_a = int(str_a)
# print(str_a)
# print(int_a)
# print(type(str_a))
# print(type(int_a))
print("------------------------------------------");
v1 = "{}원 {}엔 {}달러 {}유로".format(1000,100,10,9)
print(v1)
print("------------------------------------------");
v2 = "{:d}".format(52)
v3 = "{:5d}".format(52)
v4 = "{:05d}".format(52)
v5 = "{:05d}".format(-52)
print(v2)
print(v3)
print(v4)
print(v5)
print("------------------------------------------");
v6 = "{:+d}".format(52)
v7 = "{:+d}".format(-52)
v8 = "{: d}".format(52)
v9 = "{: d}".format(-52)
print(v6)
print(v7)
print(v8)
print(v9)
print("------------------------------------------");
v10 = "{:+5d}".format(52)
v11 = "{:+5d}".format(-52)
v12 = "{:=+5d}".format(52)
v13 = "{:=+5d}".format(-52)
v14 = "{:+05d}".format(52)
v15 = "{:+05d}".format(-52)
print(v10)
print(v11)
print(v12)
print(v13)
print(v14)
print(v15)
print("------------------------------------------");
v16 = "{:+015f}".format(52.123)
v17 = "{:+15.4f}".format(52.123)
print(v16)
print(v17)
print("------------------------------------------");
v18 = "{:g}".format(52.0) # 의미없는 소수점 제거
print(v18)
print("------------------------------------------");
print("안녕" in "안녕하세요")
print("------------------------------------------");
v19 = "10 20 30 40 50".split(" ")
print(v19)
print("------------------------------------------");
v20 = "{}".format(10)
v21 = f'{10}'
print(v20)
print(v21)
print("------------------------------------------");
print("------------------------------------------");
print("------------------------------------------");
print("------------------------------------------");
print("------------------------------------------");
print("------------------------------------------");
# ------------------------------------------
# ------------------------------------------
# 입력>123
# 123
# 123
# <class 'str'>
# <class 'int'>
# ------------------------------------------