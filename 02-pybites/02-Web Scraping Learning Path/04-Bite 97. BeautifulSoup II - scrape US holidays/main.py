from collections import defaultdict
import os
from urllib.request import urlretrieve

from bs4 import BeautifulSoup

# prep data
tmp = os.getenv("TMP", "/tmp")
page = 'us_holidays.html'
holidays_page = os.path.join(tmp, page)
urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{page}',
    holidays_page
)

with open(holidays_page) as f:
    content = f.read()

holidays = defaultdict(list)


def get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    # print(content)
    soup = BeautifulSoup(content, "html.parser")
    # print(soup.select(".holiday a")[0].text)
    # print(soup.select(".holiday time")[0].text[5:7])
    titulos = soup.select(".list-table a")
    meses = soup.select(".list-table time")
    resultado = {}
    for i in range(len(titulos)):
        print(meses[i].text[5:7] + " -- " + titulos[i].text)
        # print(titulos[i].text)
        if meses[i].text[5:7] in resultado:
            resultado[meses[i].text[5:7]].append(titulos[i].text.strip())
        else:
            resultado[meses[i].text[5:7]] = [titulos[i].text.strip()]
    print(resultado)
    return resultado

# solution given
# def get_us_bank_holidays(content=content):
#     """Receive scraped html output, make a BS object, parse the bank
#        holiday table (css class = list-table), and return a dict of
#        keys -> months and values -> list of bank holidays"""
#     soup = BeautifulSoup(content, 'html.parser')
#     table = soup.find_all("table", class_="list-table")
#
#     # start at 2nd item ignoring header
#     for tr in table[0].find_all('tr')[1:]:
#         time = tr.find('time')
#         href = tr.find('a')
#         day = href.text.strip()
#         yy, mm, dd = time.text.split('-')  # or use dt.striptime
#         holidays[mm].append(day)
#
#     return holidays


if __name__ == '__main__':
    get_us_bank_holidays()
