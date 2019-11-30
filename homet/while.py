
a=[{'school_class': '4a', 'scores': [3,4,4,3,2,3,4]},
{'school_class': '5v', 'scores': [3,2,4,3,2,5,2]},
{'school_class': '6a', 'scores': [3,4,4,5,3,5,4]},
{'school_class': '7b', 'scores': [2,3,2,1,2,1,1]}]

allsum=0
allcount=0
score1={}
class_count=len(a)

for x in range(class_count):
    b=a[x]['scores']
    classcount=len(b)
    class_sum=sum(b)
    allsum+=class_sum
    allcount+=classcount
    class_average=class_sum/classcount
    print('Class: ',a[x]['school_class'],class_average)
school_average=allsum/allcount
print('school_average: ', school_average)




