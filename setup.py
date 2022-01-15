# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.rst', encoding='utf-8') as file:
    readme = file.read()
    
setup(
  name = 'Hillfit',      
  package_dir = {'fitting':'hillfit'},
  packages = find_packages(),
  version = '0.0.5',
  license = 'GNU',
  description = "Model for fitting data with the Hill equation, and exporting the contents", 
  long_description = readme,
  author = 'Andrew Freiburger',               
  author_email = 'andrewfreiburger@gmail.com',
  url = 'https://github.com/freiburgermsu/hillfit',   
  keywords = ['biochemistry', 'systems biology', 'computational biology', 'data science', 'Hill equation'],
  install_requires = ['matplotlib', 'numpy', 'sklearn', 'scipy', 'pandas', 'sigfig']
)