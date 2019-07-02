from scipy.optimize import curve_fit

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

    def fitting(self,x_new):
        popt = self.get_param()
        print(
            '%s = %e\n%s = %e\n%s = %e\n%s = %e'\
            %('top',popt[0],'bottom',popt[1],'K',popt[2],'n',popt[3])
        )

        return self.equation(x_new,popt[0],popt[1],popt[2],popt[3])
