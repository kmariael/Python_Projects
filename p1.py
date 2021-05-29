import math

a1 = float(input('a1 ='))
a2 = float(input('a2 ='))
b1 = float(input('b1 ='))
b2 = float(input('b2 ='))

ab = a1*b1+a2*b2

ametro = math.sqrt(a1**2+a2**2)
bmetro = math.sqrt(b1**2+b2**2)

costh = ab/(ametro*bmetro)

goniath = math.degrees(math.acos(costh))

print(costh, goniath)