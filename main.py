import tkinter

window = tkinter.Tk()
window.title("RaspPiProject")
window.geometry("1280x720")
window.resizable(width=False, height=False)

hwlabel = tkinter.Label(window, text="Hello World")
hwlabel.place(x=20, y=20)

window.mainloop()
