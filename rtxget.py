import requests
import re
import time
from datetime import datetime
from twilio.rest import Client
from bs4 import BeautifulSoup
from playsound import playsound

URLs = ['https://www.hardwareluxx.de/community/threads/rtx-3060ti-gpu-verf%C3%BCgbarkeitshinweise.1284025/page-30',
        'https://www.hardwareluxx.de/community/threads/rtx-3070-gpu-verf%C3%BCgbarkeitshinweise.1284024/page-420',
        'https://www.hardwareluxx.de/community/threads/rtx-3070ti-gpu-verf%C3%BCgbarkeitshinweise.1298653/page-70',
        'https://www.hardwareluxx.de/community/threads/rtx-3080-gpu-verf%C3%BCgbarkeitshinweise.1281755/page-250']
countries = ['3060', '3060 ti', '3070', '3070 ti', '3080']
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/87.0.4280.88 Safari/537.36'}

client = Client('AC122d1d206c088b01a8c893d1ee8b7dd8', 'a955590c5e57c21076d9878837917596')


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def checkAvail():
    found = False
    i = 0
    run = -3
    pricelist60ti = []
    pricelist70 = []
    pricelist70ti = []
    pricelist80 = []

    while True:
        page = requests.get(URLs[i], headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        price = soup.body.findAll("div", {"class": "bbWrapper"})

        j = 1

        if i == 0:
            print("\nChecking for RTX 3060 ti:")
            for prices in price:
                if j > len(pricelist60ti):
                    m = re.search('Preis:\s(\d+)', str(prices))
                    m1 = re.search('href="(.+)"\srel', str(prices))

                    if m and m1:
                        pricenew = str(m.group(1)).strip()
                        pricelist60ti.append(pricenew)
                        now = datetime.now()
                        current_time = now.strftime("%H:%M:%S")

                        if int(m.group(1)) <= 600:
                            print(bcolors.OKGREEN + pricenew + '€ at ' + current_time, '\n', m1.group(1) + bcolors.ENDC)
                            if run > 0 and int(m.group(1)) <= 600:
                                playsound('alarm.mp3')
                        elif int(m.group(1)) <= 720:
                            print(bcolors.WARNING + pricenew + '€ at ' + current_time, '\n', m1.group(1) + bcolors.ENDC)
                        else:
                            print(bcolors.FAIL + pricenew + '€ at ' + current_time + bcolors.ENDC)

                j += 1
        elif i == 1:
            print("\nChecking for RTX 3070:")
            for prices in price:
                if j > len(pricelist70):
                    m = re.search('Preis:\s(\d+)', str(prices))
                    m1 = re.search('href="(.+)"\srel', str(prices))

                    if m and m1:
                        pricenew = str(m.group(1)).strip()
                        pricelist70.append(pricenew)
                        now = datetime.now()
                        current_time = now.strftime("%H:%M:%S")

                        if int(m.group(1)) <= 720:
                            print(bcolors.OKGREEN + pricenew + '€ at ' + current_time, '\n', m1.group(1) + bcolors.ENDC)

                            if run > 0 and int(m.group(1)) <= 720:
                                playsound('alarm.mp3')
                        elif int(m.group(1)) <= 1000:
                            print(bcolors.WARNING + pricenew + '€ at ' + current_time, '\n', m1.group(1) + bcolors.ENDC)
                        else:
                            print(bcolors.FAIL + pricenew + '€ at ' + current_time + bcolors.ENDC)

                j += 1
        elif i == 2:
            print("\nChecking for RTX 3070 ti:")
            for prices in price:
                if j > len(pricelist70ti):
                    m = re.search('Preis:\s(\d+)', str(prices))
                    m1 = re.search('href="(.+)"\srel', str(prices))

                    if m and m1:
                        pricenew = str(m.group(1)).strip()
                        pricelist70ti.append(pricenew)
                        now = datetime.now()
                        current_time = now.strftime("%H:%M:%S")

                        if int(m.group(1)) <= 820:
                            print(bcolors.OKGREEN + pricenew + '€ at ' + current_time, '\n', m1.group(1) + bcolors.ENDC)

                            if run > 0 and int(m.group(1)) <= 820:
                                playsound('alarm.mp3')
                        elif int(m.group(1)) <= 1050:
                            print(bcolors.WARNING + pricenew + '€ at ' + current_time, '\n', m1.group(1) + bcolors.ENDC)
                        else:
                            print(bcolors.FAIL + pricenew + '€ at ' + current_time + bcolors.ENDC)

                j += 1
        elif i == 3:
            print("\nChecking for RTX 3080:")
            for prices in price:
                if j > len(pricelist80):
                    m = re.search('Preis:\s(\d+)', str(prices))
                    m1 = re.search('href="(.+)"\srel', str(prices))

                    if m and m1:
                        pricenew = str(m.group(1)).strip()
                        pricelist80.append(pricenew)
                        now = datetime.now()
                        current_time = now.strftime("%H:%M:%S")

                        if int(m.group(1)) <= 1200:
                            print(bcolors.OKGREEN + pricenew + '€ at ' + current_time, '\n', m1.group(1) + bcolors.ENDC)

                            if run > 0 and int(m.group(1)) <= 1200:
                                playsound('alarm.mp3')
                        elif int(m.group(1)) <= 1300:
                            print(bcolors.WARNING + pricenew + '€ at ' + current_time, '\n', m1.group(1) + bcolors.ENDC)
                        else:
                            print(bcolors.FAIL + pricenew + '€ at ' + current_time + bcolors.ENDC)

                j += 1

        i += 1
        if i == len(URLs):
            i = 0
        run += 1
        time.sleep(10)


checkAvail()
