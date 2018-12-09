#!/usr/bin/env python

# @author      : nevernew (nevernew@mail.ru)
# @created     : 07/12/2018
# @description : simply send for google mail

fromaddr = "name@gmail.com"
toaddr = "example@mail.ru"
pas = "pass"
msg ="Hello!" # The /n separates the message from the headers

import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
#server.connect("smtp.google.com",465)
server.ehlo()
server.starttls()
server.ehlo()
server.login(fromaddr, pas)

#Send the mail
server.sendmail(fromaddr, toaddr, msg)
server.quit()

