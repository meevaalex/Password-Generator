import random
import string

print("===== PASSWORD GENERATOR =====")

# Ask password length
length = int(input("Enter password length: "))

# Characters to use
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ""

for i in range(length):
    password += random.choice(characters)

# Display password
print("\n🔐 Generated Password:")
print(password)