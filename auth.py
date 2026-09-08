import bcrypt
from models import User

def register_user(username: str, password: str) -> User:
    try:
        if not username.strip():
            raise ValueError("Username must not be empty!")

        if len(password)< 6:
            raise ValueError("password must be at least 6 characters!")

        existing_user = User.get_or_none(User.username == username)

        if existing_user:
            raise ValueError("username already exists!")
    except ValueError as error:
        print(f"You did not Register {error}")

    password_hash = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt())

    user = User.create(
        username=username,
        password_hash= password_hash.decode("utf-8"))

    return user


def login_user(username: str, password: str) -> User | None:
    user = User.get_or_none(User.username == username)

    if user is None:
        return None

    password_correct = bcrypt.checkpw(
        password.encode("utf-8"),
        user.password_hash.encode("utf-8"))

    if password_correct:
        return user

    return None


