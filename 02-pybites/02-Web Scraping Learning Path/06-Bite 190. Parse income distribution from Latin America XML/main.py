import os
from pathlib import Path
from urllib.request import urlretrieve

import xml.etree.ElementTree as ET

# import the countries xml file
tmp = Path(os.getenv("TMP", "/tmp"))
countries = tmp / 'countries.xml'

if not countries.exists():
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/countries.xml',
        countries
    )


def get_income_distribution(xml=countries):
    """
    - Read in the countries xml as stored in countries variable.
    - Parse the XML
    - Return a dict of:
      - keys = incomes (wb:incomeLevel)
      - values = list of country names (wb:name)
    """
    result = {}
    namespaces = {'wb': 'http://www.worldbank.org'}
    root = ET.parse(xml).getroot()
    my_countries = root.findall("wb:country", namespaces)
    for country in my_countries:
        name = country.find("wb:name", namespaces).text.strip()
        income = country.find("wb:incomeLevel", namespaces).text.strip()
        try:
            result[income].append(name)
        except KeyError:
            result[income] = [name]

    return result


# solution provided
# from collections import defaultdict
# import os
# from pathlib import Path
# import xml.dom.minidom as md
# from urllib.request import urlretrieve
#
# # import the countries xml file
# tmp = Path(os.getenv("TMP", "/tmp"))
# countries = tmp / 'countries.xml'
#
# if not countries.exists():
#     urlretrieve(
#         'https://bites-data.s3.us-east-2.amazonaws.com/countries.xml',
#         countries
#     )
#
#
# def get_income_distribution(xml=countries):
#     """
#     - Read in the countries xml as stored in countries variable.
#     - Parse the XML
#     - Return a dict of:
#       - keys = incomes (wb:incomeLevel)
#       - values = list of country names (wb:name)
#     """
#     with open(xml) as f:
#         xmlstring = f.read()
#
#     dom = md.parseString(xmlstring)
#     incomes = defaultdict(list)
#
#     for elem in dom.getElementsByTagName("wb:country"):
#         wb_name = elem.getElementsByTagName('wb:name')
#         country = wb_name[0].childNodes[0].data
#
#         wb_income = elem.getElementsByTagName('wb:incomeLevel')
#         income = wb_income[0].childNodes[0].data
#
#         incomes[income].append(country)
#
#     return incomes


if __name__ == '__main__':
    get_income_distribution()
