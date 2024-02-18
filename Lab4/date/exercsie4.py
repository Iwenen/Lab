import datetime
date1_input = input()
date2_input = input()
date1 = datetime.datetime.strptime(date1_input, "%Y-%m-%d %H:%M:%S")
date2 = datetime.datetime.strptime(date2_input, "%Y-%m-%d %H:%M:%S")
difference = abs((date2 - date1).total_seconds())
print(difference)