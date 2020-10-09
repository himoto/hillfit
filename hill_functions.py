import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

class HillFunctions(object):
    """ Fitting the Hill Equation to Experimental Data

    Parameters
    ----------
    x_data : 1d-array
        The independent variable where the data is measured.
    
    y_data : 1d-array
        The dependent data.
    
    y_error : 1d-array (default: [])
        The errorbar sizes.
    
    """
    def __init__(
            self,
            x_data,
            y_data,
            y_error=[]
    ):
        self.x_data = x_data
        self.y_data = y_data
        self.y_error = y_error

    def _equation(self, x, top, bottom, K, n):

        return bottom + (top - bottom) * x**n / (K**n + x**n)
    
    def _get_param(self):
        min_data = np.amin(self.y_data)
        max_data = np.amax(self.y_data)
        h = abs(max_data - min_data)
        param_initial = [
            max_data, 
            min_data, 
            0.5*(self.x_data[-1]-self.x_data[0]), 
            1
        ]
        param_bounds = (
            [max_data-0.5*h, min_data-0.5*h, self.x_data[0]*0.1, 0.01], 
            [max_data+0.5*h, min_data+0.5*h, self.x_data[-1]*10, 100]
        )
        bounds = [
            (max_data-0.5*h, max_data+0.5*h),
            (min_data-0.5*h, min_data+0.5*h),
            (self.x_data[0], self.x_data[-1]),
            (0.01, 100),
        ]
        
        popt, _ = curve_fit(
            self._equation, self.x_data, self.y_data, 
            p0=param_initial, 
            bounds=param_bounds, 
            maxfev=np.iinfo(np.int16).max,
        )
        
        return popt

    def _get_yfit(self, x_fit):
        popt = self._get_param()
        print(
            '%s = %.2e\n%s = %.2e' % (
                'EC50', popt[2], 'Hill coefficient', popt[3]
            )
        )

        return self._equation(x_fit, popt[0], popt[1], popt[2], popt[3]), popt[2]
    
    @staticmethod
    def _my_rc_params():
        plt.rcParams['font.size'] = 20
        plt.rcParams['axes.linewidth'] = 2
        plt.rcParams['lines.linewidth'] = 4
        plt.rcParams['lines.markersize'] = 10

    def fitting(
            self,
            color='b',
            figsize=(8, 6),
            xlabel='x',
            ylabel='y',
            xlim=(),
            ylim=(),
            xticks=[],
            yticks=[],
    ):
        x_fit = np.logspace(
            np.log10(self.x_data[0]), np.log10(self.x_data[-1]), 1000
        )
        y_fit, EC50 = self._get_yfit(x_fit)

        plt.figure(figsize=figsize)
        # rcParams
        self._my_rc_params()

        if not self.y_error:
            plt.plot(
                self.x_data, self.y_data, 'o', markerfacecolor='None',
                markeredgecolor=color, label='data', clip_on=False
            )
        else:
            exp_data = plt.errorbar(
                self.x_data, self.y_data, yerr=self.y_error, fmt='o',
                color=color, ecolor=color, elinewidth=1, capsize=5,
                markerfacecolor='None', markeredgecolor=color, label='data',
                clip_on=False
            )
            for capline in exp_data[1]:
                capline.set_clip_on(False)
            for barlinecol in exp_data[2]:
                barlinecol.set_clip_on(False)
        # fitting curve
        plt.plot(
            x_fit, y_fit, color=color, alpha=0.2, 
            solid_capstyle='round', label='curve_fit', clip_on=False
        )

        plt.xscale('log')
        if not xlim:
            plt.xlim(self.x_data[0], self.x_data[-1])
        else:
            plt.xlim(xlim)
        if not xticks:
            plt.xticks(
                [self.x_data[0], EC50, self.x_data[-1]], 
                ['%.2e'%(self.x_data[0]), '%.2e'%(EC50), '%.2e'%(self.x_data[-1])]
            )
        else:
            plt.xticks(xticks)
        if ylim:
            plt.ylim(ylim)
        if yticks:
            plt.yticks(yticks)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        plt.legend(loc='upper left', frameon=False)

        plt.gca().spines['right'].set_visible(False)
        plt.gca().spines['top'].set_visible(False)

        plt.savefig('./hill_fitting.png', dpi=300, bbox_iches='tight')