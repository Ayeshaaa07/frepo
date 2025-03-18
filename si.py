# Function to calculate simple interest
def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

# Main function to get user input and display the result
def main():
    try:
        # Input from user
        principal = float(input("Enter the principal amount (P): "))
        rate = float(input("Enter the rate of interest (R) in percentage: "))
        time = float(input("Enter the time period (T) in years: "))

        # Calculate simple interest
        simple_interest = calculate_simple_interest(principal, rate, time)

        # Display the result
        print(f"The Simple Interest is: {simple_interest:.2f}")

    except ValueError:
        print("Please enter valid numeric values.")

# Run the main function
if __name__ == "__main__":
    main()

