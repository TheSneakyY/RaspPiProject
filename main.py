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
    temp_active = False
    press_active = False

    def day_btn_click(self):
        self.active_mode = PERIOD_MODE.DAY
        self.refresh_buttons()

    def week_btn_click(self):
        self.active_mode = PERIOD_MODE.WEEK
        self.refresh_buttons()

    def month_btn_click(self):
        self.active_mode = PERIOD_MODE.MONTH
        self.refresh_buttons()

    def temp_btn_click(self):
        self.temp_active = not self.temp_active
        self.line.get_tk_widget().place_forget()
        self.update_data()
        self.create_plot(self.data)

    def press_btn_click(self):
        self.press_active = not self.press_active
        self.line.get_tk_widget().place_forget()
        self.update_data()
        self.create_plot(self.data)

    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("RaspPiProject")
        self.window.geometry("1000x600")
        self.window.resizable(width=False, height=False)

        self.canvas = tkinter.Canvas(self.window, width=1000, height=600)
        self.canvas.grid()

        self.day_button = tkinter.Button(self.window, text="Dzień")
        self.week_button = tkinter.Button(self.window, text="Tydzień")
        self.month_button = tkinter.Button(self.window, text="Miesiąc")

        self.temp_button = tkinter.Button(self.window, text="Temperatura")
        self.press_button = tkinter.Button(self.window, text="Ciśnienie")

        self.day_button.place(x=20, y=560, width=self.default_width)
        self.week_button.place(x=120, y=560, width=self.default_width)
        self.month_button.place(x=220, y=560, width=self.default_width)

        self.temp_button.place(x=720, y=560, width=self.default_width)
        self.press_button.place(x=820, y=560, width=self.default_width)

        self.day_button["state"] = DISABLED

        self.day_button.configure(command=self.day_btn_click)
        self.week_button.configure(command=self.week_btn_click)
        self.month_button.configure(command=self.month_btn_click)

        self.temp_button.configure(command=self.temp_btn_click)
        self.press_button.configure(command=self.press_btn_click)

        self.data = {
            'Data': ['2022-01-02 8:00:00', '2022-01-02 8:01:00', '2022-01-02 8:02:00', '2022-01-02 8:03:00',
                     '2022-01-02 8:04:00', '2022-01-02 8:05:00', '2022-01-02 8:06:00', '2022-01-02 8:07:00',
                     '2022-01-02 8:08:00', '2022-01-02 8:09:00'],
            'Temperature': [10, 11, 11.1, 11.1, 11.2, 7, 6.5, 6.2, 5.5, 4],
            'Pressure': [12, 11, 11, 11.1, 5, 7, 6.5, 6.2, 5.5, 4]
        }
        self.create_plot(self.data)

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

    def create_plot(self, data):
        self.figure = plt.Figure(figsize=(6, 4), dpi=100)

        if data is not None:
            self.temp_df = DataFrame(data, columns=['Data', 'Temperature'])
            self.press_df = DataFrame(data, columns=['Data', 'Pressure'])
            self.ax = self.figure.add_subplot(111)
            self.ax.set_title('Temperature')

            self.line = FigureCanvasTkAgg(self.figure, self.window)
            self.line.get_tk_widget().place(x=10, y=10, width=900, height=500)

            self.temp_df = self.temp_df[['Data', 'Temperature']]
            self.press_df = self.press_df[['Data', 'Pressure']]

            if self.temp_active:
                self.temp_df.plot(kind='line', legend=True, ax=self.ax, color='r', marker='o', fontsize=10)
            if self.press_active:
                self.press_df.plot(kind='line', legend=True, ax=self.ax, color='b', marker='o', fontsize=10)

    def update_data(self):
        # self.data = i2c.combined_data
        pass


main = Main()
