from tkinter import Tk, Frame, Label, Entry, Button, StringVar
from backend import Smartphone


class SmartphoneGUI:

    def __init__(self):
        self.win = Tk()
        self.win.title("Smartphone GUI")
        self.win.geometry("500x500")

        self.phone = Smartphone(512)

        self.main_frame = Frame(self.win)
        self.main_frame.grid(column=0, row=0)

        self.storage_capacity_var = StringVar()
        self.battery_var = StringVar()
        self.battery_saver_mode_var = StringVar()
        self.storage_left_var = StringVar()
        self.num_photos = StringVar()
        self.photo_storage_used = StringVar()
        self.num_emails = StringVar()
        self.mail_storage_used = StringVar()


    def run(self):
        self.create_widgets()
        self.update_display()
        self.win.mainloop()


    def create_widgets(self):

        Label(self.main_frame, text="BnL Smartphone").grid(row=0, column=0, sticky="w")

        Label(self.main_frame, text="Storage Capacity:").grid(row=1, column=0, sticky="w")
        Label(self.main_frame, textvariable=self.storage_capacity_var).grid(row=1, column=1, sticky="w")

        Label(self.main_frame, text="Battery:").grid(row=2, column=0, sticky="w")
        Label(self.main_frame, textvariable=self.battery_var).grid(row=2, column=1, sticky="w")

        Label(self.main_frame, text="Battery saver mode:").grid(row=3, column=0, sticky="w")
        Label(self.main_frame, textvariable=self.battery_saver_mode_var).grid(row=3, column=1, sticky="w")

        Label(self.main_frame, text="Storage left").grid(row=4, column=0, sticky="w")
        Label(self.main_frame, textvariable=self.storage_left_var).grid(row=4, column=1, sticky="w")

        Button(self.main_frame, text="Toggle Battery Saver", command=self.toggle_battery).grid(row=5, column=0, sticky="w")
        Button(self.main_frame, text="Charge Battery", command=self.charge_battery).grid(row=5, column=1, sticky="w")

        Label(self.main_frame, text="Photos App").grid(row=6, column=0, sticky="w")

        Label(self.main_frame, text="Number of Photos:").grid(row=7, column=0, sticky="w")
        Label(self.main_frame, textvariable=self.num_photos).grid(row=7, column=1, sticky="w")

        Label(self.main_frame, text="Storage Used:").grid(row=8, column=0, sticky="w")
        Label(self.main_frame, textvariable=self.photo_storage_used).grid(row=8, column=1, sticky="w")

        Button(self.main_frame, text="Take Photo", command=self.take_photo).grid(row=9, column=0, sticky="w")
        Button(self.main_frame, text="Delete Photo", command=self.delete_photo).grid(row=9, column=1, sticky="w")

        Label(self.main_frame, text="Mailbox App").grid(row=10, column=0, sticky="w")

        Label(self.main_frame, text="Number of emails:").grid(row=11, column=0, sticky="w")
        Label(self.main_frame, textvariable=self.num_emails).grid(row=11, column=1, sticky="w")

        Label(self.main_frame, text="Storage Used:").grid(row=12, column=0, sticky="w")
        Label(self.main_frame, textvariable=self.mail_storage_used).grid(row=12, column=1, sticky="w")

        self.mail_sender_content_var = StringVar()
        Entry(self.main_frame, textvariable=self.mail_sender_content_var).grid(row=13, column=0, sticky="w")

        self.mail_content_var = StringVar()
        Entry(self.main_frame, textvariable=self.mail_content_var).grid(row=13, column=1, sticky="w")

        Button(self.main_frame, text="Receive Email", command=self.receive_email).grid(row=14, column=0, sticky="w")


    def update_display(self):
        self.storage_capacity_var.set(f"{self.phone.storage_capacity}GB")
        self.battery_var.set(f"{self.phone.battery}%")

        if self.phone.battery_saver_mode:
            self.battery_saver_mode_var.set("Enabled")
        else:
            self.battery_saver_mode_var.set("Disabled")

        storage_left = self.phone.storage_capacity - self.phone.calculate_storage_used()
        self.storage_left_var.set(round(storage_left, 3))

        self.num_photos.set(self.phone.photos_app.num_photos)
        self.photo_storage_used.set(f"{self.phone.photos_app.calculate_storage_used()}GB")

        self.num_emails.set(self.phone.mailbox_app.count_emails())
        self.mail_storage_used.set(f"{self.phone.mailbox_app.calculate_storage_used()}GB")


    def take_photo(self):
        self.phone.take_photo()
        self.update_display()

    def delete_photo(self):
        self.phone.delete_photo()
        self.update_display()

    def receive_email(self):
        sender = self.mail_sender_content_var.get()
        content = self.mail_content_var.get()

        if sender and content:
            self.phone.receive_email(sender, content)

        self.update_display()

    def charge_battery(self):
        self.phone.charge_battery()
        self.update_display()

    def toggle_battery(self):
        self.phone.toggle_battery_saver()
        self.update_display()


def main():
    phone_gui = SmartphoneGUI()
    phone_gui.run()


if __name__ == "__main__":
    main()