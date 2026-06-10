#calculate the total price=250, quantity=5, discount=10%. Apply 13% tax on the discounted price.
price=250
quantity=5
discount=10
tax=13

Total_price = price * quantity

discount_amount = Total_price * discount/100

price_after_discount = Total_price - discount_amount

tax = price_after_discount * tax/100

final_price = price_after_discount + tax

print("Total price : ",Total_price)
print("Discount : ",discount_amount)
print("Discounted Price : ",price_after_discount)
print("TAX : ",tax)
print("Final Price : ",final_price)


