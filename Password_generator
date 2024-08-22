import random
import string

def random_pass(length):

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(1,length+1):
        password += random.choice(characters)
    return password

print("Welcome to password generator")
length = int(input("Enter the length of password:"))

print(f"Generated Password: {random_pass(length)}")
