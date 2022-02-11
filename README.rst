Fitting the Hill Equation to Modeled or Experimental Data
----------------------------------------------------------------------------

|PyPI version| |Actions Status| |License| |Downloads| |Pre commit| |Code style| |Imports|

.. |PyPI version| image:: https://img.shields.io/pypi/v/hillfit.svg?logo=PyPI&logoColor=white
   :target: https://pypi.python.org/pypi/hillfit/
   :alt: PyPI version

.. |Actions Status| image:: https://github.com/himoto/hillfit/workflows/Tests/badge.svg
   :target: https://github.com/himoto/hillfit/actions
   :alt: Actions Status

.. |License| image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://opensource.org/licenses/MIT
   :alt: License

.. |Downloads| image:: https://pepy.tech/badge/hillfit
   :target: https://pepy.tech/project/hillfit
   :alt: Downloads

.. |Pre commit| image:: https://results.pre-commit.ci/badge/github/himoto/hillfit/master.svg
   :target: https://results.pre-commit.ci/latest/github/himoto/hillfit/master
   :alt: pre-commit.ci status

.. |Code style| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Code style: black

.. |Imports| image:: https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336
   :target: https://pycqa.github.io/isort/
   :alt: Imports: isort


Background
+++++++++++


The `Hill equation <https://www.physiologyweb.com/calculators/hill_equation_interactive_graph.html>`_ is defined as follows:

y = bottom + ((top - bottom) * x\ :sup:`nH`\ ) / (EC50\ :sup:`nH`\ + x\ :sup:`nH`\)

where *bottom* is the minimum activity; *top* is maximum activity; *EC50* is the half-maximum effective dose; and *nH* is the Hill coefficient. The variables *x* & *y* are the stimuli dose and the cellular or tissue response. The `hillfit` module applies this biological equation, and is available with the `MIT License <https://opensource.org/licenses/MIT>`_\.

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
 hf = hillfit.HillFit(x_data, y_data)

- *x_data* & *y_data* ``list`` or ``ndarray``: specifies the x-values & y-values, respectively, of the raw data that will be fitted with the Hill equation.
- *bottom_param* ``bool``: specifies whether the accessory ``bottom`` parameter of the Hill equation will be employed in the regression.

++++++++++++++++
fitting()
++++++++++++++++

The parameterized data is fitted to the Hill equation, with the following arguments and their default values:

.. code-block:: python

 hf.fitting(x_label = 'x', y_label = 'y', title = 'Fitted Hill equation', sigfigs = 6, 
            log_x = False, bottom_param = True, print_r_sqr = True, view_figure = True)

- *x_label* & *y_label* ``str``: specifies the x-axis & y-axis labels, respectively, that will be applied to the regression plot for the raw data points and the fitted Hill equation.
- *title* ``str``: specifies the title of the regression plot for the raw data points and the fitted Hill equation.
- *sigfigs* ``int``: specifies the number of `significant figures <https://en.wikipedia.org/wiki/Significant_figures>`_ that will be used in printed instances of the fitted Hill equation.
- *log_x* ``bool``: specifies whether the x-axis of the regression plot will be converted into a logarithmic scale.
- *view_figure* ``bool``: specifies whether the regression plot will be printed in the Python environment.
- *print_r_sqr* ``bool``: specifies whether the coefficient of determination (R\ :sup:`2`\) regression plot will be printed in the Python environment.


-----------------------------
Accessible content
-----------------------------
Many data sets and exported components of the fitted information are accessible through the ``hillfit`` model object. 

- *top*, *bottom*, *ec50*, & *nH* ``float``: The fitted parameters of the Hill equation are accessible via ``hf.top``, ``hf.bottom``, ``hf.ec50``, & ``hf.nH``, respectively.
- *R*\ :sup:`2`\ ``float``: The coefficient of determination of the regression figure is available via ``hf.r_2``.
- *fitted_xs* & *fitted_ys* ``list``: The x- and y-values of the fitted Hill equation are accessible via ``hf.x_fit`` & ``hf.y_fit``, respectively.
- *fitted_equation* ``str``: The fitted Hill equation, in an amenable string format for the `eval() built-in function <https://pythongeeks.org/python-eval-function/>`_ of Python that allows the user to directly execute the string as a function for an "x" variable, is accessible via ``hf.equation``.
- *figure* & *ax* ``matplotlib.figure``: The `fig` and `ax` objects of the regression figure are available via ``hf.figure`` & ``hf.ax``, respectively. This allows users to edit the figures after the simulation is conducted.
- *x_data* & *y_data* ``ndarray``: The arrays of original data are available via ``hf.x_data`` & ``hf.y_data``, respectively.


++++++++++
export()
++++++++++

The fitted Hill equation, with its data points and parameters, and the regression information are exported to a designated folder through the following syntax and arguments:

.. code-block:: python

   hf.export(export_directory = None, export_name = None)

- *export_directory* ``str``: optionally specifies a path to where the content will be exported, where `None` selects the current working directory.
- *export_name* ``str``: optionally specifies a name for the folder of exported content, where `None` enables the code to design a unique folder name for the information.

Execution
+++++++++++

Hillfit is executed through the following sequence of the aforementioned functions, which is exemplified in the `example Notebook of our GitHub repository <./examples>`_:

.. code-block:: python

   import hillfit
   hf = hillfit.HillFit(x_data, y_data)
   hf.fitting(x_label = 'test_x', y_label = 'test_y', title = 'Fitted Hill equation', sigfigs = 6, log_x = False, view_figure = True, print_r_sqr = True)
   hf.export(export_directory = None, export_name = None)
