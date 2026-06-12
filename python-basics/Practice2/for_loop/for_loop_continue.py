for x in range(1, 11):
    if x % 2 == 0:
        continue
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

brands_of_phone = ["Samsung", "Iphone", "Xiaomi", "Oppo", "Vivo", "Realme"]
i = 0
for i in range(len(brands_of_phone)):
    if brands_of_phone[i] == "Iphone":
        continue
    print("I do not use:", brands_of_phone[i])