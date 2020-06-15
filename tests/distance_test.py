# -*- coding: UTF-8 -*-

# Import from standard library
import os
import first_ml_project
# Import from our lib
from first_ml_project.distance import haversine
import pytest


def test_haversine():
    lat1, lng1, lat2, lng2 = 48.865070, 2.380009, 48.865070, 2.380009
    assert haversine(lng1, lat1, lng2, lat2) == 0
    lat2, lng2 = 45.8561172, -1.2300099
    assert round(haversine(lng1, lat1, lng2, lat2)) == 431
