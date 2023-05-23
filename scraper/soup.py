import requests
from bs4 import BeautifulSoup

def scrap_subjects():
    subjects = {}
    url = 'https://github.com/shreeshailaya/C-DAC-Notes'
    response = requests.get(url)

    # Create a BeautifulSoup object by passing the HTML content and specify the parser
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all(class_ = 'js-navigation-open Link--primary')
    print(type(links))
    for i in links:
        subjects[i.get_text()] =  "www.github.com"+i["href"]

    
        
    
    return subjects



if __name__ == "__main__":
    scrap_subjects()
