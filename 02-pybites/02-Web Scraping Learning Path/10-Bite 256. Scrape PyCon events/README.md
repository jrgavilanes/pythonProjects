# Bite 256. Scrape PyCon events

https://codechalleng.es/bites/256/

In this Bite, we want you to scrape PyCon 2019 data.

The provided source via _get_pycon_data contains data for years other than 2019 and conferences other than PyCon, so you
have to be selective.

Complete the get_pycon_events function by scraping the required data from the source. The data is contained in a
application/ld+json data structure, which can be parsed with the json module after retrieving the content. Extract the
data required for the given PyCon namedtuple which is the name of the PyCon, the city it takes place, the country the
start date, the end date and the homepage url. Make sure to parse the start date and the end date as datetime.

After retrieving all PyCon events complete the filter_pycons function. The function takes a list of PyCon namedtumples,
a year and a continent as parameters. Based on the year and continent, return a list of all PyCons that meet the
requirements. To make it a bit easier for you, we provide a get_continent(country) function which takes a country name
as a string and returns the continent of the country as a string.

Check the tests and docstrings for additional information.

Good luck and keep calm and code in Python!
