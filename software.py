import os
import sys
import time
import re
class SMS_Advertisement:
    def __init__(self):
        if self.deviceReady():
            print('*' * 60)
            print('                     Android SMS Sender')
            print('*' * 60)
            print('             Your Android Version : ' + self.androidVersion())
            print('=' * 60)
            time.sleep(2)
            numList = self.readNumbers()
            if len(numList) == 0:
                print('\n[Error] : Your Numbers list is empty ! Please check your list in numbers.txt')
                sys.exit()
            SMS = self.readSMS()
            if SMS == '':
                print('\n[Error] : Your SMS Message is empty! Please check your message in message.txt')
                sys.exit()
            counter = 0
            for number in numList:
                if self.androidVersion() == 'Android Oreo':
                    counter += 1
                    print('(' + str(counter) + ') Sending SMS to ' + number)
                    a = os.system('./adb shell service call isms 7 i32 1 s16 \"com.android.mms.service\" s16 \"' + number + '\" s16 \"null\" s16 \"' + SMS + '\" s16 \"null\" s16 \"null\"')
                    time.sleep(2)
                elif self.androidVersion() == 'Android Pie':
                    counter += 1
                    print('('+str(counter)+') Sending SMS to ' + number)
                    a = os.system('./adb shell service call isms 7 i32 1 s16 \"com.android.mms.service\" s16 \"'+number+'\" s16 \"null\" s16 \"'+SMS+'\" s16 \"null\" s16 \"null\"')
                    time.sleep(2)
                elif self.androidVersion() == 'Android Nougat':
                    counter += 1
                    print('(' + str(counter) + ') Sending SMS to ' + number)
                    a = os.system('./adb shell service call isms 7 i32 1 s16 \"com.android.mms.service\" s16 \"'+number+'\" s16 \"null\" s16 \"'+SMS+'\" s16 \"null\" s16 \"null\"')
                    time.sleep(2)
                elif self.androidVersion() == 'Android Marshmallow':
                    counter += 1
                    print('(' + str(counter) + ') Sending SMS to ' + number)
                    a = os.system('./adb shell service call isms 7 i32 1 s16 \"com.android.mms.service\" s16 \"' + number + '\" s16 \"null\" s16 \"' + SMS + '\" s16 \"null\" s16 \"null\"')
                    time.sleep(2)
                elif self.androidVersion() == 'Android Lollipop':
                    counter += 1
                    print('(' + str(counter) + ') Sending SMS to ' + number)
                    a = os.system('./adb shell service call isms 7 i32 1 s16 \"com.android.mms.service\" s16 \"' + number + '\" s16 \"null\" s16 \"' + SMS + '\" s16 \"null\" s16 \"null\"')
                    time.sleep(2)

            print('Sending Done Successfully!')
            sys.exit()

        else:
            print('\n[Error] : Please Plug Your Device and turn on USB Debugging.. or check if you have adb Installed')
    def readNumbers(self):
        numList = []
        try:
            with open('numbers.txt') as numFile:
                for line in numFile:
                    numList.append(line.strip())
                return numList
        except FileNotFoundError:
            print('numbers.txt Not Found!')
            sys.exit()
    def readSMS(self):
        try:
            with open('message.txt', 'r') as myfile:
                SMS = open('message.txt', 'r').read()
                data = re.escape(SMS.replace("\n", " "))
                return data
        except FileNotFoundError:
            print('numbers.txt Not Found!')
            sys.exit()
    def androidVersion(self):
        a=os.popen('./adb shell getprop ro.build.version.release').read()
        if a.find("8.")!=-1:
            return('Android Oreo')
        elif a.find("9")!=-1:
            return("Android Pie")
        elif a.find("7.")!=-1:
            return('Android Nougat')
        elif a.find("6.")!=-1:
            return('Android Marshmallow')
        elif a.find("5.")!=-1:
            return('Android Lollipop')
        else:
            print('your device isn\'t compatible. Your device must be Android 5+')
            sys.exit()
    def deviceReady(self):
        a=os.popen('./adb devices').read().count('device')
        if a == 2:
            return True
        else:
            return False
a=SMS_Advertisement()
