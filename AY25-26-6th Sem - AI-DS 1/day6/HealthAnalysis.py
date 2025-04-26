# nutritionist:
import json

def get_guest_record():
    """Collect guest details interactively"""
    name = input("Enter Name: ")
    height = float(input("Enter Height (cm): "))
    weight = float(input("Enter Weight (kg): "))
    gender = input("Enter Gender (Male/Female): ").lower()
    
    return {"name": name, "height": height, "weight": weight, "gender": gender}

def calculate_bmi(weight, height):
    """Calculate BMI (Body Mass Index)"""
    bmi = weight / ((height / 100) ** 2)
    return round(bmi, 2)

def calculate_bmr(weight, height, gender):
    """Calculate BMR (Basal Metabolic Rate)"""
    if gender == "male":
        return round(88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * 30), 2)  # Assuming age 30
    elif gender == "female":
        return round(447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * 30), 2)  # Assuming age 30
    return "Unknown gender"

def save_to_json(data, filename="guest_records.json"):
    """Save guest records to JSON file"""
    try:
        with open(filename, "r") as file:
            existing_data = json.load(file)  # Load previous records
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []  # Initialize empty list if file doesn't exist or is empty

    existing_data.append(data)  # Add new record
    
    with open(filename, "w") as file:
        json.dump(existing_data, file, indent=4)
    
    print("Record saved successfully!")