from helpers import check_user_existence, get_user
from auth import login

username = input('Enter your user name: ')
password = input('Enter your password: ')


if check_user_existence(username):
    user = get_user(username)
    logged_in = login(user, password)
    if logged_in:
        user['logged_in'] = True
        print(user)
    else:
        print('Invalid password')
else:
    print('Invalid username')
