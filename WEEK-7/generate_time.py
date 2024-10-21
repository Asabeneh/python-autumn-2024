def generate_time(format = 'eu'):
    now = datetime.now()
    year = now.year
    month = now.month
    day= now.day
    hours = now.hour 
    minutes = now.minute
    seconds = now.second
    """ 
    print(day, month, year, hours, minutes, seconds)
        print(now.timestamp()) # 1970 Jan 1 00:00
        print(f'{day}/{month}/{year} {hours}:{minutes}') # European format 
        """
    eu_time_format = f'{day}/{month}/{year} {hours}:{minutes}'
    us_time_format = f'{month}/{day}/{year} {hours}:{minutes}'
    if format.lower() == 'us':
        time_format = us_time_format 
    elif format.lower()== 'eu':
        time_format = eu_time_format
    return time_format

print(generate_time('us'))
print(generate_time('US'))
print(generate_time('Eu'))
print(generate_time())