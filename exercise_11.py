from math import degrees, acos

a = int(input())
b = int(input())
c = int(input())
if a + b > c or b + c > a or a + c > b:
 l = (b ** 2 - a ** 2 + c ** 2) / (2 * b * c)
 r = (a ** 2 - b ** 2 + c ** 2) / (2 * a * c)
 t = (a ** 2 - c ** 2 + b ** 2) / (2 * a * b)
 print(l, r, t)

print ("угол 1 : ",  round(degrees(acos(l)),1))
print ("угол 2 : ",  round(degrees(acos(r)),1))
print ("угол 3 : ",  round(degrees(acos(t)),1))
