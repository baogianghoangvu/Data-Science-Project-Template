# Largely adapted from https://github.com/altair-viz/altair/blob/master/setup.py, BSD licensed

import io
import os
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


# ==============================================================================
# Utilities
# ==============================================================================

def read(path, encoding="utf-8"):
    path = os.path.join(os.path.dirname(__file__), path)
    with io.open(path, encoding=encoding) as fp:
        return fp.read()


def get_req(path):
    content = read(path)
    return [req for req in content.split("\n") if req != "" and not req.startswith("#")]


def version(path):
    """Obtain the packge version from a python file e.g. pkg/__init__.py

    See <https://packaging.python.org/en/latest/single_source_version.html>.
    """
    version_file = read(path)
    version_match = re.search(
        r"""^__version__ = ['"]([^'"]*)['"]""", version_file, re.M
    )
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


HERE = os.path.abspath(os.path.dirname(__file__))

# From https://github.com/jupyterlab/jupyterlab/blob/master/setupbase.py, BSD licensed
def find_packages(top=HERE):
    """
    Find all of the packages.
    """
    packages = []
    for d, dirs, _ in os.walk(top, followlinks=True):
        if os.path.exists(os.path.join(d, "__init__.py")):
            packages.append(os.path.relpath(d, top).replace(os.path.sep, "."))
        elif d != top:
            # Do not look for packages in subfolders if current is not a package
            dirs[:] = []
    return packages


# ==============================================================================
# Setup
# ==============================================================================

setup(
    name="customlibrary",
    version=version("./customlibrary/__init__.py"),
    description=""""Project Name" needs a short and sweet description here.""",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Author Name",
    author_email="author.email@email.com",
    url="https://github.com/author/this-repository",
    download_url="https://github.com/author/this-repository",
    packages=find_packages(),
    include_package_data=True,
    install_requires=get_req("requirements.txt"),
    extras_require={
        "dev": get_req("requirements_dev.txt"),
        "test": get_req("requirements_test.txt"),
    },
    classifiers=[
        "Development Status :: 1 - Planning",  # 1 - Planning, 2 - Pre-Alpha, 3 - Alpha, 4 - Beta, 5 - Production/Stable, 6 - Mature, 7 - Inactive
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.0",
    project_urls={
        "Bug Reports": "https://github.com/author/this-repository/issues",
        "Source": "https://github.com/author/this-repository/",
    },
)
