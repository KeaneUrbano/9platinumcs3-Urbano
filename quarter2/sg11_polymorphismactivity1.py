class Patient: # I create the patient class
    def __init__(self, name, bill_amount): # I create the initiator with all its respective attributes
        self.name = name 
        self.bill_amount = bill_amount 
    def get_name(self): # This is a getter method for name
        return self.name # When called it just returns name as it is
    def set_name(self, name): # A setter for name that uses the returned self.name
        self.name = name
    def get_bill_amount(self): # A getter for bill amount
        return self.bill_amount # Returns bill amount as it is
    def set_bill_amount(self, bill_amount): # A setter that uses returned bill_amount
        self.bill_amount = bill_amount # As this is a regular patient nothing changes
    @property # I used @property so the code could use calculate_bill as an attribute
    def calculate_bill(self):
        return self.bill_amount # No discount as they are regular patient with nothing special
    def display_patient_type(self): # A function to display all data in one go
        print(f"Patient Name: {self.name}") # Prints patient name
        print("Patient Type: Regular Patient") # Shows patient type
        print(f"Original Bill: ₱{self.bill_amount:.2f}") # Nothing changes within original and final bill since regular patient.        
        print(f"Final Bill: ₱{self.calculate_bill:.2f}")

class Senior_Patient(Patient): # This is a child class that inherits from Patient parent class
    def __init__(self, name, bill_amount): # I used the super().init function here so it inherits from Patient parent class with common attributes
            super().__init__(name, bill_amount) # Inherited the parameters for name and bill amount
    @property # Just the same as the earlier application of @property
    def calculate_bill(self): # Since this is senior patient there is a discount of 20% so I did it thorugh this method even if it is crude.
        return (self.bill_amount - (self.bill_amount * 0.20))
    def display_patient_type(self):
        print(f"Patient Name: {self.name}")
        print("Patient Type: Senior Citizen") # No changes within this method other than Patient Type turning into senior citizen.
        print(f"Original Bill: ₱{self.bill_amount:.2f}")        
        print(f"Final Bill: ₱{self.calculate_bill:.2f}")

class PhilHealth(Patient): # Just like in Senior Citizen class I did the same inheritance in PhilHealth class using super().init()
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount) # Same as senior citizen
    @property # Same application as all other classes
    def calculate_bill(self):
        return (self.bill_amount - (self.bill_amount * 0.15)) # Only differences here is that PhilHealth rank patients only get 0.15% discount
    def display_patient_type(self):
        print(f"Patient Name: {self.name}")
        print("Patient Type: PhilHealth Member") # From Regular Patient I changed to Philhealth member
        print(f"Original Bill: ₱{self.bill_amount:.2f}")        
        print(f"Final Bill: ₱{self.calculate_bill:.2f}")

print("Hospital Billing System") # Printing the title card/opening output
print(f"-----------------------\n")
# Setup of objects from Patient to PhilHealth class
patient1 = Patient("Juan Dela Cruz", 15000)
patient2 = Senior_Patient("Maria Santos", 15000)
patient3 = PhilHealth("Pedro Reyes", 15000)
# Output of all objects
patient1.display_patient_type()
patient2.display_patient_type()
patient3.display_patient_type()