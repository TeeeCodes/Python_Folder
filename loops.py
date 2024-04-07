# For Loops
loop_Num = [1, 2, 3, 4, 5]
for item in loop_Num:
    print(item)

# While Loops
i = 1
while i <= 10:
    print(i * "*")
    i = i + 1

# Lists
names = ["John", "Bob", "Mosh", "Sam", "Mary"]
print(names[0])
print(names[-1])
# Negative numbers in lists(arrays) start from the end

# this can change the name in a list
names[0] = "Jon"
print(names)
# Prints names of these indexes
print(names[0:3])

numbers = [1, 2, 3, 4, 5]
# Add numbers to List
numbers.append(6)
print(numbers)

# Insert any type into List
numbers.insert(0, -1)
print(numbers)

# Remove a number from List
numbers.remove(3)
print(numbers)

# Clears the whole List
# numbers.clear()
# print(numbers)

# Finds if the number given is in List(Boolean)
print(1 in numbers)

# Tells you how many objects are in List
print(len(numbers))

# Range Function
for ranged in range(5):
    print(ranged)