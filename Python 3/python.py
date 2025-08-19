def calculate_discount(price,discount_percent):
    
    if discount_percent >= 0.20:
        final_price = price - (price * discount_percent)

    else:
        return price
    
    original_price = 500
    discount_percent = 0.20

    calculate_discount(original_price, discount_percent / 100)
    print("The final price is:", final_price)
    
    
    