from datetime import datetime

now = datetime.now()
time_stamp =  now.strftime('%d %B %Y %H:%M:%S')

f = open('WEEK-7/log.txt', 'a')
txt = 'We added second and changed to 24 hour format'
words = ['NumPy', 'Pandas', 'Django','Flask','Scikit-learn']
for word in words:
    f.write(f'{time_stamp} - {word} is a Python library\n')
