#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import telebot
import requests
from telebot import types
from datetime import datetime, timedelta 
import smtplib, os, sys
from subprocess import getoutput
#from markdowngenerator import MarkdownGenerator

# -------------------- SETTINGS --------------------

# Telegram bot Token.
token = ""

# List with the telegram id of the allowed users.
#id_admins = [-566848012,-591814364]
id_admins = [381368076,896540588]

# --------------------------------------------------
list_host = ["tanlm","giangnbt","ducnt","phubh"]
host = [0,0,0,0]

score = [0,0,0,0]
total_score = [0,0,0,0]
host_today=[0,0,0,0]


# View the wallet data on Ethermine.

# store who is drink cafe
def store(id_user,msg):
    print(msg)
    host = [0,0,0,0]
    if "giang" in msg:
        host[1] = 1
    if "duc" in msg:
        host[2] = 1
    if "phu" in msg:
        host[3] = 1
    if "tan" in msg:
        host[0] = 1
#    if "thanht" in msg:
#        host[5] = 1
#    if "tuananh" in msg:
#        host[4] = 1
#    if "thanhict" in msg:
#        host[6] = 1
    #file=datetime.strftime(datetime.now() - timedelta(i), '%Y%m%d%H%M%S')
    sfile="/home/ducnt/test/cafe_bot/store/oder_history_cntt1.txt"
    #save to file
    os.system('echo "%s,%s,%s,%s" >> %s'  % (host[0],host[1],host[2],host[3],sfile))  
    text_send = u"*Order is success, would you know who is host to day?????????????????\n\n\n*"
    bot.send_message(chat_id=id_user, text=text_send, parse_mode="Markdown")
    

# delete last version
def cancel(id_user):
    #delete last row order_history
    row = getoutput("cat /home/ducnt/test/cafe_bot/store/oder_history_cntt1.txt | wc -l")
    head = int(row) - 1
    os.system("head -%s /home/ducnt/test/cafe_bot/store/oder_history_cntt1.txt > /tmp/order_temp_cntt1.txt" % (head))
    os.system("cat /tmp/order_temp_cntt1.txt > /home/ducnt/test/cafe_bot/store/oder_history_cntt1.txt")

    row_ = getoutput("cat /home/ducnt/test/cafe_bot/store/hosts_history_cntt1.txt | wc -l")
    head_ = int(row) - 1
    os.system("head -%s /home/ducnt/test/cafe_bot/store/hosts_history_cntt1.txt > /tmp/hosts_temp_cntt1.txt" % (head_))
    os.system("cat /tmp/hosts_temp_cntt1.txt > /home/ducnt/test/cafe_bot/store/hosts_history_cntt1.txt")


    text_send = u"\u26A0 Cancel last order is success!"
    bot.send_message(chat_id=id_user, text=text_send, parse_mode="Markdown")


