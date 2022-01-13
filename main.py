import tkinter
from enum import Enum
from tkinter.constants import DISABLED, NORMAL

from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class PERIOD_MODE(Enum):
    DAY = 0,
    WEEK = 1,
    MONTH = 2


class Main:
    default_width = 100
    active_mode = PERIOD_MODE.DAY

    def day_btn_click(self):
        self.active_mode = PERIOD_MODE.DAY
        self.refresh_buttons()

    def week_btn_click(self):
        self.active_mode = PERIOD_MODE.WEEK
        self.refresh_buttons()

    def month_btn_click(self):
        self.active_mode = PERIOD_MODE.MONTH
        self.refresh_buttons()

    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("RaspPiProject")
        self.window.geometry("1280x720")
        self.window.resizable(width=False, height=False)

        self.canvas = tkinter.Canvas(self.window, width=1280, height=720)
        self.canvas.grid()

        self.hwlabel = tkinter.Label(self.window, text="Dane za okres: ")
        self.hwlabel.place(x=20, y=20)

        self.day_button = tkinter.Button(self.window, text="Dzień")
        self.week_button = tkinter.Button(self.window, text="Tydzień")
        self.month_button = tkinter.Button(self.window, text="Miesiąc")

        self.day_button.place(x=20, y=660, width=self.default_width)
        self.week_button.place(x=120, y=660, width=self.default_width)
        self.month_button.place(x=220, y=660, width=self.default_width)

        self.day_button["state"] = DISABLED

        self.data2 = {'Year': [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010],
                      'Unemployment_Rate': [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3]
                      }
        self.df2 = DataFrame(self.data2, columns=['Year', 'Unemployment_Rate'])

        self.figure2 = plt.Figure(figsize=(5, 4), dpi=100)
        self.ax2 = self.figure2.add_subplot(111)
        self.line2 = FigureCanvasTkAgg(self.figure2, self.window)
        self.line2.get_tk_widget().place(x=20, y=100, width=1000, height=550)
        self.df2 = self.df2[['Year', 'Unemployment_Rate']].groupby('Year').sum()
        self.df2.plot(kind='line', legend=True, ax=self.ax2, color='r', marker='o', fontsize=10)
        self.ax2.set_title('Year Vs. Unemployment Rate')

        self.day_button.configure(command=self.day_btn_click)
        self.week_button.configure(command=self.week_btn_click)
        self.month_button.configure(command=self.month_btn_click)

        self.window.mainloop()

    def refresh_buttons(self):
        if self.active_mode == PERIOD_MODE.DAY:
            self.day_button["state"] = DISABLED
            self.week_button["state"] = NORMAL
            self.month_button["state"] = NORMAL
        if self.active_mode == PERIOD_MODE.WEEK:
            self.week_button["state"] = DISABLED
            self.day_button["state"] = NORMAL
            self.month_button["state"] = NORMAL
        if self.active_mode == PERIOD_MODE.MONTH:
            self.month_button["state"] = DISABLED
            self.day_button["state"] = NORMAL
            self.week_button["state"] = NORMAL


main = Main()
