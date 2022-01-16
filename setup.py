# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.rst', encoding='utf-8') as file:
    readme = file.read()
    
setup(
  name = 'Hillfit',      
  package_dir = {'fitting':'hillfit'},
  packages = find_packages(),
  version = '0.0.6',
  license = 'MIT',
  description = "Model for fitting data with the Hill equation, and exporting the contents", 
  long_description = readme,
  author = ','.join(['Andrew Freiburger', 'Hiroaki Imoto']),               
  author_email = ','.join(['andrewfreiburger@gmail.com', 'himoto@protein.osaka-u.ac.jp']),
  url = 'https://github.com/freiburgermsu/hillfit',   
  keywords = ['biochemistry', 'systems biology', 'computational biology', 'data science', 'Hill equation'],
  install_requires = ['matplotlib', 'numpy', 'sklearn', 'scipy', 'pandas', 'sigfig']
)