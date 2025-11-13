🌟 BMI Calculator (Python)

A simple, accurate, and user-friendly BMI (Body Mass Index) Calculator written in Python.
This program allows users to enter their weight and height in multiple formats, handles invalid inputs gracefully, and classifies BMI according to standard health categories.


✨ Features

✔ Accepts weight in kg or pounds
✔ Accepts height in meters OR feet + inches
✔ Converts all units automatically
✔ Validates incorrect inputs
✔ Prevents impossible height/weight values
✔ Classifies BMI into:Underweight, Normal Weight, Overweight, Obesity
✔ Clean and beginner-friendly Python code


📌 How to Run

-Make sure you have Python 3 installed.
-Save the program in a file, e.g.:
-bmi_calculator.py
-Run the file in Terminal or CMD:
-python bmi_calculator.py

🧮 BMI Formula

The BMI is calculated using the standard formula:
-->  BMI = weight_in_kg / (height_in_meters)^2

🧊 Input Formats Supported

Weight:

You can enter weight in:
kilograms → 55 kg
pounds → 120 lb, 120 lbs, pounds
Example:
Enter your weight: 62 kg

Height:

-->Two options:
    Option 1 — Meters
    press 1 to enter height in metre 1
    1.63

    Option 2 — Feet + Inches
    press 2 to enter height in foot and inches
    enter foot: 5
    enter inches: 4

📊 BMI Categories
BMI Range	        Category
  < 18.5	        Underweight
  18.5 – 24.9	    Normal Weight
  25 – 29.9	        Overweight
  ≥ 30	            Obesity


🔐 Input Validation
This program rejects invalid inputs such as:
-negative height/weight
-zero values
-unrealistic human height (> 3m)
-unrealistic weight (> 700 kg)
-non-numeric input
-unsupported units
This ensures accurate and safe results.

📝 Sample Output
Enter your weight: 60 kg
press 1 to enter height in metre
press 2 to enter height in foot and inches
1
enter height in metre 1.62
Your BMI: 22.86
Normal Weight

📂 Project Structure
BMI-Calculator/
│── bmi_calculator.py
│── README.md


🚀 Future Improvements (optional)

-GUI using Tkinter
-Web version using FastAPI
-BMI charts
-Health suggestions based on BMI
-Logging user BMI history