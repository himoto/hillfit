from numpy import array, amin, amax, logspace, log10
from scipy.optimize import curve_fit
from matplotlib import pyplot
from sklearn.metrics import r2_score
from datetime import date
from sigfig import round
from pandas import DataFrame
import re, os

class HillFit(object):
    def __init__(self, x_data, y_data):
        self.x_data = array(x_data)
        self.y_data = array(y_data)

    def _equation(self, x, *params):
        self.top = params[0]
        self.bottom = params[1]
        self.ec50 = params[2]
        self.nH = params[3]
        
        hilleq = self.bottom + (self.top - self.bottom)*x**self.nH / (self.ec50**self.nH + x**self.nH)
        return hilleq

    def _get_param(self):
        min_data = amin(self.y_data)
        max_data = amax(self.y_data)
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
        return [float(param) for param in popt]
    
    def regression(self, x_fit, y_fit, view_figure, x_label, y_label, title, *params):        
        corrected_y_data = self._equation(self.x_data, *params)
        r_2 = r2_score(self.y_data, corrected_y_data)        
        r_sqr = 'R\N{superscript two}: ' + f'{round(r_2, 6)}'
        
        pyplot.rcParams['figure.figsize'] = (11, 7)
        pyplot.rcParams['figure.dpi'] = 150
        self.figure, ax = pyplot.subplots()
        ax.plot(x_fit, y_fit, label = 'Hill fit')
        ax.scatter(self.x_data, self.y_data, label = 'raw_data')
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_title(title)
        ax.text(0.1, 0.95, r_sqr)
        ax.legend(loc = 'lower right')
        
        if view_figure:
            self.figure.show()

    def fitting(self, x_label = 'x', y_label = 'y', title = 'Fitted Hill equation', sigfigs = 6, view_figure = True):
        self.x_fit = logspace(log10(self.x_data[0]), log10(self.x_data[-1]), len(self.y_data))        
        params = self._get_param()
        self.y_fit = self._equation(self.x_fit, *params)
        self.equation = f'{round(self.bottom, sigfigs)} + ({round(self.top, sigfigs)}-{round(self.bottom, sigfigs)})*x**{(round(self.nH, sigfigs))} / ({round(self.ec50, sigfigs)}**{(round(self.nH, sigfigs))} + x**{(round(self.nH, sigfigs))})'
        
        self.regression(self.x_fit, self.y_fit, view_figure, x_label, y_label, title, *params)
        
        return self.x_fit, self.y_fit, params, self.equation
    
    def export(self, export_directory = None, export_name = None):
        # define the unique export path
        if export_directory is None:
            export_directory = os.getcwd()
            
        if export_name is None:
            export_name = '-'.join([re.sub(' ', '_', str(x)) for x in [date.today(), 'Hillfit']])
            count = 0
            export_path = os.path.join(export_directory, export_name) 
            while os.path.exists(export_path):
                count += 1
                export_name = re.sub('([0-9]+)$', str(count), export_name)
                if not re.search('(-[0-9]+$)', export_name):
                    export_name += f'-{count}'
                export_path = os.path.join(export_directory, export_name)       
            os.mkdir(export_path)
        else:
            export_path = os.path.join(export_directory, export_name) 
            count = 0
            while os.path.exists(export_path):
                if not re.search('-[0-9]+\..+', export_path):
                    export_path = re.sub('(\..+)', f'-{count}\..+', export_path)
                else:
                    export_path = re.sub('-[0-9]+', f'-{count}\..+', export_path)
                count += 1
            os.mkdir(export_path)
            
        # export the figure
        self.figure.savefig(os.path.join(export_path, 'regression.svg'))
        
        # export the raw data        
        df = DataFrame(index = range(len(self.x_data)))
        df['x'] = self.x_data
        df['y'] = self.y_data
        df.to_csv(os.path.join(export_path, 'raw_data.csv'))
        
        # export the fitted data
        df2 = DataFrame(index = range(len(self.x_fit)))
        df2['x_fit'] = self.x_fit
        df2['y_fit'] = self.y_fit
        df2.to_csv(os.path.join(export_path, 'fitted_data.csv'))
        
        # export the fitted equation
        formatted_equation = re.sub('(\*\*)', '^', self.equation)
        string = '\n'.join([f'Fitted Hill equation: {formatted_equation}', f'top = {self.top}', f'bottom = {self.bottom}', f'ec50 = {self.ec50}', f'nH = {self.nH}'])
        with open(os.path.join(export_path, 'equation.txt'), 'w') as output:
            output.writelines(string)