"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import os
import pytest


@pytest.mark.parametrize(
    "test, expected",
    [
        ([ [0, 0], [0, 0], [0, 0] ], [0, 0]),
        ([ [1, 2], [3, 4], [5, 6] ], [3, 4]),
    ])
def test_daily_mean(test, expected):
    """Test mean function works for array of zeroes and positive integers."""
    from inflammation.models import daily_mean
    npt.assert_array_equal(daily_mean(np.array(test)), np.array(expected))


@pytest.mark.parametrize(
    "test, expected",
    [
        ([[1, 2, 3, 4], [5, 6, 7, 8], [4, 3, 2, 1]], [5, 6, 7, 8]),
        ([[-1, 4, 6, 7], [-4, 6, -2, 9], [-3, 3, 0, 4]], [-1, 6, 6, 9]),
    ])
def test_daily_max(test, expected):
    """Test max function works for array of positive and negative integers"""
    from inflammation.models import daily_max
    npt.assert_array_equal(daily_max(np.array(test)), np.array(expected))

@pytest.mark.parametrize(
    "test, expected",
    [
        ([[1, 2, 3, 4], [6, 8, 0, 9], [8, 4, 7, 3]], [1, 2, 0, 3]),
        ([[3, 6, -3, 0], [4, -4, 6, 2], [4, 6, 8, 3]], [3, -4, -3, 0]),
    ])
def test_daily_min(test, expected):
    """Test min function works for array of positive and negative integers"""
    from inflammation.models import daily_min
    npt.assert_array_equal(daily_min(np.array(test)), np.array(expected))

def test_daily_min_string():
    """Test for TypeError when passing strings"""
    from inflammation.models import daily_min

    with pytest.raises(TypeError):
        error_expected = daily_min([['Hello', 'there'], ['General', 'Kenobi']])


def test_load_from_json(tmpdir):
    from inflammation.models import load_json
    example_path = os.path.join(tmpdir, 'example.json')
    with open(example_path, 'w') as temp_json_file:
        temp_json_file.write('[{"observations":[1, 2, 3]},{"observations":[4, 5, 6]}]')
    result = load_json(example_path)
    npt.assert_array_equal(result, [[1, 2, 3], [4, 5, 6]])
