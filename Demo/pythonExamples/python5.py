import calendar

class base:

    def calculateNoOfDays(self):
        from datetime import date

        date1 = date(2013, 6, 7)
        date2 = date(2013, 7, 8)

        print(date2 - date1)

    def show_calendar(self):
        month = int(input("Enter month"))
        year = int(input ("Enter year"))
        print (calendar.month(year,month))

    def doc_print(self):
        print(len.__doc__)

    def search_number(self):
        data = [1, 2, 4, 2, [4, 5]]

        no = int(input("Enter data needs to be searched"))
        i = 0
        count = 0
        for i in range(0, 5):
            if type(data[i]) == list:
                for j in range(0, len(data[i])):
                    if data[i][j] == no:
                        count = count + 1

            if data[i] == no:
                count = count + 1

        if count > 0:
            print("Desired number has been found for {} times".format(count))
            return True
        else:
            print("Try later")
            return False

    @staticmethod
    def concate_str():
        list = ['sanjana', 'Hi', 'Bye']
        str = list[0] + list[1] + list[2]
        print(str)

    def difference_between_sets(self):
        color_list_1 = set(["White", "Black", "Red"])
        color_list_2 = set(["Red", "Green"])
        print(color_list_1.difference(color_list_2))
        print(color_list_1 - color_list_2)

    def decToBin(self):
        value = int(input("Enter decimal amobut which needs to be converted into binary"))
        print(format(value, '010b'))

    def osDetermine(self):
        import platform
        print(platform.architecture())

    def minMax(self):
        L1 = ['5', '100', '1', '0']
        max = int(L1[0])
        min = int(L1[0])

        for i in range(0, len(L1), 1):
            if int(L1[i]) > max:
                max = int(L1[i])
            if int(L1[i]) < min:
                min = int(L1[i])

        print("Minimum value is {}".format(min))

        print("Maximum value is {}".format(max))

    def printArray(self):
        L1 = [2, 7, 8, 4, 0]
        for i in range(0, len(L1), 1):
            print(L1[i])

    def printReverseArray(self):
        L1 = [2, 7, 8, 4, 0]
        for i in range(len(L1) - 1, -1, -1):
            print(L1[i])

    def findNoFromArray(self):
        number = int(input("Enter number "))
        L1 = [4, 7, 8, 4, 4]
        count = 0
        for i in range(0, len(L1), 1):
            if number == L1[i]:
                count = count + 1

        print("{} is ocurred {} times".format(number, count))

    def removeNoFromArray(self):
        L1 = [4, 7, 8, 4, 4]
        print("Size of array before removing number : {}".format(len(L1)))
        number = int(input("Enter number "))

        for i in range(0, len(L1), 1):
            if number == L1[i]:
                L1.remove(L1[i])
                break

        print("Size of array after removing number : {}".format(len(L1)))

    def sortDictionary(self):
        d1 = {1: 45, 4: 67, 3: 2}
        new = sorted(d1.items(), key=lambda x: x[1])
        print(new)
        new = sorted(d1.items(), key=lambda x: x[1], reverse=True)
        print(new)

    def addIntoDictionary(self):
        d1 = {0: 10, 1: 20}
        print(d1)
        d1[2] = 30
        print(d1)

    def mergeDictionaries(self):
        dic1 = {1: 10, 2: 20}
        dic2 = {3: 30, 4: 40}
        dic3 = {5: 50, 6: 60}

        dic1.update(dic2)
        dic1.update(dic3)
        print(dic1)

    def printDicUsingForLoop(self):
        dic1 = {1: 10, 2: 20, 3: 30, 4: 40}

        for i in dic1:
            print(dic1[i])

    def generateDicwithSquersAsValues(self):
        number = int(input("Enter positive no of keys for dictionary: "))
        l1 = []
        for i in range(1, number + 1, 1):
            l1.append(i)

        l2 = []
        l2 = list(map(lambda x: x * x, l1))

        dic1 = {}
        for j in range(0, len(l1)):
            dic1[l1[j]] = l2[j]

        print(dic1)

    def setBasicOperation(self):
        s = set()
        print(type(s))
        s.add(2)
        s.add(3)
        s.add(4)
        s.add(1)
        s.add(24)
        s.add(32)
        s.add(48999)
        s.add(8761)
        print("Original set {}".format(s))
        for i in s:
            print(i)
        number = int(input("Enter no to be removed "))
        for i in s:
            if number == i:
                s.remove(i)
                break

        print("Updated set {} after removal of {}".format(s, number))

    @staticmethod
    def setFunctions():
        s = {6, 9, 33, 51, 2, 0, }
        s1 = {33, 0, 7, 2, 8, 10}

        print(s.intersection(s1))
        print(s.union(s1))
        print(s.difference(s1))
        print(s.symmetric_difference(s1))
        s.clear()
        print(s)

    @staticmethod
    def sumList(l1 = []):
        sum = 0
        for i in range(0, len(l1)):
            if type(l1[i]) == list:
                for j in range(0, len(l1[i])):
                    sum = sum + l1[i][j]
            else:
                sum = sum + l1[i]

        print("Sum of all numbers is : {}".format(sum))

    def multiplyList(self,l1 = []):
        answer = l1[0]
        for i in range(1, len(l1)):
            if type(l1[i]) == list:
                for j in range(0, len(l1[i])):
                    answer = answer * l1[i][j]
            else:
                answer = answer * l1[i]

        print("Multiplication of all numbers is {}".format(answer))

    def smallestNoFromList(self):
        l1 = [4, 6, 2, [8, 1]]
        min = l1[0]
        for i in range(1, len(l1)):
            if type(l1[i]) == list:
                for j in range(0, len(l1[i])):
                    if min > l1[i][j]:
                        min = l1[i][j]
            else:
                if min > l1[i]:
                    min = l1[i]

        print("Smallest value is {}".format(min))

    def list_4(set):
        l1 = ['abc', 'xyz', 'aba', '1221', 'rsfgrth76r', '2']
        count = 0
        for i in range(0, len(l1)):
            if len(l1[i]) >= 2:
                str = l1[i]
                if str[0] == str[-1]:
                    count = count + 1
        print("No of such strings are {}".format(count))

    def sortedList(self):
        l1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
        count = 0
        l2 = sorted(l1, key=lambda x: x[1])
        print("Sorted list {}".format(l2))

    def removeDuplicatesAndCopy(self):
        l1 = [2, 4, 10, 20, 5, 2, 20, 4]
        l2 = []
        for i in l1:
            if i not in l2:
                l2.append(i)
        print("List after duplication {}".format(l2))

        l3 = l2.copy()
        print("new list which is exactly copy of l2 {}".format(l3))

    def list_8(self):
        l1 = ['Sanjana', 'Vani', 'te', 'tyu']
        l2 = []
        number = int(input("Enter number"))
        for i in range(0, len(l1)):
            str = l1[i]
            if len(str) > number:
                l2.append(str)
        print("New list {}".format(l2))

    def list_9(self, l1=[], l2=[]):
        if len(set(l1).intersection(set(l2))) > 0:
            return True
        else:
            return False

    def list_10(self):
        l1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
        print("Original List {}".format(l1))
        l1.pop(0)
        l1.pop(-2)
        l1.pop(-1)
        print("List after removing elements: {}".format(l1))


class derived(base):
    def call_function(self):
        print("Calling function to execute class")

d = derived()
# d.call_function()

# d.calculateNoOfDays()
# d.show_calendar()
# d.doc_print()

# value = d.search_number()
# print(value)

# d.concate_str()
# d.difference_between_sets()
# d.decToBin()
# d.osDetermine()
# d.minMax()
# d.printArray()
# d.printReverseArray()
# d.findNoFromArray()
# d.removeNoFromArray()
# d.sortDictionary()
# d.addIntoDictionary()
# d.mergeDictionaries()
# d.printDicUsingForLoop()
# d.generateDicwithSquersAsValues()
# d.setBasicOperation()
# d.setFunctions()
# d.sumList([4, 6, 2, [8, 10]])
# d.multiplyList([4, 6, 2, [8, 10]])
# d.smallestNoFromList()
# d.list_4()
# d.sortedList()
# d.removeDuplicatesAndCopy()
# d.list_8()
# print(d.list_9([2, 7, 435, 678], [7, 678, 34, 5]))
# d.list_10()
