

def login(user: dict, password: str) -> bool:
    if user['password'] == password:
        return True
    return False
