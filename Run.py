# Mau Recode? oke silahkan
# ini juga gw hasil recode wkwk
#
#
#
# Maaf untuk pemilik asli Script ini
#
#
import requests
import os
from colorama import init, Fore, Style, Back
import time

init(autoreset=True)

def logo():
    os.system('clear')
    print(f"""{Fore.WHITE}
    
      NN   NN   GGGG  LL          SSSSS  PPPPPP    AAA   MM    MM       
      NNN  NN  GG  GG LL         SS      PP   PP  AAAAA  MMM  MMM       
      NN N NN GG      LL          SSSSS  PPPPPP  AA   AA MM MM MM       
      NN  NNN GG   GG LL              SS PP      AAAAAAA MM    MM       
      NN   NN  GGGGGG LLLLLLL     SSSSS  PP      AA   AA MM    MM       
{Fore.RED}                                                                        
UU   UU         LL      iii             iii tt    iii tt    iii      dd 
UU   UU nn nnn  LL          mm mm mmmm      tt        tt             dd 
UU   UU nnn  nn LL      iii mmm  mm  mm iii tttt  iii tttt  iii  dddddd 
UU   UU nn   nn LL      iii mmm  mm  mm iii tt    iii tt    iii dd   dd 
 UUUUU  nn   nn LLLLLLL iii mmm  mm  mm iii  tttt iii  tttt iii  dddddd 
                                                                        
                                                                        
    """)

def ng():

    nglusername = input(f"{Fore.BLUE}{Style.BRIGHT}Username: ")
    message = input(f"{Fore.YELLOW}{Back.GREEN}{Style.BRIGHT}Message: ")
    id = int(input("{Fore.BLACK}{Back.WHITE}{Style.BRIGHT}Masukan huruf dan nomor ( 6 karakter) : "))
    
    value =0
    notsend =0
    while True:
        headers = {
            'Host': 'ngl.link',
            'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36',
            'sec-ch-ua-platform': '"Android"',
            'origin': 'https://ngl.link',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://ngl.link/',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            }

        data = {
            'username': f'{nglusername}',
            'question': f'{message}',
            'deviceId': f'{id}',
            'gameSlug': '',
            'referrer': '',
        }


        response = requests.post('https://ngl.link/api/submit',headers=headers, data=data)
        if response.status_code == 200:
            notsend = 0
            value += 1
            print(f"{Fore.GREEN}{Style.BRIGHT}Terkirim >>")
        else:
            notsend += 1
            print(f"{Fore.RED}{Style.BRIGHT}Tidak Terkirim !")
        if notsend == 10:
            print(f"{Fore.YELLOW}Tunggu 2 Detik")
            time.sleep(2)
            notsend = 0
if __name__ == "__main__":
    logo()
    ng()
