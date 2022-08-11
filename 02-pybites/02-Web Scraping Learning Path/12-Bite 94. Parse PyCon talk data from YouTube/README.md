# Bite 94. Parse PyCon talk data from YouTube

https://codechalleng.es/bites/94/



PyCon2018 was awesome! But you clearly had to choose the whole time, so much was going on!

In this Bite we parsed all the talks from the PyCon 2018 YT channel and stored them into a list of Video namedtuples. This nested data structure is stored in a pickle file. The data looks like this:

    [Video(id='T-TwcmT6Rcw',
                 title='Raymond Hettinger - Dataclasses:  The code generator ...',
                 duration='PT45M8S',
                 metrics={'viewCount': '6047', 'likeCount': '139', 'dislikeCount': '2',
                                  'favoriteCount': '0', 'commentCount': '14'}),
     Video(id='duvZ-2UK0fc', title='Ned Batchelder .... same attributes ...),
     Video(id='GBQAKldqgZs', title='Kenneth Reitz ....same attributes ...),
     ... same Video namedtuples ...]

See the full data dump here (note this is a snapshot as of today = 23rd of May 2018, the numbers will change, but we
want static data for this Bite so we can run tests against your code).

Now the exercise: complete the 5 functions below, parsing this data set. See the docstrings and the tests for more
info...

Have fun and keep calm and code in Python!
