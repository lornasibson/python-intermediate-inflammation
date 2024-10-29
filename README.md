# Inflam
![Continuous Integration build in GitHub Actions](https://github.com/lornasibson/python-intermediate-inflammation/workflows/CI/badge.svg?branch=main)

Inflam is a data management system written in Python that manages trial data used in clinical inflammation studies.

## Main features
Here are some key features of Inflam:

- Provide basic statistical analyses over clinical trial data
- Ability to work on trial data in Comma-Separated Value (CSV) format
- Generate plots of trial data
- Analytical functions and views can be easily extended based on its Model-View-Controller architecture

## Prerequisites
This package requires Python 3.10 or newer to run
Inflam requires the following Python packages:

- [NumPy](https://www.numpy.org/) - makes use of NumPy's statistical functions (version 2.1.2 or newer)
- [Matplotlib](https://matplotlib.org/stable/index.html) - uses Matplotlib to generate statistical plots (version 3.9.2 or newer)

The following optional packages are required to run Inflam's unit tests:

- [pytest](https://docs.pytest.org/en/stable/) - Inflam's unit tests are written using pytest (version 8.3.3 or newer)
- [pytest-cov](https://pypi.org/project/pytest-cov/) - Adds test coverage stats to unit testing (version 5.0.0 or newer)


## Installation Guide
Locate the `whl` file and perform:
```bash
pip3 install dist/inflammation*.whl
```

Then build using poetry:
```bash
poetry build
```
