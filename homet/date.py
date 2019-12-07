import datetime
from datetime import date, time, datetime, timedelta, tzinfo

dt_now = datetime.now()

dt_now=dt_now.strftime('%m/%d/%Y')
print('Сегодня: ', dt_now)
dt_yes=date.today() - timedelta(days=1)
dt_yes=dt_yes.strftime('%m/%d/%y')
print("Вчера: ", dt_yes)

today = datetime.now()
last_month = today.replace(month=today.month-1)
last_month =last_month.strftime('%m/%d/%y') 
print("Прошлый месяц: ", last_month)

string_time='01/01/17 12:10:03.234567'
string_time=datetime.strptime(string_time, '%m/%d/%y %H:%M:%S.%f')
string_time=string_time.strftime('%m/%d/%Y')
print(string_time)


