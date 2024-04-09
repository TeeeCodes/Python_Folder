course = "Python for Beginners"
# Convert str to Uppercase (Returns a new str instead of changing main str)
print(course.upper())

# Index for str (-1 means not found in str)
print(course.find("y"))
# Converts to Boolean
print("Python" in  course)

# Replace certain index in str
print(course.replace('for', '4'))

# Key/Value Pairs
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

for student in students:
    # Prints both name and house & sep="," is a separator
    print(student, students[student], sep=",")

# Dictionary in python or key/Value pairs
{}
# Keyword None means no value
None

# Example
friends = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

# Loop through List w/ multiple values printed
for friend in friends:
    print(friend["name"], friend["house"], friend["patronus"], sep=", ")