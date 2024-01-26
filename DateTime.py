import datetime

nowTime = datetime.datetime.now() #showing current date and time of your laptop
print(nowTime)

print(nowTime.year)
print(nowTime.strftime("%A")) #Name of the day
print(nowTime.strftime("%c")) #Local Version of date and time

# print(datetime.datetime.__dir__(nowTime)) --> this statement prints all the method of datetime class
