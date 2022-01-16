from numpy import ndarray
from hillfit import HillFit
from datetime import date
from shutil import rmtree
from sigfig import round
import os

# define test data
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

results_x = [9.210000000000003, 9.46145508152332, 9.71977548965075, 9.98514866425862, 10.25776716278127, 10.537828799932667, 10.825536791242744, 11.121099900512625, 11.42473259129573, 11.73665518251466, 12.057094008326851, 12.386281582354876, 12.72445676640068, 13.071864943766064, 13.428758197305312, 13.79539549233901, 14.172042864561865, 14.558973613080902, 14.956468498724014, 15.364815947762844, 15.784312261197746, 16.21526182975681, 16.657977354764785, 17.112780075042302, 17.579999999999995]

results_y = [-1.2009268354077514, -1.1019386026962077, -0.9361462741726332, -0.6589530187564369, -0.1968630200694157, 0.5697006355299381, 1.8311066794316677, 3.879402140361975, 7.134776473131587, 12.135978958765994, 19.432438647098934, 29.31326172256841, 41.42513346071518, 54.5824393128962, 67.12584843884352, 77.68051747251918, 85.66803238258414, 91.24090038664565, 94.91218306602104, 97.24014055848994, 98.68074429626357, 99.55881941045381, 100.08908673834162, 100.40752377313935, 100.59810875187523]

def test_init():
    hf = HillFit(x_data, y_data)
    
    # affirm module qualities
    for ary in [hf.x_data, hf.y_data]:
        assert type(ary) is ndarray
    
    
def test_fitting():
    hf = HillFit(x_data, y_data)
    x_fit, y_fit, params, eq = hf.fitting()
    
    # affirm module qualities    
    x = 6
    assert eval(eq)
    assert type(eq) is str
    
    assert type(params) is list
    assert type(x_fit) is ndarray
    assert type(y_fit) is ndarray

    for entry in list(x_fit):
        index = list(x_fit).index(entry)
        assert round(entry, 3) == round(results_x[index], 3)
        
    for entry in list(y_fit):
        index = list(y_fit).index(entry)
        assert round(entry, 3) == round(results_y[index], 3)
                
def test_export():
    hf = HillFit(x_data, y_data)
    x_fit, y_fit, params, eq = hf.fitting()
    hf.export()
    
    # affirm module qualities    
    export_path = os.path.join(os.getcwd(), f'{date.today()}-Hillfit') 
    for export_item in ['regression.svg', 'equation.txt', 'fitted_data.csv', 'raw_data.csv']:
        assert os.path.exists(os.path.join(export_path, export_item))
   
    # delete the directory 
    rmtree(export_path)