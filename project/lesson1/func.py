
def getsumm(one, two):

    print(str(one)+'&'+str(two))
print('NO INPUT')
getsumm("Learn","Python")
print('INPUT')
getsumm(input('Ввведите первое: '),input('Введите второе: '))


def format_price(price):
    price=int(price)
    print("Цена:",price,'руб.')
format_price(56.24)
#format_price(input('Ввведите цену: ')) не работает
#Traceback (most recent call last):
#  File "D:\project\lesson1\func.py", line 15, in <module>
#    format_price(input('Ввведите цену: '))
#  File "D:\project\lesson1\func.py", line 12, in format_price
#    price=int(price)
#ValueError: invalid literal for int() with base 10: '56,6'