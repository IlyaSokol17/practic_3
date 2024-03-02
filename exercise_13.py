x = int(input())
y = int(input())
n = x % y + 1
r = y % x + 1
print(min(n, r))