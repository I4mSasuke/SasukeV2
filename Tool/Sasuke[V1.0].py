#|–––––––––––––––––––––– Info ––––––––––––––––––––––|
# Creator : 𝑆𝑎𝑠𝑢𝑘𝑒 » 𝑀𝑜𝓃𝓈𝓉𝑒𝓇
# Telegram : @I4m_Sasuke
# Channel : @I4MxCRACKERS
# Channel's Group : @I4MxCRACKERS_group




#|–––––––––––––––––––––– Utf-8 ––––––––––––––––––––––|
# -*- coding: utf-8 -*-



#|–––––––––––––––––––––– Modules ––––––––––––––––––––––|
import os



try:
    import rich
except ImportError:
    ri =('The Rich Module Not Installed yet .....')
    print(ri)
    os.system('pip install rich')
from rich.panel import Panel as s1
from rich import print as s2
from rich.markdown import Markdown as s3
from rich.console import Console as s4
try:
    import wget
except ImportError:
    os.system('clear')
    la= '\n [\xc3\x97] The Wget module is not installed!...\n'
    la1=s2(s1(la, style='red'))
    os.system('pip install wget')

try:
    import requests
except ImportError:
    os.system('clear')
    la= '\n [\xc3\x97] The requests module is not installed!...\n'
    la1=s2(s1(la, style='red'))
    os.system('pip install requests')

try:
    open('/data/data/com.termux/files/usr/bin/lolcat').read()
except FileNotFoundError:
    os.system('clear')
    la= '\n [\xc3\x97] The lolcat is not installed!...\n'
    la1=s2(s1(la, style='red'))
    os.system('pip install lolcat')






import requests, random, sys, uuid, time, wget, rich





#|––––––––––––––––––––––Date And Time––––––––––––––––––––––|
from datetime import datetime
now = datetime.now()
kat =  now.strftime("%H:%M:%S")
date = now.strftime("%d/%m/%Y")





try:
    os.system('clear')
    update = requests.get('https://raw.githubusercontent.com/I4mKillua0/Update-Active/Sasuke/Sasuke%5BV1%5DUpdating/Sasuke%5BV1%5D/Version-Sasuke').text
    if 'Sasuke-V1.0' in update:
        pass
    else:
        vaup = 'New Update Now Available\nTry To Install New Update'
        s2(s1(vaup, style='green'))
        os.system("rm 'Sasuke[V1.0].py'")
        wget.download('https://raw.githubusercontent.com/I4mSasuke/SasukeV1/main/Tool/sy.py')
        os.system('clear')
        os.system('python name.py')
except requests.exceptions.ConnectionError:
    vaE = s3('Connection Error', style='red')
    s4().print(vaE, style='A2CD5A')
    exit()
        







#|––––––––––––––––––––––Colours––––––––––––––––––––––|
x = '\33[m' # DEFAULT
k = '\033[93m' # Yellow kall
h = '\033[1;92m' # Bi Green
hh = '\033[32m' # Green
u = '\033[95m' # Pink
kk = '\033[33m' # Yellow
b = '\33[1;96m' # Shini kall
p = '\033[0;34m' # Blue










#|–––––––––––––––––––––– Banner ––––––––––––––––––––––|
def banner():
    os.system('clear')
    os.system('echo "\n\n \n  ██████  ▄▄▄        ██████  █    ██  ██ ▄█▀▓█████ \n▒██    ▒ ▒████▄    ▒██    ▒  ██  ▓██▒ ██▄█▒ ▓█   ▀ \n░ ▓██▄   ▒██  ▀█▄  ░ ▓██▄   ▓██  ▒██░▓███▄░ ▒███   \n  ▒   ██▒░██▄▄▄▄██   ▒   ██▒▓▓█  ░██░▓██ █▄ ▒▓█  ▄ \n▒██████▒▒ ▓█   ▓██▒▒██████▒▒▒▒█████▓ ▒██▒ █▄░▒████▒\n▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░\n░ ░▒  ░ ░  ▒   ▒▒ ░░ ░▒  ░ ░░░▒░ ░ ░ ░ ░▒ ▒░ ░ ░  ░\n░  ░  ░    ░   ▒   ░  ░  ░   ░░░ ░ ░ ░ ░░ ░    ░   \n      ░        ░  ░      ░     ░     ░  ░      ░  ░\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nCreator        :  𝑆𝑎𝑠𝑢𝑘𝑒 » 𝑀𝑜𝓃𝓈𝓉𝑒𝓇\nUSERNAME       :  @i4m_Sasuke\nTelegram       :  https://t.me/I4MxCRACKERS\n––––––––––––––––––––––––––––––\n" | lolcat -a -d 2 -s 1000')












