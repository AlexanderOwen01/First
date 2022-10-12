mat = eval(input("please input the matrix using [] :"))
list1 = []
for a in range(len(mat[0])):
    list2 = []
    for b in mat:
        list2.append(b[a])
    list1.append(list2)
print(f"Result: {list1}")