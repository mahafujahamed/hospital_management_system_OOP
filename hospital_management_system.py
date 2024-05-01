import csv

class Person:
    def __init__(self, name):
        self.name = name

class Doctor(Person):
    def __init__(self, name, speciality, availability):
        super().__init__(name)
        self.speciality = speciality
        self.availability = availability

    def display_profile(self):
        print(f"Name: {self.name}, Speciality: {self.speciality}, Availability: {self.availability}")

class Patient(Person):
    def __init__(self, name, date, doctor, problem):
        super().__init__(name)
        self.date = date
        self.doctor = doctor
        self.problem = problem

    def display_record(self):
        print(f"Name: {self.name}, Date: {self.date}, Doctor: {self.doctor}, Problem: {self.problem}")

class HospitalManagementSystem:
    def __init__(self):
        self.patients = []
        self.doctors = []

    def load_data_from_files(self):
        self.load_patients_from_file('patients.csv')
        self.load_doctors_from_file('doctors.csv')

    def load_patients_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    name, date, doctor, problem = row
                    self.patients.append(Patient(name, date, doctor, problem))
        except FileNotFoundError:
            print(f"File {filename} not found. No data loaded.")

    def load_doctors_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    name, speciality, availability = row
                    self.doctors.append(Doctor(name, speciality, availability))
        except FileNotFoundError:
            print(f"File {filename} not found. No data loaded.")

    def save_data_to_files(self):
        self.save_patients_to_file('patients.csv')
        self.save_doctors_to_file('doctors.csv')

    def save_patients_to_file(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for patient in self.patients:
                writer.writerow([patient.name, patient.date, patient.doctor, patient.problem])

    def save_doctors_to_file(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for doctor in self.doctors:
                writer.writerow([doctor.name, doctor.speciality, doctor.availability])

    def add_patient_record(self, patient):
        self.patients.append(patient)
        print("Patient record added successfully.")
        self.save_patients_to_file('patients.csv')

    def delete_patient_record(self, patient_name):
        for patient in self.patients:
            if patient.name == patient_name:
                self.patients.remove(patient)
                print(f"Patient {patient_name} record deleted successfully.")
                self.save_patients_to_file('patients.csv')
                return
        print(f"Patient {patient_name} not found.")

    def search_patient(self, patient_name):
        for patient in self.patients:
            if patient.name == patient_name:
                patient.display_record()
                return
        print(f"Patient {patient_name} not found.")

    def add_doctor_profile(self, doctor):
        self.doctors.append(doctor)
        print("Doctor profile added successfully.")
        self.save_doctors_to_file('doctors.csv')

    def delete_doctor_profile(self, doctor_name):
        for doctor in self.doctors:
            if doctor.name == doctor_name:
                self.doctors.remove(doctor)
                print(f"Doctor {doctor_name}'s profile deleted successfully.")
                self.save_doctors_to_file('doctors.csv')
                return
        print(f"Doctor {doctor_name} not found.")

    def display_doctor_profiles(self):
        if not self.doctors:
            print("No doctor profiles found.")
            return
        for doctor in self.doctors:
            doctor.display_profile()

    def search_doctors_by_speciality(self, speciality):
        found = False
        for doctor in self.doctors:
            if doctor.speciality == speciality:
                doctor.display_profile()
                found = True
        if not found:
            print(f"No doctors found with speciality: {speciality}")

    def check_doctor_availability(self, doctor_name):
        for doctor in self.doctors:
            if doctor.name == doctor_name:
                print(f"Doctor {doctor_name} is available on {doctor.availability}.")
                return
        print(f"Doctor {doctor_name} not found or availability not specified.")

    def book_appointment(self, doctor_name, patient_name, date):
        for doctor in self.doctors:
            if doctor.name == doctor_name:
                print(f"Appointment booked for {patient_name} with {doctor_name} on {date}.")
                return
        print(f"Doctor {doctor_name} not found.")


def admin_mode(hospital):
    while True:
        print("\nAdmin Mode:")
        print("1. Add patient record")
        print("2. Delete patient record")
        print("3. Search patient by name")
        print("4. Add doctor profile")
        print("5. Delete Doctor profile")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter patient name: ")
            date = input("Enter date: ")
            doctor_name = input("Enter doctor name: ")
            problem = input("Enter problem: ")
            patient = Patient(name, date, doctor_name, problem)
            hospital.add_patient_record(patient)

        elif choice == 2:
            patient_name = input("Enter patient name to delete record: ")
            hospital.delete_patient_record(patient_name)

        elif choice == 3:
            patient_name = input("Enter patient name to search: ")
            hospital.search_patient(patient_name)

        elif choice == 4:
            name = input("Enter doctor name: ")
            speciality = input("Enter speciality: ")
            availability = input("Enter availability: ")
            doctor = Doctor(name, speciality, availability)
            hospital.add_doctor_profile(doctor)

        elif choice == 5:
            doctor_name = input("Enter doctor name to delete profile: ")
            hospital.delete_doctor_profile(doctor_name)

        elif choice == 6:
            break
        else:
            print("Invalid choice. Please choose again.")

def user_mode(hospital):
    while True:
        print("\nUser Mode:")
        print("1. View doctor profiles")
        print("2. Search doctors by speciality")
        print("3. Check doctor availability")
        print("4. Book appointments")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            hospital.display_doctor_profiles()

        elif choice == 2:
            speciality = input("Enter speciality to search: ")
            hospital.search_doctors_by_speciality(speciality)

        elif choice == 3:
            doctor_name = input("Enter doctor name to check availability: ")
            hospital.check_doctor_availability(doctor_name)

        elif choice == 4:
            doctor_name = input("Enter doctor name for appointment: ")
            patient_name = input("Enter patient name: ")
            date = input("Enter date for appointment: ")
            hospital.book_appointment(doctor_name, patient_name, date)

        elif choice == 5:
            break
        else:
            print("Invalid choice. Please choose again.")

def main():
    hospital = HospitalManagementSystem()
    hospital.load_data_from_files()

    while True:
        print("\nSelect Mode:")
        print("1. Admin mode")
        print("2. User mode")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            admin_mode(hospital)
        elif choice == 2:
            user_mode(hospital)
        elif choice == 3:
            print("Thank You!!")
            hospital.save_data_to_files()
            break
        else:
            print("Invalid choice. Please choose again.")

main()
