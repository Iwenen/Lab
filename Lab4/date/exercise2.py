import datetime
yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
today = datetime.datetime.now()
tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
print(yesterday)
print(today)
print(tomorrow)