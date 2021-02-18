"""
Test 1: sum two number
"""

def add(param1, param2):
    return param1 + param2

"""
Test 2: centuryFromYear
Describe: if year is mod 100 with result 0 century  is year/100
else century is year/100 + 1
"""

def centuryFromYear(year):
    if (year%100 == 0):
        return int(year/100)
    else:
        return int(year/100) + 1

"""
Test 3: Check palindrome string
"""
def  checkPalindrome(inpuString):
    return inpuString == inpuString[::-1]


############################################### end The journey begins



############################################### Start Edge of the Ocean
"""
Test4 : adjacent Elements Product
"""


def adjacentElementsProduct(inputArray):
    max_value = inputArray[0] * inputArray[1]
    length = len(inputArray)
    if length == 2:
        return max_value
    value = None
    for i in range(1, length - 1):
        value = inputArray[i] * inputArray[i + 1]
        if value > max_value:
            max_value = value
    return max_value



"""
Test 5: shapeArea
"""

def shapeArea(n):
    if n == 1:
        return 1
    else:
        return n*n + shapeArea(n-1)

# Cách 2:
def shapeArea(n):
    return n*n + (n-1)*(n-1)



"""
Test 6: makeArrayConsecutive2
"""

def makeArrayConsecutive2(statues):
    return max(statues) - min(statues) - len(statues) + 1



"""
Test 7: almostIncreasingSequence
"""


def almostIncreasingSequence(sequence):
    value = None
    length = len(sequence)
    for i in range(length - 1):
        if sequence[i] >= sequence[i + 1] and i != length - 2:
            value = i
            break
    if value == None:
        return True
    sequence_2 = sequence[:]
    sequence_2.pop(value + 1)
    sequence.pop(value)
    check_1 = None
    for i in range(length - 2):
        if (sequence[i] >= sequence[i + 1]):
            check_1 = i
    check_2 = None
    for i in range(length - 2):
        if (sequence_2[i] >= sequence_2[i + 1]):
            check_2 = i
    if check_1 == None or check_2 == None:
        return True
    else:
        return False


"""
Test 8: matrixElementsSum
"""
def matrixElementsSum(matrix1):
    width = len(matrix1[0]) #4
    height = len(matrix1) #3
    total = 0
    for i in range(width):
        for j in range(height):
            if matrix1[j][i] != 0:
                total = total + matrix1[j][i]
            else:
                break
    return total


"""
Test 9: allLongestStrings
"""

def allLongestStrings(inputArray):
     stack = []
     length = 0
     for i in inputArray:
         if len(i) > length:
             length = len(i)
             stack.clear()
             stack.append(i)
         elif len(i) == length:
             stack.append(i)
     return stack


"""
Test 10: commonCharacterCount
"""
def commonCharacterCount(s1, s2):
    s1 = [i for i in s1]
    s2 = [i for i in s2]
    s3 = list(set(s1).intersection(set(s2)))
    same_count = 0
    for i in s3:
        same_count = same_count + s1.count(i) if s1.count(i) < s2.count(i) else same_count + s2.count(i)
    return same_count

def commonCharacterCount(s1, s2):
    con = [min(s1.count(i), s2.count(i)) for i in set(s1)]
    return sum(con)




"""
Test 11: isLucky
"""
import time

def isLucky(n):
    n = str(n)
    length = len(n)
    if length % 2 != 0:
        return False
    half_length = int(length/2)
    n = [int(i) for i in n]
    list1 = n[:half_length]
    list2 = n[half_length:]
    return sum(list1) == sum(list2)



"""
Test 12: sortByHeight
"""
def sortByHeight(a):
    x = []
    list = []
    length = len(a)
    for i in range(length):
        if a[i] != -1:
            x.append(i)
            list.append(a[i])
    list.sort()
    j = 0
    for i in x:
        a[i] = list[j]
        j = j + 1
    return a
'''
ôn tập:
    + hàm enumerate: gắn thêm giá trị đếm phía trước gia trị của mảng
        
'''



"""
Test 13: reverseInParentheses
"""
def reverseInParentheses(s):
    length = len(s)
    stack = []
    list = []
    for i in range(length):
        if s[i] == '(':
            stack.append(i)
        elif s[i] == ')':
            list.append(stack.pop())
            list.append(i)
    i = 0
    length_list = len(list)
    print
    while i < length_list:
        s = s[:list[i]] +"  " + s[(list[i] + 1 ): list[i + 1]][::-1] + s[(list[i + 1])+1:]
        i += 2
    return s.replace("  ","")


"""
Test 14: alternatingSums
"""

def alternatingSums(a):
    return [ sum(a[::2]), sum(a[1::2])]

"""
Test 15: addBorder
"""

def addBorder(picture):
    length = len(picture[0])
    return ['*' * (length + 2)] + ["*" + i + "*" for i in picture ] + ['*' * (length + 2)]


"""
Test 16: areSimilar
"""

def areSimilar(a, b):
    if len(a) != len(b):
         return False
    count = 0
    for i, j in zip(a,b):
        if i != j:
            count = count + 1
    if count > 2:
        return False
    a.sort()
    b.sort()

    for i, j in zip(a, b):
        if i != j:
            return False
    return True


"""
Test 17: arrayChange
"""
def arrayChange(inputArray):
    length = len(inputArray)
    total = 0
    for i in range(length - 1):
        if inputArray[i] >= inputArray[i + 1]:
            temp = inputArray[i] - inputArray[i + 1] + 1
            total = total + temp
            inputArray[i + 1] = inputArray[i] + 1
    return total



"""
Test 18: palindromeRearranging
"""

def palindromeRearranging(inputString):
    length = len(inputString)
    check_list = list(set(inputString))
    if length % 2 == 0:
        for i in check_list:
            if inputString.count(i) % 2 != 0:
                return False
    else:
        count = 0
        for i in check_list:
            if inputString.count(i) % 2 != 0:
                count = count + 1
        if count > 1:
            return False
    return True


"""
Test 19: areEquallyStrong
"""
def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    return set([yourLeft, yourRight]) == set([friendsLeft, friendsRight])


"""
Test 20: arrayMaximalAdjacentDifference
"""

def arrayMaximalAdjacentDifference(inputArray):
    length = len(inputArray)
    list_after = [abs(inputArray[i] - inputArray[i+1]) for i in range(length - 1 )]
    return max(list_after)


#regrex in python
'''
findall(): list all parameter match with the text
    ==> purpose: count the element match with your text in your head
    
search : search function searches the string for match, and return a match object if there is a match
    ==> purpose: the exactly position of element in string

split() :
    ==> return list where the string has been split at each match  like string_name.split()

sub() : 
     ==> replace the element acive in string with other string 

Metachacacters are characters with a special meaning (các ký tự có ý nghĩa đặc biệt)

[]  : A set of chacracters   (in this list for developer defines by himsefl)

\   : signals a special sequence (chứ ký ,dấu hiệu của các ký tự đặc biệt) (can also be used to escape special characters)

.   : Any character (except newline character)
'''


