import bs4, requests

def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#buyNewSection > h5 > div > div.a-column.a-span8.a-text-right.a-span-last > div > span.a-size-medium.a-color-price.offer-price.a-text-normal')
    return elems[0].text.strip()


price = getAmazonPrice('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/ref=sr_1_1?crid=30Z6ZVHQ95ULN&keywords=automate+the+boring+stuff+with+python&qid=1560760443&s=books&sprefix=automate+th%2Cgarden%2C151&sr=1-1')
print('The price is ' + price)
