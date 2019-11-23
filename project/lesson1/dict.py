a={"city": "Москва", "temperature": "20"}
print(a.get('city'))
a['temperature']=int(a['temperature'])-int(5)
print(a['temperature'])
print(a)
print('Страна:', a.get('country'))
a['country']='Россия'
print('Добавлена страна:', a.get('country'))
a['date']= '27.05.2019'
print('Добавление даты...')
print(a)