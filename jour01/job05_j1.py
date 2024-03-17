product_1 = "milk"
price_product_1 = 1.35
quantity_product_1 = 325

product_2 = "bread"
price_product_2 = 0.68
quantity_product_2 = 81

product_3 = "honey"
price_product_3 = 5
quantity_product_3 = 6

print ( product_1, price_product_1, quantity_product_1 )

print ( product_2, price_product_2, quantity_product_2 )

print ( product_3, price_product_3, quantity_product_3 )

product = input("Please enter the requested product: ")
product_quantity = input("Please enter the requested product_quantity: ")
product_quantity = int (product_quantity)

if product == product_1:
    quantity_product_1 = quantity_product_1 - product_quantity
    price_product_1 += 0.1
    new_price_product_1 = round(price_product_1, 2)
    print ( product_1, new_price_product_1, quantity_product_1 )

if product == product_2:
    quantity_product_2 = quantity_product_2 - product_quantity
    price_product_2 += 0.1
    new_price_product_2 = round(price_product_2, 2)
    print ( product_2, new_price_product_2, quantity_product_2 )

if product == product_3:
    quantity_product_3 = quantity_product_3 - product_quantity
    price_product_3 += 0.1
    new_price_product_3 = round(price_product_1, 2)
    print ( product_3, new_price_product_3, quantity_product_3 )


# if product in products:
#     print(f'{product} is available in stock.')
#     price = input ("enter unit price: ")
#     price = int(price)

# else:
#     print(f'{product} is not available in stock.')

