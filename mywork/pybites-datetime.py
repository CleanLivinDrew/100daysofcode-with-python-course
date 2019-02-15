'''Extract datetimes from log entries and calculate the time
   between the first and last shutdown events'''
from datetime import datetime
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()

# for you to code:

def convert_to_datetime(line):
    '''TODO 1:
       Given a log line extract its timestamp and convert it to a datetime object. 
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)'''
    datestring = line.split()[1]
    date = datestring.split('T')[0].split('-')
    time = datestring.split('T')[1].split(':')
    timestamp = datetime(int(date[0]), int(date[1]), int(date[2]), int(time[0]), int(time[1]), int(time[2]))
    return timestamp
    

def time_between_shutdowns(loglines):
    '''TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and calculate the 
       timedelta between the first and last one. 
       Return this datetime.timedelta object.'''
    shutdown_times = []
    for line in loglines:
        message = line.split(' ', 3)[3].rstrip()
        if message == 'Shutdown initiated.':
            shutdown_times.append(convert_to_datetime(line))
    timedelta = max(shutdown_times) - min(shutdown_times)
    return timedelta

    
data = time_between_shutdowns(loglines)
print(data)
