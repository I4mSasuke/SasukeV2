import json, requests, os
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
    update = requests.get('https://raw.githubusercontent.com/I4mKillua0/Update-Active/Sasuke/Sasuke%5BV1%5DUpdating/Sasuke%5BV1%5D/Version-Sasuke').text
    if 'Sasuke-V1.1' in update:
        pass
    else:
        vaup = 'New Update Now Available\nTry To Install New Update'
        s2(s1(vaup, style='green'))
except requests.exceptions.ConnectionError:
    vaE = s3('Connection Error', style='red')
    s4().print(vaE, style='A2CD5A')
    exit()
Print('New Update')
