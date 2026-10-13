# Investment Revenue Program

# Vajaran Nall

# Function Implimentation
def investment_revenue():

    while True:
        
        try:
            investment_amount = float(input("Enter a monthly investment amount: "))
            interest_rate = float(input("Enter a yearly interest rate: "))
            years = int(input("How many years to invest? "))            
            
            if investment_amount > 0 and interest_rate > 0 and years > 0:
                print(f"You are investing ${investment_amount:.2f} at an interest rate of {interest_rate:.2f}% for {years} years.")

            if investment_amount <= 0:
                print("Error: Investment must be a positive number.")           

            if interest_rate <= 0:
                print("Error: Yearly interest rate must be a positive number.")
                
            if years <= 0:
                print("Error: Investment period must be a positive number of years.")
                
        except ValueError:
            print("Error: Invalid Input(s).")

        else:
            monthly_rate = (interest_rate / 100) / 12
            total_revenue = 0

            for i in range(1, (years * 12) + 1):
                total_revenue = (total_revenue + investment_amount) * (1 + monthly_rate)

                print(f"Month {i} revenue: {total_revenue}")
            print(f"After {years} years, you will receive a total investment revenue of ${total_revenue:,.2f} at a yearly rate of {interest_rate:.1f}%")
            


if __name__ == "__main__":
    investment_revenue()