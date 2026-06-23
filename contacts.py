import json
import os

class Contacts:

    def __init__(self, filename="phonebook.json"):
        self.file = filename
        self.dict = {}

        if os.path.exists(self.file):
           try:
                with open(self.file, "r") as given_file:
                    self.dict = json.load(given_file)
           except FileNotFoundError:
                self.dict = {}

    def add_contact(self, phone, first_name, last_name):
        if phone in self.dict:
            return "error"
        
        self.dict[phone] = [first_name, last_name]

        self.dict = dict(sorted(self.dict.items(), key=lambda item: (item[1][1].lower(), item[1][0].lower())))

        with open(self.file, "w") as given_file:
            json.dump(self.dict, given_file, indent=4)

        return {phone:[last_name, first_name]}
    
    def modify_contact(self, phone, first_name, last_name):
        if phone not in self.dict:
            return "error"
        
        self.dict[phone]=[first_name, last_name]

        self.dict = dict(sorted(self.dict.items(), key=lambda item: (item[1][1].lower(), item[1][0].lower)))

        with open(self.file, "w") as given_file:
            json.dump(self.dict, given_file, indent=4)

        return {phone:[last_name, first_name]}
    
    def delete_contact(self, phone): 
        if phone not in self.dict:
            return "error"
        
        delete_cont = {phone: self.dict[phone]}

        del self.dict[phone]

        with open(self.file, "w") as given_file:
            json.dump(self.dict, given_file, indent=4)

        return delete_cont
    
    def send_message(self, phone, message, messagelog='message.txt'):
        if phone not in self.dict:
            return 'error'
        
        first_name, last_name = self.dict[phone]

        with open(messagelog, "a") as given_file:
            given_file.write(f"Sending to {first_name} {last_name}: {message}\n")