#|–––––––––––––––––––––– Approval ID––––––––––––––––––––––|
def Sasuke():
    
    try:
        
        id = open('/data/data/com.termux/files/usr/bin/.Sasukev1.txt','r').read()
        
    except IOError:
        key1 = open('/data/data/com.termux/files/usr/bin/.Sasukev1.txt','a')
        userid = uuid.uuid4().hex[:15]
        userid1 = ('-Sasuke')
        users = (userid1)
        id = (userid+users)
        key1.write(id)
        key1.close()
    id = open('/data/data/com.termux/files/usr/bin/.Sasukev1.txt','r').read()
    banner()
    print ('\x1b[37;1m YOUR ID : ' + id+'·_·')
    try:
        http = requests.get('https://raw.githubusercontent.com/I4mKillua0/Login/main/id.txt').text
        ip = requests.get('http://ip-api.com/json/').text
    except requests.exceptions.ConnectionError:
        clear()
        li = '# ba helly internet nabastrawetatawa'
        lo = mark(li, style='red')
        sol().print(lo, style='cyan')
        sys.exit()
    if id in http:
        print('Your ID Activated')
        time.sleep(3)
        
        menu()
    else:
        print ('\x1b[91mYour Id Not Approval: @I4m_Sasuke.......')
        
        requests.post('https://api.telegram.org/bot5865795383:AAGdprMuOn2WNUFgw0u9t-vbTFu3rx_G7aY/sendMessage?chat_id=1301202611&text='+'\n ID: '+id+'\n'+'IP'+ip)
        time.sleep(2)
        sys.exit()

            
            
            
    

















def menu():
    banner()
    kat =  now.strftime("%H:%M:%S")
    
    va = 'Creator : I4m_Sasuke\nVersion : 1.00\nTime : '+kat+' \nDate : '+date
    ka = s1(va, style='#A2CD5A')
    s2(s1(ka, style='#CAFF70', title ='Info Creator'))
    
    va2='[00] Social Media Of Creator'
    ka2=s1(va2,style='#FFE4C4')
    s2(s1(ka2, style='#76EEC6', title='Social Media'))


    va1 = '[01] Fixing && Installing All Pkg & Modules\n[02] Fixing Cookie Login\n[03] Creating Combo Iraq\n[04] Creating FB File\n[05] Encoding File\n[06] Crack Facebook {Id, File}\n[07] exit Tool'
    ka1 = s1(va1, style ='#FFE4C4')
    s2(s1(ka1, style='#76EEC6', title ='Scripts'))
    Sasuke = input(x+'['+p+'ᦓꪖᦓꪊᛕꫀ'+x+'] Choose One: ')
    if Sasuke in ['0','00']:
        va3 ='[01] Telegram\n[02] Channel Telgram\n[03] Tiktok\n[04] SnapChat'
        ka3= s1(va3, style='#76EE00')
        s2(s1(ka3, title='Social Media Of Creator', style='#FFF8DC'))
        Sasuke1 = input(x+'['+p+'ᦓꪖᦓꪊᛕꫀ'+x+'] Choose One: ')
        if Sasuke1 in ['1','01']:
            va4 = '# OPENING ......'
            ka4 = s3(va4, style='green')
            s4().print(ka4, style='green')
            
            os.system('xdg-open https://t.me/I4M_sasuke')
            time.sleep(4)
            exit()
        elif Sasuke1 in ['2','02']:
            va4 = '# OPENING ......'
            ka4 = s3(va4, style='green')
            s4().print(ka4, style='green')
            os.system('xdg-open https://t.me/I4MxCRACKERS')
            time.sleep(4)
            exit()
        elif Sasuke1 in ['3','03']:
            va4 = '# OPENING ......'
            ka4 = s3(va4, style='green')
            s4().print(ka4, style='green')
            os.system('xdg-open https://www.tiktok.com/@i4m_sasuke')
            time.sleep(4)
            exit()
        elif Sasuke1 in ['4','04']:
            va4 = '# OPENING ......'
            ka4 = s3(va4, style='green')
            s4().print(ka4, style='green')
            os.system('xdg-open https://www.snapchat.com/add/i4m_sasuke?share_id=Qwqwo_WFJqQ&locale=en-GB')
            time.sleep(4)
            exit()
    elif Sasuke in ['1','01']:
        try:
            open('rek.py','r').read()
            print('Opening Tool...')
            time.sleep(2)
            os.system('python rek.py')
            exit()
        except FileNotFoundError:
            print('Not now')
            os.system('rek.py')
            exit()













#|–––––––––––––––––––––– Using ––––––––––––––––––––––|

if __name__=='__main__': 
	menu()