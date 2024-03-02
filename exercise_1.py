bitcoin = str(input('введите стоимость биткойна в рублях '))
bitcoin = str(bitcoin)
if bitcoin[-3] == '.' or bitcoin[-3] == ' ' or bitcoin[-3] == ',':
   print(bitcoin[-4])
else:
     print(bitcoin[-3])