## Chinmay D. 10/27/2022 Hg5590
import random
import string
def IssueSix():
# Naming and starting the function
    char = string.ascii_letters + string.digits + string.punctuation
    x = random.choice(string.ascii_lowercase)
    x += random.choice(string.ascii_uppercase)
    x += random.choice(string.digits)
    x += random.choice(string.punctuation)
    for i in range(8):
        x += random.choice(char)
    passwords = list(x)
    random.SystemRandom().shuffle(passwords)
    passwords = ''.join(x)
    return x
print("List of Acceptable Passwords:")
for i in range(40):
    print(IssueSix())
# End of the function and fullfills all the criteria 