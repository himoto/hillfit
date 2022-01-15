# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as file:
    readme = file.read()
    
setup(
  name = 'Hillfit',      
  package_dir = {'fitting':'hillfit'},
  version = '0.0.1',
  license = 'MIT',
  description = "Model for fitting data with the Hill equation, and exporting the contents", 
  long_description = readme,
  author = 'Andrew Freiburger, and Hiroaki Imoto',               
  author_email = 'andrewfreiburger@gmail.com, and himoto@protein.osaka-u.ac.jp',
  url = 'https://github.com/freiburgermsu/hillfit',   
  keywords = ['biochemistry', 'systems biology', 'computational biology', 'data science'],
  install_requires = ['matplotlib', 'numpy', 'sklearn', 'scipy', 'pandas', 'sigfig']
)