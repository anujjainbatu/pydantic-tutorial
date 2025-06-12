from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int
'''
def insert_patient_data(name: str, age: int):
    if type(name) == str and type(age) == int:
        if age < 0:
            print("Age cannot be negative.")
        else:
            print(name)
            print(age)
            print("Patient data inserted successfully.")
    else:
        print("Invalid data types provided for patient data.")

insert_patient_data("John Doe", "thirty-five")
'''

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Patient data inserted successfully.")

patient_info = {"name": "John Doe", "age": 35}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)