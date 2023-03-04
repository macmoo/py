# -------------------------------------------------
print("------------------------------------------")
arr = []
for i in range(0, 20, 2):
    arr.append(i*i)
print(arr)
print("------------------------------------------")
# 리스트 내포 list comprehensions
# 리스트이름 = [표현식 for 반복자 in 반복할수 있는것]
# 리스트이름 = [표현식 for 반복자 in 반복할수 있는것 if 조건문]
arr2 = [i * i for i in range(0, 20, 2)]
print(arr2)
print("------------------------------------------")
arr3 = ["사과","자두","초코","바나나","체리"]
out3 = [fruit for fruit in arr3 if fruit != "초코"]
print(out3)
print("------------------------------------------")
