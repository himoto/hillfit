# -*- coding: utf-8 -*-
import os
from pathlib import Path

from setuptools import find_packages, setup


def get_version() -> str:

    init_filepath = os.path.join(os.path.dirname(__file__), "hillfit", "__init__.py")
    with open(init_filepath) as f:
        for line in f:
            if line.startswith("__version__"):
                return line.strip().split()[-1][1:-1]
    assert False


def main():
    with open("README.rst", encoding="utf-8") as file:
        readme = file.read()

    setup(
        name="hillfit",
        package_dir={"fitting": "hillfit"},
        packages=find_packages(),
        version=get_version(),
        license="MIT",
        description="Model for fitting data with the Hill equation, and exporting the contents",
        long_description=readme,
        author=", ".join(["Andrew Freiburger", "Hiroaki Imoto"]),
        author_email="andrewfreiburger@gmail.com",
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
        classifiers=[
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
        ],
    )


if __name__ == "__main__":
    main()
