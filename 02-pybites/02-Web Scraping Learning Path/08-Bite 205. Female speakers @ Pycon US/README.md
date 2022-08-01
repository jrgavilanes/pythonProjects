# Bite 205. Female speakers @ Pycon US

https://codechalleng.es/bites/205/

After our Code Challenge 62 / Alicante PyDay last week, we thought it would be nice to branch off a Bite exercise using
what we learned. So prepare to do some web scraping using BeautifulSoup and discover a new library called
gender_guesser. We are going to look at the percentage of female speakers at Pycon US 2019.

Here is what you need to do:

    Complete get_pycon_speaker_first_names extracting all names from PYCON_HTML we cached somewhere for you. Note that some entries have multiple names separated by comma (,) and slash (/), so you will need to extract those. Return a list of first names.
    Complete get_percentage_of_female_speakers using gender_guesser.detector's Detector() to determine the gender based on the first names passed in. This tool is not perfect: some names won't be found. However we like Pareto's principle so we're happy to get a rough indication. Return the percentage of female speakers rounded to 2 decimal places.

If next year's Pycon site doesn't change much, you now have a re-usable script you can run against Pycon 2020's data ...

Have fun and keep calm and code in Python!
