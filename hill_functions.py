import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

class HillFunctions(object):

    def __init__(self,x_data,y_data):
        self.x_data = x_data
        self.y_data = y_data

    def equation(self,x,top,bottom,K,n):

        return bottom + (top-bottom)*x**n/(K**n+x**n)

    def get_param(self):
        popt,pcov = curve_fit(
            self.equation,self.x_data,self.y_data,
            bounds=(0.0,float('inf')),maxfev=32767
        )

        return popt

    def fitting(self,x_fit):
        popt = self.get_param()
        print(
            '%s = %e\n%s = %e\n%s = %e\n%s = %e'\
            %('top',popt[0],'bottom',popt[1],'K',popt[2],'n',popt[3])
        )

        return self.equation(x_fit,popt[0],popt[1],popt[2],popt[3])

    def display(self):
        x_fit = np.linspace(self.x_data[0],self.x_data[-1],100)
        y_fit = self.fitting(x_fit)

        plt.figure(figsize=(9,6))
        plt.rcParams['font.size'] = 20
        plt.rcParams['axes.linewidth'] = 2
        plt.rcParams['lines.linewidth'] = 6
        plt.rcParams['lines.markersize'] = 10

        plt.plot(self.x_data,self.y_data,'o',color='b',markeredgecolor='c',label='data',clip_on=False)
        plt.plot(x_fit,y_fit,'b',alpha=0.2,solid_capstyle='round',label='curve_fit',clip_on=False)

        plt.xscale('log')
        plt.xlim(self.x_data[0],self.x_data[-1])
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend(loc='upper left',frameon=False)

        plt.gca().spines['right'].set_visible(False)
        plt.gca().spines['top'].set_visible(False)

        plt.show()