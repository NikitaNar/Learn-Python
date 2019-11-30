

answ={'Как дела?':'Хорошо', 'Что делаешь?':'Программирую'}

while True:
    try:
        x=input('\nВведите вопрос: ')
        if  x=="Как дела?":  print(answ['Как дела?'])
        elif  x=='Что делаешь?': print(answ['Что делаешь?'])
        else: print('Не понимаю')
        
    except (KeyboardInterrupt):
        print('\nПока')
        break