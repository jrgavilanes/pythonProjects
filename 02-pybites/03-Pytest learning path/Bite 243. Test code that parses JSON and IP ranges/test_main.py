import os
from pathlib import Path
from ipaddress import IPv4Network, AddressValueError
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
    urlretrieve(URL, PATH)
    ipv4_service_ranges = parse_ipv4_service_ranges(PATH)
    assert len(get_aws_service_range("13.248.11.0", ipv4_service_ranges)) > 0

    assert str(ipv4_service_ranges[0]) == '13.248.118.0/24 is allocated to the AMAZON service in the eu-west-1 region'

    with pytest.raises(ValueError):
        get_aws_service_range("13x.248.11.0", ipv4_service_ranges)

    with pytest.raises(ValueError):
        get_aws_service_range("13.248.11.0.12", ipv4_service_ranges)

    try:
        get_aws_service_range("13.248.11.0.12", ipv4_service_ranges)
    except ValueError as e:
        assert str(e) == "Address must be a valid IPv4 address"

    assert len(get_aws_service_range("88.248.11.0", ipv4_service_ranges)) == 0

# SOLUTION PROVIDED
# import os
# from pathlib import Path
# from ipaddress import IPv4Network
# from urllib.request import urlretrieve
#
# import pytest
#
# from ips import (ServiceIPRange, parse_ipv4_service_ranges,
#                  get_aws_service_range)
#
# URL = "https://bites-data.s3.us-east-2.amazonaws.com/ip-ranges.json"
# TMP = os.getenv("TMP", "/tmp")
# PATH = Path(TMP, "ip-ranges.json")
# IP = IPv4Network('192.0.2.8/29')
#
#
# @pytest.fixture(scope='module')
# def json_file():
#     """Import data into tmp folder"""
#     urlretrieve(URL, PATH)
#     return PATH
#
#
# def test_dataclass():
#     expected = ("192.0.2.8/29 is allocated to the pybites service "
#                 "in the US region")
#     assert str(ServiceIPRange('pybites', 'US', IP)) == expected
#
#
# def test_parse_ranges(json_file):
#     out = parse_ipv4_service_ranges(json_file)
#     assert len(out) == 1886
#
#     assert type(out) == list
#     assert all(type(element) == ServiceIPRange for element in out)
#     assert str(out[0]) == ("13.248.118.0/24 is allocated to the AMAZON "
#                            "service in the eu-west-1 region")
#
#
# def test_get_aws_service_range_zero_hits(json_file):
#     assert get_aws_service_range('13.248.118.0', []) == []
#
#
# def test_get_aws_service_range_two_hits(json_file):
#     service_range = parse_ipv4_service_ranges(json_file)
#     expected = [
#         ServiceIPRange(service='AMAZON', region='eu-west-1',
#                        cidr=IPv4Network('13.248.118.0/24')),
#         ServiceIPRange(service='GLOBALACCELERATOR', region='eu-west-1',
#                        cidr=IPv4Network('13.248.118.0/24'))
#     ]
#     assert get_aws_service_range('13.248.118.0', service_range) == expected
#
#
# def test_get_aws_service_range_exception(json_file):
#     with pytest.raises(ValueError) as exc:
#         get_aws_service_range('nonsense', {})
#     assert str(exc.value) == "Address must be a valid IPv4 address"
