def announce(f): #This is a decorator that takes a function, and adds functionality to it using the wrapper func
    def wrapper():
        print("About to run a function")
        f()
        print("Done with the function")

    return wrapper

@announce
def hello():
    print("Hello World!")

hello()

    