# Bite 190. Parse income distribution from Latin America XML

https://codechalleng.es/bites/190/

In this Bite you are going to parse some Latin American countries in xml, specifically the output of
api.worldbank.org/V2/country?region=LCN which we stored here. It's already saved for you in the countries temp file.

Complete get_income_distribution by reading in this file, parsing its XML and returning a dict of keys = wb:incomeLevel
and values = lists of country names (wb:name). defaultdict is a convenient data structure to use here. See also the
tests for the expected return.

Good luck and code more Python!
