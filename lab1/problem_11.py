list1 = [63, 55, 14, 70, 98, 51, 12, 24]
list2 = [29, 18, 32, 45, 26, 19, 92, 82]

list3 = []

for i in range(len(list1)):
  if list1[i] % 2 != 0:
    list3.append(list1[i])

for j in range(len(list2)):
  if list2[j] % 2 == 0:
    list3.append(list2[j])

print("List 3: ", list3)
