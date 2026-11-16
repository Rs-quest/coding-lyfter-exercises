
def validate_numbers(func):

    def wrapper(*args, **kwargs):

        for value in args:
            if not isinstance(value, (int, float)):
                raise ValueError("All parameters must be numbers")

        for value in kwargs.values():
            if not isinstance(value, (int, float)):
                raise ValueError("All parameters must be numbers")

        result = func(*args, **kwargs)
        return result

    return wrapper
#Testing
@validate_numbers
def sum_numbers(a, b):
    return a + b

print(sum_numbers(10, 20))
print(sum_numbers(10, "hello"))