class Smartphone:

    def __init__(self, storage_capacity):
        self.storage_capacity = int(storage_capacity)
        self.battery = 100
        self.battery_saver_mode = False

    def use_battery(self, battery_to_use):
        self.battery -= battery_to_use
        if self.battery < 0:
            self.battery = 0

    def charge_battery(self):
        if self.battery_saver_mode == True:
            self.battery = 100
        else:
            self.battery = 80


    def __str__(self):
        if self.battery_saver_mode == True:
            self.battery_saver_mode = "Enabled"
        else:
            self.battery_saver_mode = "Disabled"

        return f"Bnl Smartphone - Storage: {self.storage_capacity}GB, Battery: {self.battery}%, Battery_saver_mode: {self.battery_saver_mode}"
    

def test_smartphone():
    phone = Smartphone(512)

    phone.use_battery(30)

    print(phone)

    phone.battery_saver_mode = True

    phone.charge_battery()

    print(phone)

test_smartphone()


class PhotosApp:

    def __init__(self):
        self.num_photos = 0

    def take_photo(self):
        self.num_photos += 1

    def delete_photo(self):
        self.num_photos -= 1

    def calculate_storage_used(self):
        storage_used = self.num_photos * 24
        storage_used /= 1024
        storage_used = round(storage_used, 2)
        return storage_used
    
    def __str__(self):
        return f"Photos App - Photos: {self.num_photos}, Storage Used: {self.calculate_storage_used()}GB"
    

def test_photos_app():

    photos = PhotosApp()

    for i in range(5):
        photos.take_photo()

    print(photos)

    for i in range(2):
        photos.delete_photo()
    
    print(photos)

test_photos_app()


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
        storage_used = round(storage_used, 3)
        return storage_used
    
    def __str__(self):
        return f"Mailbox App - Emails: {self.count_emails()}, Storage Used: {self.calculate_storage_used()}GB"


def test_mailbox_app():
    emails = MailboxApp()

    print(emails)

    emails.receive_email("Jonny", "Hello World")

    print(emails)

    emails.receive_email("Marvin", "Apple sauce")

    print(emails)

test_mailbox_app()