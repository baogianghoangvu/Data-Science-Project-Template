# Data-Science-Project-Template

An A-to-Z template for data science projects in Python

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

_**Project name**_ needs a short and sweet introduction.

_**Project name**_ also does this really cool thing that doesn't fit with the short and sweet intro, so you feel the urge to write something more here.

---

## Project Milestones

* [x] Init repository
* [ ] Prep data
* [ ] EDA
* [ ] Findings

## Summary of Findings

- Something something.
- Something number 2.

## Instructions to Reproduce Findings

### Set up Python & Notebook Environment

* With Anaconda

``` bash
conda create -n projectname python=3.8 jupyter
conda activate projectname
python -m ipykernel install --user --name projectname
jupyter notebook
```

### Install Project Requirements

* Clone this repository:

``` bash
git clone https://github.com/author/thisrepository/
```

* Install standard requirements

``` bash
cd thisrepository
python -m pip install -e .
```

* Or standard + development requirements

``` bash
cd thisrepository
python -m pip install -e .[dev]
```

* Or standard + test requirements

``` bash
cd thisrepository
python -m pip install -e .[test]
```

## Authors

* [Author1 Name](mailto:author@email.com)
* [Author2 Name](mailto:author@email.com)

