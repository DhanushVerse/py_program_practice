# smart store management system
product_dts = {}
while True:
    print('='*5 + 'smart store management system' + '='*5)
    print("\n1. Add Product\n2. View Inventory\n3. Sell Product\n4. Check Low Stock\n5. Exit")
    choice = input('Select the option:')

    # Add Product
    if choice == "1":
        prd_name = input('Enter the Product name:')
        price = int(input('Enter the Price:'))
        quantity = int(input('Enter the quantity:'))
        product_dts[prd_name] = [price],[quantity]
        print(product_dts)


