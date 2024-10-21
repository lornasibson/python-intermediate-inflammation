"""Module containing mechanism for calculating standard deviation between datasets."""

import glob
import os
import numpy as np

from inflammation import models, views


def analyse_data(data_dir):
    """Calculate the standard deviation by day between datasets

    Gets all the inflammation csvs within a directory, works out the mean
    inflammation value for each day across all datasets, then graphs the
    standard deviation of these means."""
    data_file_paths = glob.glob(os.path.join(data_dir, "inflammation*.csv"))
    if len(data_file_paths) == 0:
        raise ValueError(f"No inflammation csv's found in path {data_dir}")
    data = map(models.load_csv, data_file_paths)

    daily_standard_deviation = compute_standard_deviation_by_day(data)

    graph_data = {
        "standard deviation by day": daily_standard_deviation,
    }
    # views.visualize(graph_data)
    return graph_data

def compute_standard_deviation_by_day(data):
    """Calculates the standard deviation of the datasets by day

    Args:
        data (np.ndarray): An array of the patient dataset

    Returns:
        np.ndarray: An array of the standard deviations by day
    """
    means_by_day = map(models.daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))
    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)

    return daily_standard_deviation
