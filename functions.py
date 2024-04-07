# def hello(to="world"):
#     print("Hello,", to)

# hello()
# name = input("What's your name? ")

# # Removes whitespace and Capitalizes
# name = name.strip().title()

# # Python's version of string Interpolation
# hello(name)

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n

main()