import requests
from  bs4 import BeautifulSoup
import json


import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(url):
    """
    Retrieves the number of 'citation needed' occurrences on a web page.

    Args:
        url (str): The URL of the web page to parse.

    Returns:
        int: The count of 'citation needed' occurrences on the web page.
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all('span', string="citation needed")
    return len(results)


def get_citations_needed_report(url):
    """
    Retrieves the full text surrounding each 'citation needed' occurrence on a web page.

    Args:
        url (str): The URL of the web page to parse.

    Returns:
        str: The report containing the full text surrounding each 'citation needed' occurrence,
        separated by newlines ('\n').
    """
    string = ""
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all('span', string="citation needed")
    for res in results:
        string += ( "\n" + res.parent.parent.parent.parent.text )
    return string





if __name__ == "__main__":

    tst_url = "https://en.wikipedia.org/wiki/Numerical_control"
    tst_url2 = "https://en.wikipedia.org/wiki/Water_jet_cutter"
    print(get_citations_needed_count(tst_url))
    print(get_citations_needed_report(tst_url))