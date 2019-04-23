L1=['45', 'abc', '4', 'g', '4']
T1= tuple(L1)
n1, n2, n3, n4, n5 = T1
print(n1 + n2 + n3 + n4 + n5)

for i in range(0, len(T1)):
    if T1.count(T1[i]) > 1:
        print()





