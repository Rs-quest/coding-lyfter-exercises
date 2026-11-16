
from datetime import date


# 1. User class
class User:

    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()

        age = today.year - self.date_of_birth.year

        # Check if the birthday has already passed this year
        if (today.month, today.day) < (
            self.date_of_birth.month,
            self.date_of_birth.day
        ):
            age -= 1

        return age


# 2. Decorator to check if the user is an adult
def adult_required(func):

    def wrapper(user):

        if not isinstance(user, User):
            raise TypeError("Parameter must be a User instance")

        if user.age < 18:
            raise ValueError("User must be at least 18 years old")

        return func(user)

    return wrapper


# 3. Function protected by the decorator
@adult_required
def access_restricted_content(user):
    print(f"Access granted! User is {user.age} years old.")


# 4. Tests
if __name__ == "__main__":

    # Adult user
    adult = User(date(1994, 5, 20))

    # Underage user
    minor = User(date(2010, 8, 15))

    # Test 1: Check age
    print("Adult age:", adult.age)
    print("Minor age:", minor.age)

    # Test 2: Adult access
    try:
        access_restricted_content(adult)
    except (ValueError, TypeError) as error:
        print("Error:", error)

    # Test 3: Minor access
    try:
        access_restricted_content(minor)
    except (ValueError, TypeError) as error:
        print("Error:", error)

    # Test 4: Invalid parameter
    try:
        access_restricted_content("Not a user")
    except (ValueError, TypeError) as error:
        print("Error:", error)
