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
        self.appointments = []

    def load_data_from_files(self):
        self.load_patients_from_file('patients.csv')
        self.load_doctors_from_file('doctors.csv')
        self.load_appointments_from_file('appointments.csv')

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

    def load_appointments_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    doctor_name, patient_name, date = row
                    self.appointments.append((doctor_name, patient_name, date))
        except FileNotFoundError:
            print(f"File {filename} not found. No appointments loaded.")

    def save_data_to_files(self):
        self.save_patients_to_file('patients.csv')
        self.save_doctors_to_file('doctors.csv')
        self.save_appointments_to_file('appointments.csv')

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

    def save_appointments_to_file(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for appointment in self.appointments:
                writer.writerow(appointment)

    def search_doctors_by_speciality(self, speciality):
        found = False
        doctors_available = []
        for doctor in self.doctors:
            if doctor.speciality == speciality:
                found = True
                doctors_available.append(doctor)

        if found:
            print("\nAvailable doctors:")
            for doctor in doctors_available:
                doctor.display_profile()

            # Prompt for booking only if doctors were found
            choice = input("\nDo you want to book an appointment (y/n): ")
            if choice.lower() == 'y':
                doctor_name = input("Enter doctor name to book appointment: ")
                patient_name = input("Enter patient name: ")
                date = input("Enter date for appointment: ")
                self.book_appointment(doctor_name, patient_name, date)
            else:
               print(f"No doctors found with speciality: {speciality}")

    def book_appointment(self, doctor_name, patient_name, date):
        # Check if doctor exists
        doctor_found = False
        for doctor in self.doctors:
            if doctor.name == doctor_name:
                doctor_found = True
                break

        if not doctor_found:
            print(f"Doctor {doctor_name} not found.")
            return  # Handle error or prompt user again (optional)

        # Add appointment to appointments list
        self.appointments.append((doctor_name, patient_name, date))
        print(f"Appointment booked for {patient_name} with {doctor_name} on {date}.")
        self.save_appointments_to_file('appointments.csv')  # Save appointment

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

        # ... other admin mode functionalities (unchanged) ...
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
            speciality = input("Enter speciality to search for appointments: ")
            hospital.search_doctors_by_speciality(speciality)

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

if __name__ == "__main__":
    main()