import requests
from bs4 import BeautifulSoup


def Eventos():
  page = requests.get('https://www.ingressodigital.com/')
  soup = BeautifulSoup(page.text, 'html.parser') 
  divs_info = soup.find_all("div", class_='evnts__cntnt')
  for div in soup.find_all("div", class_='evnts__cntnt'):
    print(div.find("li").get_text(),"-",div.find("h2").get_text())
        
if __name__ == "__main__":
  print("Eventos e Shows:\n")
  Eventos()