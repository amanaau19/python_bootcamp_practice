from data import PHONES


def greeting():
    customer_name = input('Please enter your name: ')
    print(f'Hello {customer_name}!, Welcome to our store')
    while True:
        choice = (input('● To look at the catalog enter "catalog" \n'
                           '● To search for phone by specifications enter "search" \n'
                           '● To search for phone by price enter "search by price" \n'
                           '● To quit the program enter "exit" \n'
                           '➔ Enter your action: '))
        if choice == 'catalog':
            print("Catalog:")
            for phone in PHONES:
                print(phone)
        elif choice == 'search':
            search_phone()
        elif choice == 'search by price':
            search_by_price()
        elif choice == 'exit':
            quit(1)


def search_phone():
    name = input('➔ Name of the phone: ')
    memory = int(input('➔ Amount of memory: '))
    color = input('➔ Color of the phone: ')
    for phone in PHONES:
        if phone['name'] == name and phone['memory'] == memory and phone['color'] == color:
            print(f'Phone name: {phone["name"]} | Memory amount: {phone["memory"]} | Color: {phone["color"]} | '
                  f'Price: ${phone["price"]}')
            purchase(phone)

            break
    else:
        print("Sorry, we don't have phones with such characteristics, try to search for another specifications")


def search_by_price():
    price = int(input('➔ Enter price: '))
    for phone in PHONES:
        if price == phone['price']:
            print(f'Phone name: {phone["name"]} | Memory amount: {phone["memory"]} | Color: {phone["color"]} | '
                  f'Price: ${phone["price"]}')
            purchase(phone)

            break
    else:
        print("Sorry, we don't have phones with that price, try to search for another one")


def purchase(phone):
    buy = input(f'● Price of the phone is ${phone["price"]}, are you ready to proceed to payment? \n'
                f'➔ Enter "yes" or "no": ')
    if buy == 'yes':
        money = int(input('➔ Enter the amount of money you will pay with: '))
        if money == phone['price']:
            print('✔ Congratulations! You have successfully purchased a phone \n'
                  'You can continue shopping or quit store')
        elif money > phone['price']:
            print(f'✔ Congratulations! You have successfully purchased a phone, your change is ${money - phone["price"]} \n'
                  f'You can continue shopping or quit store')
        elif money < phone['price']:
            print('🗙 It is not enough money to purchase a phone')

