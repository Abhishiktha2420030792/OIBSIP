def calculate_bmi(weight, height):
    """Calculate BMI using weight (kg) and height (m)."""
    return weight / (height ** 2)

def get_bmi_category(bmi):
    """Return BMI category based on WHO classification."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("=== BMI Calculator ===")
    
    try:
        # Get user input
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))
        
        # Validate input
        if weight <= 0 or height <= 0:
            print("Error: Weight and height must be positive numbers.")
            return
        
        # Calculate BMI and determine category
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)
        
        # Display results
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {category}")
        
    except ValueError:
        print("Error: Please enter valid numeric values.")

if __name__ == "__main__":
    main()
