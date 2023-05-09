# 1) Write a 'split_name' function that takes a string and returns a dictionary with first_name and last_name
def split_name(name):
    first_name, last_name = name.split(maxplit=1)
    return {
        'first_name': first_name,
        'last_name': last_name,
    }

assert split_name("Kevin Bacon") == {
    "first_name": "Kevin" ,
    "last_name": "Bacon" ,
},  f"Expected {{'first_name': 'Kevin', 'last_name': 'Bacon'}} but received {split_name('Kevin Bacon')}"

# 2) Ensure that 'split_name' can handle multi-word last names

assert split_name("Victor Von Doom") == {
    "first_name": "Victor",
    "last_name": "Von Doom",
}, f"Expected {{'first_name': 'Victor', 'last_name': 'Von Doom'}} but received {split_name('Victor Von Doom)}"

# 3) Write an 'is_palindrome' function to check if a string is a palindrome (reads the same from left-to-right)


assert is_palindrome("radar") == True, f"Expected True but got {is_palindrome('radar')}"
assert is_palindrome("stop") == False, f"Expected False but got {is_palindrome('stop')}"
