from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

PACKT = 'https://bites-data.s3.us-east-2.amazonaws.com/packt.html'
CONTENT = requests.get(PACKT).text

Book = namedtuple('Book', 'title description image link')


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    # print(CONTENT)
    soup = Soup(CONTENT, 'html.parser')
    # print(soup.prettify())
    title = soup.findAll(class_="dotd-title")[0].text.strip()
    link = soup.select("div.dotd-main-book-image a")[0].get_attribute_list("href")[0]
    image = ""
    for img in soup.select("img"):
        if "dotd_main_image" in img.get_attribute_list("src")[0]:
            image = img.get_attribute_list("src")[0]
            break

    description = soup.select("div.dotd-main-book-summary div")[2].text.strip()

    return Book(title, description, image, link)


# solution provided
# def get_book():
#     soup = Soup(CONTENT, 'html.parser')
#     book_image = soup.find('div', {'class': 'dotd-main-book-image'})
#     link = book_image.find('a').get('href')
#     image = book_image.find('img').get('src')
#     book_main = soup.find('div', {'class': 'dotd-main-book-summary'})
#     title_div = book_main.find('div', {'class': 'dotd-title'})
#     title = title_div.find('h2').text.strip()
#     descr_div = title_div.find_next_sibling("div")
#     description = descr_div.text.strip()
#
#     return Book(title=title,
#                 description=description,
#                 image=image,
#                 link=link)


if __name__ == '__main__':
    get_book()
