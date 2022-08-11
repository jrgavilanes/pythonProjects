from collections import namedtuple
import os
import pickle
import urllib.request
from datetime import datetime, timedelta

# prework
# download pickle file and store it in a tmp file
pkl_file = 'pycon_videos.pkl'
data = f'https://bites-data.s3.us-east-2.amazonaws.com/{pkl_file}'
tmp = os.getenv("TMP", "/tmp")
pycon_videos = os.path.join(tmp, pkl_file)
urllib.request.urlretrieve(data, pycon_videos)

# the pkl contains a list of Video namedtuples
Video = namedtuple('Video', 'id title duration metrics')


def load_pycon_data(_pycon_videos=pycon_videos):
    """Load the pickle file (pycon_videos) and return the data structure
       it holds"""

    try:
        videos = {}
        videos = pickle.load(open(_pycon_videos, 'rb'))
        print(videos)
        return videos
    except Exception as e:
        raise e


def get_most_popular_talks_by_views(videos):
    """Return the pycon video list sorted by viewCount"""
    result = sorted(videos, key=lambda x: -int(x[3]["viewCount"]))
    print(result)
    return result


def get_most_popular_talks_by_like_ratio(videos):
    """Return the pycon video list sorted by most likes relative to
       number of views, so 10 likes on 175 views ranks higher than
       12 likes on 300 views. Discount the dislikeCount from the likeCount.
       Return the filtered list"""
    result = sorted(videos,
                    key=lambda x: -((int(x[3]["likeCount"]) - (int(x[3]["dislikeCount"]))) / float(x[3]["viewCount"])))
    print(result)
    return result


def get_talks_gt_one_hour(videos):
    """Filter the videos list down to videos of > 1 hour"""
    result = []
    for video in videos:
        if to_seconds(video.duration) > 3600:
            result.append(video)

    # result = sorted(result, key=lambda x: -to_seconds(x[2]))
    # print(result)
    return result


def to_seconds(duration: str) -> float:
    if "H" in duration and "M" in duration and "S" in duration:
        t = datetime.strptime(duration, "PT%HH%MM%SS")
        td = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
        total_seconds = td.total_seconds()
        return total_seconds
    elif "H" in duration and "M" in duration and "S" not in duration:
        t = datetime.strptime(duration, "PT%HH%MM")
        td = timedelta(hours=t.hour, minutes=t.minute)
        total_seconds = td.total_seconds()
        return total_seconds
    elif "H" in duration and "M" not in duration and "S" in duration:
        t = datetime.strptime(duration, "PT%HH%SS")
        td = timedelta(hours=t.hour, seconds=t.second)
        total_seconds = td.total_seconds()
        return total_seconds
    elif "M" in duration and "S" not in duration:
        t = datetime.strptime(duration, "PT%MM")
        td = timedelta(minutes=t.minute)
        total_seconds = td.total_seconds()
        return total_seconds
    elif "M" not in duration and "S" in duration:
        t = datetime.strptime(duration, "PT%SS")
        td = timedelta(minutes=t.second)
        total_seconds = td.total_seconds()
        return total_seconds

    t = datetime.strptime(duration, "PT%MM%SS")
    td = timedelta(minutes=t.minute, seconds=t.second)
    total_seconds = td.total_seconds()
    return total_seconds


def get_talks_lt_twentyfour_min(videos):
    """Filter videos list down to videos that have a duration of less than
       24 minutes"""
    result = []
    for video in videos:
        if to_seconds(video.duration) < 1440:
            result.append(video)

    # result = sorted(result, key=lambda x: -to_seconds(x[2]))
    # print(result)
    return result


if __name__ == '__main__':
    my_videos = load_pycon_data()
    get_most_popular_talks_by_views(my_videos)
    get_most_popular_talks_by_like_ratio(my_videos)
    get_talks_gt_one_hour(my_videos)
    get_talks_lt_twentyfour_min(my_videos)

# solution provided
# from collections import namedtuple
# import os
# import pickle
# import re
# import urllib.request
#
# # prework
# # download pickle file and store it in a tmp file
# pkl_file = 'pycon_videos.pkl'
# data = f'https://bites-data.s3.us-east-2.amazonaws.com/{pkl_file}'
# tmp = os.getenv("TMP", "/tmp")
# pycon_videos = os.path.join(tmp, pkl_file)
# urllib.request.urlretrieve(data, pycon_videos)
#
# # the pkl contains a list of Video namedtuples
# Video = namedtuple('Video', 'id title duration metrics')
#
#
# def load_pycon_data(pycon_videos=pycon_videos):
#     """Load the pickle file (pycon_videos) and return the data structure
#        it holds"""
#     with open(pycon_videos, 'rb') as f:
#         return pickle.load(f)
#
#
# def _rating(metrics):
#     """Get like/view ratio (discount dislikes)"""
#     views = int(metrics.get('viewCount', 0))
#     dislikes = int(metrics.get('dislikeCount', 0))
#     likes = int(metrics.get('likeCount', 0)) - dislikes
#     return likes/views
#
#
# def get_most_popular_talks_by_views(videos):
#     """Return the pycon video list sorted by viewCount"""
#     for vid in sorted(videos,
#                       key=lambda v: int(v.metrics.get('viewCount')),
#                       reverse=True):
#         yield vid
#
#
# def get_most_popular_talks_by_like_ratio(videos):
#     """Return the pycon video list sorted by most likes relative to
#        number of views, so 10 likes on 175 views ranks higher than
#        12 likes on 300 views. Discount the dislikeCount from the likeCount.
#        Return the filtered list"""
#     for vid in sorted(videos,
#                       key=lambda v: _rating(v.metrics),
#                       reverse=True):
#         yield vid
#
#
# def get_talks_gt_one_hour(videos):
#     """Filter the videos list down to videos of > 1 hour"""
#     return [vid for vid in videos if 'H' in vid.duration]
#
#
# def _is_lt_n_min(duration, n=24):
#     """Helper to determine if a video is less than n minutes"""
#     if 'H' in duration:
#         return False
#
#     seconds_limit = n*60
#
#     pat = re.compile(r'^PT(\d+)M(?:(\d+)S)?$')
#     m = pat.match(duration)
#     mm, ss = m.groups()
#
#     total_seconds = int(mm) * 60 + (ss and int(ss) or 0)
#
#     return total_seconds < seconds_limit
#
#
# def get_talks_lt_twentyfour_min(videos):
#     """Filter videos list down to videos that have a duration of less than
#        24 minutes"""
#     return [vid for vid in videos if _is_lt_n_min(vid.duration)]
