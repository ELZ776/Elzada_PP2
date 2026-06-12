i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

ytubes = ["Music", "Education", "Comedy", "News", "Sports", "Movies"]
i = 0
while i < len(ytubes):
    if ytubes[i] == "Movies":
        i += 1
        continue
    print("I do not watch:", ytubes[i])
    i += 1

brands_of_phone = ["Samsung", "Iphone", "Xiaomi", "Oppo", "Vivo", "Realme"]
i = 0
while i < len(brands_of_phone):
    if brands_of_phone[i] == "Iphone":
        i += 1
        continue
    print("I do not use:", brands_of_phone[i])
    i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)