import re

def airline_ticket_reservation():
    print("Welcome to the Airline Ticket Reservation System!")
    print("I will ask you a series of questions to book your flight. Type 'exit' at any time to quit.")

    # Prompt for destination
    while True:
        user_input = input("Bot: Where would you like to fly to? ").strip().lower()
        if user_input == "exit":
            print("Bot: Thank you for using the Airline Ticket Reservation System. Goodbye!")
            return
        if re.match(r'^[a-z\s]+$', user_input):
            destination = user_input
            print(f"Bot: Great! You're traveling to {destination}.")
            break
        print("Bot: Please provide a valid destination.")

    # Prompt for departure city
    while True:
        user_input = input("Bot: What city are you departing from? ").strip().lower()
        if user_input == "exit":
            print("Bot: Thank you for using the Airline Ticket Reservation System. Goodbye!")
            return
        if re.match(r'^[a-z\s]+$', user_input):
            departure_city = user_input
            print(f"Bot: You're departing from {departure_city}.")
            break
        print("Bot: Please provide a valid departure city.")

    # Prompt for departure date
    while True:
        user_input = input("Bot: When would you like to depart? Please provide a date (e.g., 'August 15'). ").strip().lower()
        if user_input == "exit":
            print("Bot: Thank you for using the Airline Ticket Reservation System. Goodbye!")
            return
        if re.match(r'^(?:january|february|march|april|may|june|july|august|september|october|november|december) \d{1,2}$', user_input):
            departure_date = user_input
            print(f"Bot: Your departure date is set for {departure_date}.")
            break
        print("Bot: Please provide a valid departure date (e.g., 'August 15').")

    # Prompt for return date or one-way trip
    while True:
        user_input = input("Bot: Is this a round-trip or one-way? If round-trip, please provide a return date (e.g., 'August 22'). If one-way, type 'one-way'. ").strip().lower()
        if user_input == "exit":
            print("Bot: Thank you for using the Airline Ticket Reservation System. Goodbye!")
            return
        if user_input == "one-way" or re.match(r'^(?:january|february|march|april|may|june|july|august|september|october|november|december) \d{1,2}$', user_input):
            return_date = user_input
            if return_date == "one-way":
                print("Bot: You've selected a one-way trip.")
            else:
                print(f"Bot: Your return date is set for {return_date}.")
            break
        print("Bot: Please provide a valid return date or specify 'one-way'.")

    # Prompt for number of passengers
    while True:
        user_input = input("Bot: How many passengers will be traveling? ").strip().lower()
        if user_input == "exit":
            print("Bot: Thank you for using the Airline Ticket Reservation System. Goodbye!")
            return
        if re.match(r'^\d+$', user_input) and int(user_input) > 0:
            passenger_count = user_input
            print(f"Bot: Booking for {passenger_count} passengers.")
            break
        print("Bot: Please provide a valid number of passengers.")

    # Prompt for seat preference
    while True:
        user_input = input("Bot: Do you have a seat preference? (window, aisle, or middle) ").strip().lower()
        if user_input == "exit":
            print("Bot: Thank you for using the Airline Ticket Reservation System. Goodbye!")
            return
        if user_input in ["window", "aisle", "middle"]:
            seat_preference = user_input
            print(f"Bot: You've selected a {seat_preference} seat.")
            break
        print("Bot: Please provide a valid seat preference (window, aisle, or middle).")

    # Final booking confirmation
    if return_date == "one-way":
        print(f"Bot: Your flight is booked! You're flying from {departure_city} to {destination} on {departure_date}. You've booked {passenger_count} {seat_preference} seat(s). Safe travels!")
    else:
        print(f"Bot: Your flight is booked! You're flying from {departure_city} to {destination} on {departure_date}, returning on {return_date}. You've booked {passenger_count} {seat_preference} seat(s). Safe travels!")

if __name__ == "__main__":
    airline_ticket_reservation()
