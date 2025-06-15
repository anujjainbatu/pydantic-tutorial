from pydantic import BaseModel, Field

class Address(BaseModel):
    city: str
    state: str
    zip_code: str

class Patient(BaseModel):
    name: str
    age: int
    gender: str
    address: Address

address_dict = {
    "city": "New York",
    "state": "NY",
    "zip_code": "10001"
}
address1 = Address(**address_dict)

patient_dict = {
    "name": "John Doe",
    "age": 30,
    "gender": "male",
    "address": address1
}

patient1 = Patient(**patient_dict)

def update_patient_data(patient: Patient):
    print(f"Name: {patient.name}")
    print(f"Age: {patient.age}")
    print(f"Gender: {patient.gender}")
    print(f"Address: {patient.address.city}, {patient.address.state}, {patient.address.zip_code}")
update_patient_data(patient1)

# Better organization of related data (e.g., vitals, address, insurance)

# Reusability: Use Vitals in multiple models (e.g., Patient, MedicalRecord)

# Readability: Easier for developers and API consumers to understand

# Validation: Nested models are validated automatically—no extra work needed