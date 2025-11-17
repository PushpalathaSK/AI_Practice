def my_decorator(func):
    def wrapper():
        print("Preparing the pizza base..")
        func()
        print("Adding extra topping before serving")
    return wrapper
    
@my_decorator
def base():
    print("plain pizza is ready")
base()