import requests
from  bs4 import BeautifulSoup
import json


def get_citations_needed_count(url):

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all('span', string="citation needed")
    return len(results)

def get_citations_needed_report(url):

    string =""
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all('span', string="citation needed")
    for res in results :
        string += (res.parent.parent.parent.parent.text + "\n")
    return "\n" + string




if __name__ == "__main__":

    tst_url = "https://en.wikipedia.org/wiki/Numerical_control"
    tst_url2 = "https://en.wikipedia.org/wiki/Water_jet_cutter"
    print(get_citations_needed_count(tst_url))
    print(get_citations_needed_report(tst_url))