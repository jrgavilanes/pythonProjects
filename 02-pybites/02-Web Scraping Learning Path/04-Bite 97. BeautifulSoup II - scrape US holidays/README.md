# Bite 97. BeautifulSoup II - scrape US holidays

https://codechalleng.es/bites/97/

In this Bite we use BeautifulSoup to scrape US holidays from OfficeHolidays to make a lookup of holidays per month.

Check the HTML (here) for a table with CSS class list-table and parse its data. You need to populate the given holidays
defaultdict like this:

    >>> from pprint import pprint as pp
    >>> from holidays import get_us_bank_holidays
    >>> pp(get_us_bank_holidays())
    defaultdict(,
              {'01': ["New Year's Day", 'Martin Luther King Jr. Day'],
               '02': ["Presidents' Day"],
               '04': ['Emancipation Day'],
               '05': ["Mother's Day", 'Memorial Day'],
               '06': ["Father's Day"],
               '07': ['Independence Day'],
               '09': ['Labor Day'],
               '10': ['Columbus Day'],
               '11': ['Veterans Day', 'Thanksgiving', 'Day after Thanksgiving'],
               '12': ['Christmas Day']})

By the way, watch out for trailing spaces when parsing the holidays. Have fun and keep coding in Python!
