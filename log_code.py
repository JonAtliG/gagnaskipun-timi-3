

'''log
- time of entry
- log_itself
- __string__(self)

superlog
- get_logs(start_time, end_time)
- delete_entries(start_time, end_time)
- get_newest(n)
    - n defaults to 1
'''


class log():
    def __init__(self, time_of_entry = '', log_str = ''): 
        self.time_of_entry  = time_of_entry
        self.log_itself     = log_str
    
    def __str__(self): 
        return '{} -- {}'.format(self.time_of_entry, self.log_itself)


class SuperLog():
    YEAR  = 2
    MONTH = 1
    DATE  = 0

    def __init__(self):
        self.list_of_logs = list()
    
    def add_log(self, a_log:str):
        self.list_of_logs.append(a_log)

    def get_all_logs(self, start_time = None, end_time = None): 

        list_of_logs = list()
        if not ((start_time is None) and (end_time is None)):
            start_time = self.get_date(start_time)
            end_time = self.get_date(end_time)

            for a_log in self.list_of_logs:
                log_date = self.get_date(a_log.time_of_entry)
                if log_date[SuperLog.YEAR] <= start_time[SuperLog.YEAR] and log_date[SuperLog.YEAR] >= end_time[SuperLog.YEAR]:
                    if log_date[SuperLog.MONTH] <= start_time[SuperLog.MONTH] and log_date[SuperLog.MONTH] >= end_time[SuperLog.MONTH]:
                        if log_date[SuperLog.DATE] <= start_time[SuperLog.DATE] and log_date[SuperLog.DATE] >= end_time[SuperLog.DATE]:
                            list_of_logs.append(a_log)
        else:
            list_of_logs = self.list_of_logs

        return list_of_logs


    def get_date(self, date_str:str):
        day, month, year = date_str.split('-')
        return (int(day), int(month), int(year))
        
    def date_in_range(self, date_str, start_time, end_time): pass

    def delete_entries(self, start_time, end_time):
        start_time = self.get_date(start_time)
        end_time   = self.get_date(end_time) 

        for a_log in self.list_of_logs:
            log_date = self.get_date(a_log.time_of_entry)
            if log_date[SuperLog.YEAR] <= start_time[SuperLog.YEAR] and log_date[SuperLog.YEAR] >= end_time[SuperLog.YEAR]:
                if log_date[SuperLog.MONTH] <= start_time[SuperLog.MONTH] and log_date[SuperLog.MONTH] >= end_time[SuperLog.MONTH]:
                    if log_date[SuperLog.DATE] <= start_time[SuperLog.DATE] and log_date[SuperLog.DATE] >= end_time[SuperLog.DATE]:
                        self.list_of_logs.remove(a_log)
                        print('this works')

    def get_newest(self, n=1):
        my_return = str()
        i = 0
        while n - (i+1) >= 0:
            a_log = str(self.list_of_logs[-(i)] )
            my_return += a_log + '\n'
            i += 1
        return my_return


