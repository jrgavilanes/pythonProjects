from collections import namedtuple

import feedparser

# cached version to have predictable results for testing
FEED_URL = "https://bites-data.s3.us-east-2.amazonaws.com/steam_gaming.xml"

Game = namedtuple('Game', 'title link')


def get_games():
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    rss = feedparser.parse(FEED_URL)
    # print(rss)
    result = []
    for e in rss.entries:
        result.append(Game(e.title, e.link))

    return result


# solution provided
# def get_games():
#     """Parses Steam's RSS feed and returns a list of Game namedtuples"""
#     feed = feedparser.parse(FEED_URL)
#     return [Game(entry.title, entry.link)
#             for entry in feed.entries]

if __name__ == '__main__':
    print(get_games())
