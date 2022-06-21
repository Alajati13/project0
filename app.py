def validate(sum):
    def wrapper():
        print("please enter two numbers to get their sum")
        print(f"The sum is : {sum()}")
    return wrapper

        



@validate
def sum():
    x = int(input("X : "))
    y = int(input("Y : "))
    z = x + y
    return z

sum()
