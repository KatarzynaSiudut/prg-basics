time = input("enter the time (hh:mm): ")

hours = int(time[0:2])
minutes = time[3:5]

if hours >= 12:
    period = "pm"

elif hours < 12:
    period = "am"


if hours > 12:
    hours = hours - 12

elif hours == 0:
    hours = 12

print(f'time in 12 format: {hours}:{minutes}{period}')




