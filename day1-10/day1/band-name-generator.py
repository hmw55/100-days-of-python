print("Welcome to the Band Name Generator.")
mood = input("What is your current mood?\n")
animal = input("What is your favorite animal?\n")

# Suggested by Angela Yu
## print("Your band name could be: " +  mood + " " + animal)

# Best practiced and convenience
print("Your band name could be:", mood, animal)

# + (String Concatenation)
## Joins strings without spaces.
## Requires all operands to be stings.
### Use if you want full control over formatting and no spaces between strings.

# , (Print Function Argument Separator)
## Prints each item seperated by a space.
## No need to convert non-strings
### Use if you want convenience and automatic spacing, especially when combining strings with other data types.