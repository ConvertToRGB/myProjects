import os
import time
import sys
import json
from PyQt4 import QtGui
from PyQt4.phonon import Phonon
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def sortByTime(t):
    return float(os.path.getmtime(os.path.join(path,t)))

def allFiles(path):
    files = next(os.walk(unicode(path), topdown=True))[2]
    folders = next(os.walk(unicode(path), topdown=True))[1]
    for i in files:
        fPathFiles = os.path.join(path, i)
        fList.append(fPathFiles)
    if folders:
        for f in folders:
            p = os.path.join(path, f)
            allFiles(p)
    return fList

def sendMail(gmail_password, gmail_user, to, sent_from):
    email_text = "Render complete!"
    subject = "Render status: DONE"
    message = 'From: {}\nTo: {}\nSubject: {}\n\n{}'.format(gmail_user,
                                                       gmail_user,
                                                       subject,
                                                       email_text)
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, message)  
    server.close()

settingsPath = os.path.join(os.path.dirname(__file__), 'settings.json')
email = ''
password = ''
music = ''
runPath = ''
count = 3
delay = 5
nextBlock = True

while True:
    path = raw_input('Drop folder here: ').strip('"').decode('cp866')
    if os.path.isdir(path) == True:
        break
    elif path == '' or path == 'd':
        if os.path.exists(settingsPath):
            settingsLoad = json.load(open(settingsPath))
            email = settingsLoad['email']
            password = settingsLoad['password']
            music = settingsLoad['music']
            runPath = settingsLoad['runPath']
            answer = settingsLoad['answer']
            path = settingsLoad['path']
            nextBlock = False
            break
        else:
            print 'No default yet!'
            continue
    else:
        print 'Wrong path!'
        continue

if nextBlock:
    print " \
Enter [e] to send email \n \
Enter [m] to play music \n \
Enter [r] to run script or *.exe file \n \
Enter [d] to load default \n \
Enter [n] to cancel script or task \n \
Enter [a] to set delay (by default it's 5)"

    answer = raw_input('Enter what to do after render is finished: ').decode('cp866').lower()

    if answer.count('n') >= 1:
        sys.exit()

    elif answer.count('d') >= 1 and os.path.exists(settingsPath) == True or answer == '' and os.path.exists(settingsPath):
        if answer.count('e') == 0 and answer.count('m') == 0 and answer.count('r') == 0:
            settingsLoad = json.load(open(settingsPath))
            email = settingsLoad['email']
            password = settingsLoad['password']
            music = settingsLoad['music']
            runPath = settingsLoad['runPath']
            answer = settingsLoad['answer']
        else:
            settingsLoad = json.load(open(settingsPath))
            email = settingsLoad['email']
            password = settingsLoad['password']
            music = settingsLoad['music']
            runPath = settingsLoad['runPath']
            answer = settingsLoad['answer']+answer

    elif answer.count('d') >= 1 or answer == '' and os.path.exists(settingsPath) == False:
        print 'No settings yet!'

    if answer.count('e') >= 1 and answer.count('d') >= 0 or os.path.exists(settingsPath) == False and answer.count('d') > 0:
        email = raw_input('Enter email [example@gmail.com]: ').decode('cp866')
        if email == 'n':
            answer = answer.replace('e', '')
        password = raw_input('Enter password: ').decode('cp866')
        if password == 'n':
            answer = answer.replace('e', '')

    if answer.count('m') >= 1 and answer.count('d') >= 0 or os.path.exists(settingsPath) == False and answer.count('d') > 0:
        while True:
            music = raw_input('Drop music here: ').strip('"').decode('cp866')
            if os.path.isfile(music):
                break
            elif not music:
                music = 'myMusic.mp3'
                break
            elif music == 'n':
                answer = answer.replace('m', '')
                break
            else:
                print 'Wrong path!'

    if answer.count('r') >= 1 and answer.count('d') >= 0 or os.path.exists(settingsPath) == False and answer.count('d') > 0:
        while True:
            rPath = raw_input('Drop script or *.exe file here: ').strip('"').decode('cp866')
            if os.path.isfile(rPath) or rPath == '':
                runPath = rPath
                break
            elif rPath == 'n':
                answer = answer.replace('r', '')
                break
            else:
                print 'Wrong path!'

        if not rPath:
            rPath = os.path.dirname(__file__).decode('cp1251')
            print rPath
            rPath = os.path.join(rPath, 'plugins')
            if os.path.exists(rPath):
                if len(os.listdir(rPath)) > 0:
                    runPath = os.listdir(rPath)[0].decode('cp1251')
                    runPath = os.path.join(rPath, runPath)
                else:
                    while True:
                        print 'No files!'
                        runPath = raw_input('Drop script or *.exe file here or enter [n]: ').strip('"').decode('cp866')
                        if os.path.exists(runPath):
                            break
                        elif runPath == 'n':
                            answer = answer.replace('r', '')
                            break
                        else:
                            continue
            else:
                while True:
                    print 'No files!'
                    runPath = raw_input('Drop script or *.exe file here or enter [n]: ').strip('"').decode('cp866')
                    if os.path.exists(runPath):
                        break
                    elif runPath == 'n':
                        answer = answer.replace('n', '')
                        break
                    else:
                        continue

    if not answer.count('a') == 0:
        delay = raw_input('Enter delay (sec): ')

settings = {'answer': answer, 
            'email':email, 
            'password': password, 
            'music':music, 
            'runPath':runPath, 
            'delay':delay, 
            'path': path,
            'count': count}

json.dump(settings, open(settingsPath, 'w'), indent = 4)

app = QtGui.QApplication(sys.argv)

output = Phonon.AudioOutput(Phonon.MusicCategory)
m_media = Phonon.MediaObject()
Phonon.createPath(m_media, output)
m_media.setCurrentSource(Phonon.MediaSource(music))

work = True
firstLoop = 0
counter = 0
# delay = 5
while work:
    fList = []
    fList = allFiles(path)
    if not fList:
        print 'No files in directory'
        time.sleep(delay)
        continue
    fList.sort(key=sortByTime)
    fListLen = len(fList)
    fListFile = fList[-1]
    if firstLoop == 0:
        lastFListLen = fListLen
        lastFListFile = os.path.getsize(fListFile)
        firstLoop += 1
        time.sleep(delay)
        continue
    print lastFListLen
    print os.path.getsize(fListFile)
    print lastFListFile
    if firstLoop != 0:
        if counter < count:
            if lastFListLen != fListLen:
                lastFListLen = fListLen
                lastFListFile = fListFile
                counter = 0
                time.sleep(delay)
                continue
                time.sleep(delay)
            if lastFListFile != os.path.getsize(fListFile):
                lastFListLen = fListLen
                lastFListFile = os.path.getsize(fListFile)
                counter = 0
                time.sleep(delay)
                continue
            else:
                counter += 1
                time.sleep(delay)
        else:
            work = False

print 'Render is Finished!'

if answer.count('e') > 0:
    sendMail(password, email, email, email)
elif answer.count('r') > 0:
    os.startfile(runPath)
elif answer.count('m') > 0:
    m_media.play()

raw_input()