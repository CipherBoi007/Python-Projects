def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    
    return bmi, category

def main():
    print("BMI Calculator")
    print("--------------")
    
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        # Calculate BMI
        bmi, category = calculate_bmi(weight, height)
        
        # Display results
        print(f"\nYour BMI is: {bmi:.1f}")
        print(f"Category: {category}")
        
        # Display BMI categories
        print("\nBMI Categories:")
        print("- Underweight: <18.5")
        print("- Normal weight: 18.5-24.9")
        print("- Overweight: 25-29.9")
        print("- Obese: ≥30")
        
    except ValueError:
        print("Please enter valid numerical values for weight and height.")

if __name__ == "__main__":
    main()