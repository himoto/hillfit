# Fitting the Hill Equation to Experimental Data
<img align="right" src=hill_fitting.png width=50%>

Hill equation:<br>

*y = bottom + (top-bottom) · x<sup>n</sup> / (K</sub><sup>n</sup> + x<sup>n</sup>)*

- ***K*** is the concentration of *x* producing 50% maximal response
- ***n*** is the Hill coefficient

## Requirements
- **Python3+**
    - numpy
    - scipy
    - matplotlib
    - jupyter

## Usage


```python
%matplotlib inline
from hill_functions import HillFunctions

# Test Data
x_data = [
    9.210, 10.210, 10.580, 10.830, 11.080,
    11.330, 11.580, 11.830, 12.080, 12.330,
    12.580, 12.830, 13.080, 13.330, 13.580,
    13.830, 14.080, 14.330, 14.580, 14.830,
    15.080, 15.330, 15.580, 15.830, 17.580
]

y_data = [
    0.000, 0.000, 0.000, 1.667, 2.222,
    5.682, 9.524, 15.315, 16.000, 31.183,
    39.000, 47.222, 47.475, 63.208, 77.143,
    75.214, 80.612, 92.784, 94.167, 93.137,
    95.902, 96.396, 97.872, 98.246, 100.000
]

# Using class: HillFunctions
hill = HillFunctions(x_data,y_data)

hill.fitting()
```

## Installation
    $ git clone https://github.com/himoto/fitting_hilleq.git


## License
[MIT](/LICENSE)
