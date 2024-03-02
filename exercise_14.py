d = float(input('введите от 1 до 360 градусов'))
hours = d // 30
minutes = (d - hours * 30) * 2
print(f' {hours} часов {minutes} минут')