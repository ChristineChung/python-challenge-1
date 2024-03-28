#CC's Petite Boucherie Food Truck Menu

# Empty List to store customer order
order_list = []

# Menu dictionary
menu = {
    "Appetizers": {
        "Burrata": 15.50,
        "Waffle Fries": 5.00,
        "Pita and Hummus": 12.90,
        "Pear Salad": 18.75
    },
    "Main Courses": {
        "Branzino": 45.00,
        "Chicken Milanese": 30.00,
        "Kale Caesar Salad": 18.00,
        "Short Ribs": 32.00,
        "Steak - Au Poivoire": 35.00,
        "Steak - NY Strip": 40.00,
        "Steak - Cajun Rib Eye": 55.00,
        "Pasta - A La Vongole": 18.00,
        "Pasta - Homemade Lasagna": 24.00
    },
    "Drinks": {
        "Wine - Red": 12.00,
        "Wine - White": 14.00,
        "Wine - Rose": 16.00,
        "Soft Drinks - Kombucha": 4.00,
        "Soft Drinks - Iced Tea": 5.00,
        "Soft Drinks - Fresh OJ": 6.49
    },
    "Desserts": {
        "Chocolate Mousse": 15.00,
        "Pies - Apple Crumble": 8.99,
        "Pies - Boston Creme": 9.49,
        "Coffee Gelato": 8.00,
        "Caramel Churros": 12.00,
        "Fresh Fruits": 6.00
    }
}

# Launch the store and present a greeting to the customer
print("Welcome to CC's Petite Boucherie")

menu_dashes = "-" * 47

while True:
    print(menu_dashes)
    print("Today's Menu")
    print("Which section would you like to view? ")

    # Create a variable for the menu item number
    i = 1

    """Print the options to choose from menu headings (all the first 
    level dictionary items in menu)."""
    for key in menu.keys():
        print(f"{i}: {key}")
        
        # Add 1 to the menu item number
        i += 1

    # Ask the customer which menu category they want to view
    while True:
        
        # Get the customer's input
        menu_selection = input("Enter menu section number or 'q' to quit: ")

        # Exit the loop if user typed 'q'
        if menu_selection.lower() == 'q':
            break

         # Check if the customer's input is a number
        elif menu_selection.isdigit():
            
            # Check if the customer's input is a valid option
            if int(menu_selection) in range(1, i):
                # Save the menu selection name to a variable
                menu_selection_name = list(menu.keys())[int(menu_selection) - 1]
                # Print out the menu category name they selected
                print(f"You selected {menu_selection_name}")

                while True:
                    print(menu_dashes)
                    print(f"This is the {menu_selection_name} menu.")
                    print(menu_dashes)
                    print("Item # | Item name                | Price")
                    print("-------|--------------------------|-------")

                    # Initialize a menu item counter
                    item_counter = 1

                    # Print out the menu options from the selected category
                    for key, value in menu[menu_selection_name].items():
                        num_item_spaces = 24 - len(key)
                        item_spaces = ' ' * num_item_spaces
                        print(f"{item_counter}      | "
                              + f"{key}{item_spaces} | ${value:.2f}")
                        item_counter += 1
                    
                    print(menu_dashes)

                    order_choice = input("Enter the item number you would like to order (or 'b' to go back, 'c' to checkout): ")

                    if order_choice.lower() == 'b':
                        break

                    elif order_choice.lower() == 'c':
                        # Display the final order and total with quantities included
                        if order_list:
                            print("\n--- Your Order ---")
                            total_price = sum(item['price'] * item.get('quantity',1) for item in order_list)
                            
                            for index, item in enumerate(order_list, start=1):
                                quantity = item.get('quantity',1)
                                subtotal = quantity * item['price']
                                print(f"{index}: {item['name']} x{quantity} - ${subtotal:.2f}")
                            
                            print(f"Total: ${total_price:.2f}")
                            print(menu_dashes)
                            print("Thank you for your order. Enjoy your meal!")
                        else:
                            print("\nNo items were ordered.")
                        break

                    elif order_choice.isdigit() and int(order_choice) in range(1, item_counter):
                        selected_item_index = int(order_choice) - 1
                        
                        selected_item = {'name': list(menu[menu_selection_name].keys())[selected_item_index], 
                                         'price': list(menu[menu_selection_name].values())[selected_item_index]}
                        
                        quantity_input = input("Enter quantity (default is 1): ")
                        quantity = int(quantity_input) if quantity_input.isdigit() else 1
                        
                        selected_item['quantity'] = quantity
                        
                        order_list.append(selected_item)
                        print(f"{selected_item['name']} x{quantity} added to your order.")

                    else:
                        print("Invalid input. Please enter a valid item number or 'b' to go back.")

            else:
                print("Invalid input. Please enter a valid menu section number or 'q' to quit.")