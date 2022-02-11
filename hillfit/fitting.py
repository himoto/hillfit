import os
import re
from typing import List, Optional, Union

import numpy as np
from matplotlib import pyplot as plt
from pandas import DataFrame
from scipy.optimize import curve_fit
from sigfig import round
from sklearn.metrics import r2_score


class HillFit(object):
    def __init__(
        self,
        x_data: Union[List[float], np.ndarray],
        y_data: Union[List[float], np.ndarray],
        *,
        bottom_param: bool = True,
    ) -> None:
        self.x_data = np.array(x_data)
        self.y_data = np.array(y_data)
        self.bottom_param = bottom_param
        if self.x_data[0] > self.x_data[-1]:
            raise ValueError(
                "The first point {self.x_data[0]} and the last point {self.x_data[-1]} are not amenable with the scipy.curvefit function of HillFit."
            )

    def _equation(self, x: np.ndarray, *params) -> np.ndarray:
        self.top = params[0]
        self.bottom = params[1] if self.bottom_param else 0
        self.ec50 = params[2]
        self.nH = params[3]

        return self.bottom + (self.top - self.bottom) * x**self.nH / (
            self.ec50**self.nH + x**self.nH
        )

    def _get_param(self) -> List[float]:
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
        if not self.bottom_param:
            popt[1] = 0

        return [float(param) for param in popt]

    def regression(
        self,
        x_fit,
        y_fit,
        x_label,
        y_label,
        title,
        sigfigs,
        log_x,
        print_r_sqr,
        view_figure,
        *params,
    ) -> None:
        corrected_y_data = self._equation(self.x_data, *params)
        self.r_2 = r2_score(self.y_data, corrected_y_data)

        # define the regression plot
        plt.rcParams["figure.figsize"] = (11, 7)
        plt.rcParams["figure.dpi"] = 150
        self.figure, self.ax = plt.subplots()
        self.ax.plot(x_fit, y_fit, label="Hill fit")
        self.ax.scatter(self.x_data, self.y_data, label="raw_data")
        if log_x:
            self.ax.set_xscale("log")
        self.ax.set_xlabel(x_label)
        self.ax.set_ylabel(y_label)
        self.ax.set_title(title)
        self.ax.legend(loc="lower right")
        if print_r_sqr:
            # define the coordinates location of the printed R^2 on the figure
            y_coordinate = 0.7 * y_fit[-1]
            if y_coordinate < y_fit[0]:
                y_coordinate = 1 * y_fit[0]
            x_coordinate = 0.8 * x_fit[-1]
            if x_coordinate < x_fit[0]:
                x_coordinate = 2 * x_fit[0]

            self.ax.text(
                x_coordinate,
                y_coordinate,
                "R\N{superscript two}: " + f"{round(self.r_2, sigfigs)}",
            )

        if view_figure:
            self.figure.show()

    def fitting(
        self,
        x_label: str = "x",
        y_label: str = "y",
        title: str = "Fitted Hill equation",
        sigfigs: int = 6,
        log_x: bool = False,
        print_r_sqr: bool = True,
        view_figure: bool = True,
    ):
        self.x_fit = np.logspace(
            np.log10(self.x_data[0]), np.log10(self.x_data[-1]), len(self.y_data)
        )
        params = self._get_param()
        self.y_fit = self._equation(self.x_fit, *params)
        self.equation = f"{round(self.bottom, sigfigs)} + ({round(self.top, sigfigs)}-{round(self.bottom, sigfigs)})*x**{(round(self.nH, sigfigs))} / ({round(self.ec50, sigfigs)}**{(round(self.nH, sigfigs))} + x**{(round(self.nH, sigfigs))})"

        self.regression(
            self.x_fit,
            self.y_fit,
            x_label,
            y_label,
            title,
            sigfigs,
            log_x,
            print_r_sqr,
            view_figure,
            *params,
        )

    def export(
        self, export_directory: Optional[str] = None, export_name: Optional[str] = None
    ) -> None:
        # define the unique export path
        if export_directory is None:
            export_directory = os.getcwd()
        if export_name is None:
            export_name = "-".join([re.sub(" ", "_", str(x)) for x in ["Hillfit", "reg"]])

        count = 0
        export_path = os.path.join(export_directory, export_name)
        while os.path.exists(export_path):
            count += 1
            export_name = re.sub("([0-9]+)$", str(count), export_name)
            if not re.search("(-[0-9]+$)", export_name):
                export_name += f"-{count}"
            export_path = os.path.join(export_directory, export_name)
        os.mkdir(export_path)

        # export the figure
        self.figure.savefig(os.path.join(export_path, "regression.svg"))

        # export the raw data
        df = DataFrame(index=range(len(self.x_data)))
        df["x"] = self.x_data
        df["y"] = self.y_data
        df.to_csv(os.path.join(export_path, "raw_data.csv"))

        # export the fitted data
        df2 = DataFrame(index=range(len(self.x_fit)))
        df2["x_fit"] = self.x_fit
        df2["y_fit"] = self.y_fit
        df2.to_csv(os.path.join(export_path, "fitted_data.csv"))

        # export the fitted equation
        formatted_equation = re.sub("(\*\*)", "^", self.equation)
        string = "\n".join(
            [
                f"Fitted Hill equation (R\N{superscript two} of {round(self.r_2, 6)}): {formatted_equation}",
                f"top = {self.top}",
                f"bottom = {self.bottom}",
                f"ec50 = {self.ec50}",
                f"nH = {self.nH}",
            ],
        )
        with open(os.path.join(export_path, "equation.txt"), "w") as output:
            output.writelines(string)
