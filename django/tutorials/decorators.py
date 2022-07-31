from typing import AnyStr, Callable


user="admin"
user="guest"

def secure(func):
    if user == "admin":
        return func()
    else:
        return "not allowed"


@secure
def get_pass():
    return "1234"

print(get_pass)