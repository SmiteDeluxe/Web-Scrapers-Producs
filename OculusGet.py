import requests
from bs4 import BeautifulSoup


URLs = [
    'https://www.amazon.fr/Oculus-Quest-virtuelle-tout-en-g%C3%A9n%C3%A9ration/dp/B08HHD6S26/ref=sr_1_1_sspa?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=27TIZH9QA2WSV&dchild=1&keywords=oculus%2Bquest%2B2&qid=1609164031&quartzVehicle=72-827&replacementKeywords=oculus%2Bquest&sprefix=ocu%2Caps%2C247&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyUzdBRkUwSDVJVFAzJmVuY3J5cHRlZElkPUEwNTE4MDg5MzI5UjVKTUJORVFZSCZlbmNyeXB0ZWRBZElkPUEwNTU5NTAzRUVWSldBNUhHVzhUJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1',
    "https://www.amazon.es/Oculus-Quest-realidad-virtual-avanzado/dp/B08HHD6S26/ref=sr_1_1_sspa?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2YDQMSLXQ6XSH&dchild=1&keywords=oculus%2Bquest%2B2&qid=1609163027&quartzVehicle=72-1783&replacementKeywords=oculus%2Bquest&sprefix=oc%2Caps%2C223&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzU1dJTE5SOTRBV0oyJmVuY3J5cHRlZElkPUEwNjcwNDE4VjI2STlZMldBT1NOJmVuY3J5cHRlZEFkSWQ9QTA0NDMxMTMxSU9YQlRZVTdLV1JZJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1",
    "https://www.amazon.co.uk/Oculus-Quest-2-64-GB/dp/B08HK24JSD?tag=pcmaguk-21&ascsubtag=06sjy0uFq32KpDQroaZzU2N&th=1",
    "https://www.amazon.it/dp/B08HHD6S26/ref=twister_B08JDNY8C3?_encoding=UTF8&psc=1"]
countries = ['France','Spain','UK','Italy']
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}


def checkAvail():
    found = False
    i = 0

    while not found:
        page = requests.get(URLs[i], headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        price = soup.find(id='desktop_qualifiedBuyBox')

        if price is not None:
            found = True
            print('Found in', countries[i])
        else:
            print('Not found in', countries[i])
        i += 1
        if i == len(URLs):
            i = 0


checkAvail()
