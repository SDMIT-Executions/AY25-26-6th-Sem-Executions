from re import match
# Define regex patterns
patterns = {
    "Name": r"^[A-Za-z ]{3,}$",  # Name should have at least 3 characters, only letters and spaces
    "Password": r"^(?=.*[@$!%*?&])[A-Za-z0-9@$!%*?&]{8,}$",  # Password should have at least 8 characters
    "Aadhaar": r"^[0-9]{12}$",  # Aadhaar should be exactly 12 digits
    "PAN": r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$",  # PAN format: ABCDE1234F
    "Email": r"^[a-zA-Z0-9._%+-]{3,}@[a-zA-Z0-9.-]{3,}\.[a-zA-Z]{2,}$"  # Standard email format
}

# Sample inputs
inputs = {
    "Name": "Razak",
    "Password": "razak123",
    "Aadhaar": "7654567",
    "PAN": "ABCDE1234F",
    "Email": "example@ma.com"
}
valid = True
# Validate and print results
print("Validation Results:")
for field, value in inputs.items():
    if not match(patterns[field],value):
        valid = False
        print("invalid ",field)
    else: continue
else:
    print("account created" if valid else "")
