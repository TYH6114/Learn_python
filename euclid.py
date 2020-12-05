#Tính ước chúng lớn nhất của 2 số
def EUCLID(a, b):
	if b == 0:
		return a
	else:
		return EUCLID(b, a%b)

#Tính d = GCD(A,B) = AX + BY
def Extended_Euclid(a, b):
	if b == 0:
		return (a, 1, 0)
	else:
		(d1, x1, y1) = Extended_Euclid(b, a%b)
		(d, x, y)    = (d1, y1, x1 - int(a/b) * y1)
		return (d, x, y)

# Tính module với số mũ lớn
import math

def div2(number):
    binary = ''
    while True:
        if number > 0:
            k = number % 2
            number = number // 2
            binary += str(k)
        else:
            break
    return binary

def module_fast(a,b,n):
    binary = div2(b)
    d = a % n
    balance = 1
    for i in binary:
        if i == '1':
            balance = (balance*d) % n
        d = (d * d) % n
    return balance

a = 123456789987654321;
b = 546152198651652316;
m = 1000000007;
print(module_fast(a,b,m))
         
            


