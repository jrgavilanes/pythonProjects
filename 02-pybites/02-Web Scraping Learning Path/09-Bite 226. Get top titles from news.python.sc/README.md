# Bite 226. Get top titles from news.python.sc

https://codechalleng.es/bites/226/

There is a new Python news aggregator in town! Check it out here. In this Bite you will parse it!

Imagine you want to email yourself and colleagues a Friday digest of top articles, based on number of points and
comments.

Our first go would be feedparser but there is not an RSS feed yet.

So in this Bite you will use some BeautifulSoup (4.7.1) to parse the HTML yourself. Not a bad skill to have, no?

We have you parse a static copy of the site so we have predictable data to test your code against. As you can see in the
tests your code should work with the second (paginated) page as well.

Note we had some issues getting lxml to work on the platform so use bs4's html.parser for now. Also the W3C validator
does not really like the HTML so you cannot rely on article or table while parsing out the entries. Search for the title
class instead.

Good luck and bookmark this site to keep up2date with Python news. If you see anything interesting feel free to share it
on our Slack - #pybites-news channel.

Update 20th of Oct 2019: there is an RSS feed available now, but no count of comments/points so you will still need
BeautifulSoup / scraping. No worries though, if you want to scrape RSS feeds, take one of our feedparser Bites ...

Keep calm and code more Python!
