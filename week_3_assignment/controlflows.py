
def calculate_discounts(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else: 
        return price

price = int(input( 'Enter the price: '))
discount_percent = int (input('Key in the discount: '))

final_price= calculate_discounts(price, discount_percent)

if final_price != price:
    print(f" The final price after applying the discount is: ${final_price:.2f}")
else:
    print(f"No discount applied. the original price is: ${price:.2f}")