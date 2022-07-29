from collections import Counter

from bs4 import BeautifulSoup
import requests

AMAZON = "amazon.com"
# static copy
TIM_BLOG = ('https://bites-data.s3.us-east-2.amazonaws.com/'
            'tribe-mentors-books.html')
MIN_COUNT = 3


def load_page():
    """Download the blog html and return its decoded content"""
    with requests.Session() as session:
        return session.get(TIM_BLOG).content.decode('utf-8')


def get_top_books(content=None):
    """Make a BeautifulSoup object loading in content,
       find all links that contain AMAZON, extract the book title
       (stripping spacing characters), and count them.
       Return a list of (title, count) tuples where
       count is at least MIN_COUNT
    """
    if content is None:
        content = load_page()

    # code here ...
    soup = BeautifulSoup(content, "html.parser")
    link_list = soup.select("a")
    # print(link_list)
    result = {}
    for link in link_list:
        if AMAZON in link.get_attribute_list("href")[0]:
            # print(link.text.strip())
            try:
                result[link.text.strip()] += 1
            except KeyError:
                result[link.text.strip()] = 1

    # print(result)
    # result2 = []
    # for k in result.keys():
    #     if result[k] >= MIN_COUNT:
    #         result2.append((k, result[k]))
    # print(result2)
    # return result2

    # print([(k, result[k]) for k in result.keys() if result[k] >= MIN_COUNT])
    return [(k, result[k]) for k in result.keys() if result[k] >= MIN_COUNT]


# solution provided
# def get_top_books(content=None):
#     """Make a BeautifulSoup object loading in content,
#        find all links that contain AMAZON, extract the book title
#        (stripping spacing characters), and count them.
#        Return a list of (title, count) tuples where
#        count is at least MIN_COUNT
#     """
#     if content is None:
#         content = load_page()
#
#     soup = BeautifulSoup(content, "html.parser")
#
#     books = [link.text.strip() for link in soup.find_all("a")
#              if AMAZON in link["href"]]
#
#     return [book for book in Counter(books).most_common()
#             if book[1] >= MIN_COUNT]

if __name__ == '__main__':
    get_top_books()
