# -*- coding: utf-8 -*-
from pathlib import Path

from setuptools import find_packages, setup

try:
    from hillfit import __version__
except ImportError:
    __version__ = "0.1.1"


def main():
    with open("README.rst", encoding="utf-8") as file:
        readme = file.read()

    setup(
        name="hillfit",
        package_dir={"fitting": "hillfit"},
        packages=find_packages(),
        version=__version__,
        license="MIT",
        description="Model for fitting data with the Hill equation, and exporting the contents",
        long_description=readme,
        author=", ".join(["Andrew Freiburger", "Hiroaki Imoto"]),
        author_email=", ".join(["andrewfreiburger@gmail.com", "himoto@protein.osaka-u.ac.jp"]),
        url="https://github.com/himoto/hillfit",
        keywords=[
            "biochemistry",
            "systems biology",
            "computational biology",
            "data science",
            "Hill equation",
        ],
        install_requires=[
            l.strip() for l in Path("requirements.txt").read_text("utf-8").splitlines()
        ],
    )


if __name__ == "__main__":
    main()
