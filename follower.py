from instapy import InstaPy
from colorama import Fore as c
import time
import os , sys
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
def loding():
    a = ['/', '-', '\\' , '|']
    for i in range(5):
        for x in a:
            sys.stdout.write((f'\rLoding..{x}'))
            time.sleep(0.1)
            sys.stdout.flush()
def P(txt):
    for i in txt:
        print( i , end='' , flush=True)
        time.sleep(0.00000000000000001)
P(f'''

{c.YELLOW}+{c.GREEN}-------------------------------------{c.YELLOW}+
{c.GREEN}| {c.LIGHTBLUE_EX}[{c.YELLOW}%{c.LIGHTBLUE_EX}]{c.WHITE} Python V3                       {c.GREEN}|
{c.GREEN}| {c.LIGHTBLUE_EX}[{c.YELLOW}^{c.LIGHTBLUE_EX}]{c.WHITE} InstaGram Bot                   {c.GREEN}|
{c.GREEN}| {c.LIGHTBLUE_EX}[{c.YELLOW}&{c.LIGHTBLUE_EX}]{c.WHITE} Follow And Unfollow             {c.GREEN}|
{c.GREEN}| {c.LIGHTBLUE_EX}[{c.YELLOW}*{c.LIGHTBLUE_EX}]{c.WHITE} Created By MAXTOR                 {c.GREEN}|
{c.GREEN}| {c.LIGHTBLUE_EX}[{c.YELLOW}+{c.LIGHTBLUE_EX}]{c.WHITE} My Id : {c.LIGHTCYAN_EX}@CYROSIF           {c.GREEN}|
{c.GREEN}| {c.LIGHTBLUE_EX}[{c.YELLOW}+{c.LIGHTBLUE_EX}]{c.WHITE} My Channel : {c.LIGHTCYAN_EX}@CYROSIF{c.GREEN}|
{c.YELLOW}+{c.GREEN}-------------------------------------{c.YELLOW}+


''')
user_name = input(f"{c.RED}[#]{c.GREEN}Enter The User Name For Login : ")
password = input(f"{c.RED}[#]{c.GREEN}Enter The Password Name For Login : ")

session = InstaPy(username=user_name, password=password)
session.login()

def follow(name_list , sleep):
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    for i in name_list:
        time.sleep(sleep)
        session.follow_user_followers(name_list,
                                      amount=10,
                                      randomize=False,
                                      interact=True)
        P(f"{c.GREEN}[{c.WHITE}+{c.GREEN}]{c.WHITE}Followed User {c.YELLOW}: {c.GREEN}{i}")

def unfollow(customList , sleep):
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    for i in customList:
        custom_list = [i]
        session.unfollow_users(amount=10,
                               customList=(True, custom_list, "all"),
                               style="RANDOM",
                               unfollow_after=55 * 60 * 60,
                               sleep_delay=sleep
                        )
        P(f"{c.GREEN}[{c.WHITE}-{c.GREEN}]{c.RED}Unfollow User : {c.YELLOW}{i}")
        time.sleep(sleep)

name_follower = [
    "taeyong",
    "TVXQ",
    "EXO",
    "D.O",
    "Donya",
    "H.rah",
    "Therock",
    "Khodekhalse",
    "braveputak",
    "instagram",
    "pooyanmokhtari",
    "sijaloffical",
    "sohmj",
    "koorowsh",
    "behzadleito",
]

while True:
    sleep = input(f"{c.RED}[{c.YELLOW}+{c.RED}] {c.GREEN}Enter The Number Sleep For limit [ 1,50 ]:~#  ")
    q = input(f"{c.RED}[{c.YELLOW}-{c.RED}] {c.GREEN}You Do Not Want Me To Follow Them ?Yes Or No:~# ")
    loding()
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    follow(name_follower , sleep)
    if q == 'yes':
        unfollow(name_follower , sleep)
    else:
        print("Ok.!")