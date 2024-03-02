comp = int(input('введите количество завершений'))
att = int(input('введите количество попыток передачи'))
yds = int(input('введите количество пасов'))
td = int(input('введите количество пасов приземления'))
int = int(input('введите количество перехватов'))
a = (comp / att - 3) * 5
b = (yds / att - 3) * 25
c = (td / att) * 20
d = 2.375 - (int / att) * 25
if a > 2.375 :
    a = 2.375
if b > 2.375 :
    b = 2.375
if c > 2.375 :
    c = 2.375
if d > 2.375 :
    d = 2.375
if a < 0 :
    a = 0
if b < 0 :
    b = 0
if c < 0 :
    c = 0
if d < 0 :
    d = 0

passer_rating = ((a + b + c + d) / 6) * 100
print(passer_rating)