#Answer part 1
def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or more
    if discount_percent >= 20:
        # Apply the discount
        final_price = price - (price * (discount_percent / 100))
        return final_price  # Send back the discounted price
    else:
        return price  # Send back the original price if no discount
    
 #Answer part 2   
# Get input from the user
price = float(input("Enter the original price of the item: "))  # Convert input to a number
discount_percent = float(input("Enter the discount percentage: "))  # Convert input to a number

# Call the function with the user’s input
final_price = calculate_discount(price, discount_percent)

# Print the result
if final_price < price:  # If the price was reduced
    print(f"The final price after applying the discount is: {final_price}")
else:  # If no discount was applied
    print(f"No discount applied. The original price is: {price}")

