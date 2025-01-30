new_list = [1, 2, 3]
result = new_list[0]
if 2 in new_list: print(True)

for n in new_list:
    if n == 1:
        print(True)
        break

new_list2 = [1, 2, 3]
new_list2.extend([4, 5, 6])
print(new_list2)