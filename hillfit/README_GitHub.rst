Fitting data to the Hill equation
--------------------------------------------------

Background
+++++++++++


The `Hill equation <https://www.physiologyweb.com/calculators/hill_equation_interactive_graph.html>`_ is defined as follows:

:math:`y = bottom + ((top - bottom) * x^nH ) / (EC50^nH + x^nH)`

where *bottom* is the minimum activity; *top* is maximum activity; *EC50* is the half-maximum effective dose; and *nH* is the Hill coefficient. The variables *x* & *y* are the stimuli dose and the cellular or tissue response. The `hillfit` module that applies this biological equation is protected by the `MIT License <https://opensource.org/licenses/MIT>`_\.

Usage
++++++

+++++++++++++
installation
+++++++++++++

The following command are executed in a command prompt/terminal environment::
 
 pip install hillfit

+++++++++++
__init__
+++++++++++

The data environment, in a `Python IDE <https://www.simplilearn.com/tutorials/python-tutorial/python-ide>`_, is defined: 

.. code-block:: python

 import hillfit
 model = hillfit.HillFit(x_data, y_data)

- *x_data* & *y_data* ``list`` or ``ndarray``: specifies the x-values & y-values, respectively, of the raw data that will be fitted with the Hill equation.

++++++++++++++++
fitting()
++++++++++++++++

The parameterized data is fitted to the Hill equation, with the following arguments and their default values:

.. code-block:: python

 model.fitting(x_label = 'x', y_label = 'y', title = 'Fitted Hill equation', 
               sigfigs = 6, view_figure = True)

- *x_label* & *y_label* ``str``: specifies the x-axis & y-axis labels, respectively, that will be applied to the regression plot for the raw data points and the fitted Hill equation.
- *title* ``str``: specifies the title of the regression plot for the raw data points and the fitted Hill equation.
- *sigfigs* ``int``: specifies the number of `significant figures <https://en.wikipedia.org/wiki/Significant_figures>`_ that will be used in printed instances of the fitted Hill equation.
- *view_figure* ``bool``: specifies whether the regression plot will be printed in the Python environment.

++++++++++
export()
++++++++++

The fitted Hill equation, with its data points and parameters, and the regression information are exported to a designated folder through the following syntax and arguments:

.. code-block:: python

 model.export(export_path = None, export_name = None)

- *export_path* ``str``: optionally specifies a path to where the content will be exported, where `None` selects the current working directory.
- *export_name* ``str``: optionally specifies a name for the folder of exported content, where `None` enables the code to design a unique folder name for the information.

Execution
+++++++++++

Hillfit is executed through the following sequence of the aforementioned functions, which is exemplified in the `example Notebook of our GitHub repository <https://github.com/freiburgermsu/hillfit/tree/master/examples>`_:

.. code-block:: python
 
 import hillfit
 model = hillfit.HillFit(x_data, y_data)
 model.fitting(x_label = 'x', y_label = 'y', title = 'Fitted Hill equation', 
               sigfigs = 6, view_figure = True)
 model.export(export_path = None, export_name = None)
