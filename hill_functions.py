import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

class HillFunctions(object):

    def __init__(self,x_data,y_data):
        self.x_data = x_data # 1d-array
        self.y_data = y_data # 1d-array

    def _equation(self,x,top,bottom,K,n):

        return bottom + (top-bottom)*x**n/(K**n+x**n)

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
            [max_data-h,min_data-h,0,0.01],
            [max_data+h,min_data+h,self.x_data[-1],1000]
        )
        
        popt,pcov = curve_fit(
            self._equation,self.x_data,self.y_data,
            p0 = param_initial,
            bounds = param_bounds,
            maxfev = np.iinfo(np.int16).max
        )

        return popt

    def _fitting(self,x_fit):
        popt = self._get_param()
        print(
            '%s = %.2e\n%s = %.2e'\
            %('EC50',popt[2],'Hill coefficient',popt[3])
        )

        return self._equation(x_fit,popt[0],popt[1],popt[2],popt[3]),popt[2]

    def display(self):
        x_fit = np.linspace(self.x_data[0],self.x_data[-1],100)
        y_fit,EC50 = self._fitting(x_fit)

        plt.figure(figsize=(8,6))
        plt.rcParams['font.size'] = 20
        plt.rcParams['axes.linewidth'] = 2
        plt.rcParams['lines.linewidth'] = 4
        plt.rcParams['lines.markersize'] = 10

        plt.plot(
            self.x_data,self.y_data,'o',color='b',markeredgecolor='c',label='data',clip_on=False
        )
        plt.plot(
            x_fit,y_fit,'b',alpha=0.2,solid_capstyle='round',label='curve_fit',clip_on=False
        )

        plt.xscale('log')
        plt.xlim(self.x_data[0],self.x_data[-1])
        plt.xticks(
            [self.x_data[0],EC50,self.x_data[-1]],
            ['%.2e'%(self.x_data[0]),'%.2e'%(EC50),'%.2e'%(self.x_data[-1])]
        )
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend(loc='upper left',frameon=False)

        plt.gca().spines['right'].set_visible(False)
        plt.gca().spines['top'].set_visible(False)

        plt.savefig('./hill_fitting.png',bbox_iches='tight')