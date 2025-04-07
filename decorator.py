def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("Sprinkles are added 🎊")
        func(*args, **kwargs)
    return wrapper
def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("Fudge has been added 🍫")
        func(*args, **kwargs)
    return wrapper
        
@add_sprinkles    
@add_fudge
def get_icecream(flavour, quantity):
    print(f"Here is your {quantity} {flavour} ice cream 🍦")

get_icecream(flavour="chocolate", quantity=2)