def shop():
    items = {
        'Item 1': 50,
        'Item 2': 75,
        'Item 3': 150
    }
    customer_balance = 100

    print("Welcome to the Shop! \n ")
    print("Here are the available items and their prices: \n")
    for item, price in items.items():
        print(f"{item}: £{price}")

    try:
        while True:
            option = input("\nEnter the name of the item you want to purchase ('exit' to leave the shop): ")

            if option == 'exit':
                print("Thank you for visiting the shop. Goodbye!")
                break

            if option not in items:
                raise ValueError("Invalid item selected")

            item_price = items[option]
            if item_price <= customer_balance:
                customer_balance -= item_price
                print(f"Here's your {option}!")
            else:
                raise ValueError("Insufficient funds for the selected item.")

    except ValueError as e:
        print(f"Error: {str(e)}")
        response = input("Do you have more money? (yes/no): ")
        if response.lower() == "yes":
            additional_funds = float(input("Enter the additional amount of money: £"))
            customer_balance += additional_funds
            print(f"Your balance has been updated to £{customer_balance}.")
        else:
            print("You do not have enough money to make a purchase. Goodbye!")

    finally:
        print("\nThank you for visiting the shop. Goodbye!")

shop()
