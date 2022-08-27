seconds_int = int(input('Please, type seconds :'))
day = seconds_int // 86400
seconds_rest_day = seconds_int % 86400
hours = seconds_rest_day // 3600
seconds_rest_hours = seconds_rest_day % 3600
minutes = seconds_rest_hours // 60
seconds_rest_finale = seconds_rest_hours % 60

print(day, "Days", hours, "Hours", minutes, "Minutes", seconds_rest_finale, "Seconds.")