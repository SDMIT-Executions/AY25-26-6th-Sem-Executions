import csv
import re

def clean_text(text):
    """Remove non-alphanumeric characters using regex"""
    return re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Allows only letters, numbers, and spaces

# Load CSV and clean data
def clean_csv(input_file, output_file):
    with open(input_file, "r", newline="", encoding="utf-8") as infile:
        reader = csv.reader(infile)
        cleaned_data = [[clean_text(cell) for cell in row] for row in reader]  # Apply cleaning

    # Save cleaned data to a new CSV file
    with open(output_file, "w", newline="", encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        writer.writerows(cleaned_data)

    print(f"Cleaned data saved to {output_file}")

# Example Usage
clean_csv("input.csv", "cleaned_output.csv")
