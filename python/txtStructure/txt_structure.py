import os
import datetime
import time

'''input info'''
year = raw_input('Enter year [xxxx]: ')
root = os.path.dirname(__file__)
fullPath = os.path.join(root, year)
nowTime = time.time()

'''function check is there folder or not an if not, create folder'''
def isFolder(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)

'''function write txt file'''
def writeFile(root, week, wDay):
    data = 'date ' + wDay + '\n' # what to write
    writePath = os.path.join(root, str(week).zfill(2) + '.txt') # full path for txt file

    '''check is there txt file with name in variable writePath or not
    if not, then create new txt file'''
    if not os.path.exists(writePath):
        f = open(writePath, 'w')
        f.write(data)
        f.close()
    else: # add data to week if file was created afer script start
        if os.path.getmtime(writePath) >= nowTime:
            f = open(writePath, 'a')
            f.write(data)
            f.close()

'''createfolder'''
isFolder(fullPath)

'''create months and dates and other variables'''
months = []
days = []
firstDay = datetime.date(int(year), 1, 1)
day = datetime.timedelta(1)
weekDelta = datetime.timedelta(weeks = 1)
week = 1
threeDays = datetime.timedelta(3)
nextMonth = ''

'''get months names'''
for i in range(12):
    i+=1
    m = datetime.date(int(year), i, i).strftime('%B')
    months.append(m)

''' create all days'''
while str(year) == firstDay.strftime('%Y'):
    days.append(firstDay.strftime('%d.%m.%Y'))
    firstDay = firstDay + day

'''start main FOR cycle for each month'''
for i, m in enumerate(months):
    create = True # for WHILE cycle
    m_name = str(i+1).zfill(2)+'_'+m.lower() # month name in view like: 01_january
    fullMonthPath = os.path.join(fullPath, m_name) # path for month
    isFolder(fullMonthPath)

    '''create first txt for current month'''
    fileName = str(week).zfill(2)+'.txt'
    filePath = os.path.join(fullMonthPath, fileName)
    open(filePath, 'w').close()

    ''' start WHILE cycle for current month'''
    while create:
        if days: # check are days in list or not
            day_parsed = datetime.datetime.strptime(days[0], '%d.%m.%Y') # get date

            if nextMonth == m and datetime.date(int(year),i+1,15) == day_parsed.date():
                nextMonth = ''

            if day_parsed.strftime('%a') == 'Mon': # is today monday or not
                nextWeek = day_parsed + weekDelta # get next week

                if nextWeek.strftime('%m') == day_parsed.strftime('%m') == str(i+1).zfill(2): # is month next week is the same as month in day_parsed
                    
                    '''get number of lines in first txt for current month'''
                    f1 = open(filePath, 'r')
                    lines = f1.readlines()
                    linesCount = len(lines)
                    f1.close()

                    if linesCount:
                        week += 1
                        writeFile(fullMonthPath, week, days.pop(0))
                    else:
                        writeFile(fullMonthPath, week, days.pop(0))

                else:
                    thursday = day_parsed+threeDays

                    if thursday.strftime('%m') == day_parsed.strftime('%m') == str(i+1).zfill(2) or nextMonth == m:
                        if nextMonth != m:
                            week += 1
                            writeFile(fullMonthPath, week, days.pop(0))
                        else:
                            writeFile(fullMonthPath, week, days.pop(0))
                        nextMonth = ''
                    else:
                        if thursday.strftime('%Y') != day_parsed.strftime('%Y'):
                            week += 1
                            writeFile(fullMonthPath, week, days.pop(0))
                        else:
                            week = 1
                            nextMonth = thursday.strftime('%B')
                            create = False
            else: # write file if not monday
                writeFile(fullMonthPath, week, days.pop(0))
        else:
            create = False

print 'Complete!'


raw_input()