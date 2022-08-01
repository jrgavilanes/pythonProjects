from urllib.request import urlretrieve
import os
from pathlib import Path

import gender_guesser.detector as gender
from bs4 import BeautifulSoup as Soup

TMP = Path(os.getenv("TMP", "/tmp"))
PYCON_HTML = TMP / "pycon2019.html"
PYCON_PAGE = ('https://bites-data.s3.us-east-2.amazonaws.com/'
              'pycon2019.html')

if not PYCON_HTML.exists():
    urlretrieve(PYCON_PAGE, PYCON_HTML)


def _get_soup(html=PYCON_HTML):
    return Soup(html.read_text(encoding="utf-8"), "html.parser")


def get_pycon_speaker_first_names(soup=None):
    """Parse the PYCON_HTML using BeautifulSoup, extracting all
       speakers (class "speaker"). Note that some items contain
       multiple speakers so you need to extract them.
       Return a list of first names
    """
    if soup is None:
        soup = _get_soup()

    my_names = soup.select("span.speaker")
    result = []
    for name in my_names:
        speakers = name.text.strip().replace("/", ",").split(",")
        for speaker in speakers:
            result.append(speaker.strip().split(" ")[0])

    return result


def get_percentage_of_female_speakers(first_names):
    """Run gender_guesser on the names returning a percentage
       of female speakers (female and mostly_female),
       rounded to 2 decimal places."""
    d = gender.Detector(case_sensitive=False)
    total_females = 0
    for name in first_names:
        if d.get_gender(name.lower()) in ["female", "mostly_female"]:
            total_females += 1

    return round(total_females * 100 / len(first_names), 2)


if __name__ == '__main__':
    names = get_pycon_speaker_first_names()
    perc = get_percentage_of_female_speakers(names)
    print(perc)


# solution provided
# from urllib.request import urlretrieve
# import os
# from pathlib import Path
# import re
#
# import gender_guesser.detector as gender
# from bs4 import BeautifulSoup as Soup
#
# TMP = Path(os.getenv("TMP", "/tmp"))
# PYCON_HTML = TMP / "pycon2019.html"
# PYCON_PAGE = ('https://bites-data.s3.us-east-2.amazonaws.com/'
#               'pycon2019.html')
#
# if not PYCON_HTML.exists():
#     urlretrieve(PYCON_PAGE, PYCON_HTML)
#
#
# def _get_soup(html=PYCON_HTML):
#     return Soup(html.read_text(encoding="utf-8"), "html.parser")
#
#
# def _extract_names(names):
#     for name in names:
#         extracted_names = re.split(r'[,/]', name)
#         for en in extracted_names:
#             yield en.strip()
#
#
# def _get_first_names(names):
#     return [n.split()[0] for n in names]
#
#
# def get_pycon_speaker_first_names(soup=None):
#     """Parse the PYCON_HTML using BeautifulSoup, extracting all
#        speakers (class "speaker"). Note that some items contain
#        multiple speakers so you need to extract them.
#        Return a list of first names
#     """
#     if soup is None:
#         soup = _get_soup()
#
#     speakers = soup.find_all("span", {"class": "speaker"})
#     names = [speaker.text.strip() for speaker in speakers]
#
#     names = list(_extract_names(names))
#     return _get_first_names(names)
#
#
# def get_percentage_of_female_speakers(first_names):
#     """Run gender_guesser on the names returning a percentage
#        of female speakers (female and mostly_female),
#        rounded to 2 decimal places."""
#     d = gender.Detector()
#     num_females = 0
#
#     for name in first_names:
#         gg = d.get_gender(name)
#         if 'female' in gg:
#             num_females += 1
#
#     return round(num_females/len(first_names) * 100, 2)
#
#
# if __name__ == '__main__':
#     names = get_pycon_speaker_first_names()
#     perc = get_percentage_of_female_speakers(names)
#     print(perc)