def calculate_discounted_price(price, discount):
    discounted_price = price - discount
    return discounted_price


price = 1000
discount = 20

final_price = calculate_discounted_price(price, discount)
print("Final Price:", final_price)
