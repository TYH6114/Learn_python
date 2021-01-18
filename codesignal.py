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


print(almostIncreasingSequence([3, 5, 67, 98, 3]))
"""
Test 1: sum two number
"""
"""
Test 1: sum two number
"""
