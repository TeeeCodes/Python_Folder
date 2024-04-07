x = float(input("What's x? ")) 
y = float(input("What's y? "))

# Rounds x and y to nearest 2 digits
z = round(x + y, 2)

print(f"{z:,}")