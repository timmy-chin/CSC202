import datetime

# note = input('Enter Your Note: ')
t = datetime.datetime.now()
d = t.strftime('%d/%m/20%y')

print(d)