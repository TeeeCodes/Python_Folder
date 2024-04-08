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

name = input("What's your name? ")

# Switch Case
match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")