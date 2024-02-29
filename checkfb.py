

import requests,os
from user_agent import generate_user_agent
from bs4 import BeautifulSoup
os.system('clear')
request = requests.Session()
cookie = "sb=VF-XZS9sTryMUjiFP_-LHgow; c_user=100080781612506; xs=19%3Ax9KtK2-_WUMLtQ%3A2%3A1708372003%3A-1%3A5765; m_page_voice=100080781612506; fbl_ci=800276378277224; datr=G9rTZbu7SuMH221XRI4PJdCM; ps_n=0; ps_l=0; dpr=2.294114351272583; vpd=v1%3B797x424x2.294114351272583; locale=ar_AR; fbl_st=101533405%3BT%3A28484354; fbl_cs=AhDsgy%2FhZoWRG4pKgkcvxiKwGHJmNHZEMTBudmFnQnZYTG9hbGR2ZUJvQg; fr=15jUrV9zPPtbi8sT9.AWXQWqj2aPgRk2RCpAEmmpOJC0w.Bl2mvC.4F.AAA.0.0.Bl3jTO.AWXl0yZDpuA; m_pixel_ratio=2.294114351272583; wd=424x942; wl_cbv=v2%3Bclient_version%3A2419%3Btimestamp%3A1709202926"

url = request.get("https://mbasic.facebook.com/settings/apps/tabbed/",cookies= {"cookie": cookie}).text



html = BeautifulSoup(url, "html.parser")


a=html.find_all('div', class_='cr cs')
game_name = html.find_all("span", class_="ct cu")
#app_names = [tag.get_text(strip=True) for tag in game_name]
print(a)