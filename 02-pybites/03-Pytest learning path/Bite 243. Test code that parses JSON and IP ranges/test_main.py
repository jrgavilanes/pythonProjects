import os
from pathlib import Path
from ipaddress import IPv4Network
from urllib.request import urlretrieve

import pytest

from main import (ServiceIPRange, parse_ipv4_service_ranges,
                  get_aws_service_range)

URL = "https://bites-data.s3.us-east-2.amazonaws.com/ip-ranges.json"
TMP = os.getenv("TMP", "/tmp")
PATH = Path(TMP, "ip-ranges.json")
IP = IPv4Network('192.0.2.8/29')


@pytest.fixture(scope='module')
def json_file():
    """Import data into tmp folder"""
    urlretrieve(URL, PATH)
    return PATH


# write your pytest code ...
def test_get_aws_service_range():
    # urlretrieve(URL, PATH)
    ipv4_service_ranges = parse_ipv4_service_ranges(PATH)
    assert len(get_aws_service_range("13.248.11.0", ipv4_service_ranges)) > 0

    with pytest.raises(ValueError):
        get_aws_service_range("13x.248.11.0", ipv4_service_ranges)
