
def print_arguments(func):

    def wrapper(*args, **kwargs):

        print("Arguments:", args, kwargs)

        result = func(*args, **kwargs)

        print(result)

        return result

    return wrapper


#testing
@print_arguments
def sum_numbers(a, b):
    return a + b


sum_numbers(5, 10)