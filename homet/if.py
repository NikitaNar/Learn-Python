age=input('Введите свой возраст: ')
age=int(age)
if age > 21:
    print('Работаешь')
elif 18 <= age <= 21:
    print('В ВУЗе')
elif 6 <= age <= 17:
    print('В школе')
else: print('В садике')

x=input('Введите 1 строку: ')
y=input('Введите 2 строку: ')

#не сработает


if x == y:
    print('1')
elif y=='learn':
    if x!=y:print("3")
elif len(x) > len(y):
    print('2')

else: print("0")