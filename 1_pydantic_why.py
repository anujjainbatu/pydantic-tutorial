from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title="Patient Name", description="Full name of the patient", example="John Doe")]
    email: EmailStr
    linked_in: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True, description="Weight in kilograms", example=70.5)]
    married: Annotated[Optional[bool], False, Field(default=None, description="Is the patient married?")]
    allergies: Annotated[Optional[List[str]], Field(default=None, description="List of patient allergies")]
    contact_details: Dict[str, str]
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

patient_info = {"name": "John Doe", "email": "abc@gmail.com", "linked_in": "http://linkedin.com/in/abc", "age": 35, "weight": 70.5,
                "married": True, "allergies": ["pollen", "nuts"], "contact_details": {"email": "abc@gmail.com", "phone": "1234567890"}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)