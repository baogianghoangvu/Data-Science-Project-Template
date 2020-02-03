# Data-Science-Project-Template

An A-to-Z template for data science projects in Python

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

_**Project name**_ needs a short and sweet introduction.

_**Project name**_ also does this really cool thing that doesn't fit into the short and sweet intro, so you feel the urge to write something more here.

---

## Project Milestones

- [x] Init repository
- [ ] Prep data
- [ ] EDA
- [ ] ???
- [ ] Findings

## Summary of Findings

- Something something.
- ???

## Instructions to Reproduce Findings

#### Set up Python & Notebook Environment

- With Anaconda

```bash
conda create -n projectname python=3.8 jupyter
conda activate projectname
python -m ipykernel install --user --name projectname
jupyter notebook
```

#### Install Project Requirements

- Clone this repository:

```bash
cd where_you_want_to/put_your_project
git clone https://github.com/author/thisrepository/
cd thisrepository
```

- Install standard requirements

```bash
python -m pip install -e .
```

- Or standard + development requirements

```bash
python -m pip install -e .[dev]
```

- Or standard + test requirements

```bash
python -m pip install -e .[test]
```

#### Run Notebooks in order from 00 to 99

## Authors

- [Author1 Name](mailto:author1@email.com)
- [Author2 Name](mailto:author2@email.com)

## References and Notes that explain this template but don't need to be featured in an actual project repo

### Notes for template users

TBA

### References

- [Altair Viz](https://github.com/altair-viz/altair/blob/master/setup.py)
- [Chromebook Datascience](https://jhudatascience.org/chromebookdatascience/)
- [Introduction to Data Science](https://rafalab.github.io/dsbook/)