def gethost(id_user):
    total_score = [0,0,0,0]
    order = [0,0,0,0]
    host_today = [0,0,0,0]
    number=getoutput("tail -1 /home/ducnt/test/cafe_bot/store/oder_history_cntt1.txt | gawk -F, '{for(i=1;i<=NF;i++) t+=$i; print t; t=0}'")
    #get history_score
    #lines=getoutput("tail -3 /home/ducnt/test/cafe_bot/store/oder_history_cntt1.txt")
    lines=getoutput("tail -%s /home/ducnt/test/cafe_bot/store/oder_history_cntt1.txt" % (number))
    for line in lines.split():
        print("LINEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
        print(line)
        print(line.split(",")[0])
        total_score[0]=int(line.split(",")[0]) + total_score[0]
        total_score[1]=int(line.split(",")[1]) + total_score[1]
        total_score[2]=int(line.split(",")[2]) + total_score[2]
        total_score[3]=int(line.split(",")[3]) + total_score[3]
#        total_score[4]=int(line.split(",")[4]) + total_score[4]
#        total_score[5]=int(line.split(",")[5]) + total_score[5]
#        total_score[6]=int(line.split(",")[6]) + total_score[6]
    

    #lines_=getoutput("tail -3 /home/ducnt/test/cafe_bot/store/hosts_history_cntt1.txt")
    lines_=getoutput("tail -%s /home/ducnt/test/cafe_bot/store/hosts_history_cntt1.txt" % (number))
    for line_ in lines_.split():
        print("LINEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
        print(line_)
        print(line_.split(",")[0])
        total_score[0]=int(line_.split(",")[0]) + total_score[0]
        total_score[1]=int(line_.split(",")[1]) + total_score[1]
        total_score[2]=int(line_.split(",")[2]) + total_score[2]
        total_score[3]=int(line_.split(",")[3]) + total_score[3]
#        total_score[4]=int(line_.split(",")[4]) + total_score[4]
#        total_score[5]=int(line_.split(",")[5]) + total_score[5]
#        total_score[6]=int(line_.split(",")[6]) + total_score[6]
    lines2=getoutput("tail -1 /home/ducnt/test/cafe_bot/store/oder_history_cntt1.txt")
    for x in lines2.split():
        order[0]=int(x.split(",")[0])
        order[1]=int(x.split(",")[1])
        order[2]=int(x.split(",")[2])
        order[3]=int(x.split(",")[3])
#        order[4]=int(x.split(",")[4])
#        order[5]=int(x.split(",")[5])
#        order[6]=int(x.split(",")[6])
#    print("LAST 7DAT POINT")
#    print(total_score)
    text_send = "*List last "  + str(number) + " rounds:* \n\n``` tanlm:" +str(total_score[0])+"\n giangnbt:"+str(total_score[1])+"\nducnt:"+str(total_score[2])+"\nphubh:"+str(total_score[3])+"```\n"
    bot.send_message(chat_id=id_user, text=text_send, parse_mode="Markdown")
    #temp[0,0,0,0,0,0]
    temp=total_score
    #print(host_today)    
    #tim nguoi min diem
    for i in range(0,len(temp)):
        if ( order[i] > 0 ):
            print("Ong nay co uong")
        else:
            temp[i] = 99
    id_hosts = temp.index(min(i for i in temp))
    print(id_hosts)
    print(list_host[id_hosts])
    host_today[id_hosts] = sum(order)
    sfile2="/home/ducnt/test/cafe_bot/store/host_now_cntt1.txt"
    #save to file
    os.system('echo "%s,%s,%s,%s" > %s'  % (host_today[0],host_today[1],host_today[2],host_today[3],sfile2))
    os.system('echo "%s,%s,%s,%s" >> /home/ducnt/test/cafe_bot/store/hosts_history_cntt1.txt'  % (host_today[0],host_today[1],host_today[2],host_today[3]))

    #return id_hosts

    text_send = u"\u26A0 Today, the chosen one is " + str(list_host[id_hosts])
    bot.send_message(chat_id=id_user, text=text_send, parse_mode="Markdown")

def alam_host(id_user):
    lines=getoutput("tail -1 /home/ducnt/test/cafe_bot/store/host_now_cntt1.txt")
    for line in lines.split():
        host[0]=int(line.split(",")[0])
        host[1]=int(line.split(",")[1])
        host[2]=int(line.split(",")[2])
        host[3]=int(line.split(",")[3])
#        host[4]=int(line.split(",")[4])
#        host[5]=int(line.split(",")[5])
#        host[6]=int(line.split(",")[6])
    id_hosts=host.index(max(i for i in host))
    print(list_host[id_hosts])
    text_send = u"\u26A0 Today, the chosen one is " + str(list_host[id_hosts])
    bot.send_message(chat_id=id_user, text=text_send, parse_mode="Markdown")

# We check if the user has permission.
def check_admin(id_user):
    check = id_user in id_admins
    return check


# Keyboard Telegram Bot
def keyboard(chat_id, textoEnvio):
    r1 = ["cafe", "hosts","cancel"]
    keyboard = [r1]
    news_keyboard = {'keyboard': keyboard, 'resize_keyboard': True}
    bot.send_message(chat_id, textoEnvio, None, None, json.dumps(news_keyboard))


if __name__ == "__main__":
    bot = telebot.TeleBot(token)


    # Welcome message.
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        id_user = message.chat.id
        permitted = check_admin(id_user)

        if (permitted == True):
            name = message.chat.first_name
            text_send = "Welcome " + name + "!!"
            keyboard(id_user, text_send)


    # Other messages.
    @bot.message_handler()
    def main(message):

        id_user = message.chat.id
        id_adm = message.from_user.id
        permitted = check_admin(id_adm)
        name = message.from_user.username
        #print(message)
        #print(str(name))
        #print(str(id_user))
        if (permitted == True):
            text = message.text
            print(message.text)

            if "cancel" in text:
                cancel(id_user)
            # Price button.
            elif "hosts" in text:
#                gethost(id_user)
                 alam_host(id_user)
            elif "uongcafe" in text:
                print('UONGCAFE')
                store(id_user,message.text)
                gethost(id_user)

        else:
             print(str(name))
             print(str(id_user))
             text_send = "Sorry " + str(name) + "! You not admin!"
             bot.send_message(chat_id=id_user, text=text_send, parse_mode="Markdown")

    bot.polling(none_stop=True)
