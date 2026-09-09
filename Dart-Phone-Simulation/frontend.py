from tkinter import Tk, Frame, Label, Entry, Button, IntVar, StringVar

class SmartphoneGUI:

    def __init__(self):
        self.win = Tk()
        self.win.title("Smartphone GUI")
        self.win.geometry("300x200")

        self.main_frame = Frame(self.win)
        self.main_frame.grid(column=0, row=0)

        self.storage_capacity_var = StringVar(value="512GB")
        self.battery_var = StringVar(value="75%")
        self.battery_saver_mode_var = StringVar(value="Disabled")
        self.storage_left_var = StringVar(value="511.98")

        Label(self.main_frame, text="Storage Capacity:").grid(row=0, column=0)
        Label(self.main_frame, textvariable=self.storage_capacity_var).grid(row=0, column=1)

        Label(self.main_frame, text="Battery:").grid(row=1, column=0)
        Label(self.main_frame, textvariable=self.battery_var).grid(row=1, column=1)

        Label(self.main_frame, text="Battery saver mode:").grid(row=2, column=0)
        Label(self.main_frame, textvariable=self.battery_saver_mode_var).grid(row=2, column=1)

        Label(self.main_frame, text="Storage left").grid(row=3, column=0)
        Label(self.main_frame, textvariable=self.storage_left_var).grid(row=3, column=1)

        

        Button(self.main_frame, text="Open Photos").grid(row=4, column=0)
        Button(self.main_frame, text="Open Mail").grid(row=4, column=1)

        self.photos_var = IntVar()
        Entry(self.main_frame, textvariable=self.photos_var).grid(row=5, column=1)


        self.win.mainloop()


gui = SmartphoneGUI()