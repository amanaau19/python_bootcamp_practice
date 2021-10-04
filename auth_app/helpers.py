from data import USERS


def check_user_existence(username: str) -> bool:
    for user in USERS:
        if user['username'] == username:
            return True
    return False


def get_user(username: str) -> dict:
    for user in USERS:
        if user['username'] == username:
            return user
