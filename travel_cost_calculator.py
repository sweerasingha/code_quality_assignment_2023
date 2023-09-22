#EG_2020_4267

import csv

# Define dictionaries to store data
hotel_rates = {}
exchange_rates = {}
flight_costs = {}

# Load data from CSV files into dictionaries
def load_data(file, data_dict):
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            data_dict[row[0].upper()] = float(row[1])

def main():
    # Load data from CSV files
    load_data('data/hotel_rates.csv', hotel_rates)
    load_data('data/exchange_rates.csv', exchange_rates)
    load_data('data/flight_costs.csv', flight_costs)

    # Get destination input from user
    destination = input("Enter your destination: ").upper()

    # Calculate hotel and flight costs
    hotel_cost = hotel_rates.get(destination, 0.0)
    flight_cost = flight_costs.get(destination, 0.0)

    # Get stay duration from user
    try:
        days = int(input("Enter your stay duration in days: "))
    except ValueError:
        print("Invalid input for stay duration. Please enter a valid number.")
        return

    # Calculate total cost
    total_cost = (hotel_cost * days) + flight_cost

    print(f"Flight cost: USD {flight_cost:.2f}")
    print(f"Hotel cost for {days} days: USD {hotel_cost * days:.2f}")
    print(f"Total: USD {total_cost:.2f}")

    # Get currency input from user
    currency = input(f"Select your currency for final price estimation ({', '.join(exchange_rates.keys())}): ").upper()

    # Check if selected currency is available
    if currency not in exchange_rates:
        print("Selected currency is not supported.")
        return

    # Convert total cost to selected currency
    converted_cost = total_cost * exchange_rates[currency]

    print(f"Total in {currency}: {converted_cost:.2f}")

if __name__ == "__main__":
    main()
