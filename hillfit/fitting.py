from typing import NamedTuple, Tuple, Union

import numpy as np
from scipy.optimize import curve_fit


class Params(NamedTuple):
    """
    Parameters
    ----------
    bottom
        Minimum activity.
    top
        Maximum activity.
    EC50
        Half-maximum effective dose.
    nH
        Hill coefficient.
    """

    top: float
    bottom: float
    EC50: float
    nH: float


class HillFit(object):
    """
    Fitting the Hill Equation to Experimental Data.

    Attributes
    ----------
    x_data : 1d-array
        The independent variable where the data is measured.

    y_data : 1d-array
        The dependent data.
    """

    def __init__(
        self,
        x_data: Union[list, np.ndarray],
        y_data: Union[list, np.ndarray],
    ) -> None:
        self.x_data = x_data
        self.y_data = y_data

    def _equation(self, x, *params):
        """
        Hill equation.
        """
        hilleq = params[1] + (params[0] - params[1]) * x ** params[3] / (
            params[2] ** params[3] + x ** params[3]
        )
        return hilleq

    def _get_param(self) -> Params:
        """
        Use ``scipy.optimize.curve_fit()`` to estimate parameters.
        """
        min_data = np.amin(self.y_data)
        max_data = np.amax(self.y_data)
        h = abs(max_data - min_data)
        param_initial = [max_data, min_data, 0.5 * (self.x_data[-1] - self.x_data[0]), 1]
        param_bounds = (
            [max_data - 0.5 * h, min_data - 0.5 * h, self.x_data[0] * 0.1, 0.01],
            [max_data + 0.5 * h, min_data + 0.5 * h, self.x_data[-1] * 10, 100],
        )

        popt, _ = curve_fit(
            self._equation,
            self.x_data,
            self.y_data,
            p0=param_initial,
            bounds=param_bounds,
        )
        params = Params(*popt)
        return params

    def fitting(self, num: int = 1000, show_popt: bool = True) -> Tuple[np.ndarray, np.ndarray]:
        """
        Parameters
        ----------
        num : int (default: 1000)
            Number of samples to generate. Default is 1000.
        show_popt : bool (default: :obj:`True`)
            Whether to show the estimation result.
        
        Examples
        --------
        >>> import matplotlib.pyplot as plt
        >>> from hillfit import HillFit
        >>> x_data = [
        ...     9.210, 10.210, 10.580, 10.830, 11.080,
        ...     11.330, 11.580, 11.830, 12.080, 12.330,
        ...     12.580, 12.830, 13.080, 13.330, 13.580,
        ...     13.830, 14.080, 14.330, 14.580, 14.830,
        ...     15.080, 15.330, 15.580, 15.830, 17.580
        ... ]
        >>> y_data = [
        ...     0.000, 0.000, 0.000, 1.667, 2.222,
        ...     5.682, 9.524, 15.315, 16.000, 31.183,
        ...     39.000, 47.222, 47.475, 63.208, 77.143,
        ...     75.214, 80.612, 92.784, 94.167, 93.137,
        ...     95.902, 96.396, 97.872, 98.246, 100.000
        ... ]
        >>> model = HillFit(x_data, y_data)
        >>> x_fit, y_fit = model.fitting()
        >>> plt.plot(x_data, y_data, 'bo', markerfacecolor='None', markeredgecolor='b', label='data', clip_on=False)
        >>> plt.plot(x_fit, y_fit, 'b', alpha=0.2, solid_capstyle='round', label='curve_fit', clip_on=False)
        >>> plt.xscale('log')
        >>> plt.xlabel('Dose (AU)')
        >>> plt.ylabel('Response (AU)')
        >>> plt.legend()
        >>> plt.show()
        """
        popt = self._get_param()
        if show_popt:
            print(popt)
        x_fit = np.logspace(np.log10(self.x_data[0]), np.log10(self.x_data[-1]), num)
        y_fit = self._equation(x_fit, *popt)
        return x_fit, y_fit
