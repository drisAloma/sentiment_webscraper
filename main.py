import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import pandas as pd 
import time

def top_10_crypto(url):
    
    # Requesting HTTP connection
    response = requests.get(url)
    
    # Creating soup object
    soup = BeautifulSoup(response.content, 'html.parser')
    
    #Extracting Top 10 crypto by market cap 
    results = soup.find('tbody').find_all('tr')[0:10]
    
    # Details container
    name = []
    ticker = []
    price = []
    marketcap = []
    supply = []
    volume = []
    
    # Name
    for result in results:
        name.append(result.find('p',{'class':'sc-1eb5slv-0 iworPT'}).get_text())
    
    # Ticker
    for result in results:
        ticker.append(result.find('p',{'class':'sc-1eb5slv-0 gGIpIK coin-item-symbol'}).get_text())
    
    # Price
    for result in results:
        price.append(result.find('div',{'class':'sc-131di3y-0 cLgOOr'}).get_text())
    
    # Market cap
    for result in results:
        marketcap.append(result.find('span',{'class':'sc-1ow4cwt-0 iosgXe'}).get_text())
    
    # Supply
    for result in results:
        supply.append(result.find('p',{'class':'sc-1eb5slv-0 kZlTnE'}).get_text())
    
    # 24h Volume traded
    for result in results:
        volume.append(result.find('p',{'class':'sc-1eb5slv-0 hykWbK font_weight_500'}).get_text())
    
    # Creating DataF=frame
    
    coin_details = pd.DataFrame({'Name': name, 'Symbol': ticker, 'Price': price, 'Market Cap': marketcap,
                                 'Circulating Supply': supply, '24H traded volume': volume})
    
    return coin_details

if __name__ == '__main__':
    output = top_10_crypto('https://coinmarketcap.com')
    print(output)
    
