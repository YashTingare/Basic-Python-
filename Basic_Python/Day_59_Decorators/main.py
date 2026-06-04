def greet(fx):
    def mfx():
        print("Good morning")
        fx()
        print("Thank for using this function")
    return mfx

@greet
def hello():
    print("Hello Good Morning")

hello()