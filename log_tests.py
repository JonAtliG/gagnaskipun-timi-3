from log_code import log, SuperLog

# bæta við logs test
my_log1 = log('13-1-2023', 'þetta er log :)!!!')
my_log2 = log('14-1-2023', 'þetta er líka log :)!!! Jeeeiii')
# my_log3 = log('1', 'hahahah, þetta er ekki log. Feis!)

print()
my_superlog = SuperLog()

my_superlog.add_log(my_log1)
my_superlog.add_log(my_log2)

# fá alla loggana
print(my_log1)
print()
print(my_log2)

print('prenta alla logga í einu')
for my_log in my_superlog.get_all_logs():
  print(my_log)
print()

# time interval
print('stuff from specific time interval')
for my_log in my_superlog.get_all_logs('13-1-2023', '14-1-2023'):
  print(my_log)

# delete entries
print('delete entries')
my_superlog.delete_entries('13-1-2023', '14-1-2023')
for my_log in my_superlog.get_all_logs():
  print(my_log)

# get 2 newest
print('2 newest and only the newest')
print()
print(my_superlog.get_newest(2))
print()
print(my_superlog.get_newest())

pass
