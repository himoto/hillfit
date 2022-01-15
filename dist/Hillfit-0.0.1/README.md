# Fitting the Hill Equation to Experimental Data

[![Actions Status](https://github.com/himoto/hillfit/workflows/Python%20package/badge.svg)](https://github.com/himoto/hillfit/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

The Hill equation is defined as follows:<br>

> _y = bottom + (top - bottom) · x<sup>nH</sup> / (EC50</sub><sup>nH</sup> + x<sup>nH</sup>)_

where _bottom_ is minimum activity, _top_ is maximum activity, _EC50_ is half-maximum effective dose, _nH_ is the Hill coefficient, y is the cellular or tissue response and x is stimulus dose.

## Usage

```python
%matplotlib inline

import matplotlib.pyplot as plt
from hillfit import HillFit

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

model = HillFit(x_data, y_data)
x_fit, y_fit = model.fitting()

plt.plot(x_data, y_data, 'bo', markerfacecolor='None', markeredgecolor='b', label='data', clip_on=False)
plt.plot(x_fit, y_fit, 'b', alpha=0.2, solid_capstyle='round', label='curve_fit', clip_on=False)
plt.xscale('log')
plt.xlabel('Dose (AU)')
plt.ylabel('Response (AU)')
plt.legend()
plt.show()
```

<img src=image/fitting_res.png>

## Installation

    git clone https://github.com/himoto/hillfit.git

## License

MIT
