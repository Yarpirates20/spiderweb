import bs4
import requests

def getHTML(url: str) -> bs4.BeautifulSoup:
    res = requests.get(url)
    res.raise_for_status()
    page = bs4.BeautifulSoup(res.content , 'html.parser')

    return page