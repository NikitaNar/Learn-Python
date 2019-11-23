a=[3,5,7,9,10/5]
print(a, 'созданный список')
b='python'
a.append(b)
print(a,'добавлен новый элемент')
print(len(a), 'количество элементов')
print(a[:1], 'первый элемент')
с=len(a)-1
print(a[с:], 'последний элемент')
print(a[1:5], 'со 2 по 4 элемент')
a.remove('python')
print(a, 'удалён элемент python')
