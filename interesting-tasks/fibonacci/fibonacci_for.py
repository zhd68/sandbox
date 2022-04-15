fibonachi_list1 = [0, 1]

for num in range(2,500):
    fibonachi_list1.append(fibonachi_list1[num - 1] + fibonachi_list1[num - 2])

#fibonachi_list1.sort(reverse = True)
print(fibonachi_list1)