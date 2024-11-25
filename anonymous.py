
def greet(name, cb):
    print(f"Hello, {name}!")
    cb()

# def say_bye():
#     print("BYE!")
# say_bye = lambda: print("Bye!")


# Main
greet("Steve", lambda: print("Bye!"))

