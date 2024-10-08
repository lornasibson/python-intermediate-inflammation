"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import os


def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    from inflammation.models import daily_mean

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""
    from inflammation.models import daily_mean

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)

def test_daily_max_positive_integers():
    """Test that max function works for positive integers
    """
    from inflammation.models import daily_max
    test_input = np.array([[1, 2, 3, 4],
                           [5, 6, 7, 8],
                           [4, 3, 2, 1]])
    test_result = np.array([5, 6, 7, 8])

    npt.assert_array_equal(daily_max(test_input), test_result)

def test_daily_max_negative_integers():
    """Test that max function works for array of positive and negative integers"""
    from inflammation.models import daily_max
    test_input = np.array([[-1, 4, 6, 7],
                           [-4, 6, -2, 9],
                           [-3, 3, 0, 4]])
    test_result = np.array([-1, 6, 6, 9])

    npt.assert_array_equal(daily_max(test_input), test_result)

def test_daily_min_positive_integers():
    """Test that min function works for array of positive integers"""
    from inflammation.models import daily_min
    test_input = np.array([[1, 2, 3, 4],
                           [6, 8, 0, 9],
                           [8, 4, 7, 3]])
    test_result = np.array([1, 2, 0, 3])

    npt.assert_array_equal(daily_min(test_input), test_result)

def test_daily_min_negative_integers():
    """Test that min function works for array of pos and neg integers"""
    from inflammation.models import daily_min
    test_input = np.array([[3, 6, -3, 0],
                           [4, -4, 6, 2],
                           [4, 6, 8, 3]])
    test_result = np.array([3, -4, -3, 0])

    npt.assert_array_equal(daily_min(test_input), test_result)


def test_load_from_json(tmpdir):
    from inflammation.models import load_json
    example_path = os.path.join(tmpdir, 'example.json')
    with open(example_path, 'w') as temp_json_file:
        temp_json_file.write('[{"observations":[1, 2, 3]},{"observations":[4, 5, 6]}]')
    result = load_json(example_path)
    npt.assert_array_equal(result, [[1, 2, 3], [4, 5, 6]])
