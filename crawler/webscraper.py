import json 
from bs4 import BeautifulSoup
from requests import Session, RequestException
from rich import print

HEADERS = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0"}
INPUT_PATH = "/home/moritz/workspace/MyFirstApp/season_links.json"

def read_json(path: str) -> dict: 
    with open(path,"r") as file: 
        data = json.load(file)
    return data 

def request_url(session: Session, url: str, retries:int =3, timeout: int = 10 ):
    for _ in range (retries):
        try:
            response = session.get(url=url, timeout=timeout,  headers=HEADERS)
            response.raise_for_status() 

            return response.text

       
        except RequestException as raised_exception: 
            print(f"Die Anfrage an {url} ist fehlgeschlagen.")
            continue
    print(f"Die Anfrage an {url} ist final fehlgeschlagen.")
    return 

def parse_html_to_soup(html: str) -> BeautifulSoup:
        return BeautifulSoup(html, "html.parser")


def main():
    boxscore_links = read_json(path=INPUT_PATH)
    http_session=Session()

    url= "https://www.pro-football-reference.com/boxscores/202309110nyj.htm"
    html = request_url(session=http_session, url=url)
    soup =  parse_html_to_soup(html)
    table = soup.find("table", class_="linescore")
    
    print(table)

    # for key, urls in boxscore_links.items():
    #     print(key)

    #     for urls in links: 
    return 

if __name__ == "__main__": 
    main()