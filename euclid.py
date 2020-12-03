def EUCLID(a, b):
	if b == 0:
		return a
	else:
		return EUCLID(b, a%b)

def Extended_Euclid(a, b):
	if b == 0:
		return (a, 1, 0)
	else:
		(d1, x1, y1) = Extended_Euclid(b, a%b)
		(d, x, y)    = (d1, y1, x1 - int(a/b) * y1)
		return (d, x, y)
