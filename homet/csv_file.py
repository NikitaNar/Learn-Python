import csv
 
FILENAME = "users.csv"
 
users = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]
 
with open(FILENAME, "w", encoding="utf-8") as file:
    fields = ["name", "age","job"]
    writer = csv.DictWriter(file, fields, delimiter=";")
    writer.writeheader()
    for user in users:
        writer.writerow(user)


    
     

 
