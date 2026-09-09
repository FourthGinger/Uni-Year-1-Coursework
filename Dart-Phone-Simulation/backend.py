class PhotosApp:

    def __init__(self):
        self.num_photos = 0

    def take_photo(self):
        self.num_photos += 1

    def delete_photo(self):
        if self.num_photos > 0:
            self.num_photos -= 1

    def calculate_storage_used(self):
        storage_used = self.num_photos * 24
        storage_used /= 1024
        return round(storage_used, 2)


class MailboxApp:

    def __init__(self):
        self.emails = []

    def receive_email(self, sender, content):
        email = (sender, content)
        self.emails.append(email)

    def count_emails(self):
        return len(self.emails)

    def calculate_storage_used(self):
        num_emails = self.count_emails()
        storage_used = num_emails * 5
        storage_used /= 1024
        return round(storage_used, 3)


class Smartphone:

    def __init__(self, storage_capacity):
        self.storage_capacity = int(storage_capacity)
        self.battery = 100
        self.battery_saver_mode = False

        self.photos_app = PhotosApp()
        self.mailbox_app = MailboxApp()

    def use_battery(self, amount):
        if self.battery >= amount:
            self.battery -= amount

    def charge_battery(self):
        if self.battery_saver_mode:
            self.battery = 80
        else:
            self.battery = 100

    def toggle_battery_saver(self):
        self.battery_saver_mode = not self.battery_saver_mode

    def calculate_storage_used(self):
        storage = self.photos_app.calculate_storage_used()
        storage += self.mailbox_app.calculate_storage_used()
        return round(storage, 3)

    def take_photo(self):
        self.use_battery(2)
        self.photos_app.take_photo()

    def delete_photo(self):
        self.use_battery(2)
        self.photos_app.delete_photo()

    def receive_email(self, sender, content):
        self.use_battery(2)
        self.mailbox_app.receive_email(sender, content)