import os
try:
  import requests
  from ms4 import InfoIG
  import random
  import time
  from rich.console import Console
  from rich.table import Table
  from rich.text import Text
  from secrets import token_hex
except:
  os.system("pip install requests ms4 rich")
  
import requests
from ms4 import InfoIG
import random
import time
from rich.console import Console
from rich.table import Table
from rich.text import Text
from secrets import token_hex

E = '\033[1;31m'
X = '\033[1;33m'
F = '\033[2;32m'
M = '\x1b[1;37m'
B = '\x1b[38;5;208m'
memo = random.randint(100, 300)
O = f'\x1b[38;5;{memo}m'

def nx():
    os.system("clear")
    Banner = f"""{B}{E}=============================={B}
|{F}[+] YouTube    : {B} ziddi_shop
|{F}[+] TeleGram   : {B} ziddi_beatz1     
|{F}[+] Tool  : {B} Report Instagram |
{E}==============================
"""
    for mm in Banner.splitlines():
        time.sleep(0.03)
        print(mm)

nx()

user = input(f' {F}({M}1{F}) {M} Target Username De Bkl {F} :  ' + O)
print(X + ' ═════════════════════════════════  ')
ses = input(f' {F}({M}2{F}) {M} Apni SessionId De{F} :  ' + O)
csr = token_hex(8) * 2
console = Console()
bb = 0
gg = 0

id = InfoIG.Instagram_Info(user)['ID']
if id == '':
    print("Try Again")
    exit(0)
else:
    pass

class Agent:
    @staticmethod
    def user():
        ii = ["165.1.0.29.119", "166.0.0.30.120", "167.0.0.31.121", "168.0.0.32.122"]
        aa = {
            "28/9": ["720dpi", "1080dpi", "1440dpi"],
            "29/10": ["720dpi", "1080dpi", "1440dpi", "2160dpi"],
            "30/11": ["1080dpi", "1440dpi", "2160dpi"],
            "31/12": ["1440dpi", "2160dpi"]
        }
        ss = {
            "720dpi": ["1280x720", "1920x1080"],
            "1080dpi": ["1920x1080", "2560x1440", "3840x2160"],
            "1440dpi": ["2560x1440", "3840x2160"],
            "2160dpi": ["3840x2160", "7680x4320"]
        }
        dd = {
            "samsung": ["SM-T292", "SM-G973F", "SM-A515F"],
            "google": ["Pixel 4", "Pixel 5"],
            "huawei": ["P30 Pro", "Mate 40 Pro"],
            "xiaomi": ["Mi 10", "Redmi Note 10"],
            "oneplus": ["8T", "9 Pro"],
            "sony": ["XZ2", "Xperia 1"]
        }
        cc = ["qcom", "exynos", "kirin", "mediatek", "apple"]
        lan = ["en_US", "es_ES", "fr_FR", "de_DE", "zh_CN", "ja_JP", "ko_KR"]
        dp = ["phone", "tablet", "watch", "tv", "car"]
        arm = ["arm64_v8a", "armeabi-v7a", "x86", "x86_64"]
        comb = ["samsung", "google", "huawei", "xiaomi", "oneplus", "sony"]

        sos = random.choice(list(aa.keys()))
        vlo = random.choice(aa[sos])
        lop = random.choice(ss[vlo])
        ki = random.choice(comb)
        mo = random.choice(dd.get(ki, ["Unknown"]))

        user_agent = (
            f"Instagram {random.choice(ii)} Android "
            f"({sos}; {vlo}; {lop}; {ki}; {mo}; "
            f"{random.choice(arm)}; {random.choice(dp)}; "
            f"{random.choice(lan)}; {random.choice(cc)})"
        )

        return user_agent
        
        
agent = Agent.user()
cookies={'sessionid': ses}
headers={'authority': 'www.instagram.com','accept': '*/*','accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7','content-type': 'application/x-www-form-urlencoded','origin': 'https://www.instagram.com','referer': f'https://www.instagram.com/{user}','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"','sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"','sec-ch-ua-mobile': '?1','sec-ch-ua-model': '"23127PN0CC"','sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"11.0.0"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': agent,'x-asbd-id': '129477','x-csrftoken': csr,'x-ig-app-id': '1217981644879628','x-ig-www-claim': 'hmac.AR2Byo5bRm6_izoL_9eIPaUsPfeL2eY-47tk4uVtcIq41BMn','x-instagram-ajax': '1016272294','x-requested-with': 'XMLHttpRequest',}

nok = {
    'container_module': 'profilePage',
    'entry_point': '1',
    'location': '2',
    'object_id': id,
    'object_type': '5',
    'frx_prompt_request_type': '1',
}

try:
  con = requests.post(
    'https://www.instagram.com/api/v1/web/reports/get_frx_prompt/',
    cookies=cookies,
    headers=headers,
    data=nok,
).json()['response']['context']
except:
	print("Erorr SessionId Please Try again")
	exit(0)


data = {
    'container_module': 'profilePage',
    'entry_point': '1',
    'location': '2',
    'object_id': id,
    'object_type': '5',
    'context': con,
    'selected_tag_types': '["prostitution"]',
    'action_type': '2',
    'frx_prompt_request_type': '2',
}
while True:
  time.sleep(7)
  res = requests.post(
    'https://www.instagram.com/api/v1/web/reports/get_frx_prompt/',
    cookies=cookies,
    headers=headers,
    data=data,
).text
  if '"status":"ok"' in res:
      gg += 1
      os.system('clear')
      table = Table(title="Instagram Reporter")
      table.add_column("Type", justify="center", style="cyan", no_wrap=True)
      table.add_column("Count", justify="center", style="magenta")
      table.add_row("DoneReport", str(gg), style="green")
      table.add_row("BadReport", str(bb), style="red")   
      table.add_row("Username", user, style="yellow")
      table.add_row("Dev", "ZIDDI ~~ @ziddi_shop")
      console.print(table)
  else:
      bb += 1
      os.system('clear')
      table = Table(title="Instagram Reporter")
      table.add_column("Type", justify="center", style="cyan", no_wrap=True)
      table.add_column("Count", justify="center", style="magenta")
      table.add_row("DoneReport", str(gg), style="green")
      table.add_row("BadReport", str(bb), style="red")   
      table.add_row("Username", user, style="yellow")
      table.add_row("Dev", "ZIDDI ~~ @ziddi_shop")
      console.print(table)
      

