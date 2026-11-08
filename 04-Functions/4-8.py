def time_string(hours, minutes, time_format):
    if time_format == '24':
        return f'{hours:02d}:{minutes:02d}'
    elif time_format == '12':
        if hours == '0':
            hours = 12
            time = 'am'
        elif hours < '12':
            time = 'am'
        elif hours == '12':
            time = 'pm'
        else:
            hours = hours - 12
            time = 'pm'
        return f'{hours}:{minutes:02d}{time}'

print(time_string(15,38,'24'))
