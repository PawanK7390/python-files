# Input currency in rupees and output in USD.

def convert_to_usd():
    # Constant for the conversion rate
    conversion_rate = 82  # 1 USD = 82 INR

    # Taking the amount in rupees as input from the user
    rupees = float(input("Enter the amount in Rupees: "))

    # Conversion from INR to USD
    usd = rupees / conversion_rate

    # Printing the result in USD
    print(f"{rupees} INR is equivalent to {usd:.2f} USD.")


convert_to_usd()
