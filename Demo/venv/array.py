import array as arr
a = arr.array('i', [4, 7, 8, 4, 4])

for i in range(0, len(a)):
    print(a[i])

for i in a:
    print(i)
print("Printing reverse array : ")
for i in range(len(a)-1, -1, -1):
    print(a[i])

number = int(input("Enter number "))
count = 0
for i in range(0, len(a)):
    if number == a[i]:
        count = count + 1

print("{} is occurred {} times".format(number, count))


print("Size of array before removing number : {}".format(len(a)))

for i in range(0, len(a), 1):
    if number == a[i]:
        a.remove(a[i])
        break

print("Size of array after removing number : {}".format(len(a)))
