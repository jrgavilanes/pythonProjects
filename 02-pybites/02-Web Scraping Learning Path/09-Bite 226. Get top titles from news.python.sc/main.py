from collections import namedtuple

from bs4 import BeautifulSoup
import requests

# feed = https://news.python.sc/, to get predictable results we cached
# first two pages - use these:
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index2.html

Entry = namedtuple('Entry', 'title points comments')


def _create_soup_obj(url):
    """Need utf-8 to properly parse emojis"""
    resp = requests.get(url)
    resp.encoding = "utf-8"
    return BeautifulSoup(resp.text, "html.parser")


def get_top_titles(url, top=5):
    """Parse the titles (class 'title') using the soup object.
       Return a list of top (default = 5) titles ordered descending
       by number of points and comments.
    """
    soup = _create_soup_obj(url)

    # your code ...
    titles = soup.select("span.title")
    scores = soup.select("span.controls span.smaller")

    result = []
    for i in range(len(titles)):
        title = titles[i].text.strip()
        score = scores[i].text.strip().split(" ")[0]
        comments = scores[i].text.strip().split(" ")[-2]
        result.append(Entry(title=title, points=int(score), comments=int(comments)))

    result = sorted(result, key=lambda x: (-x[1], -x[2]))[:top]
    print(result)
    return result


if __name__ == '__main__':
    get_top_titles("https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html")

# solution provided
# from collections import namedtuple
# from operator import itemgetter
# import re
#
# from bs4 import BeautifulSoup
# import requests
#
# # feed = https://news.python.sc/, to get predictable results we cached
# # first two pages - use these:
# # https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html
# # https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index2.html
#
# Entry = namedtuple('Entry', 'title points comments')
#
#
# def _create_soup_obj(url):
#     """Need utf-8 to properly parse emojis"""
#     resp = requests.get(url)
#     resp.encoding = "utf-8"
#     return BeautifulSoup(resp.text, "html.parser")
#
#
# def _get_titles(soup):
#     return soup.find_all('span', {'class': 'title'})
#
#
# def _get_entry(title):
#     votes_and_comments = title.find_next('td').text
#     title = title.text.strip()
#     m = re.search(r'(\d+) points?.*(\d+) comments?',
#                   votes_and_comments, re.DOTALL)
#     points, comments = m.groups()
#     return Entry(title, int(points), int(comments))
#
#
# def get_top_titles(url, top=5):
#     """Parse the titles (class 'title') using the soup object.
#        Return a list of top (default = 5) titles ordered descending
#        by number of points and comments.
#     """
#     soup = _create_soup_obj(url)
#
#     ret = []
#     for title in _get_titles(soup):
#         ret.append(_get_entry(title))
#
#     return sorted(ret, key=itemgetter(1, 2), reverse=True)[:top]
