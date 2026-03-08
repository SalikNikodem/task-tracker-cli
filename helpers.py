from datetime import datetime


def today():
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def validate_id(func):
    def wrapper(id, *args, **kwargs):
        try:
            new_id = int(id)
        except ValueError:
            print(f"Error: Please provide valid ID number")
            return

        return func(new_id, *args, **kwargs)
    return wrapper

def validate_str(func):
    def wrapper(id, *args, **kwargs):
        try:
            new_id = int(id)
        except ValueError:
            print(f"Error: Please provide valid ID number")
            return

        return func(new_id, *args, **kwargs)
    return wrapper
