from json import *
def retrieve():
    try:
        with open("guests.json", "r") as file:
            return load(file)
    except (FileNotFoundError, JSONDecodeError):
        return {[]}  # Default structure
records = retrieve()
for guest in records:
    height = guest["height"]
    weight = guest["weight"]
    height /= 100
    bmi = weight/(height*height)
    print(guest['name'],"bmi is",bmi,end=" ")
    if bmi <= 18:print("underweight")
    elif bmi>18 and bmi<=25.9:print("normal")
    elif bmi>26 and bmi<=30:print("overweight")
    else: print("obese")