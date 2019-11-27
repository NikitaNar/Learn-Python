
import time
#list1=[3,5,7,9,10,21,3,84,23,1]
#x=0
#for score in list1:
#    print((list1[x]+1))
#    x=x+1





#string=input('Введите строку: ')
#x=-1

#for letter in string:
#    print((string[x+1]))
#    x=x+1

a=[{'school_class': '4a', 'scores': [3,4,4,3,2,3,4]},
{'school_class': '5v', 'scores': [3,2,4,3,2,5,2]},
{'school_class': '6a', 'scores': [3,4,4,5,3,5,4]},
{'school_class': '7b', 'scores': [2,3,2,1,2,1,1]}]


x=0
y=0
delta=0
b=a[x]['scores'] # print((a[lena1]['scores'][y])) [3,4,4,3,2,3,4]
print(len(b))
for score in a[x]['scores']:
    if y==0:
        print(b)
        print(b[y])
        delta=delta+b[y]
        y=y+1
    elif 0<y<len(b):
        delta=delta+b[y]
        print(b[y])
        y=y+1
    if y>=len(b):
        y=0
        delta=delta/len(b)
        print("Delta=", delta)
        b=a[x+1]['scores']
        print(b)
        continue




